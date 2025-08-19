#!/usr/bin/env python3
"""
Restore full text (graph-based reconstruction) from a raw input text file.
Steps:
- Run extractor.ingest_file to produce JSON/Cypher and obtain work_id
- Derive work_base (before first underscore)
- Run restorer.restore_text on the JSON artefact to get restored text
- Write restored text to the specified output file

Usage:
  ./venv/bin/python automation/restore_fulltext_from_input.py --input Text/7-Genre/05_...txt --out out/Genre05_SF_PipelineA_復元全文.txt
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# Project root and app paths
ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / 'lna-es-app'
if str(APPS_DIR) not in sys.path:
    sys.path.insert(0, str(APPS_DIR))

# Import extractor and restorer modules (apps.*)
from apps.extractor.extractor import ingest_file  # type: ignore
from apps.restorer.restorer import restore_text  # type: ignore
import time
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to the input .txt file')
    parser.add_argument('--out', required=True, help='Path to write restored full text')
    parser.add_argument('--outdir', default=str(ROOT / 'out'), help='Directory for cypher output')
    parser.add_argument('--datadir', default=str(ROOT / 'data'), help='Directory for JSON artefacts')
    args = parser.parse_args()

    inp_path = Path(args.input)
    if not inp_path.is_absolute():
        inp_path = (ROOT / inp_path).resolve()
    inp = str(inp_path)
    # Retry up to 3 times in case of transient JSON write/read races
    last_err = None
    restored = None
    for attempt in range(3):
        work_id, _cypher = ingest_file(inp, args.outdir, args.datadir)
        work_base = work_id.split('_')[0]
        try:
            restored = restore_text(work_base, args.datadir)
            break
        except json.JSONDecodeError as e:
            last_err = e
            time.sleep(0.2)
            continue
    if restored is None:
        raise last_err or RuntimeError("Failed to restore text after retries")
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(restored, encoding='utf-8')
    print(f"Restored full text written to {out_path}")


if __name__ == '__main__':
    main()
