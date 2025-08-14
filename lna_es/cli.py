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

    # generate
    pgen = sp.add_parser("generate", help="Generate using graph and control")
    pgen.add_argument("-g", "--graph", type=Path, required=True)
    pgen.add_argument("-c", "--control", type=Path, required=True)
    pgen.add_argument("-o", "--out-dir", type=Path, required=True)

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

    if ns.command == "generate":
        return cmd_generate(ns.graph, ns.control, ns.out_dir)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
