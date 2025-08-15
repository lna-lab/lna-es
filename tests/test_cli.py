from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable or "python3"


def run_cli(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [PY, "-m", "lna_es.cli", *args], cwd=ROOT, capture_output=True
    )


def test_help():
    cp = run_cli(["--help"])
    assert cp.returncode == 0
    assert b"abtest" in cp.stdout


def test_generate_pipeline(tmp_path: Path):
    graph = ROOT / "examples/graph.sample.json"
    control = ROOT / "examples/control_A.json"

    out_dir = tmp_path / "A"

    cp_gen = run_cli(
        ["generate", "-g", str(graph), "-c", str(control), "-o", str(out_dir)]
    )
    assert cp_gen.returncode == 0
    assert (out_dir / "draft.txt").exists()
    assert (out_dir / "metrics.json").exists()

    cp_ver = run_cli(
        [
            "verify",
            "-i",
            str(out_dir / "draft.txt"),
            "-c",
            str(control),
            "-o",
            str(out_dir / "verify.json"),
        ]
    )
    assert cp_ver.returncode == 0
    verify = json.loads((out_dir / "verify.json").read_text("utf-8"))
    assert "metrics" in verify

    cp_rew = run_cli(
        [
            "rewrite",
            "-i",
            str(out_dir / "draft.txt"),
            "-v",
            str(out_dir / "verify.json"),
            "-o",
            str(out_dir / "fixed.txt"),
        ]
    )
    assert cp_rew.returncode == 0
    assert (out_dir / "fixed.txt").exists()

    cp_audit = run_cli(
        [
            "audit",
            "-m",
            str(out_dir / "metrics.json"),
            "-v",
            str(out_dir / "verify.json"),
            "-o",
            str(out_dir / "audit_card.md"),
        ]
    )
    assert cp_audit.returncode == 0
    assert (out_dir / "audit_card.md").exists()


def test_ops_validate_examples():
    xml = ROOT / "examples/operators.sample.xml"
    jsn = ROOT / "examples/operator.sample.json"

    cp_xml = run_cli(["ops", "validate", str(xml)])
    assert cp_xml.returncode == 0
    assert b"OK: XML valid" in cp_xml.stdout

    cp_jsn = run_cli(["ops", "validate", str(jsn)])
    assert cp_jsn.returncode == 0
    assert b"OK: JSON valid" in cp_jsn.stdout
