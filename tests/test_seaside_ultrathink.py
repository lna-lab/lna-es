#!/usr/bin/env python3
"""
海風のメロディ - LNA-ES v2.0 Ultrathink 345次元フル解析テスト
"""

from lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine
import json
import time

def load_seaside_text():
    """海風のメロディテキストを読み込み"""
    with open("seaside_love_story.txt", "r", encoding="utf-8") as f:
        return f.read()

def split_sentences(text):
    """文章を句読点で分割"""
    sentences = []
    current_sentence = ""
    
    for char in text:
        current_sentence += char
        if char in ["。", "！", "？"] or (char == "」" and len(current_sentence) > 10):
            sentences.append(current_sentence.strip())
            current_sentence = ""
    
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
        
    return [s for s in sentences if len(s) > 5]  # 短すぎる文は除外

def analyze_seaside_story():
    """海風のメロディの345次元フル解析"""
    print("🌊 LNA-ES v2.0 Ultrathink: 海風のメロディ 345次元解析開始")
    print("=" * 60)
    
    # エンジン初期化
    engine = LNAESv2UltrathinkEngine()
    
    # テキスト読み込み
    full_text = load_seaside_text()
    sentences = split_sentences(full_text)
    
    print(f"📖 解析対象: {len(sentences)}文、総文字数: {len(full_text)}文字")
    print()
    
    # 全文解析結果
    all_results = []
    total_dimensions = 0
    total_aesthetic = 0.0
    
    cta_dominant_counts = {}
    ontology_dominant_counts = {}
    
    print("🔬 文別345次元解析結果:")
    print("-" * 60)
    
    start_time = time.time()
    
    for i, sentence in enumerate(sentences[:10], 1):  # 最初の10文を解析
        result = engine.process_sentence(sentence, i)
        all_results.append(result)
        
        total_dimensions += result.total_dimensions
        total_aesthetic += result.aesthetic_quality
        
        # 支配パターン統計
        dominant_cta = result.dominant_analysis['dominant_cta'][0] if result.dominant_analysis['dominant_cta'][0] != 'none' else None
        dominant_onto = result.dominant_analysis['dominant_ontology'][0] if result.dominant_analysis['dominant_ontology'][0] != 'none' else None
        
        if dominant_cta:
            cta_dominant_counts[dominant_cta] = cta_dominant_counts.get(dominant_cta, 0) + 1
        if dominant_onto:
            ontology_dominant_counts[dominant_onto] = ontology_dominant_counts.get(dominant_onto, 0) + 1
        
        print(f"文{i:2d}: [{result.total_dimensions:3d}/345] 美的: {result.aesthetic_quality:.3f}")
        print(f"     テキスト: {sentence[:50]}...")
        print(f"     支配CTA: {result.dominant_analysis['dominant_cta'][0]}")
        print(f"     支配オントロジー: {result.dominant_analysis['dominant_ontology'][0]}")
        print(f"     次元分布: CTA={result.dominant_analysis['dimension_distribution']['cta_dimensions']}, "
              f"オントロジー={result.dominant_analysis['dimension_distribution']['ontology_dimensions']}, "
              f"メタ={result.dominant_analysis['dimension_distribution']['meta_dimensions']}")
        print()
    
    processing_time = time.time() - start_time
    
    # 統計サマリー
    print("📊 解析統計サマリー")
    print("=" * 60)
    print(f"⭐ 総解析文数: {len(all_results)}")
    print(f"⭐ 平均次元数: {total_dimensions / len(all_results):.1f} / 345")
    print(f"⭐ 平均美的品質: {total_aesthetic / len(all_results):.3f}")
    print(f"⭐ 処理時間: {processing_time:.2f}秒")
    print(f"⭐ 文あたり処理時間: {processing_time / len(all_results):.3f}秒")
    print()
    
    # 支配パターン分析
    if cta_dominant_counts:
        print("🎯 支配CTAパターン:")
        for pattern, count in sorted(cta_dominant_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   {pattern.replace('cta_', '')}: {count}回")
        print()
    
    if ontology_dominant_counts:
        print("🌟 支配オントロジーパターン:")
        for pattern, count in sorted(ontology_dominant_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   {pattern.replace('onto_', '')}: {count}回")
        print()
    
    # 詳細分析結果保存
    detailed_results = {
        "story_title": "海風のメロディ",
        "analysis_timestamp": time.time(),
        "engine_version": "LNA-ES_v2.0_Ultrathink", 
        "total_sentences": len(all_results),
        "average_dimensions": total_dimensions / len(all_results),
        "average_aesthetic_quality": total_aesthetic / len(all_results),
        "processing_time_seconds": processing_time,
        "dominant_cta_patterns": cta_dominant_counts,
        "dominant_ontology_patterns": ontology_dominant_counts,
        "sentence_results": []
    }
    
    for result in all_results:
        detailed_results["sentence_results"].append({
            "sentence_id": result.sentence_id,
            "text": result.text,
            "total_dimensions": result.total_dimensions,
            "aesthetic_quality": result.aesthetic_quality,
            "dominant_cta": result.dominant_analysis['dominant_cta'],
            "dominant_ontology": result.dominant_analysis['dominant_ontology'],
            "dimension_distribution": result.dominant_analysis['dimension_distribution']
        })
    
    # 結果保存
    output_file = f"seaside_ultrathink_345d_analysis_{int(time.time())}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(detailed_results, f, ensure_ascii=False, indent=2)
    
    print(f"📄 詳細解析結果保存: {output_file}")
    print()
    print("🎉 LNA-ES v2.0 Ultrathink 345次元解析完了！")
    
    return detailed_results

if __name__ == "__main__":
    analyze_seaside_story()