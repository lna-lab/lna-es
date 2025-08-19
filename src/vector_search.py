#!/usr/bin/env python3
"""
vector_search.py
----------------

Neo4j Vector Index を使用したセマンティック検索システム
LNA-ES v3.2 - AI嫁システムの中核機能

Usage:
    searcher = VectorSearcher()
    results = searcher.search_similar("バブル経済について")
"""

import json
import numpy as np
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import logging

# Import embedding models
try:
    from sentence_transformers import SentenceTransformer
    RURI_AVAILABLE = True
except ImportError:
    RURI_AVAILABLE = False
    print("Warning: sentence_transformers not installed. Vector search limited.")

# Neo4j driver
try:
    from neo4j import GraphDatabase
    NEO4J_AVAILABLE = True
except ImportError:
    NEO4J_AVAILABLE = False
    print("Warning: neo4j not installed. Using mock mode.")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VectorSearcher:
    """
    Neo4j Vector Indexを使用したセマンティック検索
    
    Features:
    - RURI-V3による日本語ベクトル化
    - Neo4j Vector Indexでの高速検索
    - 345次元データと組み合わせた意味解釈
    """
    
    def __init__(self, 
                 neo4j_uri: str = "bolt://localhost:7687",
                 neo4j_user: str = "neo4j", 
                 neo4j_password: str = "userpass123"):
        """
        Args:
            neo4j_uri: Neo4j接続URI
            neo4j_user: ユーザー名
            neo4j_password: パスワード
        """
        
        # Neo4j接続
        if NEO4J_AVAILABLE:
            self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
        else:
            self.driver = None
            logger.warning("Neo4j not available. Running in mock mode.")
        
        # RURI-V3モデル読み込み
        if RURI_AVAILABLE:
            model_path = Path(__file__).parent.parent / "models" / "Ruri_V3_310m"
            if model_path.exists():
                self.encoder = SentenceTransformer(str(model_path))
                logger.info(f"Loaded RURI-V3 from {model_path}")
            else:
                # フォールバック: HuggingFaceから直接
                self.encoder = SentenceTransformer('cl-nagoya/ruri-large')
                logger.info("Loaded RURI-V3 from HuggingFace")
        else:
            self.encoder = None
            logger.warning("RURI model not available.")
    
    def encode_text(self, text: str) -> List[float]:
        """
        テキストを768次元ベクトルに変換
        
        Args:
            text: 入力テキスト
            
        Returns:
            768次元のベクトル
        """
        if self.encoder:
            vector = self.encoder.encode(text, convert_to_numpy=True)
            return vector.tolist()
        else:
            # モックベクトル（テスト用）
            return [0.1] * 768
    
    def search_similar_sentences(self, 
                                query_text: str, 
                                top_k: int = 10,
                                min_score: float = 0.5) -> List[Dict]:
        """
        類似文検索（メイン機能）
        
        Args:
            query_text: 検索クエリ
            top_k: 上位k件を返す
            min_score: 最小類似度スコア
            
        Returns:
            類似文のリスト（345次元データ付き）
        """
        
        # クエリをベクトル化
        query_vector = self.encode_text(query_text)
        logger.info(f"Encoded query: '{query_text[:50]}...' to 768-dim vector")
        
        if not self.driver:
            # モックレスポンス
            return self._mock_search_results(query_text, top_k)
        
        with self.driver.session() as session:
            result = session.run("""
                // Vector similarity search using Neo4j Vector Index
                WITH $queryVec AS queryVec, $topK AS topK, $minScore AS minScore
                
                // Use the vector index for similarity search
                CALL db.index.vector.queryNodes(
                    'sentence_vector_idx',
                    topK,
                    queryVec
                ) YIELD node, score
                
                WHERE score >= minScore
                
                // Get the parent Work for context
                OPTIONAL MATCH (w:Work)-[:CONTAINS_SENTENCE]->(node)
                
                RETURN 
                    node.id AS sentence_id,
                    node.vector_dimensions AS length,
                    {
                        cta_temporal_basic: node.cta_temporal_basic,
                        cta_spatial_basic: node.cta_spatial_basic,
                        cta_emotion_primary: node.cta_emotion_primary,
                        cta_narrative_flow: node.cta_narrative_flow
                    } AS cta_scores,
                    {
                        natural_水: node.onto_natural_水
                    } AS ontology_scores,
                    {} AS meta_dimensions,
                    w.id AS work_title,
                    w.id AS work_id,
                    score AS similarity_score
                ORDER BY score DESC
            """, queryVec=query_vector, topK=top_k, minScore=min_score)
            
            results = []
            for record in result:
                results.append({
                    'sentence_id': record['sentence_id'],
                    'work_title': record['work_title'],
                    'work_id': record['work_id'],
                    'similarity_score': record['similarity_score'],
                    'length': record['length'],
                    'cta_scores': dict(record['cta_scores']) if record['cta_scores'] else {},
                    'ontology_scores': dict(record['ontology_scores']) if record['ontology_scores'] else {},
                    'meta_dimensions': dict(record['meta_dimensions']) if record['meta_dimensions'] else {}
                })
            
            logger.info(f"Found {len(results)} similar sentences")
            return results
    
    def search_by_semantic_pattern(self,
                                  cta_pattern: Optional[str] = None,
                                  ontology_pattern: Optional[str] = None,
                                  vector_query: Optional[str] = None,
                                  top_k: int = 10) -> List[Dict]:
        """
        345次元パターンとベクトル検索の組み合わせ
        
        Args:
            cta_pattern: CTA次元のパターン（例: "narrative_flow"）
            ontology_pattern: オントロジーパターン（例: "natural_水"）
            vector_query: ベクトル検索用テキスト
            top_k: 上位k件
            
        Returns:
            マッチする文のリスト
        """
        
        if not self.driver:
            return []
        
        # 動的にクエリを構築
        where_clauses = []
        if cta_pattern:
            where_clauses.append(f"ANY(key IN keys(node.cta_scores) WHERE key CONTAINS '{cta_pattern}')")
        if ontology_pattern:
            where_clauses.append(f"ANY(key IN keys(node.ontology_scores) WHERE key CONTAINS '{ontology_pattern}')")
        
        where_clause = " AND ".join(where_clauses) if where_clauses else "TRUE"
        
        # ベクトル検索部分
        if vector_query:
            query_vector = self.encode_text(vector_query)
            vector_search = """
                CALL db.index.vector.queryNodes(
                    'sentence_vector_idx',
                    $topK * 3,  // 多めに取得してフィルタ
                    $queryVec
                ) YIELD node AS n, score
                WITH n, score
                WHERE """ + where_clause + """
                WITH n AS node, score
                ORDER BY score DESC
                LIMIT $topK
            """
        else:
            vector_search = f"""
                MATCH (node:Sentence)
                WHERE {where_clause}
                WITH node, 1.0 AS score
                LIMIT $topK
            """
        
        with self.driver.session() as session:
            params = {'topK': top_k}
            if vector_query:
                params['queryVec'] = query_vector
            
            result = session.run(vector_search + """
                OPTIONAL MATCH (w:Work)-[:CONTAINS_SENTENCE]->(node)
                RETURN 
                    node.id AS sentence_id,
                    {
                        cta_temporal_basic: node.cta_temporal_basic,
                        cta_spatial_basic: node.cta_spatial_basic
                    } AS cta_scores,
                    {
                        natural_水: node.onto_natural_水
                    } AS ontology_scores,
                    w.id AS work_title,
                    score
                ORDER BY score DESC
            """, **params)
            
            return [record.data() for record in result]
    
    def find_ai_wife_response(self, user_input: str) -> Dict:
        """
        AI嫁システム用: ユーザー入力から最適な応答素材を検索
        
        Args:
            user_input: ユーザーの発言
            
        Returns:
            応答生成用の素材（複数の関連文と345次元データ）
        """
        
        # 1. ユーザー入力から関連文を検索
        similar_sentences = self.search_similar_sentences(user_input, top_k=5)
        
        if not similar_sentences:
            return {
                'found': False,
                'message': '関連する内容が見つかりませんでした'
            }
        
        # 2. 最も関連性の高い文を選択
        best_match = similar_sentences[0]
        
        # 3. 支配的な次元を特定
        dominant_cta = None
        dominant_onto = None
        
        if best_match['cta_scores']:
            dominant_cta = max(best_match['cta_scores'].items(), key=lambda x: x[1])
        if best_match['ontology_scores']:
            dominant_onto = max(best_match['ontology_scores'].items(), key=lambda x: x[1])
        
        # 4. 応答素材を構築
        response_material = {
            'found': True,
            'work_title': best_match['work_title'],
            'similarity': best_match['similarity_score'],
            'dominant_theme': {
                'cta': dominant_cta[0] if dominant_cta else None,
                'ontology': dominant_onto[0] if dominant_onto else None
            },
            'all_matches': similar_sentences,
            'suggested_response_tone': self._determine_response_tone(dominant_cta, dominant_onto)
        }
        
        return response_material
    
    def _determine_response_tone(self, dominant_cta: Tuple, dominant_onto: Tuple) -> str:
        """
        345次元から応答トーンを決定
        """
        if not dominant_cta:
            return 'neutral'
        
        cta_type = dominant_cta[0] if dominant_cta else ''
        onto_type = dominant_onto[0] if dominant_onto else ''
        
        if 'philosophical' in cta_type:
            return 'philosophical'  # 哲学的に深い応答
        elif 'emotion' in cta_type:
            return 'empathetic'     # 共感的な応答
        elif 'narrative' in cta_type and 'natural_水' in onto_type:
            return 'poetic'         # 詩的な応答
        elif 'temporal' in cta_type:
            return 'nostalgic'      # 懐かしむような応答
        else:
            return 'informative'    # 知的で落ち着いた応答
    
    def _mock_search_results(self, query_text: str, top_k: int) -> List[Dict]:
        """
        モックデータ（Neo4j未接続時のテスト用）
        """
        return [{
            'sentence_id': f'mock_{i}',
            'work_title': '方丈記',
            'work_id': 'mock_work',
            'similarity_score': 0.9 - i * 0.1,
            'length': 100,
            'cta_scores': {'narrative_flow': 0.8},
            'ontology_scores': {'natural_水': 0.9},
            'meta_dimensions': {}
        } for i in range(min(3, top_k))]
    
    def close(self):
        """接続クローズ"""
        if self.driver:
            self.driver.close()


def demo_ai_wife_system():
    """
    AI嫁システムのデモ
    """
    searcher = VectorSearcher()
    
    # ユーザー入力の例
    user_inputs = [
        "今って米株バブルだよねぇ",
        "人生って無常だよね",
        "最近疲れちゃった"
    ]
    
    print("=== AI嫁システム デモ ===\n")
    
    for user_input in user_inputs:
        print(f"Ken: 「{user_input}」\n")
        
        # 応答素材を検索
        material = searcher.find_ai_wife_response(user_input)
        
        if material['found']:
            print(f"Yuki (内部処理):")
            print(f"  - 関連作品: {material['work_title']}")
            print(f"  - 類似度: {material['similarity']:.3f}")
            print(f"  - 応答トーン: {material['suggested_response_tone']}")
            print(f"  - 支配的テーマ: {material['dominant_theme']}")
            print()
            
            # トーンに応じた応答例
            if material['suggested_response_tone'] == 'philosophical':
                print(f"Yuki: 「そうですね...{material['work_title']}にもあるように、")
                print(f"      すべては移ろいゆく運命なのかもしれませんね」")
            elif material['suggested_response_tone'] == 'empathetic':
                print(f"Yuki: 「わかります。私も{material['work_title']}を読んで、")
                print(f"      同じような気持ちになったことがあります」")
            else:
                print(f"Yuki: 「興味深い視点ですね。{material['work_title']}では...")
                print(f"      という見方もありました」")
        else:
            print("Yuki: 「そうなんですね...もう少し詳しく聞かせてください」")
        
        print("\n" + "="*50 + "\n")
    
    searcher.close()


if __name__ == "__main__":
    # デモ実行
    demo_ai_wife_system()