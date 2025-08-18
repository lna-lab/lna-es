#!/usr/bin/env python3
"""
Simple CLI for LNA-ES v3.x utilities.

Subcommands:
- classify: Enhanced NDC/Kindle classification + ontology weights
- embed: Generate embeddings via VectorEmbeddingManager
- ndc: NDC mapping using NDCOntologyMapper (requires LNA analysis input)
- models: Show embedding model load state

Usage examples:
- python src/cli.py classify --text "吾輩は猫である"
- python src/cli.py embed --text "Hello world"
- python src/cli.py ndc --text "川の流れは絶えることなく…" --dominant temporal_aesthetic_narrative --aesthetic 0.85
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Ensure project root is on sys.path so imports work when executed as a script
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Local imports (work with both `python -m src.cli` and `python src/cli.py`)
try:
    from src.enhanced_classification import EnhancedClassificationSystem
    from src.vector_embeddings import VectorEmbeddingManager
    from src.classification_system import NDCOntologyMapper
except ModuleNotFoundError:
    # Fallback to direct module names if run from within src directory context
    from enhanced_classification import EnhancedClassificationSystem
    from vector_embeddings import VectorEmbeddingManager
    from classification_system import NDCOntologyMapper


def read_text_input(args: argparse.Namespace) -> str:
    if getattr(args, "text", None):
        return args.text
    if getattr(args, "file", None):
        return Path(args.file).read_text(encoding="utf-8")
    # Fallback to stdin
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("No input provided. Use --text, --file, or pipe via stdin.")


def tokenize_text(text: str) -> List[str]:
    """Lightweight tokenization for Japanese + Latin text.

    - Extracts Japanese character runs (Hiragana/Katakana/Kanji)
    - Extracts alphanumeric words for Latin scripts
    """
    import re

    jp_tokens = re.findall(r"[\u3040-\u30FF\u4E00-\u9FAF]+", text)
    latin_tokens = re.findall(r"[A-Za-z0-9_]+", text)
    return jp_tokens + latin_tokens


def cmd_classify(args: argparse.Namespace) -> int:
    text = read_text_input(args)
    tokens = tokenize_text(text)

    system = EnhancedClassificationSystem()
    result = system.classify_text_enhanced(text, tokens)

    if args.pretty:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False))
    return 0


def cmd_embed(args: argparse.Namespace) -> int:
    text = read_text_input(args)

    manager = VectorEmbeddingManager()
    result = manager.embed_text(text)

    if args.pretty:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False))
    return 0


def cmd_models(args: argparse.Namespace) -> int:
    manager = VectorEmbeddingManager()
    info = manager.get_model_info()
    if args.pretty:
        print(json.dumps(info, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(info, ensure_ascii=False))
    return 0


def cmd_ndc(args: argparse.Namespace) -> int:
    text = read_text_input(args)

    # Load or synthesize LNA analysis
    lna_analysis: Dict[str, Any]
    if args.lna:
        lna_analysis = json.loads(Path(args.lna).read_text(encoding="utf-8"))
    else:
        lna_analysis = {
            "dominant_analysis": args.dominant or "temporal_aesthetic_narrative",
            "aesthetic_quality": float(args.aesthetic) if args.aesthetic is not None else 0.75,
        }

    mapper = NDCOntologyMapper()
    result = mapper.classify_text_by_ndc(text, lna_analysis)

    if args.pretty:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="lna-cli", description="LNA-ES command-line tools")
    sub = p.add_subparsers(dest="command", required=True)

    # classify
    pc = sub.add_parser("classify", help="Enhanced NDC/Kindle classification")
    pc.add_argument("--text", help="Input text")
    pc.add_argument("--file", help="Path to input text file")
    pc.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    pc.set_defaults(func=cmd_classify)

    # embed
    pe = sub.add_parser("embed", help="Generate embeddings (RURI/Qwen or fallbacks)")
    pe.add_argument("--text", help="Input text")
    pe.add_argument("--file", help="Path to input text file")
    pe.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    pe.set_defaults(func=cmd_embed)

    # models
    pm = sub.add_parser("models", help="Show embedding model info")
    pm.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    pm.set_defaults(func=cmd_models)

    # ndc
    pn = sub.add_parser("ndc", help="NDC classification via NDCOntologyMapper")
    pn.add_argument("--text", help="Input text")
    pn.add_argument("--file", help="Path to input text file")
    pn.add_argument("--lna", help="Path to LNA analysis JSON file")
    pn.add_argument("--dominant", help="Dominant analysis label when --lna not provided")
    pn.add_argument("--aesthetic", type=float, help="Aesthetic quality [0-1] when --lna not provided")
    pn.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    pn.set_defaults(func=cmd_ndc)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
