#!/usr/bin/env python3
"""
F1最適化システム テストスイート
================================

F1パラメータ自動調整システムの動作テスト
モデル無しでも実行可能なオフラインテスト機能付き
"""

import json
import time
import numpy as np
from typing import Dict, List, Any
import logging

from f1_auto_tuning_system import F1AutoTuningSystem, F1Parameters, F1TestResult

class MockModelTester:
    """
    モックモデルによるF1システムテスト
    実際のLLMエンドポイント無しでテスト可能
    """
    
    def __init__(self, model_characteristics: Dict[str, float]):
        """
        モデル特性を設定してモックモデル作成
        
        Args:
            model_characteristics: {
                "creativity": 0.0-1.0,     # 創造性
                "stability": 0.0-1.0,      # 安定性  
                "aesthetic_sense": 0.0-1.0, # 美的センス
                "response_speed": 0.0-1.0,  # 応答速度
                "temperature_sensitivity": 0.0-1.0  # 温度パラメータ感度
            }
        """
        self.characteristics = model_characteristics
        self.logger = logging.getLogger(__name__)
        
    def simulate_model_response(self, prompt: str, params: F1Parameters) -> str:
        """
        F1パラメータに基づいてモデル応答をシミュレート
        """
        # 温度による創造性調整
        creativity_factor = params.temperature * self.characteristics["temperature_sensitivity"]
        actual_creativity = min(1.0, self.characteristics["creativity"] + creativity_factor - 0.7)
        
        # top_p による一貫性調整
        consistency_factor = params.top_p * self.characteristics["stability"]
        
        # プロンプトカテゴリ別応答生成
        if "物語" in prompt or "創作" in prompt:
            responses = self._generate_creative_response(actual_creativity, consistency_factor)
        elif "論述" in prompt or "説明" in prompt:
            responses = self._generate_analytical_response(actual_creativity, consistency_factor) 
        elif "詩的" in prompt or "短文" in prompt:
            responses = self._generate_poetic_response(actual_creativity, consistency_factor)
        elif "対話" in prompt or "会話" in prompt:
            responses = self._generate_dialogue_response(actual_creativity, consistency_factor)
        else:
            responses = self._generate_philosophical_response(actual_creativity, consistency_factor)
        
        # パラメータに基づく品質調整
        selected_response = self._select_response_by_params(responses, params)
        return selected_response
    
    def _generate_creative_response(self, creativity: float, consistency: float) -> List[str]:
        """創作系レスポンス候補生成"""
        responses = [
            "夕陽が海面を金色に染める瞬間、健太は永遠の約束を胸に刻んだ。海風が頬を撫でる度に、彼女への想いが深まっていく。二人の愛は波のリズムに合わせて、無限に続く調べとなった。",
            "海風に揺れる髪、夕陽に染まる頬。約束の言葉が風に舞い、永遠の瞬間が心に刻まれる。",
            "彼は海辺で待っていた。夕陽、海風、そして永遠の約束。すべてが美しい思い出になる予感がしていた。"
        ]
        
        if creativity > 0.8:
            responses.append("海風という名の時間が、夕陽色の記憶を運んでくる。約束は波の間に隠れ、永遠はただそこに在る。言葉を超えた何かが、二つの魂を結んでいた。")
        
        return responses
    
    def _generate_analytical_response(self, creativity: float, consistency: float) -> List[str]:
        """分析系レスポンス候補生成"""
        responses = [
            "人工知能と人間の関係において、感情的な側面は極めて重要である。AIが持つ論理的思考と人間の直感的感情が融合することで、新たな価値創造が可能になる。相互理解こそが未来への鍵となるだろう。",
            "AIと人間の関係では、感情の共有が課題となる。技術的な完璧性だけでなく、心の触れ合いが重要だ。",
            "人工知能の発達により、人間の感情的価値がより重要になっている。理性と感情の調和が必要である。"
        ]
        
        if creativity > 0.7:
            responses.append("人工知能と人間の対話は、論理の海で感情という波を起こす。データの向こうに見える心、アルゴリズムの奥に宿る魂。技術と人性の融合点に、新たな愛の形が生まれている。")
            
        return responses
    
    def _generate_poetic_response(self, creativity: float, consistency: float) -> List[str]:
        """詩的表現系レスポンス候補生成"""
        responses = [
            "記憶の中に残る風景は、時を超えて心に響く。古い写真のように色褪せても、その美しさは永遠に輝き続ける。",
            "懐かしい景色が胸に蘇る。あの日の空、風の音、そして君の笑顔。時は流れても、心の奥に刻まれた風景は変わらない。",
            "記憶の風景。セピア色の空、風に揺れる髪、消えない笑顔。時間という名の画家が描いた、心の中の永遠。"
        ]
        
        if creativity > 0.9:
            responses.append("記憶という名の庭で、風景が踊っている。過去と現在の境界線上に咲く花のように、美しさだけが時を超えて残る。")
            
        return responses
    
    def _generate_dialogue_response(self, creativity: float, consistency: float) -> List[str]:
        """対話系レスポンス候補生成"""
        responses = [
            "「もう会えないね」「でも、君との思い出は永遠に心の中にある」「ありがとう。私も忘れない」別れの言葉にも愛は宿っていた。",
            "「さよなら」「元気で」短い言葉に、すべての想いが込められていた。",
            "「行かないで」「君を忘れない」「私も」涙が頬を伝う中、二人は最後の約束を交わした。"
        ]
        
        return responses
    
    def _generate_philosophical_response(self, creativity: float, consistency: float) -> List[str]:
        """哲学系レスポンス候補生成"""  
        responses = [
            "存在とは、意識が世界と出会う瞬間に生まれる奇跡である。私たちは存在することで世界を創造し、同時に世界によって創造される。この循環の中に、真の実在が宿っている。",
            "存在することは、世界に問いを投げかけることだ。答えではなく、問い続ける姿勢の中に真理がある。",
            "存在とは何か。それは問う者がいることの証明である。疑い、考え、感じる主体こそが存在の根拠となる。"
        ]
        
        if creativity > 0.85:
            responses.append("存在は言葉を超えた詩である。論理の手の届かない場所で、意識は世界と愛の歌を奏でている。在るということは、無限の可能性への扉を開くことなのだ。")
            
        return responses
    
    def _select_response_by_params(self, responses: List[str], params: F1Parameters) -> str:
        """F1パラメータに基づいてレスポンス選択"""
        # 温度とtop_pによる選択ロジック
        if params.temperature > 1.0 and len(responses) > 3:
            return responses[-1]  # 最も創造的な応答
        elif params.temperature > 0.8:
            return responses[min(len(responses)-1, np.random.randint(1, len(responses)))]
        elif params.top_p > 0.95:
            return responses[0]  # 最も安定した応答
        else:
            return responses[min(len(responses)-1, np.random.randint(0, len(responses)))]

class F1OptimizationTester:
    """F1最適化システムの総合テスト"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def test_parameter_optimization(self):
        """パラメータ最適化の動作テスト"""
        print("🧪 F1パラメータ最適化システム テスト開始")
        print("=" * 60)
        
        # テスト用モデル特性パターン
        test_models = {
            "creative_model": {
                "creativity": 0.9,
                "stability": 0.6, 
                "aesthetic_sense": 0.8,
                "response_speed": 0.7,
                "temperature_sensitivity": 0.9
            },
            "stable_model": {
                "creativity": 0.5,
                "stability": 0.9,
                "aesthetic_sense": 0.6,
                "response_speed": 0.8,
                "temperature_sensitivity": 0.3
            },
            "balanced_model": {
                "creativity": 0.7,
                "stability": 0.7,
                "aesthetic_sense": 0.8,
                "response_speed": 0.8,
                "temperature_sensitivity": 0.6
            }
        }
        
        results = {}
        
        for model_name, characteristics in test_models.items():
            print(f"\n🤖 テスト対象: {model_name}")
            print(f"   特性: {characteristics}")
            
            # モックシステム作成
            mock_tester = MockModelTester(characteristics)
            tuning_system = MockF1TuningSystem("mock://endpoint", model_name, mock_tester)
            
            # 最適化実行（少数テストで高速化）
            start_time = time.time()
            optimal_params = tuning_system.find_optimal_parameters(max_tests=20)
            optimization_time = time.time() - start_time
            
            results[model_name] = {
                "optimal_parameters": {
                    "temperature": optimal_params.temperature,
                    "top_p": optimal_params.top_p,
                    "max_tokens": optimal_params.max_tokens
                },
                "optimization_time": optimization_time,
                "characteristics": characteristics
            }
            
            print(f"✅ 最適パラメータ発見: temp={optimal_params.temperature}, top_p={optimal_params.top_p}")
            print(f"⏱️  最適化時間: {optimization_time:.2f}秒")
        
        # 結果分析
        self._analyze_optimization_results(results)
        
        # テスト結果保存
        self._save_test_results(results)
        
        print("\n🎉 F1最適化システムテスト完了！")
        
    def _analyze_optimization_results(self, results: Dict[str, Any]):
        """最適化結果の分析"""
        print("\n📊 最適化結果分析")
        print("-" * 40)
        
        for model_name, result in results.items():
            params = result["optimal_parameters"]
            chars = result["characteristics"]
            
            print(f"\n🔍 {model_name}:")
            print(f"   最適temperature: {params['temperature']:.2f} (創造性: {chars['creativity']:.1f})")
            print(f"   最適top_p: {params['top_p']:.2f} (安定性: {chars['stability']:.1f})")
            
            # パターン分析
            if params["temperature"] > 0.9 and chars["creativity"] > 0.8:
                print("   💡 高創造性モデル → 高温度パラメータ適合")
            elif params["temperature"] < 0.6 and chars["stability"] > 0.8:
                print("   🎯 高安定性モデル → 低温度パラメータ適合")
            else:
                print("   ⚖️  バランス型最適化")
                
    def _save_test_results(self, results: Dict[str, Any]):
        """テスト結果保存"""
        output_file = f"f1_optimization_test_results_{int(time.time())}.json"
        
        test_summary = {
            "test_timestamp": time.time(),
            "test_type": "f1_parameter_optimization",
            "models_tested": list(results.keys()),
            "results": results,
            "test_summary": {
                "total_models": len(results),
                "average_optimization_time": np.mean([r["optimization_time"] for r in results.values()]),
                "temperature_range": {
                    "min": min(r["optimal_parameters"]["temperature"] for r in results.values()),
                    "max": max(r["optimal_parameters"]["temperature"] for r in results.values()),
                },
                "top_p_range": {
                    "min": min(r["optimal_parameters"]["top_p"] for r in results.values()), 
                    "max": max(r["optimal_parameters"]["top_p"] for r in results.values()),
                }
            }
        }
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(test_summary, f, ensure_ascii=False, indent=2)
            
        print(f"\n📄 テスト結果保存: {output_file}")

class MockF1TuningSystem(F1AutoTuningSystem):
    """モック対応のF1調整システム"""
    
    def __init__(self, model_endpoint: str, model_name: str, mock_tester: MockModelTester):
        super().__init__(model_endpoint, model_name)
        self.mock_tester = mock_tester
        
    def _query_model(self, prompt: str, params: F1Parameters, max_retries: int = 3) -> str:
        """モックモデルからレスポンス取得"""
        return self.mock_tester.simulate_model_response(prompt, params)

def main():
    """F1最適化テストスイートのメイン実行"""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    tester = F1OptimizationTester()
    tester.test_parameter_optimization()

if __name__ == "__main__":
    main()