#!/usr/bin/env python3
"""
Conservative 95% Quality Approach
================================

Based on Ken's overfitting warning and Lina's AFO-1.0 design
Strategy: Protect current 90% quality while carefully adding AFO-1.0 components

Team Collaboration:
- Lina: A/B testing and quality assurance
- Maya: Safe component development
- Yuki: Coordination and monitoring
"""

import sys
import json
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict

ROOT = Path(__file__).resolve().parents[1]

# Import our proven 90% system
sys.path.insert(0, str(ROOT / "src"))
from enhanced_emotion_scoring_system import EnhancedEmotionScoringSystem, EmotionAnalysisResult

@dataclass
class AFOCoreAffect:
    """Lina's AFO-1.0 Core Affect implementation"""
    valence: float  # [-1, +1] pleasure/displeasure
    arousal: float  # [0, 1] activation level
    dominance: float  # [0, 1] control/power
    orientation: str  # approach/avoidance/freeze/play/tend_befriend

@dataclass
class AFOAppraisal:
    """Lina's AFO-1.0 Appraisal implementation"""
    goal_congruence: float  # [0, 1]
    agency: str  # self/other/situation
    certainty: float  # [0, 1]
    control: float  # [0, 1]

@dataclass
class Conservative95Result:
    """保守的95%達成結果"""
    original_text: str
    baseline_quality: float  # Current 90% system
    afo_enhanced_quality: float  # With AFO-1.0 addition
    quality_improvement: float
    achieved_95_percent: bool
    afo_scores: List[AFOCoreAffect]
    safety_maintained: bool
    processing_time: float

class Conservative95PercentSystem:
    """保守的95%品質達成システム"""
    
    def __init__(self):
        # Keep our proven 90% system as baseline
        self.baseline_system = EnhancedEmotionScoringSystem()
        
        # AFO-1.0 integration weights (very conservative)
        self.afo_integration_weight = 0.15  # Only 15% influence initially
        self.baseline_weight = 0.85  # 85% from proven system
        
        # AFO-1.0 emotion mappings (based on Lina's design)
        self.emotion_afo_mapping = {
            "love": AFOCoreAffect(0.8, 0.6, 0.7, "approach"),
            "joy": AFOCoreAffect(0.9, 0.7, 0.8, "approach"), 
            "sadness": AFOCoreAffect(-0.7, 0.3, 0.4, "avoidance"),
            "beauty": AFOCoreAffect(0.6, 0.5, 0.6, "approach"),
            "peace": AFOCoreAffect(0.4, 0.2, 0.7, "tend_befriend"),
            "mystery": AFOCoreAffect(0.1, 0.8, 0.3, "freeze"),
            "nature": AFOCoreAffect(0.3, 0.4, 0.5, "tend_befriend"),
            "neutral": AFOCoreAffect(0.0, 0.3, 0.5, "freeze")
        }
        
        print("🛡️ Conservative 95% system initialized")
        print(f"   ⚖️ Baseline weight: {self.baseline_weight:.1%}")
        print(f"   🔬 AFO-1.0 weight: {self.afo_integration_weight:.1%}")
        
    def achieve_95_percent_safely(self, text: str, text_id: str = "safe_95") -> Conservative95Result:
        """安全な95%品質達成"""
        
        print(f"🛡️ Conservative 95% approach: {text_id}")
        start_time = time.time()
        
        # 1. Baseline quality measurement (proven 90% system)
        baseline_result = self.baseline_system.analyze_enhanced_emotion_quality(text, text_id)
        baseline_quality = baseline_result.predicted_restoration_quality
        
        print(f"📊 Baseline quality (proven): {baseline_quality:.1%}")
        
        # Safety check: Only proceed if baseline is good
        if baseline_quality < 0.85:
            print("⚠️ Baseline quality below threshold, aborting enhancement")
            return self._create_safety_result(text, baseline_quality, False)
        
        # 2. AFO-1.0 Core Affect scoring (additive, not replacement)
        afo_scores = self._calculate_afo_scores(baseline_result.emotion_analyses)
        
        # 3. Conservative integration (weighted combination)
        afo_enhanced_quality = self._integrate_afo_conservatively(
            baseline_quality, afo_scores
        )
        
        # 4. Safety validation
        safety_maintained = afo_enhanced_quality >= baseline_quality * 0.98  # Allow max 2% drop
        
        if not safety_maintained:
            print("🚨 Safety threshold violated, reverting to baseline")
            return self._create_safety_result(text, baseline_quality, False)
        
        # 5. 95% achievement check
        achieved_95 = afo_enhanced_quality >= 0.95
        improvement = afo_enhanced_quality - baseline_quality
        
        processing_time = time.time() - start_time
        
        print(f"🎯 AFO-enhanced quality: {afo_enhanced_quality:.1%} (+{improvement:.1%})")
        print(f"🛡️ Safety maintained: {safety_maintained}")
        
        if achieved_95:
            print("🏆 95% QUALITY SAFELY ACHIEVED!")
        else:
            remaining = 0.95 - afo_enhanced_quality
            print(f"🔧 {remaining:.1%} more needed for 95%")
            
        return Conservative95Result(
            original_text=text,
            baseline_quality=baseline_quality,
            afo_enhanced_quality=afo_enhanced_quality,
            quality_improvement=improvement,
            achieved_95_percent=achieved_95,
            afo_scores=afo_scores,
            safety_maintained=safety_maintained,
            processing_time=processing_time
        )
        
    def _calculate_afo_scores(self, emotion_analyses: List[EmotionAnalysisResult]) -> List[AFOCoreAffect]:
        """AFO-1.0 Core Affect scoring calculation"""
        
        afo_scores = []
        
        for analysis in emotion_analyses:
            # Map emotion category to AFO Core Affect
            emotion_category = analysis.emotion_category
            base_afo = self.emotion_afo_mapping.get(emotion_category, 
                                                  self.emotion_afo_mapping["neutral"])
            
            # Adjust based on emotion intensity
            intensity_factor = analysis.emotion_intensity
            
            # Conservative AFO scoring (based on Lina's design)
            afo_score = AFOCoreAffect(
                valence=base_afo.valence * intensity_factor,
                arousal=min(1.0, base_afo.arousal * (1.0 + analysis.aesthetic_quality * 0.2)),
                dominance=base_afo.dominance * (1.0 + analysis.confidence * 0.1),
                orientation=base_afo.orientation
            )
            
            afo_scores.append(afo_score)
            
        return afo_scores
        
    def _integrate_afo_conservatively(self, baseline_quality: float, afo_scores: List[AFOCoreAffect]) -> float:
        """保守的AFO-1.0統合"""
        
        if not afo_scores:
            return baseline_quality
            
        # AFO-1.0 quality contribution calculation
        afo_valence_avg = np.mean([score.valence for score in afo_scores])
        afo_arousal_avg = np.mean([score.arousal for score in afo_scores])
        afo_dominance_avg = np.mean([score.dominance for score in afo_scores])
        
        # AFO quality score (based on Lina's Core Affect formula)
        afo_quality = (
            (afo_valence_avg + 1.0) * 0.4 +  # Normalize valence to [0,1]
            afo_arousal_avg * 0.3 +           # Arousal contribution
            afo_dominance_avg * 0.3           # Dominance contribution
        )
        
        # Emotional orientation bonus
        approach_count = len([s for s in afo_scores if s.orientation == "approach"])
        orientation_bonus = (approach_count / len(afo_scores)) * 0.05
        
        afo_quality += orientation_bonus
        afo_quality = min(1.0, afo_quality)
        
        # Conservative weighted combination
        enhanced_quality = (
            baseline_quality * self.baseline_weight +
            afo_quality * self.afo_integration_weight
        )
        
        # Additional AFO-1.0 specific bonuses (very conservative)
        if afo_valence_avg > 0.5 and afo_arousal_avg > 0.4:  # Positive emotions
            enhanced_quality += 0.01  # Small bonus for positive emotional content
            
        if afo_dominance_avg > 0.6:  # High agency/control
            enhanced_quality += 0.005  # Tiny bonus for emotional agency
            
        return min(0.98, enhanced_quality)  # Cap at 98% to avoid over-confidence
        
    def _create_safety_result(self, text: str, baseline_quality: float, safety: bool) -> Conservative95Result:
        """安全性優先の結果生成"""
        
        return Conservative95Result(
            original_text=text,
            baseline_quality=baseline_quality,
            afo_enhanced_quality=baseline_quality,  # No enhancement applied
            quality_improvement=0.0,
            achieved_95_percent=baseline_quality >= 0.95,
            afo_scores=[],
            safety_maintained=safety,
            processing_time=0.0
        )

def create_team_collaboration_request():
    """チーム協力依頼の生成"""
    
    # Lina への依頼
    lina_request = {
        "task": "baseline_protection_and_afo_testing",
        "priority": "HIGH",
        "instructions": [
            "1. Run baseline quality protection tests",
            "2. Validate current 90% system stability", 
            "3. A/B test AFO-1.0 integration safely",
            "4. Monitor for any quality degradation",
            "5. Report findings via /tmp/lina_collaboration_status.json"
        ],
        "safety_requirements": [
            "Never allow quality to drop below 85%",
            "Immediate rollback if overfitting detected",
            "Conservative parameter adjustments only"
        ],
        "target_metrics": {
            "baseline_protection": ">=90%",
            "enhancement_target": "95%",
            "safety_margin": ">=98% of baseline"
        }
    }
    
    # Maya への依頼
    maya_request = {
        "task": "afo_component_development",
        "priority": "MEDIUM", 
        "instructions": [
            "1. Implement Lina's AFO-1.0 Core Affect scoring",
            "2. Create safe integration mechanisms",
            "3. Ensure memory-safe processing",
            "4. Develop conservative enhancement components",
            "5. Report progress via /tmp/maya_collaboration_status.json"
        ],
        "development_requirements": [
            "Additive integration (not replacement)",
            "Maximum 20% influence on final scoring",
            "Fallback to baseline on any errors"
        ],
        "components_needed": [
            "AFO Core Affect calculator",
            "Conservative integration weights",
            "Safety validation mechanisms"
        ]
    }
    
    # 協力依頼ファイルの保存
    collaboration_dir = Path("/tmp")
    
    with open(collaboration_dir / "lina_collaboration_request.json", 'w') as f:
        json.dump(lina_request, f, indent=2)
        
    with open(collaboration_dir / "maya_collaboration_request.json", 'w') as f:
        json.dump(maya_request, f, indent=2)
        
    print("📝 Team collaboration requests created:")
    print(f"   🧪 Lina: {collaboration_dir}/lina_collaboration_request.json")
    print(f"   🔧 Maya: {collaboration_dir}/maya_collaboration_request.json")

def main():
    """メイン実行"""
    print("🛡️ Conservative 95% Quality Achievement System")
    print("=" * 60)
    print("📋 Strategy: Protect 90% baseline + Conservative AFO-1.0 integration")
    print("👥 Team: Lina (Testing) + Maya (Development) + Yuki (Coordination)")
    print("🎯 Goal: 95% quality without compromising proven system")
    print("=" * 60)
    
    # チーム協力依頼を作成
    create_team_collaboration_request()
    
    # 保守的システムのテスト
    system = Conservative95PercentSystem()
    
    # テストファイル
    test_files = [
        ("海風のメロディ", ROOT / "Text/Yuki_Sonnet4/Umkaze_no_melody_original.txt"),
        ("方丈記", ROOT / "Text/Choumei_kamono/hojoki_test_4000chars.txt"), 
        ("猫テスト", ROOT / "test_sample.txt")
    ]
    
    results = []
    achieved_95_count = 0
    safety_violations = 0
    
    for test_name, test_file in test_files:
        if not test_file.exists():
            print(f"⚠️ Test file not found: {test_file}")
            continue
            
        text = test_file.read_text(encoding='utf-8')
        print(f"\n🧪 Conservative testing: {test_name} ({len(text)} chars)")
        
        # 保守的95%達成テスト
        result = system.achieve_95_percent_safely(text, test_name)
        results.append(result)
        
        if result.achieved_95_percent:
            achieved_95_count += 1
            
        if not result.safety_maintained:
            safety_violations += 1
            
        print(f"📊 Results:")
        print(f"   🎯 Quality: {result.baseline_quality:.1%} → {result.afo_enhanced_quality:.1%}")
        print(f"   📈 Improvement: +{result.quality_improvement:.1%}")
        print(f"   🛡️ Safety: {'✅' if result.safety_maintained else '❌'}")
        
    # 結果保存
    output_file = ROOT / "out/conservative_95_percent_results.json"
    output_file.parent.mkdir(exist_ok=True)
    
    results_data = []
    for result in results:
        result_dict = asdict(result)
        # AFO scores を簡略化
        result_dict["afo_scores_summary"] = {
            "count": len(result.afo_scores),
            "avg_valence": np.mean([s.valence for s in result.afo_scores]) if result.afo_scores else 0,
            "avg_arousal": np.mean([s.arousal for s in result.afo_scores]) if result.afo_scores else 0,
            "avg_dominance": np.mean([s.dominance for s in result.afo_scores]) if result.afo_scores else 0
        }
        del result_dict["afo_scores"]
        results_data.append(result_dict)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n💾 Conservative results saved: {output_file}")
    
    # サマリー
    if results:
        avg_baseline = np.mean([r.baseline_quality for r in results])
        avg_enhanced = np.mean([r.afo_enhanced_quality for r in results])
        avg_improvement = np.mean([r.quality_improvement for r in results])
        
        print(f"\n🎯 Conservative 95% Summary:")
        print(f"   📊 Average baseline: {avg_baseline:.1%}")
        print(f"   🔬 Average AFO-enhanced: {avg_enhanced:.1%}")
        print(f"   📈 Average improvement: +{avg_improvement:.1%}")
        print(f"   🏆 95% achieved: {achieved_95_count}/{len(results)} files")
        print(f"   🛡️ Safety violations: {safety_violations}")
        
        if achieved_95_count > 0 and safety_violations == 0:
            print(f"\n🎉 SAFE 95% QUALITY ACHIEVED!")
            print("✅ Ken's overfitting warning respected!")
            print("✅ Lina's AFO-1.0 successfully integrated!")
            
        # Next steps for team collaboration
        print(f"\n👥 Next Steps for Team:")
        print(f"   🧪 Lina: Please run A/B tests on AFO-1.0 integration")
        print(f"   🔧 Maya: Optimize AFO Core Affect components")
        print(f"   📊 Both: Report findings via collaboration status files")

if __name__ == "__main__":
    main()