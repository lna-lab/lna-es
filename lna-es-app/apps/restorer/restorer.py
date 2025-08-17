#!/usr/bin/env python3
"""
restorer.py
---------------

This module reconstructs a human‑readable summary from the JSON artefacts
produced by the extractor.  It uses the stored key terms for each segment to
generate a short synopsis.  The original text is neither required nor
referenced.
"""

import argparse
import json
from pathlib import Path


def restore_text(doc_id: str, data_dir: str) -> str:
    """Generate a restored summary for the given work id.

    Args:
        doc_id: The base identifier of the work (as returned by the extractor).
        data_dir: Directory containing JSON artefacts.

    Returns:
        A reconstructed summary as a single string.
    """
    data_path = Path(data_dir) / f"{doc_id}.json"
    if not data_path.exists():
        raise FileNotFoundError(f"Could not find data file for work id {doc_id}")
    with open(data_path, encoding='utf-8') as f:
        data = json.load(f)
    segments = data.get('segments', [])
    # Sort segments by order
    segments_sorted = sorted(segments, key=lambda x: x['order'])
    summary_parts = []
    for seg in segments_sorted:
        terms = seg.get('key_terms', [])
        if terms:
            summary_parts.append(' '.join(terms))
    return '\n'.join(summary_parts)


def main() -> None:
    parser = argparse.ArgumentParser(description='Restore a summary from LNA‑ES graph artefacts.')
    parser.add_argument('--doc', required=True, help='Work base identifier to restore')
    parser.add_argument('--datadir', default='data', help='Directory containing JSON artefacts')
    parser.add_argument('--output', default=None, help='Output file for restored text')
    args = parser.parse_args()
    summary = restore_text(args.doc, args.datadir)
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"Restored text written to {args.output}")
    else:
        print(summary)


if __name__ == '__main__':
    main()