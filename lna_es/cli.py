from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ABTestArgs:
    control_a: Path
    control_b: Path
    graph: Path
    out_dir: Path


def _ensure_out_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(text)


def cmd_abtest(args: ABTestArgs) -> int:
    # Load controls to validate structure (currently unused in mock logic)
    _load_json(args.control_a)
    _load_json(args.control_b)
    graph = _load_json(args.graph)
    _ensure_out_dir(args.out_dir)

    # Minimal, deterministic mock results
    summary = {
        "controls": {
            "A": args.control_a.name,
            "B": args.control_b.name,
        },
        "graph_nodes": len(graph.get("nodes", [])),
        "graph_edges": len(graph.get("edges", [])),
        "winner": "A" if (len(graph.get("nodes", [])) % 2 == 0) else "B",
    }
    _write_json(args.out_dir / "summary.json", summary)

    # produce placeholder drafts
    _write_text(args.out_dir / "A" / "draft.txt", "[DRAFT A]\n")
    _write_text(args.out_dir / "B" / "draft.txt", "[DRAFT B]\n")
    return 0


# ops compile


def cmd_ops_compile(operators_path: Path, out_path: Path) -> int:
    # For now, just wrap the YAML/XML path into a tiny JSON structure
    result = {
        "dialect_source": str(operators_path),
        "compiled": True,
        "version": "0.1.0",
    }
    _write_json(out_path, result)
    return 0


def cmd_ops_validate(operators_path: Path) -> int:
    """Validate operators file.

    - If XML: validate against spec/operators.xsd
    - If JSON: validate against spec/operator.schema.json (single operator schema)
    """
    ext = operators_path.suffix.lower()
    repo_root = Path(__file__).resolve().parents[1]
    if ext == ".xml":
        try:
            import xmlschema

            xsd_path = repo_root / "spec" / "operators.xsd"
            schema = xmlschema.XMLSchema(xsd_path)
            schema.validate(str(operators_path))
            print(f"OK: XML valid against {xsd_path}")
            return 0
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: XML validation failed: {exc}")
            return 1
    elif ext == ".json":
        try:
            import jsonschema

            schema_path = repo_root / "spec" / "operator.schema.json"
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            instance = json.loads(operators_path.read_text(encoding="utf-8"))
            jsonschema.validate(instance=instance, schema=schema)
            print(f"OK: JSON valid against {schema_path}")
            return 0
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: JSON validation failed: {exc}")
            return 1
    else:
        print("ERROR: Unsupported file type. Use .xml or .json")
        return 2


# generate


def cmd_generate(graph_path: Path, control_path: Path, out_dir: Path) -> int:
    graph = _load_json(graph_path)
    control = _load_json(control_path)
    _ensure_out_dir(out_dir)

    metrics = {
        "nodes": len(graph.get("nodes", [])),
        "edges": len(graph.get("edges", [])),
        "locks": list(sorted([k for k, v in control.get("locks", {}).items() if v])),
    }
    _write_text(out_dir / "draft.txt", "[DRAFT]\n")
    _write_json(out_dir / "metrics.json", metrics)
    return 0


def cmd_verify(draft_path: Path, control_path: Path, out_path: Path) -> int:
    # Minimal verification: compute metrics and a toy violation
    with draft_path.open("r", encoding="utf-8") as f:
        draft_text = f.read()
    control = _load_json(control_path)

    metrics = {
        "chars": len(draft_text),
        "lines": draft_text.count("\n") + (0 if draft_text.endswith("\n") else 1),
        "locks_enabled": sum(1 for v in control.get("locks", {}).values() if v),
    }
    violations: list[dict[str, Any]] = []
    if "TODO" in draft_text:
        violations.append(
            {
                "rule": "no_todo",
                "severity": "minor",
                "message": "Draft contains TODO markers",
                "span": None,
            }
        )

    result = {"metrics": metrics, "violations": violations}
    _write_json(out_path, result)
    return 0


def cmd_rewrite(draft_path: Path, verify_path: Path, out_path: Path) -> int:
    # Minimal rewrite: if no_todo violation exists, strip literal 'TODO'
    with draft_path.open("r", encoding="utf-8") as f:
        draft_text = f.read()
    verify = _load_json(verify_path)
    out_text = draft_text
    for v in verify.get("violations", []):
        if v.get("rule") == "no_todo":
            out_text = out_text.replace("TODO", "")
    _write_text(out_path, out_text)
    return 0


def cmd_audit(metrics_path: Path, verify_path: Path, out_path: Path) -> int:
    metrics = _load_json(metrics_path)
    verify = _load_json(verify_path)

    lines: list[str] = []
    lines.append("# Audit Card")
    lines.append("")
    lines.append("## Metrics")
    for key, value in metrics.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Violations")
    violations = verify.get("violations", [])
    if not violations:
        lines.append("- none")
    else:
        for v in violations:
            rule = v.get("rule", "<unknown>")
            severity = v.get("severity", "info")
            message = v.get("message", "")
            lines.append(f"- [{severity}] {rule}: {message}")

    _write_text(out_path, "\n".join(lines) + "\n")
    return 0


def cmd_preset_load(xml_path: Path, out_path: Path) -> int:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # collect operator names grouped by category
    index: dict[str, list[str]] = {}
    if "}" in root.tag:
        ns = {"ns": root.tag.split("}")[0].strip("{")}
        categories = root.findall(".//ns:category", ns)
        for category in categories:
            cat_name = category.get("name", "unknown")
            ops = [op.get("name", "?") for op in category.findall("ns:operator", ns)]
            index[cat_name] = ops
    else:
        for category in root.findall(".//category"):
            cat_name = category.get("name", "unknown")
            ops = [op.get("name", "?") for op in category.findall("operator")]
            index[cat_name] = ops
    summary = {
        "source": str(xml_path),
        "categories": {k: len(v) for k, v in index.items()},
        "total_operators": sum(len(v) for v in index.values()),
        "operators_by_category": index,
    }
    _write_json(out_path, summary)
    print(f"Cached axis0 index to {out_path}")
    return 0


def cmd_cta_analyze(input_path: Path, out_path: Path, ontology_dir: Path | None) -> int:
    text = input_path.read_text(encoding="utf-8")
    # toy segmentation: split by punctuation
    import re

    segments = [s.strip() for s in re.split(r"[。.!?\n]", text) if s.strip()]
    # toy scoring using ontology terms occurrence
    ontology_terms: set[str] = set()
    if ontology_dir is not None and ontology_dir.exists():
        try:
            import yaml

            for yml in sorted(ontology_dir.glob("*.y*ml")):
                try:
                    data = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
                    if isinstance(data, dict):
                        for key in (
                            "semantic_roots",
                            "primitives",
                            "spectral_extensions",
                        ):
                            for item in data.get(key, []) or []:
                                for k in ("root", "name"):
                                    val = item.get(k)
                                    if isinstance(val, str):
                                        ontology_terms.add(val.strip())
                        # associations
                        for item in data.get("semantic_roots", []) or []:
                            for assoc in item.get("associations", []) or []:
                                if isinstance(assoc, str):
                                    ontology_terms.add(assoc.strip())
                except Exception:
                    continue
        except Exception:
            pass

    scored = []
    for idx, seg in enumerate(segments):
        score = 0.0
        hits = []
        for term in ontology_terms:
            if term and term in seg:
                score += 0.1
                hits.append(term)
        scored.append(
            {"id": idx, "text": seg, "score": round(min(score, 1.0), 3), "hits": hits}
        )

    _write_json(out_path, {"segments": scored})
    return 0


def cmd_cta_to_graph(input_path: Path, out_path: Path, threshold: float) -> int:
    data = _load_json(input_path)
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    for seg in data.get("segments", []):
        if seg.get("score", 0) >= threshold:
            node_id = f"seg-{seg.get('id')}"
            nodes.append(
                {
                    "id": node_id,
                    "type": "Segment",
                    "name": node_id,
                    "text": seg.get("text"),
                }
            )
    _write_json(out_path, {"nodes": nodes, "edges": edges})
    return 0


def cmd_graph_reconstruct(
    control_path: Path,
    out_path: Path,
    use_ai_brain: bool,
    ai_threshold: float = 1.0,
    ontology_dir: Path | None = None,
    ai_heuristics: bool = False,
) -> int:
    control = _load_json(control_path)
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    # Build nodes from HARD invariants
    hard = control.get("invariants", {}).get("HARD", [])
    # Optionally include SOFT invariants when ontology is requested
    use_soft = use_ai_brain or (ontology_dir is not None and ai_threshold < 1.0)
    soft = control.get("invariants", {}).get("SOFT", []) if use_soft else []

    def add_node(n: dict[str, Any]) -> None:
        node: dict[str, Any] = {k: v for k, v in n.items()}
        # Create a simple id from name/place/symbol
        ident = (
            node.get("name")
            or node.get("place")
            or node.get("symbol")
            or node.get("type")
        )
        node_id = str(ident)
        node["id"] = node_id
        # Normalize type casing similar to sample
        typemap = {
            "character": "Character",
            "setting": "Setting",
            "scene": "Scene",
            "motif": "Motif",
        }
        node_type = node.get("type")
        if isinstance(node_type, str):
            node["type"] = typemap.get(node_type, node_type)
        nodes.append(node)

    for inv in hard:
        if inv.get("type") in {"character", "setting"}:
            add_node(inv)
        if inv.get("type") == "relation":
            edges.append(
                {"src": inv.get("src"), "rel": inv.get("rel"), "dst": inv.get("dst")}
            )

    # AI-brain heuristics: include SOFT (scene/motif) and score candidate associations
    for inv in soft:
        if inv.get("type") in {"scene", "motif"}:
            add_node(inv)

    # Load ontology (optional)
    ontology_terms: set[str] = set()
    if ontology_dir is not None:
        try:
            import yaml

            for yml in sorted(ontology_dir.glob("*.y*ml")):
                try:
                    data = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
                    # Collect common fields
                    if isinstance(data, dict):
                        if "semantic_roots" in data:
                            for item in data.get("semantic_roots", []) or []:
                                name = item.get("root")
                                if isinstance(name, str):
                                    ontology_terms.add(name.strip())
                                for assoc in item.get("associations", []) or []:
                                    if isinstance(assoc, str):
                                        ontology_terms.add(assoc.strip())
                        if "primitives" in data:
                            for item in data.get("primitives", []) or []:
                                name = item.get("name")
                                if isinstance(name, str):
                                    ontology_terms.add(name.strip())
                        if "spectral_extensions" in data:
                            for item in data.get("spectral_extensions", []) or []:
                                name = item.get("name")
                                if isinstance(name, str):
                                    ontology_terms.add(name.strip())
                except Exception:
                    continue
        except Exception:
            pass

    # Optional candidate generation from heuristics/ontology
    names = {n.get("name"): n.get("id") for n in nodes if n.get("name")}
    places = {n.get("place"): n.get("id") for n in nodes if n.get("place")}
    candidates: list[tuple[dict[str, str], float]] = []

    if ai_heuristics and use_ai_brain:
        # Example heuristic 1: a known scene name to its setting (demo data)
        if "防波堤" in names and "湘南" in places:
            candidates.append(
                (
                    {
                        "src": names.get("防波堤", "防波堤"),
                        "rel": "LOCATED_IN",
                        "dst": places.get("湘南", "湘南"),
                    },
                    0.9,
                )
            )
        # Example heuristic 2: motif "海" associated with scene 防波堤
        if any(inv.get("symbol") == "海" for inv in soft) and "防波堤" in names:
            candidates.append(
                (
                    {"src": "海", "rel": "ASSOCIATED_WITH", "dst": names["防波堤"]},
                    0.7,
                )
            )

    # Ontology assist (weak)
    if ontology_terms:
        motif_labels = {inv.get("symbol") or inv.get("name") for inv in soft}
        motif_labels = {m for m in motif_labels if isinstance(m, str)}
        for m in motif_labels:
            if m in ontology_terms:
                for scene_name, scene_id in names.items():
                    if scene_name and scene_name != m:
                        candidates.append(
                            (
                                {"src": m, "rel": "ASSOCIATED_WITH", "dst": scene_id},
                                0.55,
                            )
                        )

    for edge, score in candidates:
        if score >= ai_threshold:
            edges.append(edge)

    graph = {"nodes": nodes, "edges": edges}
    _write_json(out_path, graph)
    return 0


def _node_key(n: dict[str, Any]) -> tuple:
    return (
        n.get("type"),
        n.get("name") or n.get("place") or n.get("symbol") or n.get("id"),
    )


def cmd_graph_eval(gt_path: Path, pred_path: Path, out_path: Path) -> int:
    gt = _load_json(gt_path)
    pr = _load_json(pred_path)

    gt_nodes = {_node_key(n) for n in gt.get("nodes", [])}
    pr_nodes = {_node_key(n) for n in pr.get("nodes", [])}

    tp_nodes = len(gt_nodes & pr_nodes)
    fp_nodes = len(pr_nodes - gt_nodes)
    fn_nodes = len(gt_nodes - pr_nodes)

    def prf(tp: int, fp: int, fn: int) -> dict[str, float]:
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
        return {
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4),
        }

    node_metrics = prf(tp_nodes, fp_nodes, fn_nodes)

    # Edge matching by (src_label, rel, dst_label) using name/place/symbol/id
    def label_for(n: dict[str, Any]) -> str:
        return n.get("name") or n.get("place") or n.get("symbol") or n.get("id") or ""

    def edge_set(g: dict[str, Any]) -> set[tuple[str, str, str]]:
        nodes = g.get("nodes", [])
        label_index: dict[str, dict[str, Any]] = {label_for(n): n for n in nodes}
        id_to_label: dict[str, str] = {}
        for n in nodes:
            nid = n.get("id")
            if isinstance(nid, str):
                id_to_label[nid] = label_for(n)

        def normalize(x: Any) -> str:
            if isinstance(x, str):
                if x in label_index:
                    return x
                if x in id_to_label:
                    return id_to_label[x]
            return str(x)

        es: set[tuple[str, str, str]] = set()
        for e in g.get("edges", []):
            src = normalize(e.get("src"))
            dst = normalize(e.get("dst"))
            rel = str(e.get("rel"))
            es.add((src, rel, dst))
        return es

    gt_edges = edge_set(gt)
    pr_edges = edge_set(pr)
    tp_edges = len(gt_edges & pr_edges)
    fp_edges = len(pr_edges - gt_edges)
    fn_edges = len(gt_edges - pr_edges)
    edge_metrics = prf(tp_edges, fp_edges, fn_edges)

    result = {
        "nodes": {"tp": tp_nodes, "fp": fp_nodes, "fn": fn_nodes, **node_metrics},
        "edges": {"tp": tp_edges, "fp": fp_edges, "fn": fn_edges, **edge_metrics},
    }
    _write_json(out_path, result)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="lna_es")
    sp = p.add_subparsers(dest="command")

    # abtest
    pab = sp.add_parser("abtest", help="Run a minimal AB test")
    pab.add_argument("-A", "--control-a", type=Path, required=True)
    pab.add_argument("-B", "--control-b", type=Path, required=True)
    pab.add_argument("-g", "--graph", type=Path, required=True)
    pab.add_argument("-o", "--out-dir", type=Path, required=True)

    # ops
    pops = sp.add_parser("ops", help="Operators related commands")
    pops_sp = pops.add_subparsers(dest="ops_cmd", required=True)
    pops_compile = pops_sp.add_parser("compile", help="Compile operator dialect")
    pops_compile.add_argument("operators", type=Path)
    pops_compile.add_argument("-o", "--out", type=Path, required=True)
    pops_validate = pops_sp.add_parser(
        "validate", help="Validate operators file (XML/JSON)"
    )
    pops_validate.add_argument("operators", type=Path)

    # preset
    ppreset = sp.add_parser("preset", help="Preset/dialect utilities")
    ppreset_sp = ppreset.add_subparsers(dest="preset_cmd", required=True)
    pp_load = ppreset_sp.add_parser(
        "load", help="Load AI-brain XML and emit summary cache"
    )
    pp_load.add_argument(
        "xml",
        type=Path,
        nargs="?",
        default=Path("packages/instant_dialogue/lna_axis0_sonnet4.xml"),
        help="Path to axis0 XML",
    )
    pp_load.add_argument(
        "-o",
        "--out",
        type=Path,
        default=Path("runs/cache/axis0_index.json"),
        help="Output JSON path",
    )

    # generate
    pgen = sp.add_parser("generate", help="Generate using graph and control")
    pgen.add_argument("-g", "--graph", type=Path, required=True)
    pgen.add_argument("-c", "--control", type=Path, required=True)
    pgen.add_argument("-o", "--out-dir", type=Path, required=True)

    # verify
    pver = sp.add_parser("verify", help="Verify a draft against control")
    pver.add_argument("-i", "--input", type=Path, required=True)
    pver.add_argument("-c", "--control", type=Path, required=True)
    pver.add_argument("-o", "--out", type=Path, required=True)

    # rewrite
    prew = sp.add_parser("rewrite", help="Rewrite a draft based on verification")
    prew.add_argument("-i", "--input", type=Path, required=True)
    prew.add_argument("-v", "--verify", type=Path, required=True)
    prew.add_argument("-o", "--out", type=Path, required=True)

    # audit
    paudit = sp.add_parser("audit", help="Emit audit card from metrics & verify")
    paudit.add_argument("-m", "--metrics", type=Path, required=True)
    paudit.add_argument("-v", "--verify", type=Path, required=True)
    paudit.add_argument("-o", "--out", type=Path, required=True)

    # graph tools
    peval = sp.add_parser("graph-eval", help="Evaluate predicted graph vs ground truth")
    peval.add_argument("-g", "--ground", type=Path, required=True)
    peval.add_argument("-p", "--pred", type=Path, required=True)
    peval.add_argument("-o", "--out", type=Path, required=True)

    prec = sp.add_parser(
        "graph-reconstruct", help="Reconstruct graph from control (toy)"
    )
    prec.add_argument("-c", "--control", type=Path, required=True)
    prec.add_argument("-o", "--out", type=Path, required=True)
    prec.add_argument(
        "--ai-brain", action="store_true", help="Enable AI-brain heuristics"
    )
    prec.add_argument(
        "--ai-threshold",
        type=float,
        default=1.0,
        help="Threshold for AI-brain candidate edges (0..1). Default 1.0 disables",
    )
    prec.add_argument(
        "--ontology-dir",
        type=Path,
        default=None,
        help="Optional ontology directory (.yml/.yaml files) to assist associations",
    )
    prec.add_argument(
        "--ontology-soft",
        action="store_true",
        help=(
            "Include SOFT invariants when ontology-dir is set (for recall). "
            "Overrides threshold rule"
        ),
    )
    prec.add_argument(
        "--ai-heuristics",
        action="store_true",
        help="Enable demo AI-brain heuristics (when --ai-brain). Default off",
    )

    # CTA (toy) commands
    pcta = sp.add_parser("cta", help="Toy CTA pipeline (demo-only)")
    pcta_sp = pcta.add_subparsers(dest="cta_cmd", required=True)
    pcta_an = pcta_sp.add_parser("analyze", help="Analyze text into toy CTA scores")
    pcta_an.add_argument("-i", "--input", type=Path, required=True)
    pcta_an.add_argument("-o", "--out", type=Path, required=True)
    pcta_an.add_argument("--ontology-dir", type=Path, default=None)

    pcta_g = pcta_sp.add_parser("to-graph", help="Convert CTA JSON to toy graph")
    pcta_g.add_argument("-i", "--input", type=Path, required=True)
    pcta_g.add_argument("-o", "--out", type=Path, required=True)
    pcta_g.add_argument("--threshold", type=float, default=0.5)

    return p


def main(argv: list[str] | None = None) -> int:
    # Auto-init: ensure axis0 cache exists once per workspace
    try:
        repo_root = Path(__file__).resolve().parents[1]
        cache = repo_root / "runs/cache/axis0_index.json"
        xml_default = repo_root / "packages/instant_dialogue/lna_axis0_sonnet4.xml"
        if not cache.exists() and xml_default.exists():
            cache.parent.mkdir(parents=True, exist_ok=True)
            cmd_preset_load(xml_default, cache)
    except Exception:
        pass

    parser = build_parser()
    ns = parser.parse_args(argv)

    if ns.command == "abtest":
        return cmd_abtest(
            ABTestArgs(
                control_a=ns.control_a,
                control_b=ns.control_b,
                graph=ns.graph,
                out_dir=ns.out_dir,
            )
        )

    if ns.command == "ops" and ns.ops_cmd == "compile":
        return cmd_ops_compile(ns.operators, ns.out)
    if ns.command == "ops" and ns.ops_cmd == "validate":
        return cmd_ops_validate(ns.operators)

    if ns.command == "preset" and ns.preset_cmd == "load":
        return cmd_preset_load(ns.xml, ns.out)

    if ns.command == "generate":
        return cmd_generate(ns.graph, ns.control, ns.out_dir)

    if ns.command == "verify":
        return cmd_verify(ns.input, ns.control, ns.out)

    if ns.command == "rewrite":
        return cmd_rewrite(ns.input, ns.verify, ns.out)

    if ns.command == "audit":
        return cmd_audit(ns.metrics, ns.verify, ns.out)

    if ns.command == "graph-eval":
        return cmd_graph_eval(ns.ground, ns.pred, ns.out)

    if ns.command == "graph-reconstruct":
        return cmd_graph_reconstruct(
            ns.control,
            ns.out,
            ns.ai_brain,
            ns.ai_threshold,
            ns.ontology_dir,
            ns.ai_heuristics,
        )

    if ns.command == "cta" and ns.cta_cmd == "analyze":
        return cmd_cta_analyze(ns.input, ns.out, ns.ontology_dir)

    if ns.command == "cta" and ns.cta_cmd == "to-graph":
        return cmd_cta_to_graph(ns.input, ns.out, ns.threshold)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
