#!/usr/bin/env python3
"""
動的ユーザー補正システム
========================

ユーザーの出力指定に応じてリアルタイムで補正値を調整する
革新的な動的重みづけシステム

例:
- 法律文章 → 中学生向け出力
- 哲学論文 → カジュアルな会話調
- 技術文書 → 詩的表現で
- 詩的作品 → 論理的説明調

Based on Ken's insight: "ユーザーからの指定があったときに補正がかかる"
"""

import json
import time
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import logging

@dataclass
class UserOutputOrder:
    """ユーザー出力オーダー"""
    original_genre: str                    # 元ジャンル
    target_style: str                      # 目標スタイル
    target_audience: str                   # 対象読者層
    complexity_level: str                  # 複雑度レベル (simple/moderate/complex)
    tone: str                             # 語調 (formal/casual/poetic/technical)
    specific_requirements: List[str]       # 具体的要求
    correction_strength: float             # 補正強度 (0.0-1.0)

@dataclass
class DynamicCorrectionProfile:
    """動的補正プロファイル"""
    correction_id: str
    user_order: UserOutputOrder
    
    # 計算された補正値
    genre_correction_weights: Dict[str, float]
    style_correction_weights: Dict[str, float]
    complexity_corrections: Dict[str, float]
    tone_corrections: Dict[str, float]
    
    # 予測効果
    predicted_transformation_quality: float
    estimated_accuracy_change: float
    user_satisfaction_prediction: float
    
    # メタデータ
    created_timestamp: float
    correction_reasoning: List[str]

class DynamicUserCorrectionSystem:
    """
    動的ユーザー補正システム
    ユーザーオーダーに応じてリアルタイム補正実行
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # 補正マトリックス初期化
        self.genre_style_matrix = self._initialize_genre_style_matrix()
        self.complexity_adjustments = self._initialize_complexity_adjustments()
        self.tone_modifiers = self._initialize_tone_modifiers()
        self.audience_adaptations = self._initialize_audience_adaptations()
        
        print("🎛️ 動的ユーザー補正システム初期化完了")
        print("   リアルタイム補正機能準備完了")
        
    def _initialize_genre_style_matrix(self) -> Dict[str, Dict[str, Dict[str, float]]]:
        """ジャンル-スタイル変換マトリックス"""
        return {
            # 法律文章の変換
            "legal_document": {
                "casual_explanation": {
                    "cta_complexity": -0.6,        # 複雑さを大幅削減
                    "cta_formality": -0.7,         # 堅い表現を削減
                    "cta_accessibility": +0.8,     # わかりやすさ向上
                    "onto_jargon": -0.9,          # 専門用語削減
                    "onto_everyday": +0.7,        # 日常語彙増加
                },
                "middle_school_friendly": {
                    "cta_complexity": -0.8,
                    "cta_formality": -0.8,
                    "cta_accessibility": +0.9,
                    "cta_simplicity": +0.8,
                    "onto_jargon": -0.95,
                    "onto_educational": +0.8,
                },
                "storytelling_style": {
                    "cta_narrative": +0.7,
                    "cta_formality": -0.6,
                    "cta_emotion": +0.5,
                    "onto_character": +0.6,
                    "onto_scene_setting": +0.5,
                }
            },
            
            # 哲学論文の変換
            "philosophical_discourse": {
                "casual_conversation": {
                    "cta_formality": -0.7,
                    "cta_accessibility": +0.6,
                    "cta_conversational": +0.8,
                    "onto_abstract": -0.5,
                    "onto_everyday": +0.6,
                },
                "poetic_expression": {
                    "cta_metaphysical": +0.3,
                    "cta_poetic": +0.9,
                    "cta_aesthetic": +0.8,
                    "onto_metaphor": +0.7,
                    "onto_beauty": +0.6,
                }
            },
            
            # 技術文書の変換
            "technical_document": {
                "poetic_style": {
                    "cta_technical": -0.6,
                    "cta_poetic": +0.8,
                    "cta_aesthetic": +0.7,
                    "cta_metaphorical": +0.6,
                    "onto_beauty": +0.5,
                },
                "beginner_friendly": {
                    "cta_complexity": -0.7,
                    "cta_accessibility": +0.8,
                    "cta_educational": +0.7,
                    "onto_jargon": -0.8,
                    "onto_explanatory": +0.8,
                }
            },
            
            # ロマンティック物語の変換
            "romantic_narrative": {
                "analytical_style": {
                    "cta_emotion": -0.4,
                    "cta_analytical": +0.7,
                    "cta_logical": +0.6,
                    "onto_analysis": +0.6,
                    "onto_structure": +0.5,
                },
                "academic_paper": {
                    "cta_formality": +0.8,
                    "cta_emotion": -0.6,
                    "cta_analytical": +0.8,
                    "cta_academic": +0.9,
                    "onto_scholarly": +0.7,
                }
            }
        }
    
    def _initialize_complexity_adjustments(self) -> Dict[str, Dict[str, float]]:
        """複雑度調整パラメータ"""
        return {
            "simple": {
                "cta_complexity": -0.8,
                "cta_simplicity": +0.9,
                "cta_accessibility": +0.8,
                "cta_clarity": +0.7,
                "onto_basic": +0.8,
                "onto_advanced": -0.7,
            },
            "moderate": {
                "cta_complexity": -0.3,
                "cta_simplicity": +0.4,
                "cta_accessibility": +0.5,
                "cta_depth": +0.2,
                "onto_intermediate": +0.6,
            },
            "complex": {
                "cta_complexity": +0.3,
                "cta_sophistication": +0.7,
                "cta_depth": +0.8,
                "cta_nuance": +0.6,
                "onto_advanced": +0.7,
            }
        }
    
    def _initialize_tone_modifiers(self) -> Dict[str, Dict[str, float]]:
        """語調モディファイアー"""
        return {
            "formal": {
                "cta_formality": +0.8,
                "cta_respectful": +0.7,
                "cta_professional": +0.8,
                "onto_formal_register": +0.8,
            },
            "casual": {
                "cta_formality": -0.7,
                "cta_conversational": +0.8,
                "cta_relaxed": +0.7,
                "onto_colloquial": +0.6,
            },
            "poetic": {
                "cta_poetic": +0.9,
                "cta_aesthetic": +0.8,
                "cta_metaphorical": +0.7,
                "cta_lyrical": +0.8,
                "onto_beauty": +0.6,
            },
            "technical": {
                "cta_technical": +0.8,
                "cta_precise": +0.8,
                "cta_analytical": +0.7,
                "onto_technical": +0.8,
            }
        }
    
    def _initialize_audience_adaptations(self) -> Dict[str, Dict[str, float]]:
        """対象読者層適応パラメータ"""
        return {
            "children": {
                "cta_simplicity": +0.9,
                "cta_playful": +0.7,
                "cta_engaging": +0.8,
                "cta_complexity": -0.9,
                "onto_educational": +0.6,
            },
            "teenagers": {
                "cta_engaging": +0.8,
                "cta_relatable": +0.7,
                "cta_contemporary": +0.6,
                "cta_formality": -0.5,
                "onto_youth_culture": +0.5,
            },
            "adults": {
                "cta_mature": +0.6,
                "cta_sophisticated": +0.5,
                "cta_professional": +0.4,
            },
            "experts": {
                "cta_sophisticated": +0.8,
                "cta_precise": +0.8,
                "cta_technical": +0.7,
                "onto_advanced": +0.8,
            },
            "general_public": {
                "cta_accessibility": +0.8,
                "cta_clarity": +0.7,
                "cta_balanced": +0.6,
            }
        }
    
    def generate_dynamic_correction(self, user_order: UserOutputOrder) -> DynamicCorrectionProfile:
        """
        ユーザーオーダーに基づく動的補正プロファイル生成
        """
        print(f"🎯 動的補正生成: {user_order.original_genre} → {user_order.target_style}")
        print("=" * 60)
        
        correction_id = self._generate_correction_id()
        
        # === Phase 1: ジャンル-スタイル補正計算 ===
        print("📊 Phase 1: ジャンル-スタイル変換補正計算")
        genre_corrections = self._calculate_genre_style_corrections(
            user_order.original_genre, user_order.target_style
        )
        
        # === Phase 2: スタイル補正計算 ===
        print("🎨 Phase 2: スタイル特化補正計算")
        style_corrections = self._calculate_style_corrections(user_order)
        
        # === Phase 3: 複雑度補正計算 ===
        print("⚙️ Phase 3: 複雑度レベル補正計算")
        complexity_corrections = self._calculate_complexity_corrections(user_order.complexity_level)
        
        # === Phase 4: 語調補正計算 ===
        print("🗣️ Phase 4: 語調モディファイア計算")
        tone_corrections = self._calculate_tone_corrections(user_order.tone)
        
        # === Phase 5: 対象読者適応補正 ===
        print("👥 Phase 5: 対象読者適応補正計算")
        audience_corrections = self._calculate_audience_corrections(user_order.target_audience)
        
        # === Phase 6: 補正強度適用 ===
        print("💪 Phase 6: 補正強度適用")
        final_corrections = self._apply_correction_strength(
            {**genre_corrections, **style_corrections, **complexity_corrections, 
             **tone_corrections, **audience_corrections},
            user_order.correction_strength
        )
        
        # === Phase 7: 効果予測 ===
        transformation_quality = self._predict_transformation_quality(final_corrections, user_order)
        accuracy_change = self._estimate_accuracy_change(final_corrections)
        satisfaction_prediction = self._predict_user_satisfaction(transformation_quality, user_order)
        
        # === Phase 8: 推論説明生成 ===
        reasoning = self._generate_correction_reasoning(user_order, final_corrections)
        
        profile = DynamicCorrectionProfile(
            correction_id=correction_id,
            user_order=user_order,
            genre_correction_weights=genre_corrections,
            style_correction_weights={**style_corrections, **complexity_corrections, **tone_corrections},
            complexity_corrections=complexity_corrections,
            tone_corrections=tone_corrections,
            predicted_transformation_quality=transformation_quality,
            estimated_accuracy_change=accuracy_change,
            user_satisfaction_prediction=satisfaction_prediction,
            created_timestamp=time.time(),
            correction_reasoning=reasoning
        )
        
        print(f"\n📈 補正効果予測:")
        print(f"   変換品質: {transformation_quality:.3f}")
        print(f"   精度変化: {accuracy_change:+.3f}")
        print(f"   ユーザー満足度予測: {satisfaction_prediction:.3f}")
        
        print("\n🎉 動的補正プロファイル生成完了!")
        
        return profile
    
    def apply_corrections_to_system(self, corrections: DynamicCorrectionProfile, 
                                  base_weighting: Dict[str, float]) -> Dict[str, float]:
        """
        動的補正をシステム重みづけに適用
        """
        print("🔧 動的補正適用実行")
        
        adjusted_weights = base_weighting.copy()
        
        # 各補正を段階的に適用
        all_corrections = {
            **corrections.genre_correction_weights,
            **corrections.style_correction_weights,
            **corrections.complexity_corrections,
            **corrections.tone_corrections
        }
        
        applied_count = 0
        for dimension, correction_value in all_corrections.items():
            if dimension in adjusted_weights:
                original_weight = adjusted_weights[dimension]
                adjusted_weights[dimension] = max(0.1, min(2.0, original_weight + correction_value))
                
                if abs(correction_value) > 0.1:  # 有意な補正のみカウント
                    applied_count += 1
                    print(f"   📏 {dimension}: {original_weight:.3f} → {adjusted_weights[dimension]:.3f} ({correction_value:+.3f})")
        
        print(f"✅ {applied_count}次元に補正適用完了")
        
        return adjusted_weights
    
    def create_user_friendly_explanation(self, corrections: DynamicCorrectionProfile) -> str:
        """
        ユーザー向け説明文生成
        """
        order = corrections.user_order
        
        explanation = f"""
🎯 **変換内容**
元のスタイル: {order.original_genre}
目標スタイル: {order.target_style}
対象読者: {order.target_audience}
複雑度レベル: {order.complexity_level}

🔧 **適用される主な補正**
"""
        
        # 主要な補正を抽出
        all_corrections = {**corrections.genre_correction_weights, **corrections.style_correction_weights}
        significant_corrections = {k: v for k, v in all_corrections.items() if abs(v) > 0.3}
        
        for dimension, value in sorted(significant_corrections.items(), key=lambda x: abs(x[1]), reverse=True)[:5]:
            direction = "強化" if value > 0 else "抑制"
            explanation += f"• {dimension}: {direction} (補正値: {value:+.2f})\n"
        
        explanation += f"""
📊 **予測効果**
変換品質: {corrections.predicted_transformation_quality:.1%}
ユーザー満足度予測: {corrections.user_satisfaction_prediction:.1%}

💡 **推奨事項**
"""
        
        for reason in corrections.correction_reasoning[:3]:
            explanation += f"• {reason}\n"
        
        return explanation
    
    def _calculate_genre_style_corrections(self, original_genre: str, target_style: str) -> Dict[str, float]:
        """ジャンル-スタイル変換補正計算"""
        if original_genre in self.genre_style_matrix:
            genre_data = self.genre_style_matrix[original_genre]
            if target_style in genre_data:
                corrections = genre_data[target_style].copy()
                print(f"   適用補正数: {len(corrections)}")
                return corrections
        
        # フォールバック: 一般的な補正
        print("   汎用補正適用")
        return self._generate_fallback_corrections(original_genre, target_style)
    
    def _generate_fallback_corrections(self, original_genre: str, target_style: str) -> Dict[str, float]:
        """汎用補正生成"""
        corrections = {}
        
        # 簡易的なルールベース補正
        if "casual" in target_style:
            corrections["cta_formality"] = -0.5
            corrections["cta_conversational"] = +0.6
        
        if "simple" in target_style or "beginner" in target_style:
            corrections["cta_complexity"] = -0.6
            corrections["cta_accessibility"] = +0.7
        
        if "poetic" in target_style:
            corrections["cta_poetic"] = +0.7
            corrections["cta_aesthetic"] = +0.6
        
        return corrections
    
    def _calculate_style_corrections(self, user_order: UserOutputOrder) -> Dict[str, float]:
        """スタイル特化補正計算"""
        corrections = {}
        
        # 具体的要求に基づく補正
        for requirement in user_order.specific_requirements:
            if "わかりやすく" in requirement or "簡単に" in requirement:
                corrections["cta_accessibility"] = corrections.get("cta_accessibility", 0) + 0.5
                corrections["cta_simplicity"] = corrections.get("cta_simplicity", 0) + 0.4
            
            if "詳しく" in requirement or "専門的に" in requirement:
                corrections["cta_depth"] = corrections.get("cta_depth", 0) + 0.6
                corrections["cta_technical"] = corrections.get("cta_technical", 0) + 0.5
            
            if "感情的に" in requirement or "心に響く" in requirement:
                corrections["cta_emotion"] = corrections.get("cta_emotion", 0) + 0.6
                corrections["cta_empathetic"] = corrections.get("cta_empathetic", 0) + 0.5
        
        return corrections
    
    def _calculate_complexity_corrections(self, complexity_level: str) -> Dict[str, float]:
        """複雑度補正計算"""
        return self.complexity_adjustments.get(complexity_level, {})
    
    def _calculate_tone_corrections(self, tone: str) -> Dict[str, float]:
        """語調補正計算"""
        return self.tone_modifiers.get(tone, {})
    
    def _calculate_audience_corrections(self, target_audience: str) -> Dict[str, float]:
        """対象読者補正計算"""
        # 複数の読者層をサポート
        audience_words = target_audience.lower().split()
        corrections = {}
        
        for audience_type, adjustments in self.audience_adaptations.items():
            if audience_type in target_audience.lower() or any(word in audience_words for word in audience_type.split("_")):
                for dimension, value in adjustments.items():
                    corrections[dimension] = corrections.get(dimension, 0) + value
        
        return corrections
    
    def _apply_correction_strength(self, corrections: Dict[str, float], strength: float) -> Dict[str, float]:
        """補正強度適用"""
        return {dimension: value * strength for dimension, value in corrections.items()}
    
    def _predict_transformation_quality(self, corrections: Dict[str, float], user_order: UserOutputOrder) -> float:
        """変換品質予測"""
        # 補正の多様性と強度に基づく品質予測
        correction_diversity = len([v for v in corrections.values() if abs(v) > 0.1])
        average_correction_strength = np.mean([abs(v) for v in corrections.values()]) if corrections else 0
        
        base_quality = 0.7
        diversity_bonus = min(0.2, correction_diversity * 0.02)
        strength_bonus = min(0.1, average_correction_strength * 0.1)
        
        return min(1.0, base_quality + diversity_bonus + strength_bonus)
    
    def _estimate_accuracy_change(self, corrections: Dict[str, float]) -> float:
        """精度変化予測"""
        # 大きな補正は一時的に精度を下げる可能性
        large_corrections = [abs(v) for v in corrections.values() if abs(v) > 0.5]
        
        if large_corrections:
            accuracy_impact = -len(large_corrections) * 0.02
        else:
            accuracy_impact = 0.01  # 小さな改善
        
        return max(-0.1, min(0.05, accuracy_impact))
    
    def _predict_user_satisfaction(self, transformation_quality: float, user_order: UserOutputOrder) -> float:
        """ユーザー満足度予測"""
        base_satisfaction = transformation_quality
        
        # 具体的要求の充足度ボーナス
        requirement_bonus = len(user_order.specific_requirements) * 0.02
        
        # 補正強度による調整
        if user_order.correction_strength > 0.8:
            strength_bonus = 0.05  # 強い補正を求める場合の満足度向上
        else:
            strength_bonus = 0.02
        
        return min(1.0, base_satisfaction + requirement_bonus + strength_bonus)
    
    def _generate_correction_reasoning(self, user_order: UserOutputOrder, 
                                     corrections: Dict[str, float]) -> List[str]:
        """補正根拠説明生成"""
        reasoning = []
        
        # 変換方向の説明
        reasoning.append(f"{user_order.original_genre}から{user_order.target_style}への変換を実施")
        
        # 主要補正の説明
        major_corrections = {k: v for k, v in corrections.items() if abs(v) > 0.4}
        if major_corrections:
            strongest_correction = max(major_corrections.keys(), key=lambda k: abs(major_corrections[k]))
            direction = "強化" if major_corrections[strongest_correction] > 0 else "抑制"
            reasoning.append(f"{strongest_correction}次元を重点的に{direction}して変換効果を最大化")
        
        # 対象読者への配慮
        if user_order.target_audience:
            reasoning.append(f"{user_order.target_audience}に適した表現レベルに調整")
        
        # 複雑度調整の説明
        if user_order.complexity_level == "simple":
            reasoning.append("理解しやすさを優先して複雑な表現を簡素化")
        elif user_order.complexity_level == "complex":
            reasoning.append("表現の深度と洗練性を向上")
        
        return reasoning
    
    def _generate_correction_id(self) -> str:
        """補正ID生成"""
        timestamp = int(time.time() * 1000)
        return f"CORR_{timestamp}"

def main():
    """動的ユーザー補正システムのデモ実行"""
    print("🎛️ 動的ユーザー補正システム")
    print("=" * 60)
    
    # システム初期化
    correction_system = DynamicUserCorrectionSystem()
    
    # テストケース1: 法律文章を中学生向けに
    test_order_1 = UserOutputOrder(
        original_genre="legal_document",
        target_style="middle_school_friendly",
        target_audience="teenagers",
        complexity_level="simple",
        tone="casual",
        specific_requirements=["わかりやすく", "専門用語を避けて", "具体例を入れて"],
        correction_strength=0.8
    )
    
    # テストケース2: 技術文書を詩的に
    test_order_2 = UserOutputOrder(
        original_genre="technical_document", 
        target_style="poetic_style",
        target_audience="general_public",
        complexity_level="moderate",
        tone="poetic",
        specific_requirements=["美しい表現で", "感情に訴える", "メタファーを使って"],
        correction_strength=0.7
    )
    
    try:
        print("🧪 テストケース1: 法律文章 → 中学生向け")
        correction_1 = correction_system.generate_dynamic_correction(test_order_1)
        
        print(f"\n📝 ユーザー向け説明:")
        explanation_1 = correction_system.create_user_friendly_explanation(correction_1)
        print(explanation_1)
        
        print("\n" + "="*60)
        print("🧪 テストケース2: 技術文書 → 詩的表現")
        correction_2 = correction_system.generate_dynamic_correction(test_order_2)
        
        print(f"\n📝 ユーザー向け説明:")
        explanation_2 = correction_system.create_user_friendly_explanation(correction_2)
        print(explanation_2)
        
        # 実際の重みづけ適用テスト
        base_weights = {
            "cta_complexity": 1.0,
            "cta_formality": 1.0,
            "cta_accessibility": 1.0,
            "cta_poetic": 0.5,
            "onto_technical": 1.0
        }
        
        print("\n🔧 実際の重みづけ適用テスト:")
        adjusted_weights = correction_system.apply_corrections_to_system(correction_1, base_weights)
        
        print("\n🎉 動的ユーザー補正システム実行完了!")
        
    except Exception as e:
        print(f"❌ 実行エラー: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main()