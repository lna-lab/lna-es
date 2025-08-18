#!/usr/bin/env python3
"""
Kindle JSON Validation Engine

Loads enhanced Kindle JSON and provides a cross-validation helper that
analyzes text and compares against existing classification results to
produce simple alignment/consensus metrics.
"""
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json


class KindleJSONValidator:
    def __init__(self, data_dir: Path | None = None) -> None:
        self.data_dir = data_dir or Path(__file__).parent
        self.kindle_data = self._load_kindle_json()

    def _load_kindle_json(self) -> List[Dict[str, Any]]:
        path = self.data_dir / "kindle_enhanced.json"
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                processed = []
                for cat in data.get("categories", []):
                    keywords = [cat.get("name", "")] + cat.get("children", [])
                    processed.append({"category": cat.get("name", ""), "keywords": keywords})
                return processed
            except Exception:
                pass
        # Fallback minimal set
        return [
            {"category": "文学・評論", "keywords": ["文学", "小説", "物語", "評論", "詩", "恋愛"]},
            {"category": "科学・テクノロジー", "keywords": ["科学", "技術", "分子", "結合", "実験", "研究"]},
            {"category": "ビジネス", "keywords": ["経営", "戦略", "市場", "マーケティング", "分析"]},
        ]

    def analyze_kindle_patterns(self, text: str) -> List[Dict[str, Any]]:
        tokens = self._simple_tokens(text)
        scores: Dict[str, Dict[str, Any]] = {}
        for cat in self.kindle_data:
            name = cat.get("category", "")
            kwords = cat.get("keywords", [])
            matches = sum(1 for t in tokens for k in kwords if t and k and (k in t or t in k))
            score = matches / max(1, len(tokens))
            scores[name] = {"category": name, "score": score, "matches": matches}
        return sorted(scores.values(), key=lambda x: x["score"], reverse=True)

    def check_cta_kindle_consistency(self, cta_result: Dict[str, Any], kindle_cats: List[Dict[str, Any]]) -> float:
        # Compare top Kindle category with CTA ontology emphasis (heuristic):
        if not kindle_cats:
            return 0.0
        top_k = kindle_cats[0]["category"]
        onto = (cta_result or {}).get("ontology_weights") or {}
        # Simple mapping: literature-like aligns with narrative/emotion, science with natural/causality, business with action/relationship
        if "文" in top_k or "Literature" in top_k:
            keys = ["narrative_structure", "emotion", "character_function"]
        elif "科学" in top_k or "Technology" in top_k:
            keys = ["natural", "causality", "temporal"]
        elif "ビジネス" in top_k or "Business" in top_k:
            keys = ["action", "relationship", "causality"]
        else:
            keys = list(onto.keys())[:3]
        val = sum(onto.get(k, 0.0) for k in keys)
        return min(1.0, val) if onto else 0.0

    def check_ndc_kindle_consistency(self, ndc_result: Dict[str, Any], kindle_cats: List[Dict[str, Any]]) -> float:
        if not kindle_cats:
            return 0.0
        top_k = kindle_cats[0]["category"]
        ndc_top = ((ndc_result or {}).get("ndc", {}) or {}).get("classifications", [])
        ndc_top_code = ndc_top[0]["code"] if ndc_top else ""
        # Literature alignment
        if ("文" in top_k or "Literature" in top_k) and ndc_top_code.startswith("9"):
            return 1.0
        # Science alignment
        if ("科学" in top_k or "Science" in top_k) and ndc_top_code.startswith("4"):
            return 1.0
        # Business alignment
        if ("ビジネス" in top_k or "Business" in top_k) and ndc_top_code.startswith("6"):
            return 1.0
        return 0.0

    def calculate_triple_consensus(self, cta_result: Dict[str, Any], ndc_result: Dict[str, Any], kindle_cats: List[Dict[str, Any]]) -> float:
        # Simple consensus = average of two alignments
        a = self.check_cta_kindle_consistency(cta_result, kindle_cats)
        b = self.check_ndc_kindle_consistency(ndc_result, kindle_cats)
        return (a + b) / 2.0

    def calculate_validation_boost(self, validation: Dict[str, Any]) -> float:
        # If both alignments are strong, boost confidence
        cta_k = validation.get("cta_kindle_alignment", 0.0)
        ndc_k = validation.get("ndc_kindle_alignment", 0.0)
        return 0.1 if (cta_k > 0.5 and ndc_k > 0.5) else 0.0

    @staticmethod
    def _simple_tokens(text: str) -> List[str]:
        import re
        jp = re.findall(r"[\u3040-\u30FF\u4E00-\u9FAF]+", text)
        en = re.findall(r"[A-Za-z0-9_]+", text)
        return jp + en

