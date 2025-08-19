"""
Semantic Generator for LNA-ES v3.2
345次元解析から文章を生成する真のセマンティック復元システム

原文を一切保存せず、純粋に数値化された意味情報から文章を再構築
"""

from typing import Dict, List, Any, Tuple
import numpy as np


class SemanticGenerator:
    """345次元セマンティック情報から文章を生成"""
    
    def __init__(self):
        # CTA次元の意味マッピング（44次元）
        self.cta_meanings = {
            "temporal_basic": "時間の流れ",
            "temporal_qualitative": "時間の質感",
            "temporal_duration": "持続性",
            "temporal_rhythm": "リズム",
            "temporal_memory": "記憶",
            "spatial_basic": "空間的広がり",
            "spatial_relationship": "空間的関係",
            "spatial_boundary": "境界",
            "spatial_movement": "動き",
            "spatial_texture": "質感",
            "emotion_primary": "基本感情",
            "emotion_complex": "複雑な感情",
            "emotion_subtle": "微細な感情",
            "emotion_transition": "感情の変化",
            "emotion_resonance": "共鳴",
            "relationship_human": "人間関係",
            "relationship_social": "社会的関係",
            "relationship_dynamic": "関係の動態",
            "relationship_intimacy": "親密さ",
            "relationship_power": "力関係",
            "causality_direct": "直接的因果",
            "causality_implicit": "暗黙の因果",
            "causality_chain": "因果の連鎖",
            "action_physical": "物理的行動",
            "action_mental": "精神的行動",
            "narrative_basic": "基本的な語り",
            "narrative_structure": "物語構造",
            "narrative_perspective": "視点",
            "narrative_flow": "流れ",
            "character_identity": "人物の同一性",
            "character_development": "人物の成長",
            "character_motivation": "動機",
            "discourse_style": "文体",
            "cultural_context": "文化的文脈",
            "cultural_values": "価値観",
            "cultural_symbols": "シンボル",
            "cultural_aesthetics": "美学",
            "linguistic_beauty": "言語的美",
            "linguistic_register": "言語レベル",
            "indirect_emotion": "間接的感情",
            "metaphysical_existence": "存在論",
            "metaphysical_consciousness": "意識",
            "metaphysical_transcendence": "超越",
            "metaphysical_unity": "統一"
        }
        
        # オントロジー次元の意味マッピング（主要なもの）
        self.ontology_meanings = {
            "natural_水": "水の要素",
            "natural_花": "花の要素",
            "natural_風": "風の要素",
            "natural_木": "木の要素",
            "temporal_時": "時間",
            "temporal_朝": "朝",
            "temporal_夜": "夜",
            "temporal_永遠": "永遠",
            "sensation_美しい": "美しさ",
            "action_見る": "観察",
            "spatial_道": "道",
            "spatial_海": "海",
            "spatial_空": "空",
            "spatial_街": "街",
            "spatial_庭": "庭",
            "narrative_思い出": "思い出",
            "narrative_物語": "物語",
            "narrative_話": "話",
            "character_心": "心",
            "discourse_声": "声"
        }
    
    def generate_from_dimensions(self, 
                                cta_scores: Dict[str, float],
                                ontology_scores: Dict[str, float],
                                meta_dimensions: Dict[str, float],
                                sentence_length: int = 50) -> str:
        """
        345次元から文章を生成
        
        Args:
            cta_scores: CTA分析スコア（44次元）
            ontology_scores: オントロジースコア（15次元）
            meta_dimensions: メタ次元（286次元）
            sentence_length: 文の長さのヒント
            
        Returns:
            生成された文章
        """
        
        # 支配的な次元を抽出
        dominant_ctas = self._get_dominant_dimensions(cta_scores, top_n=3)
        dominant_ontos = self._get_dominant_dimensions(ontology_scores, top_n=3)
        
        # メタ次元から全体的な特徴を抽出
        emotional_intensity = meta_dimensions.get("meta_emotional_intensity", 0)
        spatial_complexity = meta_dimensions.get("meta_spatial_complexity", 0)
        temporal_depth = meta_dimensions.get("meta_temporal_depth", 0)
        transcendental_quality = meta_dimensions.get("meta_transcendental_quality", 0)
        
        # 文章の基本構造を決定
        sentence_structure = self._determine_structure(
            dominant_ctas, dominant_ontos,
            emotional_intensity, spatial_complexity,
            temporal_depth, transcendental_quality
        )
        
        # セマンティック要素から文章を構築
        generated_text = self._build_sentence(
            sentence_structure,
            dominant_ctas,
            dominant_ontos,
            sentence_length
        )
        
        return generated_text
    
    def _get_dominant_dimensions(self, scores: Dict[str, float], top_n: int = 3) -> List[Tuple[str, float]]:
        """支配的な次元を抽出"""
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:top_n]
    
    def _determine_structure(self, dominant_ctas, dominant_ontos,
                            emotional_intensity, spatial_complexity,
                            temporal_depth, transcendental_quality) -> str:
        """文章の基本構造を決定"""
        
        # 最も強いCTA次元に基づいて文型を選択
        if dominant_ctas and dominant_ctas[0][0].startswith("temporal"):
            if temporal_depth > 0.5:
                return "temporal_philosophical"  # 時間に関する哲学的考察
            else:
                return "temporal_descriptive"  # 時間の描写
                
        elif dominant_ctas and dominant_ctas[0][0].startswith("spatial"):
            if spatial_complexity > 0.5:
                return "spatial_complex"  # 複雑な空間描写
            else:
                return "spatial_simple"  # シンプルな空間描写
                
        elif dominant_ctas and dominant_ctas[0][0].startswith("emotion"):
            if emotional_intensity > 0.5:
                return "emotional_intense"  # 強い感情表現
            else:
                return "emotional_subtle"  # 繊細な感情表現
                
        elif dominant_ctas and dominant_ctas[0][0].startswith("metaphysical"):
            return "philosophical"  # 哲学的考察
            
        else:
            return "narrative"  # 一般的な叙述
    
    def _build_sentence(self, structure: str, 
                       dominant_ctas: List[Tuple[str, float]],
                       dominant_ontos: List[Tuple[str, float]],
                       target_length: int) -> str:
        """セマンティック要素から文章を構築"""
        
        # 構造別のテンプレート
        templates = {
            "temporal_philosophical": [
                "{temporal}の中で{concept}は{quality}として{action}",
                "{concept}は{temporal}を超えて{quality}に{action}",
                "{temporal}という{concept}において{quality}が{action}"
            ],
            "temporal_descriptive": [
                "{temporal}に{concept}が{action}",
                "{concept}は{temporal}に{quality}く{action}",
                "{temporal}、{concept}は{action}"
            ],
            "spatial_complex": [
                "{spatial}に{concept}が{quality}く{action}、そして{concept2}も{action2}",
                "{spatial}では{concept}と{concept2}が{quality}に{action}",
                "{concept}は{spatial}を{quality}く{action}ながら{concept2}へ"
            ],
            "spatial_simple": [
                "{spatial}に{concept}がある",
                "{concept}は{spatial}で{action}",
                "{spatial}の{concept}は{quality}"
            ],
            "emotional_intense": [
                "{emotion}が{concept}を{quality}く{action}",
                "{concept}は{emotion}に満ちて{action}",
                "深い{emotion}の中で{concept}は{action}"
            ],
            "emotional_subtle": [
                "{concept}に{emotion}が宿る",
                "静かな{emotion}が{concept}を{action}",
                "{concept}は{emotion}を感じさせる"
            ],
            "philosophical": [
                "{concept}とは何か、それは{quality}な{concept2}である",
                "{concept}の{quality}さは{concept2}のようなもの",
                "この世の{concept}は皆{quality}く{action}"
            ],
            "narrative": [
                "{concept}が{action}",
                "{concept}は{quality}",
                "{concept}について{action}"
            ]
        }
        
        # キーワードを抽出
        keywords = self._extract_keywords(dominant_ctas, dominant_ontos)
        
        # テンプレートを選択して埋める
        import random
        template = random.choice(templates.get(structure, templates["narrative"]))
        
        # プレースホルダーを埋める
        sentence = template.format(**keywords)
        
        # 長さ調整（簡易版）
        if len(sentence) < target_length * 0.5:
            # 短すぎる場合は修飾を追加
            sentence = self._expand_sentence(sentence, keywords, target_length)
        elif len(sentence) > target_length * 1.5:
            # 長すぎる場合は簡潔化
            sentence = self._shorten_sentence(sentence, target_length)
        
        return sentence
    
    def _extract_keywords(self, dominant_ctas, dominant_ontos) -> Dict[str, str]:
        """支配的次元からキーワードを抽出"""
        
        keywords = {}
        
        # CTAからコンセプトを抽出
        concept_map = {
            "temporal_basic": "時の流れ",
            "temporal_qualitative": "時の質",
            "temporal_memory": "記憶",
            "spatial_basic": "空間",
            "spatial_movement": "動き",
            "emotion_primary": "感情",
            "emotion_subtle": "微細な心",
            "metaphysical_existence": "存在",
            "metaphysical_consciousness": "意識",
            "narrative_flow": "物語"
        }
        
        # 動作を抽出
        action_map = {
            "temporal": "流れる",
            "spatial": "広がる",
            "emotion": "揺れる",
            "metaphysical": "存在する",
            "narrative": "語られる"
        }
        
        # 性質を抽出
        quality_map = {
            "temporal": "移ろいやす",
            "spatial": "広",
            "emotion": "深",
            "metaphysical": "永遠",
            "narrative": "美し"
        }
        
        # オントロジーから具体的要素を抽出
        onto_elements = {
            "natural_水": "水",
            "natural_花": "花",
            "natural_風": "風",
            "temporal_朝": "朝",
            "temporal_夜": "夜",
            "spatial_道": "道",
            "spatial_海": "海",
            "character_心": "心"
        }
        
        # キーワードを設定
        if dominant_ctas:
            cta_key = dominant_ctas[0][0]
            cta_type = cta_key.split('_')[0]
            
            keywords["concept"] = concept_map.get(cta_key, "もの")
            keywords["action"] = action_map.get(cta_type, "ある")
            keywords["quality"] = quality_map.get(cta_type, "ある")
            
            if len(dominant_ctas) > 1:
                keywords["concept2"] = concept_map.get(dominant_ctas[1][0], "それ")
                keywords["action2"] = action_map.get(dominant_ctas[1][0].split('_')[0], "ある")
        
        if dominant_ontos:
            onto_key = dominant_ontos[0][0]
            if onto_key in onto_elements:
                keywords[onto_key.split('_')[0]] = onto_elements[onto_key]
            
            # 感情要素
            if "emotion" in onto_key:
                keywords["emotion"] = onto_elements.get(onto_key, "思い")
        
        # デフォルト値の設定
        keywords.setdefault("temporal", "時")
        keywords.setdefault("spatial", "ここ")
        keywords.setdefault("emotion", "思い")
        keywords.setdefault("concept", "それ")
        keywords.setdefault("concept2", "もの")
        keywords.setdefault("action", "ある")
        keywords.setdefault("action2", "なる")
        keywords.setdefault("quality", "ある")
        
        return keywords
    
    def _expand_sentence(self, sentence: str, keywords: Dict[str, str], target_length: int) -> str:
        """文を拡張"""
        expansions = [
            "まるで{concept2}のように",
            "それは実に{quality}く",
            "この{temporal}において",
            "あたかも{concept2}の如く"
        ]
        
        import random
        expansion = random.choice(expansions).format(**keywords)
        return f"{sentence}、{expansion}"
    
    def _shorten_sentence(self, sentence: str, target_length: int) -> str:
        """文を短縮"""
        # 簡易版：句読点で区切って前半を取る
        if "、" in sentence:
            parts = sentence.split("、")
            return parts[0] + "。"
        return sentence[:target_length] + "..."