"""
evaluate_restoration.py
=======================

This script evaluates the quality of text restoration by comparing an
original manuscript to its reconstructed counterpart.  It computes a
similarity score using Python's `difflib.SequenceMatcher`, which provides
a ratio between 0 and 1 indicating how closely the two texts match.  A
score of 1.0 means perfect correspondence, while 0.0 indicates no
similarity.

Usage::

    python evaluate_restoration.py --original original.txt --restored restored.txt

The script prints the similarity ratio as a percentage.
"""

import argparse
import difflib


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def calculate_similarity(original: str, restored: str) -> float:
    """
    Compute a similarity ratio between two strings using SequenceMatcher.
    The ratio is between 0 and 1, where 1 means identical.
    """
    matcher = difflib.SequenceMatcher(None, original, restored)
    return matcher.ratio()


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate restoration quality between two texts.")
    parser.add_argument("--original", required=True, help="Path to the original text file.")
    parser.add_argument("--restored", required=True, help="Path to the restored text file.")
    args = parser.parse_args()

    original_text = read_text(args.original)
    restored_text = read_text(args.restored)
    score = calculate_similarity(original_text, restored_text)
    print(f"Similarity: {score * 100:.2f}%")


if __name__ == "__main__":
    main()