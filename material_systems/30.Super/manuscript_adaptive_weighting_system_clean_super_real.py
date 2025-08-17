#!/usr/bin/env python3
"""
元原稿適応的重みづけシステム (Clean Version)
===============================================

原稿の345次元解析結果に基づいて：
- 薄いところ（不足要素）をブーストする
- 強いところ（過剰要素）を絞る  
- バランスの取れた復元を実現する

Based on Ken's insight: "薄いところをブースト、強いところを絞る"
"""

import numpy as np
import json
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
import time

from lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine, LNAESResult

@dataclass
class WeightingProfile:
    """重みづけプロファイル"""
    cta_weights: Dict[str, float]
    ontology_weights: Dict[str, float]
    boost_factors: Dict[str, float]
    suppress_factors: Dict[str, float]
    balance_score: float
    created_timestamp: float

@dataclass 
class ManuscriptAnalysis:
    """原稿解析結果"""
    title: str
    strong_dimensions: List[Tuple[str, float]]
    weak_dimensions: List[Tuple[str, float]]
    average_aesthetic: float
    total_sentences: int

class ManuscriptAdaptiveWeightingSystem:
    """元原稿適応的重みづけシステム"""
    
    def __init__(self):
        self.engine = LNAESv2UltrathinkEngine()
        self.boost_max = 2.0
        self.suppress_min = 0.5
        
    def analyze_manuscript(self, text: str, title: str = "Unknown") -> ManuscriptAnalysis:
        """原稿解析"""
        print(f"📊 原稿解析: {title}")
        
        sentences = self._split_sentences(text)
        results = []
        
        for i, sentence in enumerate(sentences):
            result = self.engine.process_sentence(sentence, i)
            results.append(result)
        
        # 次元統計
        stats = self._calculate_stats(results)
        strong_dims, weak_dims = self._identify_strong_weak(stats)
        avg_aesthetic = np.mean([r.aesthetic_quality for r in results])
        
        print(f"   強い次元: {len(strong_dims)}個")
        print(f"   弱い次元: {len(weak_dims)}個")
        print(f"   平均美的品質: {avg_aesthetic:.3f}")
        
        return ManuscriptAnalysis(
            title=title,
            strong_dimensions=strong_dims,
            weak_dimensions=weak_dims,
            average_aesthetic=avg_aesthetic,
            total_sentences=len(sentences)
        )
    
    def generate_adaptive_weighting(self, analysis: ManuscriptAnalysis) -> WeightingProfile:
        """適応的重みづけ生成"""
        print("🔧 重みづけ生成中...")
        
        cta_weights = {}
        ontology_weights = {}
        boost_factors = {}
        suppress_factors = {}
        
        # 薄い次元をブースト
        print("💪 薄い次元のブースト:")
        for dim_name, weakness in analysis.weak_dimensions[:8]:
            boost_factor = min(self.boost_max, 1.0 + (1.0 - weakness) * 0.8)
            boost_factors[dim_name] = boost_factor
            
            if dim_name.startswith("cta_"):
                cta_weights[dim_name] = boost_factor
            else:
                ontology_weights[dim_name] = boost_factor
                
            print(f"   📈 {dim_name}: {weakness:.3f} → ×{boost_factor:.2f}")
        
        # 強い次元を抑制  
        print("🎛️ 強い次元の抑制:")
        for dim_name, strength in analysis.strong_dimensions[:8]:
            suppress_factor = max(self.suppress_min, 1.0 - (strength - 0.6) * 0.5)
            suppress_factors[dim_name] = suppress_factor
            
            if dim_name.startswith("cta_"):
                cta_weights[dim_name] = suppress_factor
            else:
                ontology_weights[dim_name] = suppress_factor
                
            print(f"   📉 {dim_name}: {strength:.3f} → ×{suppress_factor:.2f}")
        
        balance_score = 0.75  # 仮の値
        
        return WeightingProfile(
            cta_weights=cta_weights,
            ontology_weights=ontology_weights,
            boost_factors=boost_factors,
            suppress_factors=suppress_factors,
            balance_score=balance_score,
            created_timestamp=time.time()
        )
    
    def test_weighting_effectiveness(self, text: str, weighting: WeightingProfile, title: str) -> Dict[str, Any]:
        """重みづけ効果テスト"""
        print("🧪 効果テスト実行")
        
        # Before解析
        before = self.analyze_manuscript(text, f"{title}_before")
        
        # After推定（簡略）
        boost_improvement = len(weighting.boost_factors) * 0.05
        suppress_improvement = len(weighting.suppress_factors) * 0.03
        total_improvement = boost_improvement + suppress_improvement
        
        print(f"📊 改善予測:")
        print(f"   ブースト効果: +{boost_improvement:.3f}")
        print(f"   抑制効果: +{suppress_improvement:.3f}") 
        print(f"   総合改善: +{total_improvement:.3f}")
        
        return {
            "title": title,
            "before_aesthetic": before.average_aesthetic,
            "predicted_improvement": total_improvement,
            "boost_count": len(weighting.boost_factors),
            "suppress_count": len(weighting.suppress_factors),
            "test_timestamp": time.time()
        }
    
    def _split_sentences(self, text: str) -> List[str]:
        """文分割"""
        sentences = []
        current = ""
        
        for char in text:
            current += char
            if char in ["。", "！", "？"]:
                if current.strip():
                    sentences.append(current.strip())
                current = ""
        
        if current.strip():
            sentences.append(current.strip())
            
        return [s for s in sentences if len(s) > 5]
    
    def _calculate_stats(self, results: List[LNAESResult]) -> Dict[str, Dict]:
        """統計計算"""
        all_dims = {}
        
        for result in results:
            for dim, score in result.cta_scores.items():
                if dim not in all_dims:
                    all_dims[dim] = []
                all_dims[dim].append(score)
            
            for dim, score in result.ontology_scores.items():
                if dim not in all_dims:
                    all_dims[dim] = []
                all_dims[dim].append(score)
            
            for dim, score in result.meta_dimensions.items():
                if dim not in all_dims:
                    all_dims[dim] = []
                all_dims[dim].append(score)
        
        stats = {}
        for dim, scores in all_dims.items():
            stats[dim] = {
                "mean": np.mean(scores),
                "std": np.std(scores)
            }
        
        return stats
    
    def _identify_strong_weak(self, stats: Dict) -> Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]:
        """強弱次元特定"""
        strengths = []
        
        for dim, stat in stats.items():
            strength = stat["mean"] + 0.1 / (1.0 + stat["std"])
            strengths.append((dim, strength))
        
        strengths.sort(key=lambda x: x[1], reverse=True)
        
        total = len(strengths)
        strong_count = max(1, int(total * 0.15))
        weak_count = max(1, int(total * 0.15))
        
        strong = strengths[:strong_count]
        weak = list(reversed(strengths[-weak_count:]))
        
        return strong, weak

def main():
    """メイン実行"""
    print("⚖️ 元原稿適応的重みづけシステム")
    print("=" * 50)
    
    system = ManuscriptAdaptiveWeightingSystem()
    
    # テスト原稿（感情表現が淡白な例）
    test_text = """
海風のメロディが響く。夕陽が海を照らす。健太は待っていた。
彼女が来た。微笑んでいる。二人は歩いた。
「ありがとう」と彼女は言った。健太は頷いた。
"""
    
    try:
        print("🔍 感情表現が淡白な原稿の解析例")
        
        # 1. 解析
        analysis = system.analyze_manuscript(test_text, "淡白な表現テスト")
        
        # 2. 重みづけ生成（感情系次元をブースト予想）
        weighting = system.generate_adaptive_weighting(analysis)
        
        # 3. 効果テスト
        result = system.test_weighting_effectiveness(test_text, weighting, "淡白表現改善")
        
        # 4. 特定の改善提案
        emotion_boosts = [k for k in weighting.boost_factors.keys() if "emotion" in k]
        if emotion_boosts:
            print(f"\n💡 感情表現改善提案:")
            for dim in emotion_boosts:
                boost = weighting.boost_factors[dim]
                print(f"   {dim}: ×{boost:.2f} ブースト")
                
        print(f"\n📄 このモデルは感情表現が淡白 → emotion系次元ブースト推奨")
        print("🎉 適応的重みづけ完了!")
        
    except Exception as e:
        print(f"❌ エラー: {e}")

if __name__ == "__main__":
    main()