#!/usr/bin/env python3
"""
ultrathink_extractor.py
-----------------------

LNA-ES v3.2 Ultrathink Engine Integration
革命的パイプライン: text → Ultrathink Engine → 345次元解析 → 高精度グラフ化

Based on material_systems/10.Ultra breakthrough and extractor.py integration
Replaces NDC/Kindle classification with 345-dimensional semantic analysis
"""

import sys
import json
import os
import time
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import Ultrathink Engine
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR / "material_systems" / "10.Ultra"))
from lna_es_v2_ultrathink_engine_super_real import LNAESv2UltrathinkEngine, LNAESResult

# Import enhanced ID generation
from enhanced_id_generator import EnhancedIDGenerator

class UltrathinkExtractor:
    """
    LNA-ES v3.2 Ultrathink Extractor
    
    Revolutionary pipeline:
    text → Ultrathink Engine → 345-dimensional analysis → Neo4j graph
    """
    
    def __init__(self):
        self.engine = LNAESv2UltrathinkEngine()
        self.id_generator = EnhancedIDGenerator()
        
        # RURI-V3モデル読み込み
        self.ruri_model = None
        try:
            from sentence_transformers import SentenceTransformer
            model_path = Path(__file__).parent.parent / "models" / "Ruri_V3_310m"
            if model_path.exists():
                self.ruri_model = SentenceTransformer(str(model_path))
                logger.info(f"✅ Loaded RURI-V3 from {model_path}")
            else:
                logger.warning(f"RURI-V3 model not found at {model_path}")
        except ImportError:
            logger.warning("sentence_transformers not installed")
        
    def extract_with_ultrathink(self, text: str, title: str = "unknown") -> Dict[str, Any]:
        """
        Ultrathink Engine統合抽出
        
        Args:
            text: 入力テキスト
            title: タイトル（オプション）
            
        Returns:
            Ultrathink解析結果とグラフデータ
        """
        start_time = time.time()
        
        # 1. Work ID生成
        work_id = self.id_generator.generate_work_id(title, title + ".txt")
        
        # 2. テキスト分割（文単位）
        sentences = self._split_sentences(text)
        
        # 3. Ultrathink Engine解析 + RURI-V3ベクトル埋め込み
        logger.info("Starting Ultrathink Engine analysis...")
        ultrathink_results = []
        
        for i, sentence in enumerate(sentences):
            if sentence.strip():
                # 文ID生成（自動インクリメント）
                sentence_id = self.id_generator.generate_sentence_id(work_id)
                
                # Ultrathink解析実行
                dimensions = self.engine.analyze_345_dimensions(sentence)
                
                # RURI-V3ベクトル埋め込み生成
                vector_embedding = self._generate_ruri_embedding(sentence)
                
                # LNAESResult形式に変換（ベクトル付き）
                result = self._create_lnaes_result(sentence_id, sentence, dimensions, vector_embedding)
                ultrathink_results.append(result)
        
        # 4. 文書レベル集約
        document_analysis = self._aggregate_document_analysis(ultrathink_results)
        
        # 5. グラフ構造生成
        graph_data = self._generate_graph_structure(
            work_id, title, text, ultrathink_results, document_analysis
        )
        
        processing_time = time.time() - start_time
        
        # 6. Cypher script生成
        cypher_script = self._generate_cypher_script(work_id, graph_data, document_analysis)
        
        return {
            "work_id": work_id,
            "title": title,
            "processing_time": processing_time,
            "ultrathink_results": ultrathink_results,
            "document_analysis": document_analysis,
            "graph_data": graph_data,
            "cypher_script": cypher_script,
            "metadata": {
                "total_sentences": len(sentences),
                "total_dimensions": 345,
                "aesthetic_quality": document_analysis.get("aesthetic_quality", 0.0),
                "dominant_cta": document_analysis.get("dominant_cta"),
                "dominant_ontology": document_analysis.get("dominant_ontology")
            }
        }
    
    def _generate_cypher_script(self, work_id: str, graph_data: Dict[str, Any], 
                               doc_analysis: Dict[str, Any]) -> str:
        """UltrathinkグラフデータからCypherスクリプト生成"""
        
        cypher_lines = []
        
        # 1. 制約定義（Community Edition対応）
        cypher_lines.extend([
            "// LNA-ES v3.2 Ultrathink Graph Schema (Community Edition)",
            "// 345-dimensional semantic analysis constraints",
            "",
            "// Work constraints",
            "CREATE CONSTRAINT work_id_unique IF NOT EXISTS FOR (w:Work) REQUIRE w.id IS UNIQUE;",
            "",
            "// Sentence constraints", 
            "CREATE CONSTRAINT sentence_id_unique IF NOT EXISTS FOR (s:Sentence) REQUIRE s.id IS UNIQUE;",
            "",
            "// CTA Dimension constraints",
            "CREATE CONSTRAINT cta_id_unique IF NOT EXISTS FOR (c:CTA_Dimension) REQUIRE c.id IS UNIQUE;",
            "",
            "// Entity constraints",
            "CREATE CONSTRAINT entity_id_unique IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE;",
            "",
        ])
        
        # 2. パラメータ定義
        cypher_lines.append("// Parameters")
        
        # Work parameters
        cypher_lines.extend([
            f":param work_id => '{work_id}';",
            f":param aesthetic_quality => {doc_analysis.get('aesthetic_quality', 0.0)};",
            f":param dominant_cta => '{doc_analysis.get('dominant_cta', ['none', 0])[0]}';",
            f":param dominant_ontology => '{doc_analysis.get('dominant_ontology', ['none', 0])[0]}';",
            f":param total_dimensions => 345;",
            f":param ultrathink_enabled => true;",
            ""
        ])
        
        # 3. ノード作成
        cypher_lines.extend([
            "// Create nodes",
            "",
            "// Work node",
            "CREATE (w:Work {",
            "  id: $work_id,",
            "  aesthetic_quality: $aesthetic_quality,", 
            "  dominant_cta: $dominant_cta,",
            "  dominant_ontology: $dominant_ontology,",
            "  total_dimensions: $total_dimensions,",
            "  ultrathink_enabled: $ultrathink_enabled",
            "});",
            ""
        ])
        
        # 4. Sentence nodes
        nodes = graph_data.get("nodes", [])
        for node in nodes:
            if node["type"] == "Sentence":
                # CTA scores をフラット化
                cta_params = []
                for cta, score in node.get("cta_scores", {}).items():
                    param_name = f"cta_{cta.replace('-', '_')}"
                    cypher_lines.append(f":param {param_name} => {score};")
                    cta_params.append(f"{param_name}: ${param_name}")
                
                # Ontology scores をフラット化  
                onto_params = []
                for onto, score in node.get("ontology_scores", {}).items():
                    param_name = f"onto_{onto.replace('-', '_').replace('_', '_')}"
                    cypher_lines.append(f":param {param_name} => {score};")
                    onto_params.append(f"{param_name}: ${param_name}")
                
                cypher_lines.extend([
                    f":param sentence_id_{node['id'][-4:]} => '{node['id']}';",
                    f":param sentence_aesthetic_{node['id'][-4:]} => {node.get('aesthetic_quality', 0.0)};",
                    ""
                ])
                
                # ベクトル埋め込みパラメータ追加
                vector_embedding = node.get("metadata", {}).get("vector_embedding", [])
                if vector_embedding:
                    cypher_lines.append(f":param vector_embedding_{node['id'][-4:]} => {json.dumps(vector_embedding)};")
                    cypher_lines.append(f":param vector_dimensions_{node['id'][-4:]} => {len(vector_embedding)};")
                
                cypher_lines.extend([
                    f"CREATE (s_{node['id'][-4:]}:Sentence {{",
                    f"  id: $sentence_id_{node['id'][-4:]},",
                    f"  aesthetic_quality: $sentence_aesthetic_{node['id'][-4:]},",
                    f"  ultrathink_analyzed: true"
                ])
                
                if vector_embedding:
                    cypher_lines.extend([
                        f"  vector_embedding: $vector_embedding_{node['id'][-4:]},",
                        f"  vector_dimensions: $vector_dimensions_{node['id'][-4:]},"
                    ])
                
                if cta_params:
                    cypher_lines.append(f"  // CTA scores")
                    for param in cta_params:
                        cypher_lines.append(f"  {param},")
                
                if onto_params:
                    cypher_lines.append(f"  // Ontology scores") 
                    for param in onto_params:
                        cypher_lines.append(f"  {param},")
                
                # 最後のカンマを削除
                if cypher_lines[-1].endswith(","):
                    cypher_lines[-1] = cypher_lines[-1][:-1]
                
                cypher_lines.extend([
                    "});",
                    ""
                ])
        
        # 5. CTA Dimension nodes
        for node in nodes:
            if node["type"] == "CTA_Dimension":
                cypher_lines.extend([
                    f":param cta_dim_id_{node['id'][-4:]} => '{node['id']}';",
                    f":param cta_type_{node['id'][-4:]} => '{node['cta_type']}';",
                    f":param cta_score_{node['id'][-4:]} => {node['aggregate_score']};",
                    ""
                ])
                
                cypher_lines.extend([
                    f"CREATE (c_{node['id'][-4:]}:CTA_Dimension {{",
                    f"  id: $cta_dim_id_{node['id'][-4:]},",
                    f"  cta_type: $cta_type_{node['id'][-4:]},",
                    f"  aggregate_score: $cta_score_{node['id'][-4:]},",
                    f"  ultrathink_enhanced: true",
                    f"}});",
                    ""
                ])
        
        # 6. 関係作成
        cypher_lines.extend([
            "// Create relationships",
            ""
        ])
        
        relationships = graph_data.get("relationships", [])
        for i, rel in enumerate(relationships):
            from_ref = f"w" if rel["from"] == work_id else f"s_{rel['from'][-4:]}"
            to_ref = f"s_{rel['to'][-4:]}" if rel["type"] == "CONTAINS_SENTENCE" else f"c_{rel['to'][-4:]}"
            
            weight = rel.get("properties", {}).get("weight", rel.get("properties", {}).get("ultrathink_weight", 1.0))
            
            cypher_lines.extend([
                f":param rel_weight_{i} => {weight};",
                f"MATCH (from), (to) WHERE from.id = '{rel['from']}' AND to.id = '{rel['to']}'",
                f"CREATE (from)-[:{rel['type']} {{weight: $rel_weight_{i}, ultrathink_derived: true}}]->(to);",
                ""
            ])
        
        cypher_lines.append("// Ultrathink Engine analysis complete")
        
        return "\n".join(cypher_lines)
    
    def _generate_ruri_embedding(self, text: str) -> List[float]:
        """RURI-V3による768次元ベクトル埋め込み生成"""
        try:
            # self.ruri_modelは__init__で既に読み込み済み
            if self.ruri_model is not None:
                # 実際のRURI-V3推論
                embedding = self.ruri_model.encode(text, convert_to_numpy=True)
                logger.debug(f"Generated RURI-V3 embedding for text: {text[:50]}...")
                return embedding.tolist()
            else:
                # フォールバック: 疑似768次元ベクトル生成
                np.random.seed(hash(text) % 2**32)
                embedding = np.random.normal(0, 1, 768).tolist()
                logger.debug(f"Generated fallback embedding for text: {text[:50]}...")
                return embedding
                
        except Exception as e:
            logger.warning(f"RURI embedding failed, using fallback: {e}")
            # フォールバック
            np.random.seed(hash(text) % 2**32)
            return np.random.normal(0, 1, 768).tolist()
    
    def _create_lnaes_result(self, sentence_id: str, text: str, dimensions: Dict[str, float], 
                           vector_embedding: Optional[List[float]] = None) -> LNAESResult:
        """Ultrathink解析結果をLNAESResult形式に変換"""
        
        # 次元を分類
        cta_scores = {k[4:]: v for k, v in dimensions.items() if k.startswith("cta_")}
        ontology_scores = {k[5:]: v for k, v in dimensions.items() if k.startswith("onto_")}
        meta_dimensions = {k: v for k, v in dimensions.items() if not k.startswith(("cta_", "onto_"))}
        
        # 支配的要素特定
        dominant_cta = max(cta_scores.items(), key=lambda x: x[1]) if cta_scores else ("none", 0.0)
        dominant_ontology = max(ontology_scores.items(), key=lambda x: x[1]) if ontology_scores else ("none", 0.0)
        dominant_meta = max(meta_dimensions.items(), key=lambda x: x[1]) if meta_dimensions else ("none", 0.0)
        
        # 美的品質計算
        aesthetic_quality = sum(cta_scores.values()) / len(cta_scores) if cta_scores else 0.0
        
        return LNAESResult(
            sentence_id=sentence_id,
            text=text,
            cta_scores=cta_scores,
            ontology_scores=ontology_scores,
            meta_dimensions=meta_dimensions,
            dominant_analysis={
                "dominant_cta": dominant_cta,
                "dominant_ontology": dominant_ontology,
                "dominant_meta": dominant_meta
            },
            aesthetic_quality=aesthetic_quality,
            total_dimensions=len(dimensions),
            metadata={
                "ultrathink_enabled": True,
                "analysis_timestamp": time.time(),
                "vector_embedding": vector_embedding,
                "vector_dimensions": len(vector_embedding) if vector_embedding else 0
            }
        )
    
    def _split_sentences(self, text: str) -> List[str]:
        """テキストを文に分割"""
        # 簡易文分割（日本語対応）
        import re
        sentences = re.split(r'[。！？\n]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _aggregate_document_analysis(self, results: List[LNAESResult]) -> Dict[str, Any]:
        """文レベル解析を文書レベルに集約"""
        if not results:
            return {}
        
        # CTA次元集約
        cta_aggregate = {}
        ontology_aggregate = {}
        meta_aggregate = {}
        aesthetic_qualities = []
        
        for result in results:
            # CTA集約
            for cta, score in result.cta_scores.items():
                cta_aggregate[cta] = cta_aggregate.get(cta, 0) + score
            
            # オントロジー集約
            for onto, score in result.ontology_scores.items():
                ontology_aggregate[onto] = ontology_aggregate.get(onto, 0) + score
            
            # メタ次元集約
            for meta, score in result.meta_dimensions.items():
                meta_aggregate[meta] = meta_aggregate.get(meta, 0) + score
            
            aesthetic_qualities.append(result.aesthetic_quality)
        
        # 正規化
        num_sentences = len(results)
        cta_aggregate = {k: v/num_sentences for k, v in cta_aggregate.items()}
        ontology_aggregate = {k: v/num_sentences for k, v in ontology_aggregate.items()}
        meta_aggregate = {k: v/num_sentences for k, v in meta_aggregate.items()}
        
        # 支配的要素特定
        dominant_cta = max(cta_aggregate.items(), key=lambda x: x[1]) if cta_aggregate else None
        dominant_ontology = max(ontology_aggregate.items(), key=lambda x: x[1]) if ontology_aggregate else None
        dominant_meta = max(meta_aggregate.items(), key=lambda x: x[1]) if meta_aggregate else None
        
        return {
            "cta_aggregate": cta_aggregate,
            "ontology_aggregate": ontology_aggregate,
            "meta_aggregate": meta_aggregate,
            "aesthetic_quality": sum(aesthetic_qualities) / len(aesthetic_qualities),
            "dominant_cta": dominant_cta,
            "dominant_ontology": dominant_ontology,
            "dominant_meta": dominant_meta,
            "total_dimensions": 345,
            "ultrathink_enabled": True
        }
    
    def _generate_graph_structure(self, work_id: str, title: str, text: str, 
                                 results: List[LNAESResult], 
                                 doc_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """グラフ構造生成（Ultrathink強化版）"""
        
        # ノード生成
        nodes = []
        relationships = []
        
        # 文書ノード
        work_node = {
            "id": work_id,
            "type": "Work",
            "title": title,
            "ultrathink_enabled": True,
            "aesthetic_quality": doc_analysis.get("aesthetic_quality", 0.0),
            "dominant_cta": doc_analysis.get("dominant_cta", [None, 0])[0],
            "dominant_ontology": doc_analysis.get("dominant_ontology", [None, 0])[0],
            "total_dimensions": 345
        }
        nodes.append(work_node)
        
        # 文ノード生成
        for result in results:
            sentence_node = {
                "id": result.sentence_id,
                "type": "Sentence",
                # text_previewは削除 - 345次元のみを保存
                "cta_scores": result.cta_scores,  # 44次元
                "ontology_scores": result.ontology_scores,  # 15次元  
                "meta_dimensions": result.meta_dimensions,  # 286次元
                "aesthetic_quality": result.aesthetic_quality,
                "sentence_length": len(result.text),  # 長さのヒントのみ
                "ultrathink_analyzed": True,
                "metadata": result.metadata  # ベクトル埋め込み情報含む
            }
            nodes.append(sentence_node)
            
            # Work-Sentence関係
            relationships.append({
                "from": work_id,
                "to": result.sentence_id,
                "type": "CONTAINS_SENTENCE",
                "properties": {
                    "ultrathink_weight": result.aesthetic_quality
                }
            })
        
        # CTAクラスターノード生成
        if "cta_aggregate" in doc_analysis:
            for cta, score in doc_analysis["cta_aggregate"].items():
                if score > 0.1:  # 閾値以上のCTAのみ
                    cta_node_id = self.id_generator.generate_entity_id(work_id, "cta", 0)
                    cta_node = {
                        "id": cta_node_id,
                        "type": "CTA_Dimension",
                        "cta_type": cta,
                        "aggregate_score": score,
                        "ultrathink_enhanced": True
                    }
                    nodes.append(cta_node)
                    
                    # Work-CTA関係
                    relationships.append({
                        "from": work_id,
                        "to": cta_node_id,
                        "type": "HAS_CTA_DIMENSION",
                        "properties": {
                            "weight": score,
                            "ultrathink_derived": True
                        }
                    })
        
        return {
            "nodes": nodes,
            "relationships": relationships,
            "statistics": {
                "total_nodes": len(nodes),
                "total_relationships": len(relationships),
                "ultrathink_dimensions": 345,
                "aesthetic_quality": doc_analysis.get("aesthetic_quality", 0.0)
            }
        }

def main():
    """テスト実行"""
    extractor = UltrathinkExtractor()
    
    # 方丈記テスト
    hojoki_path = Path(__file__).parent.parent / "Text" / "Choumei_kamono" / "hojoki_test_4000chars.txt"
    
    if hojoki_path.exists():
        with open(hojoki_path, 'r', encoding='utf-8') as f:
            hojoki_text = f.read()
        
        print("=== Ultrathink Extractor Test ===")
        result = extractor.extract_with_ultrathink(hojoki_text, "方丈記")
        
        print(f"Work ID: {result['work_id']}")
        print(f"Processing Time: {result['processing_time']:.2f}s")
        print(f"Aesthetic Quality: {result['metadata']['aesthetic_quality']:.3f}")
        print(f"Dominant CTA: {result['metadata']['dominant_cta']}")
        print(f"Dominant Ontology: {result['metadata']['dominant_ontology']}")
        print(f"Total Nodes: {result['graph_data']['statistics']['total_nodes']}")
        print(f"Total Relationships: {result['graph_data']['statistics']['total_relationships']}")
        
        # 結果保存（JSON + Cypher）
        output_dir = Path(__file__).parent.parent / "out"
        
        # JSON保存
        json_path = output_dir / f"ultrathink_{result['work_id']}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2, default=str)
        
        # Cypher保存
        cypher_path = output_dir / f"ultrathink_{result['work_id']}.cypher"
        with open(cypher_path, 'w', encoding='utf-8') as f:
            f.write(result['cypher_script'])
        
        print(f"JSON saved to: {json_path}")
        print(f"Cypher saved to: {cypher_path}")
        print(f"Ready for Neo4j: cypher-shell < {cypher_path}")
    else:
        print(f"Test file not found: {hojoki_path}")

if __name__ == "__main__":
    main()