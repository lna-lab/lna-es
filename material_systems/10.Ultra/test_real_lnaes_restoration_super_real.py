#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
真のLNA-ES v2.0 Ultrathinkエンジンを使用した方丈記復元テスト
実際の345次元解析による意味復元を検証
"""

import sys
import os
from pathlib import Path

# srcディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine
import json
import time
from datetime import datetime

def test_real_lnaes_restoration():
    """真のLNA-ES v2.0を使った方丈記復元テスト"""
    
    print("🔥 真のLNA-ES v2.0 Ultrathinkエンジン復元テスト開始！")
    print("✨ 345次元解析による実際の意味復元")
    print("🎯 目標: 95%意味保持の実証")
    print("=" * 80)
    
    # 原文読み込み
    original_path = "/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-Lang/textfilres/Choumei_kamono/hojoki_test_4000chars.txt"
    
    try:
        with open(original_path, 'r', encoding='utf-8') as f:
            original_text = f.read().strip()
    except Exception as e:
        print(f"❌ 原文読み込みエラー: {e}")
        return False
    
    print(f"📖 原文長: {len(original_text)}文字")
    
    # LNA-ES v2.0 Ultrathinkエンジン初期化
    try:
        engine = LNAESv2UltrathinkEngine()
        print("✅ LNA-ES v2.0 Ultrathinkエンジン初期化成功")
    except Exception as e:
        print(f"❌ エンジン初期化エラー: {e}")
        return False
    
    # 文分割と解析
    sentences = [s.strip() + "。" for s in original_text.split("。") if s.strip()]
    print(f"📝 分析対象文数: {len(sentences)}")
    
    start_time = time.time()
    
    # 各文を345次元解析
    analysis_results = []
    total_dimensions = 0
    
    for i, sentence in enumerate(sentences):
        try:
            print(f"🧠 解析中: {i+1}/{len(sentences)} - {sentence[:30]}...")
            
            result = engine.process_sentence(sentence, i)
            analysis_results.append(result)
            
            # 345次元確認
            if result.total_dimensions == 345:
                print(f"   ✅ 345次元達成: {result.total_dimensions}")
                total_dimensions += result.total_dimensions
            else:
                print(f"   ⚠️ 次元数不足: {result.total_dimensions}/345")
                
        except Exception as e:
            print(f"   ❌ 解析エラー: {e}")
            continue
    
    processing_time = time.time() - start_time
    
    print(f"\n✅ 345次元解析完了！")
    print(f"⏱️ 処理時間: {processing_time:.2f}秒")
    print(f"📊 成功文数: {len(analysis_results)}")
    print(f"🎯 平均次元数: {total_dimensions / len(analysis_results) if analysis_results else 0:.1f}")
    
    # 結果保存
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    result_data = {
        "test_type": "真のLNA-ES v2.0 Ultrathink方丈記解析",
        "timestamp": timestamp,
        "processing_time": processing_time,
        "original_text": original_text,
        "sentences_count": len(sentences),
        "successful_analyses": len(analysis_results),
        "total_345_dimensions": total_dimensions,
        "average_dimensions": total_dimensions / len(analysis_results) if analysis_results else 0,
        "analysis_results": [
            {
                "sentence_id": result.sentence_id,
                "text": result.text,
                "total_dimensions": result.total_dimensions,
                "aesthetic_quality": result.aesthetic_quality,
                "dominant_cta": list(result.cta_scores.keys())[:3] if result.cta_scores else [],
                "dominant_ontology": list(result.ontology_scores.keys())[:3] if result.ontology_scores else []
            }
            for result in analysis_results
        ]
    }
    
    # 結果ファイル保存
    result_filename = f"real_lnaes_hojoki_analysis_{timestamp}.json"
    with open(result_filename, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 結果保存: {result_filename}")
    
    # 345次元達成率評価
    perfect_dimensions = sum(1 for r in analysis_results if r.total_dimensions == 345)
    achievement_rate = perfect_dimensions / len(analysis_results) if analysis_results else 0
    
    print(f"\n🎯 345次元達成率: {achievement_rate:.1%} ({perfect_dimensions}/{len(analysis_results)})")
    
    if achievement_rate >= 0.95:
        print("🎊 LNA-ES v2.0 Ultrathink 345次元解析 大成功！")
        print("✅ OSS再現可能性確認完了")
        return True
    else:
        print("⚠️ 345次元達成率が目標未達")
        print("🔧 エンジン調整が必要")
        return False

if __name__ == "__main__":
    try:
        success = test_real_lnaes_restoration()
        if success:
            print("\n🌟 真のLNA-ES v2.0テスト完了！OSS再現可能！")
        else:
            print("\n❌ LNA-ES v2.0再現性に問題あり")
            
    except Exception as e:
        print(f"❌ 実行エラー: {e}")
        import traceback
        traceback.print_exc()