#!/usr/bin/env python3
"""
Lina Automation API (prototype)

Lightweight HTTP API using the Python standard library to:
- Run benchmarks via CLI and Extractor
- Record metrics in out/metrics.json
- Provide simple auto-approval hooks for routine tasks

Endpoints:
- GET  /health -> {status: ok}
- POST /lina/benchmark  body: {"target": "path or base name", "methods": ["cli","extractor"], "metrics": ["time","consistency"]}
- POST /lina/auto_approve body: {"request_type": "performance_test", ...}
- GET  /lina/metrics -> metrics.json content (if exists)
 - POST /lina/consistency body: {"agg": "sentence_mean|segment_mean"}
 - POST /lina/complete_pipeline body: {"target": "path", "verify_quality": true}
 - POST /lina/regression_test body: {"texts": ["..."], "min_quality": 0.95}

Run:
  python -m automation.lina_api  (serves on 0.0.0.0:3001)
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json
import subprocess
import shlex
import os
import re

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'out'
DATA_DIR = ROOT / 'data'


def ensure_dirs():
    OUT_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)


def parse_time_mem(text: str):
    d = {"real_sec": None, "max_rss": None, "peak_mem": None}
    m = re.search(r"\n\s*([0-9.]+) real\s+([0-9.]+) user\s+([0-9.]+) sys", text)
    if m:
        d["real_sec"] = float(m.group(1))
    m = re.search(r"maximum resident set size\n\s*([0-9]+)", text)
    if m:
        d["max_rss"] = int(m.group(1))
    m = re.search(r"peak memory footprint\n\s*([0-9]+)", text)
    if m:
        d["peak_mem"] = int(m.group(1))
    return d


def run_cmd(cmd: str) -> tuple[int, str, str]:
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(ROOT))
    out, err = proc.communicate()
    return proc.returncode, out.decode('utf-8', errors='ignore'), err.decode('utf-8', errors='ignore')


def update_metrics(key: str, payload):
    ensure_dirs()
    mp = OUT_DIR / 'metrics.json'
    try:
        metrics = json.loads(mp.read_text(encoding='utf-8')) if mp.exists() else {}
    except Exception:
        metrics = {}
    metrics[key] = payload
    mp.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding='utf-8')


class Handler(BaseHTTPRequestHandler):
    def _send(self, code=200, payload=None):
        body = json.dumps(payload or {"status": "ok"}, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa
        if self.path == '/health':
            return self._send(200, {"status": "ok"})
        if self.path == '/lina/metrics':
            mp = OUT_DIR / 'metrics.json'
            if mp.exists():
                try:
                    data = json.loads(mp.read_text(encoding='utf-8'))
                except Exception:
                    data = {"error": "metrics parse error"}
                return self._send(200, data)
            return self._send(404, {"error": "metrics not found"})
        return self._send(404, {"error": "not found"})

    def do_POST(self):  # noqa
        length = int(self.headers.get('Content-Length', '0'))
        body = self.rfile.read(length).decode('utf-8') if length else '{}'
        try:
            data = json.loads(body or '{}')
        except Exception:
            data = {}

        if self.path == '/lina/auto_approve':
            # Minimal auto-approval: approve routine performance tests
            approved = data.get('request_type') in {'performance_test', 'benchmark'}
            return self._send(200, {"approved": approved})

        if self.path == '/lina/benchmark':
            target = data.get('target') or ''
            methods = data.get('methods') or ['cli', 'extractor']
            metrics_req = data.get('metrics') or ['time']
            # Resolve target path
            tpath = Path(target)
            if not tpath.is_absolute():
                # try Text/ and samples/
                for base in [ROOT / 'Text', ROOT / 'samples']:
                    candidate = base / target
                    if candidate.exists():
                        tpath = candidate
                        break
            if not tpath.exists():
                return self._send(400, {"error": f"target not found: {target}"})

            res = {"target": str(tpath)}
            # CLI classify
            if 'cli' in methods:
                code, out, err = run_cmd(f"/usr/bin/time -l ./venv/bin/python -m src.cli classify --file {shlex.quote(str(tpath))} --pretty")
                res['cli'] = {"rc": code, "stderr": err.splitlines()[-20:]}
                (OUT_DIR / 'last_cli.json').write_text(out, encoding='utf-8')
                res['cli']['time'] = parse_time_mem(err)
            # Extractor
            if 'extractor' in methods:
                code, out, err = run_cmd(f"/usr/bin/time -l ./venv/bin/python lna-es-app/apps/extractor/extractor.py --input {shlex.quote(str(tpath))} --outdir out --datadir data")
                res['extractor'] = {"rc": code, "stderr": err.splitlines()[-20:]}
                res['extractor']['time'] = parse_time_mem(err)

            update_metrics('api_last_benchmark', res)
            return self._send(200, res)

        if self.path == '/lina/consistency':
            # Compute consistency between last CLI classify and latest extractor JSON
            agg_method = data.get('agg', 'sentence_mean')
            # Load CLI output
            cli_path = OUT_DIR / 'last_cli.json'
            if not cli_path.exists():
                return self._send(400, {"error": "no last_cli.json; run /lina/benchmark with cli first"})
            try:
                cli = json.loads(cli_path.read_text(encoding='utf-8'))
            except Exception:
                return self._send(400, {"error": "invalid last_cli.json"})

            # Find latest extractor JSON
            extractor_jsons = sorted(DATA_DIR.glob('*.json'), key=lambda p: p.stat().st_mtime, reverse=True)
            if not extractor_jsons:
                return self._send(400, {"error": "no extractor JSON found"})
            d = json.loads(extractor_jsons[0].read_text(encoding='utf-8'))

            # Compute ontology aggregation
            sentences = d.get('sentences', [])
            segments = d.get('segments', [])
            agg = {}
            if agg_method == 'segment_mean' and segments:
                # Average sentence scores per segment, then mean across segments
                seg_scores = []
                for seg in segments:
                    ids = seg.get('sentences', [])
                    vals = [s for s in sentences if s.get('sentenceId') in ids]
                    if not vals:
                        continue
                    keys = vals[0].get('ontoScores', {}).keys()
                    seg_agg = {k: sum(v['ontoScores'].get(k, 0.0) for v in vals)/len(vals) for k in keys}
                    seg_scores.append(seg_agg)
                if seg_scores:
                    keys = seg_scores[0].keys()
                    agg = {k: sum(s[k] for s in seg_scores)/len(seg_scores) for k in keys}
            else:
                # sentence_mean (default)
                if sentences:
                    keys = sentences[0].get('ontoScores', {}).keys()
                    agg = {k: sum(s['ontoScores'].get(k, 0.0) for s in sentences)/len(sentences) for k in keys}

            # Compute metrics
            def top3_codes(obj, key_code, limit=3):
                return [x.get(key_code) for x in obj[:limit] if isinstance(x, dict)]

            cli_ndc = top3_codes(cli.get('ndc', {}).get('classifications', []), 'code')
            cli_kd = top3_codes(cli.get('kindle', {}).get('classifications', []), 'category')
            ext_ndc = top3_codes(d.get('work', {}).get('ndc', []), 'code')
            ext_kd = top3_codes(d.get('work', {}).get('kindle', []), 'category')

            def match_rate(a, b):
                a = [x for x in a if x]
                b = [x for x in b if x]
                return (len(set(a) & set(b)) / max(len(set(a)), len(set(b)))) if a and b else 0.0

            # Pearson on top-5 ontology keys from CLI vs extractor agg
            cli_onto = cli.get('ontology_weights', {})
            top5 = sorted(cli_onto.items(), key=lambda x: x[1], reverse=True)[:5]
            keys = [k for k, _ in top5]
            xs = [cli_onto[k] for k in keys]
            ys = [agg.get(k, 0.0) for k in keys]
            def pearson(xs, ys):
                n = len(xs)
                if n < 2:
                    return None
                mx = sum(xs)/n
                my = sum(ys)/n
                num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
                denx = sum((x-mx)**2 for x in xs) ** 0.5
                deny = sum((y-my)**2 for y in ys) ** 0.5
                return (num / (denx*deny)) if (denx*deny) else None

            payload = {
                'agg': agg_method,
                'ndc_top3_match_rate': match_rate(cli_ndc, ext_ndc),
                'kindle_top3_match_rate': match_rate(cli_kd, ext_kd),
                'ontology_top5_pearson': pearson(xs, ys)
            }
            update_metrics('api_last_consistency', payload)
            return self._send(200, payload)

        if self.path == '/lina/triple_classification':
            # Run triple validation classification for provided text
            text = (data or {}).get('text') or ''
            if not text.strip():
                return self._send(400, {"error": "text required"})
            try:
                from src.triple_validation import TripleValidationClassifier
            except Exception:
                from triple_validation import TripleValidationClassifier
            clf = TripleValidationClassifier()
            result = clf.classify_with_triple_validation(text)
            update_metrics('api_last_triple', result)
            return self._send(200, result)

        if self.path == '/lina/complete_pipeline':
            target = data.get('target') or ''
            verify = bool(data.get('verify_quality', True))
            tpath = Path(target)
            if not tpath.is_absolute():
                for base in [ROOT / 'Text', ROOT, ROOT / 'samples']:
                    cand = base / target
                    if cand.exists():
                        tpath = cand
                        break
            if not tpath.exists():
                return self._send(400, {"error": f"target not found: {target}"})
            stem = tpath.stem
            # Run complete pipeline
            verify_flag = '--verify-quality' if verify else ''
            code, out, err = run_cmd(f"/usr/bin/time -l ./venv/bin/python src/complete_pipeline.py {shlex.quote(str(tpath))} {verify_flag} --output-dir out")
            # Read result json
            res_file = OUT_DIR / f"{stem}_pipeline_results.json"
            result = {}
            if res_file.exists():
                try:
                    result = json.loads(res_file.read_text(encoding='utf-8'))
                except Exception:
                    result = {"error": "result parse error"}
            payload = {
                "rc": code,
                "time": parse_time_mem(err),
                "result": {
                    "restoration_quality": result.get('restoration_quality'),
                    "privacy_compliant": result.get('privacy_compliant'),
                    "pipeline_success": result.get('pipeline_success')
                },
                "result_file": str(res_file)
            }
            update_metrics('api_last_complete_pipeline', payload)
            return self._send(200, payload)

        if self.path == '/lina/regression_test':
            # Run complete pipeline on inline texts (temporary files) and check quality≥min_quality
            texts = data.get('texts') or []
            min_q = float(data.get('min_quality', 0.95))
            results = []
            (OUT_DIR / 'regression').mkdir(exist_ok=True)
            for i, txt in enumerate(texts):
                tmp = OUT_DIR / 'regression' / f'tmp_reg_{i}.txt'
                tmp.write_text(str(txt), encoding='utf-8')
                code, out, err = run_cmd(f"/usr/bin/time -l ./venv/bin/python src/complete_pipeline.py {shlex.quote(str(tmp))} --verify-quality --output-dir out")
                res_file = OUT_DIR / f"{tmp.stem}_pipeline_results.json"
                r = {}
                if res_file.exists():
                    try:
                        r = json.loads(res_file.read_text(encoding='utf-8'))
                    except Exception:
                        r = {}
                results.append({
                    "file": str(tmp),
                    "quality": r.get('restoration_quality'),
                    "pass": (r.get('restoration_quality') or 0.0) >= min_q
                })
            payload = {"min_quality": min_q, "results": results}
            update_metrics('api_last_regression', payload)
            return self._send(200, payload)

        return self._send(404, {"error": "not found"})


def main():
    ensure_dirs()
    port = int(os.environ.get('LINA_API_PORT', '3001'))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Lina API listening on http://0.0.0.0:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
