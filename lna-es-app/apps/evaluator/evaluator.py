#!/usr/bin/env python3
"""
evaluator.py
----------------

This module provides a simple evaluation of a restored summary against the
original text.  It computes the length ratio and Jaccard similarity of
token sets as rudimentary proxies for the more complex metrics described in
the requirements specification.
"""

import argparse
from pathlib import Path
import re


def tokenize(text: str) -> list:
    return re.findall(r"\b\w+\b", text.lower())


def evaluate(original_path: str, restored_path: str) -> dict:
    with open(original_path, encoding='utf-8', errors='ignore') as f:
        orig_text = f.read()
    with open(restored_path, encoding='utf-8', errors='ignore') as f:
        rest_text = f.read()
    orig_tokens = tokenize(orig_text)
    rest_tokens = tokenize(rest_text)
    # Length ratio
    len_ratio = len(rest_tokens) / len(orig_tokens) if orig_tokens else 0.0
    # Jaccard similarity
    set_orig = set(orig_tokens)
    set_rest = set(rest_tokens)
    intersection = set_orig.intersection(set_rest)
    union = set_orig.union(set_rest)
    jaccard = len(intersection) / len(union) if union else 0.0
    return {
        'original_tokens': len(orig_tokens),
        'restored_tokens': len(rest_tokens),
        'length_ratio': len_ratio,
        'jaccard_similarity': jaccard
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Evaluate restored text against the original.')
    parser.add_argument('--orig', required=True, help='Path to the original text file')
    parser.add_argument('--rest', required=True, help='Path to the restored text file')
    args = parser.parse_args()
    results = evaluate(args.orig, args.rest)
    print("Evaluation results:\n")
    for k, v in results.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    main()