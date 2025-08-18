#!/usr/bin/env python3
"""
Maya API Server (recovery-safe, curl-first)

Endpoints (localhost:3000):
- GET  /health                 -> {status, extractor_ready}
- GET  /maya/status            -> {current_tasks, memory_status}
- POST /maya/extractor         -> {success, work_id, cypher_file, stdout, stderr}
  Body: {"target": "path/to/text.txt"}
- POST /maya/coordinate_lina   -> Proxy coordination to Lina's API
  Body: {"task": "...", ...}

This server avoids long-lived heavy work; it only executes single-file extractor runs
and performs explicit garbage collection between operations.
"""
import gc
import json
import os
import re
import shlex
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict
from urllib import request as urlrequest

# Project root (repo root)
REPO_ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = REPO_ROOT / 'venv' / 'bin' / 'python'
EXTRACTOR_PATH = REPO_ROOT / 'lna-es-app' / 'apps' / 'extractor' / 'extractor.py'
DEFAULT_OUTDIR = REPO_ROOT / 'out'
DEFAULT_DATADIR = REPO_ROOT / 'data'

LINA_BASE_URL = os.environ.get('LINA_API_BASE', 'http://localhost:3001')


def _json_bytes(data: Dict[str, Any]) -> bytes:
    return json.dumps(data, ensure_ascii=False).encode('utf-8')


def _post_json(url: str, payload: Dict[str, Any], timeout: float = 30.0) -> Dict[str, Any]:
    try:
        req = urlrequest.Request(url, data=_json_bytes(payload), headers={'Content-Type': 'application/json'})
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset('utf-8')
            text = resp.read().decode(charset)
            return json.loads(text)
    except Exception as exc:  # Keep resilient
        return {"error": "request_failed", "details": str(exc), "url": url}


def safe_extractor_run(target_file: str) -> Dict[str, Any]:
    """Run extractor once, capture results, and force GC for memory stability."""
    result: Dict[str, Any] = {"success": False}
    try:
        if not target_file:
            return {"success": False, "error": "missing_target"}
        target_path = Path(target_file)
        if not target_path.is_absolute():
            target_path = (REPO_ROOT / target_path).resolve()
        if not target_path.exists():
            return {"success": False, "error": "target_not_found", "path": str(target_path)}

        # Ensure output dirs exist
        DEFAULT_OUTDIR.mkdir(parents=True, exist_ok=True)
        DEFAULT_DATADIR.mkdir(parents=True, exist_ok=True)

        cmd = [
            str(VENV_PYTHON),
            str(EXTRACTOR_PATH),
            '--input', str(target_path),
            '--outdir', str(DEFAULT_OUTDIR),
            '--datadir', str(DEFAULT_DATADIR),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        stdout = proc.stdout
        stderr = proc.stderr

        work_id = None
        cypher_file = None
        # Parse stdout lines for Work ID and Cypher file path
        for line in stdout.splitlines():
            if line.startswith('Ingestion complete. Work ID:'):
                work_id = line.split(':', 1)[1].strip()
            elif line.startswith('Cypher file:'):
                cypher_file = line.split(':', 1)[1].strip()

        result.update({
            'success': proc.returncode == 0,
            'work_id': work_id,
            'cypher_file': cypher_file,
            'stdout': stdout,
            'stderr': stderr,
            'returncode': proc.returncode,
        })
        return result
    except subprocess.TimeoutExpired as exc:
        return {"success": False, "error": "timeout", "details": str(exc)}
    except Exception as exc:  # Resilient server behavior
        return {"success": False, "error": str(exc)}
    finally:
        gc.collect()


class MayaHandler(BaseHTTPRequestHandler):
    server_version = 'MayaAPI/0.1'

    def _send(self, code: int, payload: Dict[str, Any]) -> None:
        data = _json_bytes(payload)
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _get_json(self) -> Dict[str, Any]:
        try:
            length = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            length = 0
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode('utf-8'))
        except Exception:
            return {}

    def do_GET(self) -> None:  # noqa: N802
        if self.path == '/health':
            self._send(200, {"status": "maya_ok", "extractor_ready": EXTRACTOR_PATH.exists()})
            return
        if self.path == '/maya/status':
            self._send(200, {"current_tasks": [], "memory_status": "stable"})
            return
        self._send(404, {"error": "not_found", "path": self.path})

    def do_POST(self) -> None:  # noqa: N802
        if self.path == '/maya/extractor':
            data = self._get_json()
            result = safe_extractor_run(data.get('target'))
            self._send(200 if result.get('success') else 500, result)
            return
        if self.path == '/maya/coordinate_lina':
            data = self._get_json() or {}
            resp = _post_json(f"{LINA_BASE_URL}/lina/coordinate_maya", data)
            self._send(200 if 'error' not in resp else 502, resp)
            return
        self._send(404, {"error": "not_found", "path": self.path})


def run_server(port: int = 3000) -> None:
    with HTTPServer(('0.0.0.0', port), MayaHandler) as httpd:
        print(f"Maya API server listening on http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    port_str = os.environ.get('MAYA_API_PORT', '3000')
    try:
        port = int(port_str)
    except ValueError:
        port = 3000
    run_server(port)
