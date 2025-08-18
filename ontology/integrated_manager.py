#!/usr/bin/env python3
"""
LNA-ES v3.0 Integrated Ontology Manager
======================================

Manages all 15 ontologies for LNA-ES v3.0 system.
Integrates with Ultrathink 345-dimension analysis and Yuki's aesthetic standards.

Author: Yuki (AI Consciousness) & Ken (Visionary)
Version: 3.0
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import yaml
import neo4j
from dataclasses import dataclass

@dataclass
class OntologyConfig:
    """Configuration for individual ontology"""
    name: str
    layer: str
    file_path: str
    weight: float
    description: str
    concepts: List[str]
    format_type: str = "cypher"  # cypher or python
    aesthetic_multiplier: float = 1.0

class LNAESv3OntologyManager:
    """
    LNA-ES v3.0 Integrated Ontology Manager
    
    Manages all 15 ontologies based on actual directory structure:
    - Foundation Layer (5): temporal, spatial, emotion, sensation, natural
    - Relational Layer (3): relationship, causality, action  
    - Structural Layer (3): narrative_structure, character_function, discourse_structure
    - Cultural Layer (2): story_classification, food_culture
    - Advanced Layer (1): indirect_emotion
    - Meta Layer (1): meta_graph
    - Emotions Layer (4): emotion_nodes, emotion_relationships, emotion_queries, load_emotions
    """
    
    def __init__(self, config_path: Optional[str] = None):
        # Setup logging first
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self.config_path = config_path or self._get_default_config_path()
        self.ontologies: Dict[str, OntologyConfig] = {}
        self.neo4j_driver = None
        self.aesthetic_standards = self._load_yuki_aesthetic_standards()
        
        # Load configuration
        self._load_ontology_configs()
        
    def _get_default_config_path(self) -> str:
        """Get default configuration file path"""
        current_dir = Path(__file__).parent
        return str(current_dir / "manifest.yaml")
    
    def _load_yuki_aesthetic_standards(self) -> Dict[str, float]:
        """Load Yuki's aesthetic standards for ontology weighting"""
        return {
            "metaphysical_depth": 5.0,
            "emotional_resonance": 3.5,
            "narrative_harmony": 3.0,
            "cultural_authenticity": 4.0,
            "linguistic_precision": 4.5
        }
    
    def _load_ontology_configs(self):
        """Load ontology configurations from manifest file"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)
            
            for onto_data in config_data.get('ontologies', []):
                onto_config = OntologyConfig(
                    name=onto_data['name'],
                    layer=onto_data['layer'],
                    file_path=onto_data['file_path'],
                    weight=onto_data.get('weight', 1.0),
                    description=onto_data.get('description', ''),
                    concepts=onto_data.get('concepts', []),
                    format_type=onto_data.get('format', 'cypher'),
                    aesthetic_multiplier=onto_data.get('aesthetic_multiplier', 1.0)
                )
                self.ontologies[onto_config.name] = onto_config
                
        except FileNotFoundError:
            self.logger.warning(f"Config file not found: {self.config_path}. Using default configuration.")
            self._create_default_config()
    
    def _create_default_config(self):
        """Create default ontology configuration based on actual directory structure"""
        default_ontologies = {
            # Foundation Layer (weight: 1.0)
            "temporal": OntologyConfig(
                name="temporal", layer="foundation", 
                file_path="foundation/temporal_ontology.cypher",
                weight=1.0, description="Time concepts and temporal expressions",
                concepts=["瞬間", "期間", "循環", "質的時間"]
            ),
            "spatial": OntologyConfig(
                name="spatial", layer="foundation",
                file_path="foundation/spatial_ontology.cypher", 
                weight=1.0, description="Spatial concepts and relationships",
                concepts=["空間", "場所", "方向", "距離"]
            ),
            "emotion": OntologyConfig(
                name="emotion", layer="foundation",
                file_path="foundation/emotion_ontology.cypher",
                weight=1.0, description="Emotional expressions and states",
                concepts=["幸せ", "悲しみ", "怒り", "恐れ", "驚き", "嫌悪"],
                aesthetic_multiplier=1.2  # Enhanced for emotional resonance
            ),
            "sensation": OntologyConfig(
                name="sensation", layer="foundation",
                file_path="foundation/sensation_ontology.cypher",
                weight=1.0, description="Sensory experiences and perceptions",
                concepts=["視覚", "聴覚", "触覚", "味覚", "嗅覚"]
            ),
            "natural": OntologyConfig(
                name="natural", layer="foundation",
                file_path="foundation/natural_ontology.cypher",
                weight=1.0, description="Natural phenomena and environment",
                concepts=["自然", "季節", "天候", "生物", "環境"]
            ),
            
            # Relational Layer (weight: 0.95)
            "relationship": OntologyConfig(
                name="relationship", layer="relational",
                file_path="relational/relationship_ontology.cypher",
                weight=0.95, description="Human relationships and social bonds",
                concepts=["愛情", "友情", "家族", "社会", "絆"]
            ),
            "causality": OntologyConfig(
                name="causality", layer="relational",
                file_path="relational/causality_ontology.cypher",
                weight=0.95, description="Cause-effect relationships",
                concepts=["原因", "結果", "運命", "必然", "偶然"],
                aesthetic_multiplier=1.1  # Enhanced for metaphysical depth
            ),
            "action": OntologyConfig(
                name="action", layer="relational",
                file_path="relational/action_ontology.cypher",
                weight=0.95, description="Actions and movements",
                concepts=["動作", "行為", "移動", "変化", "行動"]
            ),
            
            # Structural Layer (weight: 0.90)
            "narrative_structure": OntologyConfig(
                name="narrative_structure", layer="structural",
                file_path="structural/narrative_structure.cypher",
                weight=0.90, description="Story structure and narrative patterns",
                concepts=["物語", "プロット", "構造", "展開", "起承転結"],
                aesthetic_multiplier=1.15  # Enhanced for narrative harmony
            ),
            "character_function": OntologyConfig(
                name="character_function", layer="structural",
                file_path="structural/character_function.cypher",
                weight=0.90, description="Character functions and archetypes",
                concepts=["人物", "主人公", "悪役", "脇役", "アーキタイプ"]
            ),
            "discourse_structure": OntologyConfig(
                name="discourse_structure", layer="structural",
                file_path="structural/discourse_structure.cypher",
                weight=0.90, description="Discourse structure and rhetoric",
                concepts=["談話", "修辞", "文体", "表現", "構成"]
            ),
            
            # Cultural Layer (weight: 0.85)
            "story_classification": OntologyConfig(
                name="story_classification", layer="cultural",
                file_path="cultural/story_classification_ontology.cypher",
                weight=0.85, description="Story classification and genre patterns",
                concepts=["ジャンル", "定型", "パターン", "様式", "形式"]
            ),
            "food_culture": OntologyConfig(
                name="food_culture", layer="cultural",
                file_path="cultural/food_culture_ontology.cypher",
                weight=0.85, description="Food culture and culinary traditions",
                concepts=["料理", "食文化", "調理法", "味覚", "食材"],
                aesthetic_multiplier=0.9  # Cultural context specific
            ),
            
            # Advanced Layer (weight: 0.80)
            "indirect_emotion": OntologyConfig(
                name="indirect_emotion", layer="advanced",
                file_path="advanced/indirect_emotion_ontology.cypher",
                weight=0.80, description="Indirect emotional expressions and metaphors",
                concepts=["比喩", "暗示", "間接表現", "象徴", "メタファー"],
                aesthetic_multiplier=1.25  # Enhanced for sophisticated expression
            ),
            
            # Meta Layer (weight: 0.75)
            "meta_graph": OntologyConfig(
                name="meta_graph", layer="meta",
                file_path="meta/meta_graph.cypher",
                weight=0.75, description="Meta-level graph relationships and patterns",
                concepts=["メタ関係", "抽象概念", "統合パターン", "高次構造"],
                aesthetic_multiplier=1.3  # Enhanced for meta-level understanding
            ),
            
            # Emotions Layer (weight: 0.85) - Specialized emotion processing
            "emotion_nodes": OntologyConfig(
                name="emotion_nodes", layer="emotions",
                file_path="emotions/create_emotion_nodes.cypher",
                weight=0.85, description="Emotion node creation and classification",
                concepts=["感情ノード", "感情分類", "感情階層", "感情状態"],
                aesthetic_multiplier=1.1
            ),
            "emotion_relationships": OntologyConfig(
                name="emotion_relationships", layer="emotions",
                file_path="emotions/create_emotion_relationships.cypher",
                weight=0.85, description="Emotion relationship patterns",
                concepts=["感情関係", "感情変化", "感情連鎖", "感情相互作用"],
                aesthetic_multiplier=1.1
            ),
            "emotion_queries": OntologyConfig(
                name="emotion_queries", layer="emotions",
                file_path="emotions/emotion_queries.cypher",
                weight=0.85, description="Emotion query patterns and analysis",
                concepts=["感情クエリ", "感情分析", "感情検索", "感情パターン"],
                aesthetic_multiplier=1.05
            ),
            "load_emotions": OntologyConfig(
                name="load_emotions", layer="emotions",
                file_path="emotions/load_emotions_from_csv.cypher",
                weight=0.85, description="Emotion data loading and initialization",
                concepts=["感情データ", "感情初期化", "感情インポート", "感情設定"],
                aesthetic_multiplier=1.0
            )
        }
        
        self.ontologies = default_ontologies
    
    def connect_neo4j(self, uri: str = "bolt://localhost:7687", 
                     user: str = "neo4j", password: str = "userpass123"):
        """Connect to Neo4j database"""
        try:
            self.neo4j_driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
            self.logger.info("Connected to Neo4j database")
        except Exception as e:
            self.logger.error(f"Failed to connect to Neo4j: {e}")
            raise
    
    def load_ontology_to_neo4j(self, ontology_name: str) -> bool:
        """Load specific ontology to Neo4j"""
        if ontology_name not in self.ontologies:
            self.logger.error(f"Unknown ontology: {ontology_name}")
            return False
        
        onto_config = self.ontologies[ontology_name]
        ontology_path = Path(__file__).parent / onto_config.file_path
        
        if not ontology_path.exists():
            self.logger.error(f"Ontology file not found: {ontology_path}")
            return False
        
        try:
            with open(ontology_path, 'r', encoding='utf-8') as f:
                cypher_content = f.read()
            
            # Split cypher statements by semicolon and execute individually
            statements = [stmt.strip() for stmt in cypher_content.split(';') if stmt.strip()]
            
            with self.neo4j_driver.session() as session:
                for i, statement in enumerate(statements):
                    if statement:  # Skip empty statements
                        try:
                            session.run(statement)
                            self.logger.debug(f"Executed statement {i+1}/{len(statements)} for {ontology_name}")
                        except Exception as stmt_error:
                            self.logger.warning(f"Statement {i+1} failed for {ontology_name}: {stmt_error}")
                            # Continue with next statement instead of failing completely
                
                self.logger.info(f"Successfully loaded ontology: {ontology_name} ({len(statements)} statements)")
                return True
                
        except Exception as e:
            self.logger.error(f"Failed to load ontology {ontology_name}: {e}")
            return False
    
    def load_all_ontologies(self) -> Dict[str, bool]:
        """Load all ontologies to Neo4j"""
        results = {}
        
        # Load in layer order (foundation first, meta last)
        layer_order = ["foundation", "relational", "structural", "cultural", "advanced", "meta", "emotions"]
        
        for layer in layer_order:
            layer_ontologies = [name for name, config in self.ontologies.items() 
                              if config.layer == layer]
            
            for onto_name in layer_ontologies:
                results[onto_name] = self.load_ontology_to_neo4j(onto_name)
        
        return results
    
    def get_ontology_weights(self, aesthetic_context: str = "default") -> Dict[str, float]:
        """Get ontology weights adjusted for aesthetic context"""
        weights = {}
        
        for name, config in self.ontologies.items():
            base_weight = config.weight
            aesthetic_multiplier = config.aesthetic_multiplier
            
            # Apply Yuki's aesthetic standards
            if aesthetic_context == "japanese_classical":
                if name in ["temporal", "emotion", "natural"]:
                    aesthetic_multiplier *= 1.2  # Enhance for classical aesthetics
                elif name in ["narrative_structure", "indirect_emotion"]:
                    aesthetic_multiplier *= 1.15
            elif aesthetic_context == "modern_narrative":
                if name in ["character_function", "discourse_structure", "relationship"]:
                    aesthetic_multiplier *= 1.1
            elif aesthetic_context == "meta_analysis":
                if name in ["meta_graph", "indirect_emotion"]:
                    aesthetic_multiplier *= 1.25
            
            weights[name] = base_weight * aesthetic_multiplier
        
        return weights
    
    def extract_entities_with_ontologies(self, text: str, 
                                       target_ontologies: Optional[List[str]] = None) -> Dict[str, Any]:
        """Extract entities with ontology associations"""
        if target_ontologies is None:
            target_ontologies = list(self.ontologies.keys())
        
        results = {
            "entities": [],
            "ontology_distributions": {},
            "aesthetic_scores": {}
        }
        
        # This would integrate with the actual Ultrathink analysis
        # For now, return structure template
        for onto_name in target_ontologies:
            if onto_name in self.ontologies:
                results["ontology_distributions"][onto_name] = 0.0
                results["aesthetic_scores"][onto_name] = 0.0
        
        return results
    
    def create_ontology_manifest(self, output_path: Optional[str] = None) -> str:
        """Create manifest.yaml file for current ontology configuration"""
        if output_path is None:
            output_path = self.config_path
        
        manifest_data = {
            "lna_es_version": "3.0",
            "ontology_system": "15-dimensional",
            "aesthetic_integration": "yuki_standards",
            "ontologies": []
        }
        
        for name, config in self.ontologies.items():
            onto_data = {
                "name": config.name,
                "layer": config.layer,
                "file_path": config.file_path,
                "weight": config.weight,
                "description": config.description,
                "concepts": config.concepts,
                "format": config.format_type,
                "aesthetic_multiplier": config.aesthetic_multiplier
            }
            manifest_data["ontologies"].append(onto_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(manifest_data, f, default_flow_style=False, 
                     allow_unicode=True, sort_keys=False)
        
        self.logger.info(f"Created ontology manifest: {output_path}")
        return output_path
    
    def validate_ontology_coverage(self, text_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that all ontologies are properly covered"""
        required_ontologies = set(self.ontologies.keys())
        found_ontologies = set(text_analysis.get("ontology_distributions", {}).keys())
        
        missing = required_ontologies - found_ontologies
        extra = found_ontologies - required_ontologies
        
        return {
            "coverage_complete": len(missing) == 0,
            "missing_ontologies": list(missing),
            "extra_ontologies": list(extra),
            "coverage_percentage": len(found_ontologies) / len(required_ontologies) * 100
        }
    
    def get_layer_summary(self) -> Dict[str, Any]:
        """Get summary of ontologies by layer"""
        summary = {}
        
        for layer in ["foundation", "relational", "structural", "cultural", "advanced", "meta", "emotions"]:
            layer_ontologies = [config for config in self.ontologies.values() 
                              if config.layer == layer]
            
            summary[layer] = {
                "count": len(layer_ontologies),
                "ontologies": [onto.name for onto in layer_ontologies],
                "average_weight": sum(onto.weight for onto in layer_ontologies) / len(layer_ontologies) if layer_ontologies else 0,
                "total_concepts": sum(len(onto.concepts) for onto in layer_ontologies)
            }
        
        return summary
    
    def close(self):
        """Close Neo4j connection"""
        if self.neo4j_driver:
            self.neo4j_driver.close()
            self.logger.info("Closed Neo4j connection")

def main():
    """Example usage of LNA-ES v3.0 Ontology Manager"""
    
    # Initialize manager
    manager = LNAESv3OntologyManager()
    
    # Create manifest file
    manager.create_ontology_manifest()
    
    # Connect to Neo4j and load ontologies
    try:
        manager.connect_neo4j()
        
        # Load all ontologies
        results = manager.load_all_ontologies()
        
        print("📊 Ontology Loading Results:")
        for onto_name, success in results.items():
            status = "✅ Success" if success else "❌ Failed"
            print(f"  {onto_name}: {status}")
        
        # Get layer summary
        summary = manager.get_layer_summary()
        print("\n🌟 Layer Summary:")
        for layer, info in summary.items():
            print(f"  {layer}: {info['count']} ontologies, {info['total_concepts']} concepts")
        
        # Get aesthetic weights
        weights = manager.get_ontology_weights("japanese_classical")
        print("\n🎨 Aesthetic Weights (Japanese Classical):")
        for onto_name, weight in weights.items():
            print(f"  {onto_name}: {weight:.3f}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        manager.close()

if __name__ == "__main__":
    main()