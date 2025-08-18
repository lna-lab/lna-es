#!/usr/bin/env python3
"""
Triple Validation Classifier (prototype)

Uses EnhancedClassificationSystem as primary analysis, and KindleJSONValidator
as tertiary validation. Provides helpers to compute a consensus and confidence.
"""
from typing import Dict, Any
from pathlib import Path

from src.enhanced_classification import EnhancedClassificationSystem
from src.kindle_validation import KindleJSONValidator


class TripleValidationClassifier:
    def __init__(self) -> None:
        self.primary = EnhancedClassificationSystem()
        self.kindle_validator = KindleJSONValidator()

    def classify_with_triple_validation(self, text: str) -> Dict[str, Any]:
        tokens = self._simple_tokens(text)
        # Primary: enhanced classification (contains NDC/Kindle/ontology)
        primary = self.primary.classify_text_enhanced(text, tokens)
        # Secondary: reuse NDC section from primary
        ndc_result = {"ndc": primary.get("ndc", {}).get("classifications", [])}
        # Tertiary: Kindle JSON validator
        kindle_categories = self.kindle_validator.analyze_kindle_patterns(text)
        validation_result = {
            "cta_kindle_alignment": self.kindle_validator.check_cta_kindle_consistency(primary, kindle_categories),
            "ndc_kindle_alignment": self.kindle_validator.check_ndc_kindle_consistency(primary, kindle_categories),
            "triple_consensus": self.kindle_validator.calculate_triple_consensus(primary, primary, kindle_categories),
        }
        confidence = self._calculate_triple_confidence(primary, validation_result)
        return {
            "primary": primary,
            "tertiary_kindle": {
                "kindle_classification": kindle_categories,
                "validation_result": validation_result,
                "confidence_boost": self.kindle_validator.calculate_validation_boost(validation_result),
            },
            "consensus_classification": self._consensus_label(primary, kindle_categories),
            "confidence_score": confidence,
        }

    def _calculate_triple_confidence(self, primary: Dict[str, Any], validation_result: Dict[str, Any]) -> float:
        base = primary.get("confidence", 0.0)
        boost = self.kindle_validator.calculate_validation_boost(validation_result)
        return float(base + boost)

    @staticmethod
    def _consensus_label(primary: Dict[str, Any], kindle_cats):
        # Favor agreement between primary.kindle top and validator top; otherwise fall back to primary kindle
        pk = primary.get("kindle", {}).get("classifications", [])
        ptop = pk[0]["category"] if pk else None
        vtop = kindle_cats[0]["category"] if kindle_cats else None
        label = vtop if (ptop and vtop and (ptop == vtop)) else (ptop or vtop)
        return {"kindle": label}

    @staticmethod
    def _simple_tokens(text: str):
        import re
        jp = re.findall(r"[\u3040-\u30FF\u4E00-\u9FAF]+", text)
        en = re.findall(r"[A-Za-z0-9_]+", text)
        return jp + en

