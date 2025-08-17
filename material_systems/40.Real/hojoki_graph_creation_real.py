#!/usr/bin/env python3
"""
方丈記テキストのグラフ化スクリプト
MCP機能を使用してテキストをグラフデータベースに変換
"""

import os
import sys
import json
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "lna-es"))

from src.ultrathink_graph_extractor import UltrathinkGraphExtractor

def create_hojoki_graph():
    """方丈記テキストをグラフ化する"""
    result = None
    
    # テキストファイルのパス
    text_file = project_root / "lna-es" / "data" / "hojoki_test_4000chars.txt"
    
    if not text_file.exists():
        print(f"エラー: テキストファイルが見つかりません: {text_file}")
        return
    
    # テキストを読み込み
    with open(text_file, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    print("方丈記テキストを読み込みました")
    print(f"テキスト長: {len(text_content)} 文字")
    
    # Ultrathinkグラフ抽出エンジンを初期化
    try:
        extractor = UltrathinkGraphExtractor()
        print("Ultrathinkグラフ抽出エンジンを初期化しました")
        
        # テキストをグラフ化
        print("テキストをグラフ化中...")
        result = extractor.extract_complete_graph(
            text=text_content,
            title="方丈記 - 鴨長明"
        )
        
        if result:
            print("✅ 方丈記のグラフ化が完了しました！")
            print(f"作成されたノード数: {len(result.nodes)}")
            print(f"作成されたエッジ数: {len(result.edges)}")
            print(f"抽出精度: {result.extraction_accuracy:.1%}")
            
            # 結果の詳細を表示
            print(f"\n詳細情報:")
            print(f"  人物エンティティ: {len(result.person_entities)}")
            print(f"  場所エンティティ: {len(result.place_entities)}")
            print(f"  物体エンティティ: {len(result.object_entities)}")
            print(f"  概念エンティティ: {len(result.concept_entities)}")
            print(f"  感情エンティティ: {len(result.emotion_entities)}")
            print(f"  行動エンティティ: {len(result.action_entities)}")
            print(f"  処理時間: {result.processing_time:.3f}秒")
        else:
            print("❌ グラフ化に失敗しました")
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
    
    return result

def analyze_hojoki_graph():
    """作成されたグラフを分析する"""
    
    try:
        print("\n📊 グラフ分析結果:")
        print("方丈記のテキストから以下の要素が抽出されました:")
        
        # 結果オブジェクトから詳細情報を表示
        if 'result' in globals():
            result = globals()['result']
            print(f"  総エンティティ数: {result.total_entities}")
            print(f"  抽出精度: {result.extraction_accuracy:.1%}")
            
            # 主要なエンティティを表示
            if result.person_entities:
                print(f"\n👥 主要人物:")
                for person in result.person_entities[:5]:
                    print(f"    - {person.entity_text} (信頼度: {person.confidence_score:.2f})")
            
            if result.place_entities:
                print(f"\n🏛️ 主要場所:")
                for place in result.place_entities[:5]:
                    print(f"    - {place.entity_text} (信頼度: {place.confidence_score:.2f})")
            
            if result.concept_entities:
                print(f"\n💭 主要概念:")
                for concept in result.concept_entities[:5]:
                    print(f"    - {concept.entity_text} (信頼度: {concept.confidence_score:.2f})")
        else:
            print("分析データが見つかりませんでした")
            
    except Exception as e:
        print(f"分析中にエラーが発生しました: {e}")

if __name__ == "__main__":
    print("🎯 方丈記グラフ化プロジェクト開始")
    print("=" * 50)
    
    # グラフ作成
    global result
    result = create_hojoki_graph()
    
    # グラフ分析
    analyze_hojoki_graph()
    
    print("\n🎉 処理完了！")
