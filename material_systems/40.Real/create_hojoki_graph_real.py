#!/usr/bin/env python3
"""
方丈記グラフ作成スクリプト
"""

import sys
import os
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent / "lna-es"
sys.path.append(str(project_root))

from src.neo4j_graph_manager import Neo4jGraphContext

def create_hojoki_graph():
    """方丈記のグラフを作成"""
    
    # 方丈記のテキスト（簡略版）
    hojoki_text = """
    現代語訳　方丈記
    鴨長明
    佐藤春夫訳
    
    河の流れは常に絶える事がなく、しかも流れ行く河の水は移り変って絶間がない。
    奔流に現われる飛沫は一瞬も止る事がなく、現れるや直に消えてしまって又新しく現れるのである。
    世の中の人々の運命や、人々の住家の移り変りの激しい事等は丁度河の流れにも譬えられ、
    又奔流に現われては消えさる飛沫の様に極めてはかないものである。
    
    人間のこういう運命、朝に生れては夕に死して行かなくてはならない果敢ない運命、
    変転極りない運命、こういう事を深く考えて見ると全く、
    結んでは直に消え、消えては又結ぶ水流の泡沫の如きものではないかと思ったりする。
    
    長い年月の間に火事の為に、地震の為、或いは他の色んな変事の為に、
    立派な美しい家が無くなってしまったり、又お金持の家が貧しくなったり、
    貴い地位にあった人が賤しい身分に落ちぶれたりする、
    こうした人々やその住家の移り変りの極りない事は恰も朝顔の花に置く朝露と、その花との様なものである。
    """
    
    try:
        with Neo4jGraphContext(password="userpass123") as graph:
            print("✅ Neo4jに接続しました")
            
            # グラフデータを作成
            graph_data = {
                "text_id": "hojoki_analysis_2025",
                "original_text": hojoki_text,
                "language": "ja",
                "char_count": len(hojoki_text),
                "source": "方丈記（鴨長明）",
                "era": "鎌倉時代",
                "segments": [
                    {
                        "theme": "無常観と人生の儚さ",
                        "key_concepts": ["無常", "儚さ", "運命", "変転"],
                        "philosophical_core": "人生は川の流れや泡のように儚く、常に変化する",
                        "modern_relevance": "現代社会における変化の激しさと人生の不確実性"
                    },
                    {
                        "theme": "自然現象と人間の運命",
                        "key_concepts": ["火事", "地震", "旋風", "災害"],
                        "philosophical_core": "自然の力は人間の努力を無にする",
                        "modern_relevance": "自然災害と人間社会の脆弱性"
                    },
                    {
                        "theme": "住居と人生の関係",
                        "key_concepts": ["住家", "移り変り", "富", "貧困"],
                        "philosophical_core": "住居は人生の栄枯盛衰を象徴する",
                        "modern_relevance": "住宅事情と社会格差の問題"
                    }
                ]
            }
            
            # グラフを作成
            text_id = graph.create_text_analysis_graph(graph_data)
            print(f"✅ 方丈記グラフを作成しました: {text_id}")
            
            # データベース統計を取得
            stats = graph.get_database_stats()
            print(f"📊 データベース統計: {stats}")
            
            return text_id
            
    except Exception as e:
        print(f"❌ グラフ作成エラー: {e}")
        return None

if __name__ == "__main__":
    create_hojoki_graph()
