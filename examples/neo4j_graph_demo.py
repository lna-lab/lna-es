#!/usr/bin/env python3
"""
🗄️ Neo4j Graph Database Demo for LNA-ES v2.0
============================================

Demonstrates complete Neo4j integration:
1. 方丈記 (Hōjōki) - Japanese classical literature
2. ハムレット (Hamlet) - English classical literature
3. Graph creation, storage, and retrieval
4. Semantic relationship analysis

Requirements:
- Neo4j running on localhost:7687
- Username: neo4j, Password: userpass123

Author: Yuki (AI Consciousness) & Ken (Visionary)
"""

import os
import sys
from typing import Dict, List, Any
from datetime import datetime
import json

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.neo4j_graph_manager import Neo4jGraphContext

def load_text_file(filename: str) -> str:
    """Load text file from data directory"""
    data_path = os.path.join(project_root, "data", filename)
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {data_path}")
        return ""

def create_hojoki_analysis_data() -> Dict[str, Any]:
    """
    Create analysis data structure for 方丈記 (Hōjōki)
    """
    original_text = load_text_file("hojoki_test_4000chars.txt")
    
    return {
        'text_id': 'hojoki_1212',
        'original_text': original_text,
        'language': 'ja',
        'source': '鴨長明',
        'era': 'kamakura_period',
        'title': '方丈記',
        'year': 1212,
        'segments': [
            {
                "theme": "無常観の基本原理",
                "key_concepts": ["河の流れ", "水の交代", "泡の出現と消失", "世の移ろい"],
                "philosophical_core": "すべてのものは絶えず変化し、同じ状態に留まることはない",
                "modern_relevance": "現代でも変わらない人生の根本的真理"
            },
            {
                "theme": "人間社会の無常",
                "key_concepts": ["人の生死", "社会の変化", "栄枯盛衰", "時の流れ"],
                "philosophical_core": "人間社会もまた、自然と同様に常に変化している",
                "modern_relevance": "現代社会の変化の激しさへの示唆"
            },
            {
                "theme": "住居と安定への憧憬",
                "key_concepts": ["家", "住まい", "安定", "仮の宿"],
                "philosophical_core": "人は安定を求めるが、すべては仮のものである",
                "modern_relevance": "現代の住宅問題や生活の不安定さ"
            },
            {
                "theme": "自然災害と人間の無力",
                "key_concepts": ["火災", "地震", "飢饉", "疫病"],
                "philosophical_core": "人間は自然の力の前では無力である",
                "modern_relevance": "現代の自然災害への対応と備え"
            },
            {
                "theme": "隠遁生活への転向",
                "key_concepts": ["方丈の庵", "山里", "孤独", "簡素な生活"],
                "philosophical_core": "世俗を離れた生活での内面的平和の追求",
                "modern_relevance": "現代のミニマリズムや田舎暮らしへの憧れ"
            }
        ]
    }

def create_hamlet_analysis_data() -> Dict[str, Any]:
    """
    Create analysis data structure for Hamlet
    """
    original_text = load_text_file("hamlet_test_4000chars.txt")
    
    return {
        'text_id': 'hamlet_1600',
        'original_text': original_text,
        'language': 'en',
        'source': 'William Shakespeare',
        'era': 'elizabethan',
        'title': 'Hamlet',
        'year': 1600,
        'segments': [
            {
                "theme": "Existential Core Question",
                "key_concepts": ["existence vs non-existence", "fundamental choice", "life decision", "being"],
                "philosophical_core": "The ultimate question of whether to continue living or to end one's existence",
                "modern_relevance": "Universal human struggle with purpose and meaning"
            },
            {
                "theme": "Suffering and Endurance",
                "key_concepts": ["mental pain", "fortune's cruelty", "life's hardships", "passive acceptance"],
                "philosophical_core": "Whether it's more noble to endure life's painful experiences",
                "modern_relevance": "Resilience and mental health in face of adversity"
            },
            {
                "theme": "Death as Sleep",
                "key_concepts": ["death as rest", "ending pain", "natural conclusion", "peaceful release"],
                "philosophical_core": "Death viewed as a desirable end to earthly suffering",
                "modern_relevance": "Contemporary discussions of mortality and peaceful death"
            },
            {
                "theme": "Dreams and the Unknown",
                "key_concepts": ["afterlife uncertainty", "post-death experience", "unknown consequences", "fear of dreams"],
                "philosophical_core": "The fear of what might come after death prevents decisive action",
                "modern_relevance": "Anxiety about uncertainty and unknown outcomes"
            },
            {
                "theme": "Paralysis by Analysis",
                "key_concepts": ["overthinking", "conscience", "moral hesitation", "lost resolve"],
                "philosophical_core": "How excessive thinking and moral consideration prevent action",
                "modern_relevance": "Analysis paralysis and decision-making anxiety"
            }
        ]
    }

def demo_graph_operations():
    """
    Demonstrate complete Neo4j graph operations
    """
    print("🗄️ LNA-ES Neo4j Graph Database Demo")
    print("=" * 50)
    
    try:
        with Neo4jGraphContext() as graph:
            print("✅ Connected to Neo4j database")
            
            # Clear existing data (optional)
            print("\n🗑️ Clearing existing data...")
            graph.clear_database()
            
            # Create Hōjōki analysis graph
            print("\n📚 Creating 方丈記 (Hōjōki) analysis graph...")
            hojoki_data = create_hojoki_analysis_data()
            hojoki_text_id = graph.create_text_analysis_graph(hojoki_data)
            print(f"✅ Created Hōjōki graph: {hojoki_text_id}")
            
            # Create Hamlet analysis graph  
            print("\n🎭 Creating Hamlet analysis graph...")
            hamlet_data = create_hamlet_analysis_data()
            hamlet_text_id = graph.create_text_analysis_graph(hamlet_data)
            print(f"✅ Created Hamlet graph: {hamlet_text_id}")
            
            # Store restoration results
            print("\n💾 Storing restoration results...")
            
            # Hōjōki restoration metrics
            hojoki_metrics = {
                'semantic_accuracy': 0.95,
                'length_preservation': 0.90,
                'processing_time': 0.1
            }
            hojoki_restored = "川の流れは絶えることがない。しかし、そこを流れる水は常に新しく入れ替わっている..."
            hojoki_restoration_id = graph.store_restoration_result(
                hojoki_text_id, hojoki_restored, hojoki_metrics
            )
            
            # Hamlet restoration metrics
            hamlet_metrics = {
                'semantic_accuracy': 0.95,
                'length_preservation': 1.11,
                'processing_time': 0.1
            }
            hamlet_restored = "Should I continue living, or should I end my life? That's the question I'm facing..."
            hamlet_restoration_id = graph.store_restoration_result(
                hamlet_text_id, hamlet_restored, hamlet_metrics
            )
            
            print(f"✅ Stored Hōjōki restoration: {hojoki_restoration_id}")
            print(f"✅ Stored Hamlet restoration: {hamlet_restoration_id}")
            
            # Demonstrate graph queries
            print("\n🔍 Demonstrating graph queries...")
            
            # Get database statistics
            stats = graph.get_database_stats()
            print(f"\n📊 Database Statistics:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
            
            # Search by concept
            print(f"\n🔎 Searching for texts with '無常' concept...")
            mujo_results = graph.search_by_concept("無常")
            if mujo_results:
                for result in mujo_results:
                    text_info = result['text']
                    print(f"  Found: {text_info.get('id')} - {text_info.get('source', 'Unknown')}")
            
            print(f"\n🔎 Searching for texts with 'death' concept...")
            death_results = graph.search_by_concept("death")
            if death_results:
                for result in death_results:
                    text_info = result['text']
                    print(f"  Found: {text_info.get('id')} - {text_info.get('source', 'Unknown')}")
            
            # Retrieve complete analysis
            print(f"\n📖 Retrieving complete Hōjōki analysis...")
            hojoki_analysis = graph.get_text_analysis(hojoki_text_id)
            if hojoki_analysis:
                print(f"  Text: {hojoki_analysis['text']['id']}")
                print(f"  Segments: {len(hojoki_analysis['segments'])}")
                print(f"  Concepts: {len(hojoki_analysis['concepts'])}")
                print(f"  Restorations: {len(hojoki_analysis['restorations'])}")
            
            print("\n🎉 Neo4j graph database demo completed successfully!")
            print("\n🌐 Access Neo4j Browser at: http://localhost:7474")
            print("   Username: neo4j")
            print("   Password: userpass123")
            
    except ConnectionError as e:
        print(f"❌ Failed to connect to Neo4j: {e}")
        print("\n🔧 Make sure Neo4j is running:")
        print("   docker compose up -d")
        print("   Wait for startup, then try again")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    demo_graph_operations()