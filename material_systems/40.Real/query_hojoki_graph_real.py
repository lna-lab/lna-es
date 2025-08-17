#!/usr/bin/env python3
"""
方丈記グラフクエリ・可視化スクリプト
Neo4jに保存された方丈記グラフを分析・可視化
"""

import os
import sys
import json
from pathlib import Path
from neo4j import GraphDatabase
from typing import Dict, List, Any

class HojokiGraphAnalyzer:
    """方丈記グラフ分析クラス"""
    
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="userpass123"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()
        
    def get_basic_stats(self):
        """基本統計を取得"""
        with self.driver.session() as session:
            stats = {}
            
            # ノード数
            result = session.run("MATCH (n:HOJOKI) RETURN count(n) as count")
            stats['hojoki_texts'] = result.single()['count']
            
            result = session.run("MATCH (n:HOJOKI_ENTITY) RETURN count(n) as count")
            stats['entities'] = result.single()['count']
            
            # エンティティタイプ別統計
            result = session.run("""
                MATCH (n:HOJOKI_ENTITY)
                RETURN n.entity_type as type, count(n) as count
                ORDER BY count DESC
            """)
            stats['entity_types'] = {record['type']: record['count'] for record in result}
            
            # 関係エッジ数
            result = session.run("MATCH ()-[r:CONTAINS_ENTITY]->() RETURN count(r) as count")
            stats['contains_relationships'] = result.single()['count']
            
            return stats
    
    def get_top_entities(self, entity_type: str = None, limit: int = 10):
        """上位エンティティを取得"""
        with self.driver.session() as session:
            if entity_type:
                query = """
                    MATCH (n:HOJOKI_ENTITY)
                    WHERE n.entity_type = $entity_type
                    RETURN n.entity_text as text, n.confidence_score as confidence, n.entity_type as type
                    ORDER BY n.confidence_score DESC
                    LIMIT $limit
                """
                result = session.run(query, entity_type=entity_type, limit=limit)
            else:
                query = """
                    MATCH (n:HOJOKI_ENTITY)
                    RETURN n.entity_text as text, n.confidence_score as confidence, n.entity_type as type
                    ORDER BY n.confidence_score DESC
                    LIMIT $limit
                """
                result = session.run(query, limit=limit)
            
            return [record for record in result]
    
    def search_entities(self, search_term: str, limit: int = 10):
        """エンティティを検索"""
        with self.driver.session() as session:
            query = """
                MATCH (n:HOJOKI_ENTITY)
                WHERE n.entity_text CONTAINS $search_term
                RETURN n.entity_text as text, n.confidence_score as confidence, n.entity_type as type
                ORDER BY n.confidence_score DESC
                LIMIT $limit
            """
            result = session.run(query, search_term=search_term, limit=limit)
            return [record for record in result]
    
    def get_entity_context(self, entity_text: str):
        """エンティティの文脈を取得"""
        with self.driver.session() as session:
            query = """
                MATCH (n:HOJOKI_ENTITY)
                WHERE n.entity_text = $entity_text
                RETURN n.entity_text as text, n.context_window as context, 
                       n.confidence_score as confidence, n.entity_type as type
                LIMIT 1
            """
            result = session.run(query, entity_text=entity_text)
            return result.single()
    
    def get_related_entities(self, entity_text: str, limit: int = 5):
        """関連エンティティを取得"""
        with self.driver.session() as session:
            query = """
                MATCH (e1:HOJOKI_ENTITY)-[:CONTAINS_ENTITY]-(text:HOJOKI)-[:CONTAINS_ENTITY]-(e2:HOJOKI_ENTITY)
                WHERE e1.entity_text = $entity_text AND e1 <> e2
                RETURN e2.entity_text as text, e2.entity_type as type, e2.confidence_score as confidence
                ORDER BY e2.confidence_score DESC
                LIMIT $limit
            """
            result = session.run(query, entity_text=entity_text, limit=limit)
            return [record for record in result]
    
    def get_text_summary(self):
        """テキスト概要を取得"""
        with self.driver.session() as session:
            query = """
                MATCH (n:HOJOKI)
                RETURN n.title as title, n.author as author, n.text_length as length,
                       n.extraction_accuracy as accuracy, n.total_entities as entities
            """
            result = session.run(query)
            return result.single()

def print_separator(title: str):
    """セパレータを表示"""
    print(f"\n{'='*60}")
    print(f"📊 {title}")
    print(f"{'='*60}")

def main():
    """メイン処理"""
    print("🎯 方丈記グラフ分析プロジェクト")
    print("=" * 50)
    
    analyzer = HojokiGraphAnalyzer()
    
    try:
        # 基本統計
        print_separator("基本統計")
        stats = analyzer.get_basic_stats()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        
        # テキスト概要
        print_separator("テキスト概要")
        summary = analyzer.get_text_summary()
        if summary:
            print(f"📖 タイトル: {summary['title']}")
            print(f"👤 著者: {summary['author']}")
            print(f"📏 テキスト長: {summary['length']} 文字")
            print(f"🎯 抽出精度: {summary['accuracy']:.1%}")
            print(f"🏷️ 総エンティティ数: {summary['entities']}")
        
        # 上位エンティティ（人物）
        print_separator("上位人物エンティティ")
        top_persons = analyzer.get_top_entities("PERSON", 10)
        for i, person in enumerate(top_persons, 1):
            print(f"{i:2d}. {person['text']} (信頼度: {person['confidence']:.2f})")
        
        # 上位エンティティ（場所）
        print_separator("上位場所エンティティ")
        top_places = analyzer.get_top_entities("PLACE", 10)
        for i, place in enumerate(top_places, 1):
            print(f"{i:2d}. {place['text']} (信頼度: {place['confidence']:.2f})")
        
        # 上位エンティティ（概念）
        print_separator("上位概念エンティティ")
        top_concepts = analyzer.get_top_entities("CONCEPT", 10)
        for i, concept in enumerate(top_concepts, 1):
            print(f"{i:2d}. {concept['text']} (信頼度: {concept['confidence']:.2f})")
        
        # 上位エンティティ（行動）
        print_separator("上位行動エンティティ")
        top_actions = analyzer.get_top_entities("ACTION", 10)
        for i, action in enumerate(top_actions, 1):
            print(f"{i:2d}. {action['text']} (信頼度: {action['confidence']:.2f})")
        
        # 検索例
        print_separator("検索例: '京都'")
        search_results = analyzer.search_entities("京都", 5)
        for i, result in enumerate(search_results, 1):
            print(f"{i}. {result['text']} ({result['type']}, 信頼度: {result['confidence']:.2f})")
        
        # エンティティ文脈例
        if top_persons:
            print_separator(f"エンティティ文脈例: '{top_persons[0]['text']}'")
            context = analyzer.get_entity_context(top_persons[0]['text'])
            if context:
                print(f"📝 エンティティ: {context['text']}")
                print(f"🏷️ タイプ: {context['type']}")
                print(f"🎯 信頼度: {context['confidence']:.2f}")
                print(f"📄 文脈: {context['context'][:200]}...")
        
        # 関連エンティティ例
        if top_persons:
            print_separator(f"関連エンティティ例: '{top_persons[0]['text']}'")
            related = analyzer.get_related_entities(top_persons[0]['text'], 5)
            for i, rel in enumerate(related, 1):
                print(f"{i}. {rel['text']} ({rel['type']}, 信頼度: {rel['confidence']:.2f})")
        
    finally:
        analyzer.close()
    
    print("\n🎉 方丈記グラフ分析完了！")

if __name__ == "__main__":
    main()
