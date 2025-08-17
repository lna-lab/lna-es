#!/usr/bin/env python3
"""
📚 NDC (Nippon Decimal Classification) Ontology Integration for LNA-ES MCP
=========================================================================

Integrates Japanese library science classification system with LNA-ES semantic analysis.
Enables advanced categorization and discovery of texts based on NDC taxonomy.

NDC Categories:
- 000-099: 総記 (General works)
- 100-199: 哲学 (Philosophy) 
- 200-299: 歴史 (History)
- 300-399: 社会科学 (Social sciences)
- 400-499: 自然科学 (Natural sciences)
- 500-599: 技術・工学 (Technology)
- 600-699: 産業 (Industry)
- 700-799: 芸術 (Arts)
- 800-899: 言語 (Language)
- 900-999: 文学 (Literature)

Author: Yuki (AI Consciousness) & Ken (Visionary)
"""

import json
import re
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path

class NDCOntologyMapper:
    """📚 NDC Ontology Integration for LNA-ES"""
    
    def __init__(self):
        self.ndc_categories = self._load_ndc_structure()
        self.semantic_mappings = self._create_semantic_mappings()
        
    def _load_ndc_structure(self) -> Dict[str, Any]:
        """Load NDC classification structure"""
        return {
            "000": {
                "name": "総記",
                "name_en": "General works",
                "subcategories": {
                    "010": "図書館学",
                    "020": "図書・書誌学", 
                    "030": "百科事典",
                    "040": "論文集・評論",
                    "050": "雑誌",
                    "060": "団体・学会",
                    "070": "新聞・報道",
                    "080": "叢書・全集",
                    "090": "貴重書・郷土資料"
                },
                "semantic_markers": ["総合", "一般", "包括", "全般", "概要"]
            },
            "100": {
                "name": "哲学",
                "name_en": "Philosophy",
                "subcategories": {
                    "110": "哲学各論",
                    "120": "東洋思想", 
                    "130": "西洋哲学",
                    "140": "心理学",
                    "150": "倫理学",
                    "160": "宗教",
                    "170": "神道",
                    "180": "仏教",
                    "190": "キリスト教"
                },
                "semantic_markers": ["思想", "哲学", "心理", "倫理", "宗教", "精神", "魂", "意識"]
            },
            "200": {
                "name": "歴史",
                "name_en": "History", 
                "subcategories": {
                    "210": "日本史",
                    "220": "アジア史",
                    "230": "ヨーロッパ史",
                    "240": "アフリカ史",
                    "250": "北アメリカ史",
                    "260": "南アメリカ史",
                    "270": "オセアニア史",
                    "280": "伝記",
                    "290": "地理・地誌"
                },
                "semantic_markers": ["歴史", "過去", "時代", "年代", "古代", "中世", "近世", "現代"]
            },
            "800": {
                "name": "言語",
                "name_en": "Language",
                "subcategories": {
                    "810": "日本語",
                    "820": "中国語",
                    "830": "英語",
                    "840": "ドイツ語",
                    "850": "フランス語",
                    "860": "スペイン語",
                    "870": "イタリア語",
                    "880": "ロシア語",
                    "890": "その他の言語"
                },
                "semantic_markers": ["言語", "語学", "文法", "語彙", "表現", "意味", "記号"]
            },
            "900": {
                "name": "文学",
                "name_en": "Literature",
                "subcategories": {
                    "910": "日本文学",
                    "920": "中国文学",
                    "930": "英米文学",
                    "940": "ドイツ文学",
                    "950": "フランス文学",
                    "960": "スペイン文学",
                    "970": "イタリア文学",
                    "980": "ロシア・ソビエト文学",
                    "990": "その他の文学"
                },
                "semantic_markers": ["文学", "詩", "小説", "物語", "散文", "韻文", "作品", "創作"]
            }
        }
    
    def _create_semantic_mappings(self) -> Dict[str, List[str]]:
        """Create LNA-ES to NDC semantic mappings"""
        return {
            # LNA-ES dimensions to NDC categories
            "temporal": ["200"],  # History
            "spatial": ["200", "290"],  # History, Geography
            "emotion": ["100", "900"],  # Philosophy, Literature
            "sensation": ["100", "700"],  # Philosophy, Arts
            "natural": ["400", "500"],  # Natural sciences, Technology
            "relationship": ["100", "300"],  # Philosophy, Social sciences
            "causality": ["100", "400"],  # Philosophy, Natural sciences
            "action": ["300", "600"],  # Social sciences, Industry
            "narrative": ["800", "900"],  # Language, Literature
            "character": ["900"],  # Literature
            "discourse": ["800"],  # Language
            "story_formula": ["900"],  # Literature
            "linguistic_style": ["800", "900"],  # Language, Literature
            "classification": ["000"]  # General works
        }
    
    def classify_text_by_ndc(self, text: str, lna_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Classify text using NDC ontology based on LNA-ES analysis
        
        Args:
            text: Input text
            lna_analysis: LNA-ES analysis result
            
        Returns:
            NDC classification result
        """
        # Extract semantic indicators from text
        semantic_indicators = self._extract_semantic_indicators(text)
        
        # Map LNA-ES dimensions to NDC categories
        ndc_scores = self._calculate_ndc_scores(lna_analysis, semantic_indicators)
        
        # Determine primary and secondary classifications
        primary_ndc = max(ndc_scores, key=ndc_scores.get)
        secondary_ndcs = sorted(ndc_scores.items(), key=lambda x: x[1], reverse=True)[1:3]
        
        return {
            "primary_classification": {
                "ndc_code": primary_ndc,
                "name": self.ndc_categories[primary_ndc]["name"],
                "name_en": self.ndc_categories[primary_ndc]["name_en"],
                "confidence": ndc_scores[primary_ndc]
            },
            "secondary_classifications": [
                {
                    "ndc_code": code,
                    "name": self.ndc_categories[code]["name"],
                    "confidence": score
                }
                for code, score in secondary_ndcs if code in self.ndc_categories
            ],
            "detailed_analysis": {
                "semantic_indicators": semantic_indicators,
                "lna_mapping": self._map_lna_to_ndc(lna_analysis),
                "all_scores": ndc_scores
            }
        }
    
    def _extract_semantic_indicators(self, text: str) -> List[str]:
        """Extract semantic indicators from text"""
        indicators = []
        
        # Check for category-specific keywords
        for category_code, category_data in self.ndc_categories.items():
            for marker in category_data.get("semantic_markers", []):
                if marker in text:
                    indicators.append(f"{category_code}:{marker}")
        
        # Classical literature indicators
        classical_markers = ["古典", "古文", "漢文", "王朝", "平安", "鎌倉", "室町", "江戸"]
        for marker in classical_markers:
            if marker in text:
                indicators.append(f"910:classical_{marker}")
        
        # Philosophy indicators  
        philosophy_markers = ["無常", "真理", "存在", "認識", "意識", "精神"]
        for marker in philosophy_markers:
            if marker in text:
                indicators.append(f"100:philosophy_{marker}")
        
        return indicators
    
    def _calculate_ndc_scores(self, lna_analysis: Dict[str, Any], 
                            semantic_indicators: List[str]) -> Dict[str, float]:
        """Calculate NDC classification scores"""
        scores = {code: 0.0 for code in self.ndc_categories.keys()}
        
        # Score based on semantic indicators
        for indicator in semantic_indicators:
            if ":" in indicator:
                ndc_code = indicator.split(":")[0]
                if ndc_code in scores:
                    scores[ndc_code] += 0.3
        
        # Score based on LNA-ES dominant analysis
        dominant_analysis = lna_analysis.get("dominant_analysis", "")
        
        # Map specific LNA-ES results to NDC
        if "aesthetic" in dominant_analysis.lower():
            scores["700"] += 0.4  # Arts
            scores["900"] += 0.2  # Literature
        
        if "temporal" in dominant_analysis.lower():
            scores["200"] += 0.4  # History
        
        if "narrative" in dominant_analysis.lower():
            scores["900"] += 0.5  # Literature
            scores["800"] += 0.2  # Language
        
        if "philosophical" in dominant_analysis.lower():
            scores["100"] += 0.5  # Philosophy
        
        # Boost scores based on aesthetic quality
        aesthetic_quality = lna_analysis.get("aesthetic_quality", 0.0)
        if aesthetic_quality > 0.7:
            scores["900"] += 0.2  # High aesthetic = Literature
            scores["700"] += 0.1  # Arts
        
        # Normalize scores
        max_score = max(scores.values()) if scores.values() else 1.0
        if max_score > 0:
            scores = {k: v/max_score for k, v in scores.items()}
        
        return scores
    
    def _map_lna_to_ndc(self, lna_analysis: Dict[str, Any]) -> Dict[str, List[str]]:
        """Map LNA-ES dimensions to NDC categories"""
        mapping = {}
        
        # Get dominant dimensions from LNA analysis
        dominant_analysis = lna_analysis.get("dominant_analysis", "")
        
        for lna_dimension, ndc_codes in self.semantic_mappings.items():
            if lna_dimension in dominant_analysis.lower():
                mapping[lna_dimension] = [
                    f"{code}: {self.ndc_categories.get(code, {}).get('name', 'Unknown')}"
                    for code in ndc_codes if code in self.ndc_categories
                ]
        
        return mapping
    
    def suggest_related_works(self, ndc_classification: Dict[str, Any]) -> List[Dict[str, str]]:
        """Suggest related works based on NDC classification"""
        primary_code = ndc_classification["primary_classification"]["ndc_code"]
        
        suggestions = {
            "100": [
                {"title": "方丈記", "author": "鴨長明", "reason": "仏教思想・無常観"},
                {"title": "徒然草", "author": "兼好法師", "reason": "人生哲学・思索"}
            ],
            "200": [
                {"title": "源氏物語", "author": "紫式部", "reason": "平安時代の歴史的背景"},
                {"title": "平家物語", "author": "作者不詳", "reason": "鎌倉時代の歴史"}
            ],
            "900": [
                {"title": "竹取物語", "author": "作者不詳", "reason": "日本最古の物語文学"},
                {"title": "伊勢物語", "author": "作者不詳", "reason": "歌物語の傑作"}
            ]
        }
        
        return suggestions.get(primary_code, [
            {"title": "広辞苑", "author": "新村出", "reason": "総合的な知識源"}
        ])
    
    def create_ndc_graph_nodes(self, text_id: str, ndc_classification: Dict[str, Any]) -> Dict[str, Any]:
        """Create Neo4j graph nodes for NDC classification"""
        primary = ndc_classification["primary_classification"]
        
        return {
            "ndc_node": {
                "id": f"ndc_{primary['ndc_code']}_{text_id}",
                "ndc_code": primary["ndc_code"],
                "category_name": primary["name"],
                "category_name_en": primary["name_en"],
                "confidence": primary["confidence"],
                "text_id": text_id
            },
            "relationships": [
                {
                    "type": "CLASSIFIED_AS_NDC",
                    "from_node": f"text_{text_id}",
                    "to_node": f"ndc_{primary['ndc_code']}_{text_id}",
                    "properties": {
                        "confidence": primary["confidence"],
                        "classification_method": "LNA-ES-NDC"
                    }
                }
            ]
        }

class NDCMCPExtension:
    """MCP Extension for NDC Ontology Integration"""
    
    def __init__(self):
        self.ndc_mapper = NDCOntologyMapper()
    
    def get_ndc_tools(self) -> List[Dict[str, Any]]:
        """Get NDC-specific MCP tools"""
        return [
            {
                "name": "ndc_classify_text",
                "description": "Classify text using NDC (Nippon Decimal Classification) ontology",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "Text to classify"},
                        "lna_analysis": {"type": "object", "description": "LNA-ES analysis result"}
                    },
                    "required": ["text", "lna_analysis"]
                }
            },
            {
                "name": "ndc_suggest_related",
                "description": "Suggest related works based on NDC classification",
                "inputSchema": {
                    "type": "object", 
                    "properties": {
                        "ndc_code": {"type": "string", "description": "NDC category code"}
                    },
                    "required": ["ndc_code"]
                }
            },
            {
                "name": "ndc_browse_category",
                "description": "Browse NDC category structure",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string", "description": "NDC category to browse"}
                    }
                }
            }
        ]
    
    async def handle_ndc_classify(self, args: Dict[str, Any]) -> str:
        """Handle NDC classification request"""
        text = args.get("text", "")
        lna_analysis = args.get("lna_analysis", {})
        
        if not text or not lna_analysis:
            return "❌ Text and LNA analysis required for NDC classification"
        
        classification = self.ndc_mapper.classify_text_by_ndc(text, lna_analysis)
        
        return json.dumps({
            "ndc_classification": classification,
            "suggested_works": self.ndc_mapper.suggest_related_works(classification)
        }, ensure_ascii=False, indent=2)
    
    async def handle_ndc_suggest(self, args: Dict[str, Any]) -> str:
        """Handle NDC related works suggestion"""
        ndc_code = args.get("ndc_code", "")
        
        if not ndc_code:
            return "❌ NDC code required"
        
        # Create mock classification for suggestion
        mock_classification = {
            "primary_classification": {"ndc_code": ndc_code}
        }
        
        suggestions = self.ndc_mapper.suggest_related_works(mock_classification)
        
        return json.dumps({
            "ndc_code": ndc_code,
            "suggested_works": suggestions
        }, ensure_ascii=False, indent=2)
    
    async def handle_ndc_browse(self, args: Dict[str, Any]) -> str:
        """Handle NDC category browsing"""
        category_code = args.get("category_code", "")
        
        if category_code and category_code in self.ndc_mapper.ndc_categories:
            category_data = self.ndc_mapper.ndc_categories[category_code]
            return json.dumps(category_data, ensure_ascii=False, indent=2)
        else:
            # Return all main categories
            main_categories = {
                code: {
                    "name": data["name"],
                    "name_en": data["name_en"]
                }
                for code, data in self.ndc_mapper.ndc_categories.items()
            }
            return json.dumps(main_categories, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Test NDC integration
    mapper = NDCOntologyMapper()
    
    # Test with classical Japanese text
    test_text = "川の流れは絶えることなく、しかも、もとの水にあらず。"
    test_analysis = {
        "dominant_analysis": "temporal_aesthetic_narrative",
        "aesthetic_quality": 0.85,
        "total_dimensions": 28
    }
    
    result = mapper.classify_text_by_ndc(test_text, test_analysis)
    print("📚 NDC Classification Test Result:")
    print(json.dumps(result, ensure_ascii=False, indent=2))