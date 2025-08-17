#!/usr/bin/env python3
"""
方丈記グラフをNeo4jデータベースに保存するスクリプト
"""

import os
import sys
import json
from pathlib import Path
from neo4j import GraphDatabase
from typing import Dict, List, Any

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "lna-es"))

from src.ultrathink_graph_extractor import UltrathinkGraphExtractor

class Neo4jGraphSaver:
    """Neo4jグラフ保存クラス"""
    
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="userpass123"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()
        
    def save_extraction_result(self, result):
        """抽出結果をNeo4jに保存"""
        with self.driver.session() as session:
            # 既存のデータをクリア
            session.run("MATCH (n:HOJOKI) DETACH DELETE n")
            session.run("MATCH (n:HOJOKI_ENTITY) DETACH DELETE n")
            session.run("MATCH (n:HOJOKI_RELATION) DETACH DELETE n")
            
            print("🗑️ 既存のデータをクリアしました")
            
            # メインテキストノードを作成
            text_node_id = session.run("""
                CREATE (n:HOJOKI {
                    title: $title,
                    author: $author,
                    text_length: $text_length,
                    extraction_accuracy: $accuracy,
                    total_entities: $total_entities,
                    processing_time: $processing_time,
                    created_timestamp: $timestamp
                }) RETURN id(n) as node_id
            """, {
                'title': '方丈記 - 鴨長明',
                'author': '鴨長明',
                'text_length': len(result.source_text),
                'accuracy': result.extraction_accuracy,
                'total_entities': result.total_entities,
                'processing_time': result.processing_time,
                'timestamp': result.created_timestamp
            }).single()['node_id']
            
            print(f"📝 メインテキストノードを作成しました (ID: {text_node_id})")
            
            # エンティティノードを作成
            entity_count = 0
            for entity_type, entities in [
                ('PERSON', result.person_entities),
                ('PLACE', result.place_entities),
                ('OBJECT', result.object_entities),
                ('CONCEPT', result.concept_entities),
                ('EMOTION', result.emotion_entities),
                ('ACTION', result.action_entities)
            ]:
                for entity in entities:
                    session.run("""
                        CREATE (n:HOJOKI_ENTITY {
                            entity_text: $text,
                            entity_type: $type,
                            confidence_score: $confidence,
                            position_start: $start,
                            position_end: $end,
                            context_window: $context,
                            high_resolution_id: $hr_id
                        })
                    """, {
                        'text': entity.entity_text,
                        'type': entity_type,
                        'confidence': entity.confidence_score,
                        'start': entity.position_start,
                        'end': entity.position_end,
                        'context': entity.context_window,
                        'hr_id': entity.high_resolution_id
                    })
                    entity_count += 1
                    
                    # メインテキストとの関係を作成
                    session.run("""
                        MATCH (text:HOJOKI), (entity:HOJOKI_ENTITY)
                        WHERE id(text) = $text_id AND entity.high_resolution_id = $hr_id
                        CREATE (text)-[:CONTAINS_ENTITY]->(entity)
                    """, {
                        'text_id': text_node_id,
                        'hr_id': entity.high_resolution_id
                    })
            
            print(f"🏷️ {entity_count}個のエンティティノードを作成しました")
            
            # グラフエッジを作成
            edge_count = 0
            for edge in result.edges:
                session.run("""
                    CREATE (n:HOJOKI_RELATION {
                        source_node_id: $source_id,
                        target_node_id: $target_id,
                        relationship_type: $rel_type,
                        confidence_score: $confidence,
                        high_resolution_id: $hr_id
                    })
                """, {
                    'source_id': edge.source_node_id,
                    'target_id': edge.target_node_id,
                    'rel_type': edge.relationship_type,
                    'confidence': edge.confidence_score,
                    'hr_id': edge.high_resolution_id
                })
                edge_count += 1
                
                # エンティティ間の関係を作成
                session.run("""
                    MATCH (source:HOJOKI_ENTITY), (target:HOJOKI_ENTITY)
                    WHERE source.high_resolution_id = $source_hr_id AND target.high_resolution_id = $target_hr_id
                    CREATE (source)-[:RELATES_TO {type: $rel_type, confidence: $confidence}]->(target)
                """, {
                    'source_hr_id': edge.source_node_id,
                    'target_hr_id': edge.target_node_id,
                    'rel_type': edge.relationship_type,
                    'confidence': edge.confidence_score
                })
            
            print(f"🔗 {edge_count}個の関係エッジを作成しました")
            
            return {
                'text_node_id': text_node_id,
                'entity_count': entity_count,
                'edge_count': edge_count
            }
    
    def get_graph_stats(self):
        """グラフ統計を取得"""
        with self.driver.session() as session:
            stats = {}
            
            # ノード数
            result = session.run("MATCH (n:HOJOKI) RETURN count(n) as count")
            stats['hojoki_nodes'] = result.single()['count']
            
            result = session.run("MATCH (n:HOJOKI_ENTITY) RETURN count(n) as count")
            stats['entity_nodes'] = result.single()['count']
            
            result = session.run("MATCH (n:HOJOKI_RELATION) RETURN count(n) as count")
            stats['relation_nodes'] = result.single()['count']
            
            # エッジ数
            result = session.run("MATCH ()-[r:CONTAINS_ENTITY]->() RETURN count(r) as count")
            stats['contains_edges'] = result.single()['count']
            
            result = session.run("MATCH ()-[r:RELATES_TO]->() RETURN count(r) as count")
            stats['relates_edges'] = result.single()['count']
            
            # エンティティタイプ別統計
            result = session.run("""
                MATCH (n:HOJOKI_ENTITY)
                RETURN n.entity_type as type, count(n) as count
                ORDER BY count DESC
            """)
            stats['entity_types'] = {record['type']: record['count'] for record in result}
            
            return stats

def main():
    """メイン処理"""
    print("🎯 方丈記Neo4j保存プロジェクト開始")
    print("=" * 50)
    
    # グラフ抽出
    print("📖 方丈記テキストを読み込み中...")
    text_file = project_root / "lna-es" / "data" / "hojoki_test_4000chars.txt"
    
    with open(text_file, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    print(f"テキスト長: {len(text_content)} 文字")
    
    # グラフ抽出
    print("\n🔍 グラフ抽出実行中...")
    extractor = UltrathinkGraphExtractor()
    result = extractor.extract_complete_graph(
        text=text_content,
        title="方丈記 - 鴨長明"
    )
    
    print(f"✅ 抽出完了: {result.total_entities}エンティティ, {len(result.edges)}エッジ")
    
    # Neo4jに保存
    print("\n💾 Neo4jに保存中...")
    saver = Neo4jGraphSaver()
    
    try:
        save_result = saver.save_extraction_result(result)
        print(f"✅ 保存完了:")
        print(f"   テキストノードID: {save_result['text_node_id']}")
        print(f"   エンティティ数: {save_result['entity_count']}")
        print(f"   エッジ数: {save_result['edge_count']}")
        
        # 統計情報を表示
        print("\n📊 グラフ統計:")
        stats = saver.get_graph_stats()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        
    finally:
        saver.close()
    
    print("\n🎉 方丈記グラフ保存完了！")

if __name__ == "__main__":
    main()

