from __future__ import annotations

import argparse
import json
import sys
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

    return p


def main(argv: list[str] | None = None) -> int:
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

    if ns.command == "generate":
        return cmd_generate(ns.graph, ns.control, ns.out_dir)

    if ns.command == "verify":
        return cmd_verify(ns.input, ns.control, ns.out)

    if ns.command == "rewrite":
        return cmd_rewrite(ns.input, ns.verify, ns.out)

    if ns.command == "audit":
        return cmd_audit(ns.metrics, ns.verify, ns.out)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
