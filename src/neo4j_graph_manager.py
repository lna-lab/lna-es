#!/usr/bin/env python3
"""
🗄️ Neo4j Graph Manager for LNA-ES v2.0
========================================

Manages Neo4j graph database operations for LNA-ES semantic analysis.
- Creates semantic nodes and relationships
- Stores 345-dimension analysis results
- Enables graph-based text restoration
- Supports Cypher query operations

Author: Yuki (AI Consciousness) & Ken (Visionary)
"""

from typing import Dict, List, Any, Optional, Tuple
import json
from datetime import datetime
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import logging

class Neo4jGraphManager:
    """
    🧠 Neo4j Graph Database Manager for LNA-ES
    """
    
    def __init__(self, uri: str = "bolt://localhost:7687", 
                 user: str = "neo4j", password: str = "userpass123"):
        """
        Initialize Neo4j connection
        
        Args:
            uri: Neo4j Bolt URI
            user: Database username
            password: Database password
        """
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def connect(self) -> bool:
        """
        Establish connection to Neo4j database
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            # Test connection
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                test_value = result.single()["test"]
                if test_value == 1:
                    self.logger.info("✅ Successfully connected to Neo4j database")
                    return True
        except ServiceUnavailable as e:
            self.logger.error(f"❌ Failed to connect to Neo4j: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Unexpected error connecting to Neo4j: {e}")
            return False
            
    def close(self):
        """Close Neo4j driver connection"""
        if self.driver:
            self.driver.close()
            self.logger.info("🔒 Neo4j connection closed")
    
    def clear_database(self):
        """
        ⚠️ Clear all nodes and relationships in database
        USE WITH CAUTION - This deletes all data!
        """
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            self.logger.info("🗑️ Database cleared")
    
    def create_text_analysis_graph(self, analysis_data: Dict[str, Any]) -> str:
        """
        Create a complete graph structure for text analysis
        
        Args:
            analysis_data: Dictionary containing:
                - text_id: Unique identifier for text
                - original_text: Source text
                - segments: List of semantic segments
                - metadata: Additional information
                
        Returns:
            str: Created text node ID
        """
        text_id = analysis_data.get('text_id', f"text_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        
        with self.driver.session() as session:
            # Create main text node
            text_node_query = """
            CREATE (t:Text {
                id: $text_id,
                original_text: $original_text,
                language: $language,
                character_count: $char_count,
                created_at: datetime(),
                source: $source,
                era: $era
            })
            RETURN t.id as text_id
            """
            
            result = session.run(text_node_query, {
                'text_id': text_id,
                'original_text': analysis_data.get('original_text', ''),
                'language': analysis_data.get('language', 'ja'),
                'char_count': len(analysis_data.get('original_text', '')),
                'source': analysis_data.get('source', 'LNA-ES'),
                'era': analysis_data.get('era', 'classical')
            })
            
            created_text_id = result.single()["text_id"]
            
            # Create semantic segments
            for i, segment in enumerate(analysis_data.get('segments', [])):
                self._create_segment_subgraph(session, text_id, i, segment)
            
            self.logger.info(f"📊 Created text analysis graph for: {text_id}")
            return created_text_id
    
    def _create_segment_subgraph(self, session, text_id: str, segment_index: int, segment_data: Dict):
        """
        Create subgraph for a semantic segment
        
        Args:
            session: Neo4j session
            text_id: Parent text ID
            segment_index: Segment position
            segment_data: Segment information
        """
        segment_id = f"{text_id}_seg_{segment_index}"
        
        # Create segment node
        segment_query = """
        MATCH (t:Text {id: $text_id})
        CREATE (s:Segment {
            id: $segment_id,
            index: $index,
            theme: $theme,
            philosophical_core: $core,
            modern_relevance: $relevance
        })
        CREATE (t)-[:HAS_SEGMENT {order: $index}]->(s)
        RETURN s.id as segment_id
        """
        
        session.run(segment_query, {
            'text_id': text_id,
            'segment_id': segment_id,
            'index': segment_index,
            'theme': segment_data.get('theme', ''),
            'core': segment_data.get('philosophical_core', ''),
            'relevance': segment_data.get('modern_relevance', '')
        })
        
        # Create concept nodes and relationships
        for concept in segment_data.get('key_concepts', []):
            self._create_concept_node(session, segment_id, concept)
    
    def _create_concept_node(self, session, segment_id: str, concept: str):
        """
        Create concept node and link to segment
        
        Args:
            session: Neo4j session
            segment_id: Parent segment ID
            concept: Concept text
        """
        concept_id = f"concept_{abs(hash(concept)) % 100000}"
        
        concept_query = """
        MATCH (s:Segment {id: $segment_id})
        MERGE (c:Concept {id: $concept_id, text: $concept})
        CREATE (s)-[:HAS_CONCEPT]->(c)
        RETURN c.id as concept_id
        """
        
        session.run(concept_query, {
            'segment_id': segment_id,
            'concept_id': concept_id,
            'concept': concept
        })
    
    def store_restoration_result(self, text_id: str, restored_text: str, 
                               metrics: Dict[str, Any]) -> str:
        """
        Store text restoration result
        
        Args:
            text_id: Original text ID
            restored_text: Restored text content
            metrics: Restoration metrics
            
        Returns:
            str: Restoration node ID
        """
        restoration_id = f"{text_id}_restored_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        with self.driver.session() as session:
            restoration_query = """
            MATCH (t:Text {id: $text_id})
            CREATE (r:Restoration {
                id: $restoration_id,
                restored_text: $restored_text,
                semantic_accuracy: $semantic_accuracy,
                length_preservation: $length_preservation,
                processing_time: $processing_time,
                created_at: datetime(),
                method: 'LNA-ES-v2-Ultrathink'
            })
            CREATE (t)-[:HAS_RESTORATION]->(r)
            RETURN r.id as restoration_id
            """
            
            result = session.run(restoration_query, {
                'text_id': text_id,
                'restoration_id': restoration_id,
                'restored_text': restored_text,
                'semantic_accuracy': metrics.get('semantic_accuracy', 0.0),
                'length_preservation': metrics.get('length_preservation', 0.0),
                'processing_time': metrics.get('processing_time', 0.0)
            })
            
            created_restoration_id = result.single()["restoration_id"]
            self.logger.info(f"💾 Stored restoration result: {restoration_id}")
            return created_restoration_id
    
    def get_text_analysis(self, text_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve complete text analysis from graph
        
        Args:
            text_id: Text identifier
            
        Returns:
            Dict containing text analysis data or None
        """
        with self.driver.session() as session:
            query = """
            MATCH (t:Text {id: $text_id})
            OPTIONAL MATCH (t)-[:HAS_SEGMENT]->(s:Segment)
            OPTIONAL MATCH (s)-[:HAS_CONCEPT]->(c:Concept)
            OPTIONAL MATCH (t)-[:HAS_RESTORATION]->(r:Restoration)
            RETURN t, collect(DISTINCT s) as segments, 
                   collect(DISTINCT c) as concepts,
                   collect(DISTINCT r) as restorations
            """
            
            result = session.run(query, {'text_id': text_id})
            record = result.single()
            
            if not record:
                return None
                
            return {
                'text': dict(record['t']),
                'segments': [dict(s) for s in record['segments']],
                'concepts': [dict(c) for c in record['concepts']],
                'restorations': [dict(r) for r in record['restorations']]
            }
    
    def search_by_concept(self, concept_text: str) -> List[Dict[str, Any]]:
        """
        Search texts by concept
        
        Args:
            concept_text: Concept to search for
            
        Returns:
            List of matching texts with their analysis
        """
        with self.driver.session() as session:
            query = """
            MATCH (c:Concept)-[:HAS_CONCEPT*]-(s:Segment)-[:HAS_SEGMENT*]-(t:Text)
            WHERE c.text CONTAINS $concept_text
            RETURN DISTINCT t, collect(DISTINCT s) as segments
            """
            
            results = session.run(query, {'concept_text': concept_text})
            
            matches = []
            for record in results:
                matches.append({
                    'text': dict(record['t']),
                    'segments': [dict(s) for s in record['segments']]
                })
            
            return matches
    
    def get_database_stats(self) -> Dict[str, int]:
        """
        Get database statistics
        
        Returns:
            Dictionary with node and relationship counts
        """
        with self.driver.session() as session:
            stats_query = """
            MATCH (n)
            RETURN labels(n)[0] as label, count(n) as count
            """
            
            results = session.run(stats_query)
            stats = {}
            
            for record in results:
                label = record['label'] or 'Unknown'
                stats[label] = record['count']
            
            # Get relationship counts
            rel_query = """
            MATCH ()-[r]->()
            RETURN type(r) as relationship_type, count(r) as count
            """
            
            rel_results = session.run(rel_query)
            for record in rel_results:
                rel_type = record['relationship_type']
                stats[f"rel_{rel_type}"] = record['count']
            
            return stats

# Context manager for automatic connection handling
class Neo4jGraphContext:
    """Context manager for Neo4j graph operations"""
    
    def __init__(self, uri: str = "bolt://localhost:7687", 
                 user: str = "neo4j", password: str = "userpass123"):
        self.manager = Neo4jGraphManager(uri, user, password)
    
    def __enter__(self):
        if self.manager.connect():
            return self.manager
        else:
            raise ConnectionError("Failed to connect to Neo4j database")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.manager.close()

# Convenience function
def create_lna_es_graph(analysis_data: Dict[str, Any]) -> str:
    """
    Convenience function to create LNA-ES analysis graph
    
    Args:
        analysis_data: Complete analysis data
        
    Returns:
        str: Created text node ID
    """
    with Neo4jGraphContext() as graph:
        return graph.create_text_analysis_graph(analysis_data)

if __name__ == "__main__":
    # Test connection
    manager = Neo4jGraphManager()
    if manager.connect():
        print("✅ Neo4j connection test successful!")
        stats = manager.get_database_stats()
        print(f"📊 Database stats: {stats}")
        manager.close()
    else:
        print("❌ Neo4j connection test failed!")