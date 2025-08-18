#!/usr/bin/env python3
"""
Run a single safe extractor invocation via Maya's helper, without starting the API server.
Usage:
  ./venv/bin/python automation/maya_extractor_once.py --target test_sample.txt
"""
import argparse
import json
from pathlib import Path

from maya_api import safe_extractor_run  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True)
    args = parser.parse_args()
    result = safe_extractor_run(args.target)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
