#!/usr/bin/env python3
"""
F1最適化パラメータ自動調整システム
===================================

各モデルの特性を自動テスト・解析し、345次元解析に最適な
F1パラメータ（temperature, top_p, max_tokens等）を発見・適用するシステム

Based on Yuki's insight: "モデル自身に最適化パラメータを見つけさせる"
"""

import json
import time
import requests
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
from dataclasses import dataclass, asdict
from pathlib import Path
import logging

from lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine

@dataclass
class F1Parameters:
    """F1最適化パラメータセット"""
    temperature: float
    top_p: float
    max_tokens: int
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    
class F1TestResult:
    """F1テスト結果"""
    def __init__(self, params: F1Parameters, score: float, details: Dict[str, Any]):
        self.parameters = params
        self.score = score
        self.details = details
        self.timestamp = time.time()

class F1AutoTuningSystem:
    """
    F1パラメータ自動調整システム
    モデルの応答品質を測定し、最適なパラメータを発見
    """
    
    def __init__(self, model_endpoint: str, model_name: str = "unknown"):
        self.model_endpoint = model_endpoint
        self.model_name = model_name
        self.logger = logging.getLogger(__name__)
        
        # Ultrathinkエンジン（解析用）
        self.analysis_engine = LNAESv2UltrathinkEngine()
        
        # テスト用プロンプトセット
        self.test_prompts = self._initialize_test_prompts()
        
        # パラメータ探索範囲
        self.param_ranges = {
            "temperature": (0.3, 1.2, 0.1),  # (min, max, step)
            "top_p": (0.7, 1.0, 0.05),
            "max_tokens": [300, 500, 800],
        }
        
        self.logger.info(f"F1AutoTuningSystem initialized for {model_name} at {model_endpoint}")
        
    def _initialize_test_prompts(self) -> List[Dict[str, str]]:
        """
        F1テスト用プロンプトセット初期化
        様々な文体・複雑度でモデル特性を測定
        """
        return [
            {
                "category": "creative_narrative",
                "prompt": "以下のキーワードから美しい物語を150文字で創作してください：\n海風、夕陽、約束、永遠",
                "target_complexity": 0.8,
                "target_aesthetics": 0.9
            },
            {
                "category": "analytical_description", 
                "prompt": "人工知能と人間の関係について、感情的な側面を重視して200文字で論述してください",
                "target_complexity": 0.9,
                "target_aesthetics": 0.6
            },
            {
                "category": "poetic_expression",
                "prompt": "「記憶の中の風景」をテーマに、詩的な表現で100文字の短文を書いてください",
                "target_complexity": 0.7,
                "target_aesthetics": 1.0
            },
            {
                "category": "dialogue_natural",
                "prompt": "恋人同士の別れの会話を、自然で感動的な対話として120文字で表現してください",
                "target_complexity": 0.6,
                "target_aesthetics": 0.8
            },
            {
                "category": "metaphysical_reflection",
                "prompt": "存在とは何かについて、哲学的かつ詩的に180文字で表現してください",
                "target_complexity": 1.0,
                "target_aesthetics": 0.85
            }
        ]
    
    def test_f1_parameters(self, params: F1Parameters) -> F1TestResult:
        """
        指定されたF1パラメータでモデル性能をテスト
        """
        self.logger.info(f"Testing F1 parameters: {asdict(params)}")
        
        total_score = 0.0
        test_details = {
            "individual_scores": [],
            "response_times": [],
            "response_lengths": [],
            "aesthetic_qualities": [],
            "complexity_scores": [],
            "target_matches": []
        }
        
        for test_case in self.test_prompts:
            start_time = time.time()
            
            # モデルに問い合わせ
            response = self._query_model(test_case["prompt"], params)
            response_time = time.time() - start_time
            
            if not response:
                continue
                
            # 345次元解析による品質評価
            analysis_result = self.analysis_engine.process_sentence(response, 0)
            
            # スコア計算
            individual_score = self._calculate_response_score(
                response, 
                analysis_result, 
                test_case,
                response_time
            )
            
            # 詳細記録
            test_details["individual_scores"].append(individual_score)
            test_details["response_times"].append(response_time)
            test_details["response_lengths"].append(len(response))
            test_details["aesthetic_qualities"].append(analysis_result.aesthetic_quality)
            test_details["complexity_scores"].append(len([v for v in analysis_result.cta_scores.values() if v > 0.5]))
            test_details["target_matches"].append(abs(analysis_result.aesthetic_quality - test_case["target_aesthetics"]))
            
            total_score += individual_score
            
        # 平均スコア計算
        average_score = total_score / len(self.test_prompts) if self.test_prompts else 0.0
        
        # 追加メトリクス
        test_details["average_response_time"] = np.mean(test_details["response_times"]) if test_details["response_times"] else 0
        test_details["average_aesthetic_quality"] = np.mean(test_details["aesthetic_qualities"]) if test_details["aesthetic_qualities"] else 0
        test_details["aesthetic_consistency"] = 1.0 - np.std(test_details["aesthetic_qualities"]) if test_details["aesthetic_qualities"] else 0
        test_details["target_match_accuracy"] = 1.0 - np.mean(test_details["target_matches"]) if test_details["target_matches"] else 0
        
        return F1TestResult(params, average_score, test_details)
    
    def _query_model(self, prompt: str, params: F1Parameters, max_retries: int = 3) -> Optional[str]:
        """
        モデルAPIに問い合わせを送信
        """
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "あなたは創造性豊かな日本語の文章生成AIです。美しく感動的な文章を生成してください。"
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "temperature": params.temperature,
            "top_p": params.top_p,
            "max_tokens": params.max_tokens,
            "frequency_penalty": params.frequency_penalty,
            "presence_penalty": params.presence_penalty
        }
        
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.model_endpoint,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        return result["choices"][0]["message"]["content"].strip()
                else:
                    self.logger.warning(f"Model API returned status {response.status_code}: {response.text}")
                    
            except Exception as e:
                self.logger.warning(f"Model query attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1 * (attempt + 1))  # 指数的バックオフ
                    
        return None
    
    def _calculate_response_score(self, response: str, analysis: Any, test_case: Dict, response_time: float) -> float:
        """
        レスポンス品質スコア計算（0.0-1.0）
        """
        # 基本品質メトリクス
        aesthetic_score = analysis.aesthetic_quality  # 美的品質 
        complexity_bonus = min(1.0, len([v for v in analysis.cta_scores.values() if v > 0.3]) / 20)  # 複雑性ボーナス
        
        # ターゲット適合度
        target_aesthetic_match = 1.0 - abs(analysis.aesthetic_quality - test_case["target_aesthetics"])
        target_complexity_match = 1.0 - abs(complexity_bonus - test_case["target_complexity"])
        
        # レスポンス時間ペナルティ（10秒超で減点）
        time_penalty = max(0.0, min(0.3, (response_time - 10) / 10)) if response_time > 10 else 0.0
        
        # 長度適合度（極端に短すぎる/長すぎる場合の減点）
        length = len(response)
        length_score = 1.0
        if length < 50:
            length_score = length / 50
        elif length > 300:
            length_score = max(0.5, 1.0 - (length - 300) / 200)
            
        # 総合スコア
        total_score = (
            aesthetic_score * 0.35 +
            complexity_bonus * 0.15 +
            target_aesthetic_match * 0.25 +
            target_complexity_match * 0.15 +
            length_score * 0.10
        ) - time_penalty
        
        return max(0.0, min(1.0, total_score))
    
    def find_optimal_parameters(self, max_tests: int = 50) -> F1Parameters:
        """
        最適なF1パラメータを自動探索
        Grid Search + 最適化アルゴリズム使用
        """
        self.logger.info(f"Starting F1 parameter optimization (max {max_tests} tests)")
        
        best_result = None
        all_results = []
        
        # Grid Search Phase
        test_count = 0
        temp_range = np.arange(*self.param_ranges["temperature"])
        top_p_range = np.arange(*self.param_ranges["top_p"])
        
        for temp in temp_range:
            for top_p in top_p_range:
                for max_tokens in self.param_ranges["max_tokens"]:
                    if test_count >= max_tests:
                        break
                        
                    params = F1Parameters(
                        temperature=round(temp, 2),
                        top_p=round(top_p, 2), 
                        max_tokens=max_tokens
                    )
                    
                    result = self.test_f1_parameters(params)
                    all_results.append(result)
                    
                    if best_result is None or result.score > best_result.score:
                        best_result = result
                        self.logger.info(f"New best score: {result.score:.3f} with params {asdict(params)}")
                    
                    test_count += 1
                    
                if test_count >= max_tests:
                    break
            if test_count >= max_tests:
                break
        
        # Fine-tuning Phase (周辺値の詳細探索)
        if best_result and test_count < max_tests:
            fine_tune_results = self._fine_tune_parameters(best_result.parameters, max_tests - test_count)
            all_results.extend(fine_tune_results)
            
            # 最良結果更新
            for result in fine_tune_results:
                if result.score > best_result.score:
                    best_result = result
        
        # 結果保存
        self._save_optimization_results(all_results, best_result)
        
        self.logger.info(f"Optimization completed. Best score: {best_result.score:.3f}")
        return best_result.parameters if best_result else F1Parameters(0.7, 0.9, 500)
    
    def _fine_tune_parameters(self, base_params: F1Parameters, max_tests: int) -> List[F1TestResult]:
        """
        最適パラメータの周辺値での細かい調整
        """
        results = []
        test_count = 0
        
        # 最適値周辺の細かいステップでテスト
        fine_steps = {
            "temperature": 0.05,
            "top_p": 0.02
        }
        
        for temp_delta in [-0.1, -0.05, 0.0, 0.05, 0.1]:
            for top_p_delta in [-0.04, -0.02, 0.0, 0.02, 0.04]:
                if test_count >= max_tests:
                    break
                    
                new_temp = max(0.1, min(1.5, base_params.temperature + temp_delta))
                new_top_p = max(0.5, min(1.0, base_params.top_p + top_p_delta))
                
                params = F1Parameters(
                    temperature=round(new_temp, 2),
                    top_p=round(new_top_p, 2),
                    max_tokens=base_params.max_tokens
                )
                
                result = self.test_f1_parameters(params)
                results.append(result)
                test_count += 1
                
            if test_count >= max_tests:
                break
                
        return results
    
    def _save_optimization_results(self, all_results: List[F1TestResult], best_result: F1TestResult):
        """
        最適化結果をファイルに保存
        """
        output_data = {
            "model_name": self.model_name,
            "model_endpoint": self.model_endpoint,
            "optimization_timestamp": time.time(),
            "total_tests": len(all_results),
            "best_parameters": asdict(best_result.parameters),
            "best_score": best_result.score,
            "best_details": best_result.details,
            "all_results": [
                {
                    "parameters": asdict(r.parameters),
                    "score": r.score,
                    "timestamp": r.timestamp
                }
                for r in all_results
            ]
        }
        
        output_file = f"f1_optimization_{self.model_name}_{int(time.time())}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
            
        self.logger.info(f"Optimization results saved to {output_file}")
    
    def apply_optimal_parameters(self, target_system: str = "lna_es_v2") -> Dict[str, Any]:
        """
        発見された最適パラメータを実際のシステムに適用
        """
        optimal_params = self.find_optimal_parameters()
        
        # LNA-ES v2.0システム用設定生成
        system_config = {
            "model_name": self.model_name,
            "endpoint": self.model_endpoint,
            "f1_parameters": asdict(optimal_params),
            "ultrathink_integration": True,
            "created_by": "F1AutoTuningSystem",
            "creation_timestamp": time.time(),
            "target_system": target_system
        }
        
        # 設定ファイル保存
        config_file = f"{target_system}_f1_config_{self.model_name}_{int(time.time())}.json"
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(system_config, f, ensure_ascii=False, indent=2)
            
        self.logger.info(f"Optimal F1 configuration saved to {config_file}")
        return system_config

def main():
    """F1自動調整システムのデモ実行"""
    print("🔧 F1最適化パラメータ自動調整システム")
    print("=" * 50)
    
    # デモ用設定（実際の使用時は適切なエンドポイントを指定）
    model_endpoint = "http://100.82.154.101:2346/v1/chat/completions" 
    model_name = "test_model"
    
    # システム初期化
    tuning_system = F1AutoTuningSystem(model_endpoint, model_name)
    
    # 最適パラメータ探索（デモでは少数テスト）
    print(f"🚀 {model_name} の最適F1パラメータを探索中...")
    
    try:
        optimal_config = tuning_system.apply_optimal_parameters("lna_es_v2_ultrathink")
        
        print("✅ 最適化完了！")
        print(f"📊 最適F1パラメータ:")
        for key, value in optimal_config["f1_parameters"].items():
            print(f"   {key}: {value}")
            
    except Exception as e:
        print(f"❌ テスト中にエラー発生: {e}")
        print("💡 実際の使用時は適切なモデルエンドポイントを指定してください")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()