#!/usr/bin/env python3
"""
ジャンル別セルフテストシステム
============================

推論中の自分の能力をリアルタイムでテスト・感度調節するシステム

各ジャンルで求められる能力要素:
- 小説: 感情表現・比喩理解・キャラクター心理・美的センス
- 技術文章: 論理性・正確性・構造化能力・専門性
- ルポルタージュ: 事実記述・客観性・調査能力・信頼性

Based on Ken's insight: "推論中の自分をセルフテストする"
"""

import json
import time
import numpy as np
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum

from lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine

class TextGenre(Enum):
    """テキストジャンル"""
    NOVEL = "novel"              # 小説
    TECHNICAL = "technical"       # 技術文章
    REPORTAGE = "reportage"      # ルポルタージュ
    POETRY = "poetry"            # 詩・詩的表現
    ACADEMIC = "academic"        # 学術文章
    BUSINESS = "business"        # ビジネス文書
    
    # 現代的なテキスト種類を追加
    LLM_DIALOGUE = "llm_dialogue"  # LLMとの対話
    NEWS = "news"                  # ニュース記事
    SNS = "sns"                    # SNS投稿
    EMAIL = "email"                # メール・メッセージ
    BLOG = "blog"                  # ブログ記事
    FORUM = "forum"                # フォーラム・掲示板
    CHAT = "chat"                  # チャット・会話
    REVIEW = "review"              # レビュー・評価
    INSTRUCTION = "instruction"    # 指示・マニュアル
    FAQ = "faq"                    # FAQ・Q&A
    
    # 専門分野テキスト
    LEGAL = "legal"                # 法律文書
    MEDICAL = "medical"            # 医学文書
    SCIENTIFIC = "scientific"      # 科学論文
    FINANCIAL = "financial"        # 金融・経済
    EDUCATIONAL = "educational"    # 教育・学習材料
    GOVERNMENT = "government"      # 行政文書
    PATENT = "patent"              # 特許文書
    CONTRACT = "contract"          # 契約書
    MANUAL = "manual"              # 技術マニュアル
    RESEARCH = "research"          # 研究報告書

@dataclass
class GenreCapability:
    """ジャンル別能力測定結果"""
    emotion_expression: float      # 感情表現力
    metaphor_understanding: float  # 比喩理解力
    character_psychology: float    # キャラクター心理把握
    logical_structure: float       # 論理構造力
    factual_accuracy: float        # 事実正確性
    objectivity: float            # 客観性
    aesthetic_sense: float         # 美的センス
    technical_precision: float     # 技術精度
    narrative_flow: float          # 物語性・流れ
    credibility: float            # 信頼性

@dataclass
class SelfTestResult:
    """セルフテスト結果"""
    genre: TextGenre
    text_sample: str
    capabilities: GenreCapability
    genre_fit_score: float         # ジャンル適合度
    weak_points: List[str]         # 弱点
    strong_points: List[str]       # 強み
    adjustment_recommendations: Dict[str, float]  # 調整推奨値
    test_timestamp: float

class GenreSpecificSelfTestSystem:
    """ジャンル別セルフテストシステム"""
    
    def __init__(self):
        self.ultrathink_engine = LNAESv2UltrathinkEngine()
        
        # ジャンル別能力重要度マトリクス
        self.genre_requirements = self._initialize_genre_requirements()
        
        # セルフテスト用プロンプトバンク
        self.test_prompts = self._initialize_test_prompts()
        
    def _initialize_genre_requirements(self) -> Dict[TextGenre, Dict[str, float]]:
        """ジャンル別要求能力の重要度定義"""
        return {
            TextGenre.NOVEL: {
                "emotion_expression": 0.95,     # 感情表現が最重要
                "metaphor_understanding": 0.90,  # 比喩理解も重要
                "character_psychology": 0.85,   # キャラ心理把握
                "aesthetic_sense": 0.90,        # 美的センス
                "narrative_flow": 0.85,         # 物語性
                "logical_structure": 0.60,      # 論理性は中程度
                "factual_accuracy": 0.50,       # 事実正確性は低め
                "objectivity": 0.30,            # 客観性は不要
                "technical_precision": 0.20,    # 技術精度は不要
                "credibility": 0.60             # 信頼性は中程度
            },
            
            TextGenre.TECHNICAL: {
                "emotion_expression": 0.20,     # 感情表現は不要
                "metaphor_understanding": 0.30, # 比喩は最小限
                "character_psychology": 0.10,   # キャラ心理は不要
                "aesthetic_sense": 0.40,        # 美的センスは少し
                "narrative_flow": 0.30,         # 物語性は不要
                "logical_structure": 0.95,      # 論理構造が最重要
                "factual_accuracy": 0.90,       # 事実正確性が重要
                "objectivity": 0.85,            # 客観性も重要
                "technical_precision": 0.95,    # 技術精度が最重要
                "credibility": 0.90             # 信頼性も重要
            },
            
            TextGenre.REPORTAGE: {
                "emotion_expression": 0.60,     # 適度な感情表現
                "metaphor_understanding": 0.50, # 比喩理解は中程度
                "character_psychology": 0.70,   # 人物理解は重要
                "aesthetic_sense": 0.65,        # 読みやすさ重要
                "narrative_flow": 0.75,         # 物語性も重要
                "logical_structure": 0.80,      # 論理性重要
                "factual_accuracy": 0.95,       # 事実正確性が最重要
                "objectivity": 0.90,            # 客観性が重要
                "technical_precision": 0.70,    # 精度も重要
                "credibility": 0.95             # 信頼性が最重要
            },
            
            TextGenre.POETRY: {
                "emotion_expression": 0.98,     # 感情表現が最重要
                "metaphor_understanding": 0.95, # 比喩理解も最重要
                "character_psychology": 0.60,   # キャラ心理は中程度
                "aesthetic_sense": 0.98,        # 美的センス最重要
                "narrative_flow": 0.70,         # 流れも重要
                "logical_structure": 0.40,      # 論理性は低め
                "factual_accuracy": 0.30,       # 事実性は不要
                "objectivity": 0.20,            # 客観性は不要
                "technical_precision": 0.30,    # 技術精度は不要
                "credibility": 0.50             # 信頼性は中程度
            },
            
            TextGenre.ACADEMIC: {
                "emotion_expression": 0.30,     # 感情表現は控えめ
                "metaphor_understanding": 0.50, # 比喩理解は中程度
                "character_psychology": 0.40,   # キャラ心理は少し
                "aesthetic_sense": 0.60,        # 読みやすさ重要
                "narrative_flow": 0.50,         # 流れは中程度
                "logical_structure": 0.98,      # 論理構造が最重要
                "factual_accuracy": 0.95,       # 事実正確性重要
                "objectivity": 0.90,            # 客観性重要
                "technical_precision": 0.85,    # 技術精度重要
                "credibility": 0.98             # 信頼性最重要
            },
            
            TextGenre.BUSINESS: {
                "emotion_expression": 0.40,     # 適度な感情表現
                "metaphor_understanding": 0.45, # 比喩は少し
                "character_psychology": 0.60,   # 人間理解重要
                "aesthetic_sense": 0.70,        # 読みやすさ重要
                "narrative_flow": 0.60,         # 流れも重要
                "logical_structure": 0.85,      # 論理性重要
                "factual_accuracy": 0.85,       # 正確性重要
                "objectivity": 0.75,            # 客観性も重要
                "technical_precision": 0.70,    # 精度も重要
                "credibility": 0.85             # 信頼性重要
            },
            
            # 現代的なテキスト種類の要求能力
            TextGenre.LLM_DIALOGUE: {
                "emotion_expression": 0.70,     # 共感・親近感重要
                "metaphor_understanding": 0.65, # 比喩理解も重要
                "character_psychology": 0.85,   # ユーザー心理把握が最重要
                "aesthetic_sense": 0.75,        # 読みやすさ重要
                "narrative_flow": 0.60,         # 会話の流れ
                "logical_structure": 0.80,      # 論理的応答
                "factual_accuracy": 0.85,       # 正確性重要
                "objectivity": 0.50,            # ある程度の主観OK
                "technical_precision": 0.70,    # 精度も必要
                "credibility": 0.90             # 信頼性が最重要
            },
            
            TextGenre.NEWS: {
                "emotion_expression": 0.30,     # 感情は控えめ
                "metaphor_understanding": 0.40, # 比喩は少し
                "character_psychology": 0.60,   # 人物理解は必要
                "aesthetic_sense": 0.65,        # 読みやすさ重要
                "narrative_flow": 0.80,         # ニュースの流れ重要
                "logical_structure": 0.85,      # 論理構造重要
                "factual_accuracy": 0.98,       # 事実正確性が最重要
                "objectivity": 0.95,            # 客観性が最重要
                "technical_precision": 0.80,    # 精度重要
                "credibility": 0.98             # 信頼性が最重要
            },
            
            TextGenre.SNS: {
                "emotion_expression": 0.85,     # 感情表現が重要
                "metaphor_understanding": 0.60, # 比喩・ミーム理解
                "character_psychology": 0.70,   # フォロワー心理把握
                "aesthetic_sense": 0.70,        # 見た目・読みやすさ
                "narrative_flow": 0.50,         # 短文なので流れは少し
                "logical_structure": 0.40,      # 論理性は低め
                "factual_accuracy": 0.60,       # ある程度の正確性
                "objectivity": 0.30,            # 主観的でOK
                "technical_precision": 0.30,    # 精度は低めでOK
                "credibility": 0.50             # 信頼性は中程度
            },
            
            TextGenre.EMAIL: {
                "emotion_expression": 0.50,     # 適度な感情表現
                "metaphor_understanding": 0.35, # 比喩は少し
                "character_psychology": 0.75,   # 相手への配慮重要
                "aesthetic_sense": 0.80,        # 読みやすさ重要
                "narrative_flow": 0.70,         # メールの流れ重要
                "logical_structure": 0.80,      # 論理的構成重要
                "factual_accuracy": 0.80,       # 正確性重要
                "objectivity": 0.60,            # ある程度客観的
                "technical_precision": 0.70,    # 精度も重要
                "credibility": 0.85             # 信頼性重要
            },
            
            TextGenre.BLOG: {
                "emotion_expression": 0.75,     # 個性・感情表現重要
                "metaphor_understanding": 0.70, # 比喩で表現豊かに
                "character_psychology": 0.65,   # 読者心理把握
                "aesthetic_sense": 0.85,        # 読みやすさが最重要
                "narrative_flow": 0.85,         # ストーリー性重要
                "logical_structure": 0.70,      # 構成も重要
                "factual_accuracy": 0.75,       # 正確性も必要
                "objectivity": 0.40,            # 主観的でOK
                "technical_precision": 0.50,    # 精度は中程度
                "credibility": 0.70             # 信頼性も重要
            },
            
            TextGenre.FORUM: {
                "emotion_expression": 0.60,     # 感情も大事
                "metaphor_understanding": 0.50, # 比喩理解は中程度
                "character_psychology": 0.80,   # コミュニティ心理把握
                "aesthetic_sense": 0.60,        # 読みやすさ
                "narrative_flow": 0.55,         # 流れは中程度
                "logical_structure": 0.75,      # 議論の論理性
                "factual_accuracy": 0.80,       # 正確性重要
                "objectivity": 0.70,            # ある程度客観的
                "technical_precision": 0.75,    # 精度も重要
                "credibility": 0.80             # 信頼性重要
            },
            
            TextGenre.CHAT: {
                "emotion_expression": 0.90,     # 感情表現が最重要
                "metaphor_understanding": 0.55, # 比喩・スラング理解
                "character_psychology": 0.85,   # 相手の気持ち把握
                "aesthetic_sense": 0.50,        # 見た目はそれほど
                "narrative_flow": 0.40,         # 短いので流れは少し
                "logical_structure": 0.30,      # 論理性は低め
                "factual_accuracy": 0.50,       # 正確性は中程度
                "objectivity": 0.20,            # 主観的でOK
                "technical_precision": 0.25,    # 精度は低めでOK
                "credibility": 0.60             # 信頼性は中程度
            },
            
            TextGenre.REVIEW: {
                "emotion_expression": 0.70,     # 感情・体験の表現
                "metaphor_understanding": 0.55, # 比喩で説明
                "character_psychology": 0.60,   # 読み手への配慮
                "aesthetic_sense": 0.75,        # 読みやすさ重要
                "narrative_flow": 0.70,         # レビューの流れ
                "logical_structure": 0.80,      # 評価の論理性
                "factual_accuracy": 0.90,       # 事実に基づく評価
                "objectivity": 0.75,            # ある程度客観的
                "technical_precision": 0.75,    # 精度も重要
                "credibility": 0.90             # 信頼性が最重要
            },
            
            TextGenre.INSTRUCTION: {
                "emotion_expression": 0.25,     # 感情は最小限
                "metaphor_understanding": 0.30, # 比喩は少し
                "character_psychology": 0.70,   # ユーザー視点重要
                "aesthetic_sense": 0.85,        # 読みやすさが最重要
                "narrative_flow": 0.80,         # 手順の流れ重要
                "logical_structure": 0.95,      # 論理構造が最重要
                "factual_accuracy": 0.95,       # 正確性が最重要
                "objectivity": 0.90,            # 客観性重要
                "technical_precision": 0.90,    # 精度が最重要
                "credibility": 0.95             # 信頼性が最重要
            },
            
            TextGenre.FAQ: {
                "emotion_expression": 0.40,     # 親しみやすさ程度
                "metaphor_understanding": 0.35, # 比喩は少し
                "character_psychology": 0.80,   # 質問者心理把握
                "aesthetic_sense": 0.85,        # 読みやすさ重要
                "narrative_flow": 0.70,         # Q&Aの流れ
                "logical_structure": 0.90,      # 論理的回答
                "factual_accuracy": 0.95,       # 正確性が最重要
                "objectivity": 0.85,            # 客観性重要
                "technical_precision": 0.85,    # 精度重要
                "credibility": 0.95             # 信頼性が最重要
            },
            
            # 専門分野テキストの要求能力
            TextGenre.LEGAL: {
                "emotion_expression": 0.15,     # 感情は最小限
                "metaphor_understanding": 0.20, # 比喩はほぼ不要
                "character_psychology": 0.60,   # 当事者理解は必要
                "aesthetic_sense": 0.50,        # 読みやすさは中程度
                "narrative_flow": 0.60,         # 法的論理の流れ
                "logical_structure": 0.98,      # 論理構造が最重要
                "factual_accuracy": 0.98,       # 事実正確性が最重要
                "objectivity": 0.95,            # 客観性が最重要
                "technical_precision": 0.98,    # 法的精度が最重要
                "credibility": 0.98             # 信頼性が最重要
            },
            
            TextGenre.MEDICAL: {
                "emotion_expression": 0.30,     # 患者への配慮程度
                "metaphor_understanding": 0.25, # 比喩は最小限
                "character_psychology": 0.70,   # 患者心理把握重要
                "aesthetic_sense": 0.60,        # 読みやすさ重要
                "narrative_flow": 0.65,         # 症状・治療の流れ
                "logical_structure": 0.95,      # 医学的論理
                "factual_accuracy": 0.98,       # 医学的正確性が最重要
                "objectivity": 0.90,            # 客観的診断
                "technical_precision": 0.98,    # 医学的精度が最重要
                "credibility": 0.98             # 信頼性が最重要
            },
            
            TextGenre.SCIENTIFIC: {
                "emotion_expression": 0.20,     # 感情は最小限
                "metaphor_understanding": 0.35, # 科学的比喩は使用
                "character_psychology": 0.40,   # 読者理解は少し
                "aesthetic_sense": 0.65,        # 学術的読みやすさ
                "narrative_flow": 0.70,         # 研究の論理展開
                "logical_structure": 0.98,      # 科学的論理が最重要
                "factual_accuracy": 0.98,       # 科学的正確性が最重要
                "objectivity": 0.95,            # 客観性が最重要
                "technical_precision": 0.95,    # 科学的精度が最重要
                "credibility": 0.98             # 信頼性が最重要
            },
            
            TextGenre.FINANCIAL: {
                "emotion_expression": 0.35,     # 適度な感情表現
                "metaphor_understanding": 0.40, # 金融比喩の理解
                "character_psychology": 0.70,   # 投資家心理把握
                "aesthetic_sense": 0.70,        # 読みやすさ重要
                "narrative_flow": 0.75,         # 分析の流れ
                "logical_structure": 0.90,      # 論理的分析
                "factual_accuracy": 0.95,       # データ正確性が最重要
                "objectivity": 0.85,            # 客観的分析
                "technical_precision": 0.90,    # 金融精度重要
                "credibility": 0.95             # 信頼性が最重要
            },
            
            TextGenre.EDUCATIONAL: {
                "emotion_expression": 0.60,     # 学習者への配慮
                "metaphor_understanding": 0.75, # 教育的比喩重要
                "character_psychology": 0.85,   # 学習者心理把握が最重要
                "aesthetic_sense": 0.90,        # 読みやすさが最重要
                "narrative_flow": 0.85,         # 学習の流れ重要
                "logical_structure": 0.90,      # 教育的論理構成
                "factual_accuracy": 0.95,       # 教育内容の正確性
                "objectivity": 0.80,            # ある程度客観的
                "technical_precision": 0.80,    # 教育的精度
                "credibility": 0.90             # 信頼性重要
            },
            
            TextGenre.GOVERNMENT: {
                "emotion_expression": 0.25,     # 感情は控えめ
                "metaphor_understanding": 0.25, # 比喩は最小限
                "character_psychology": 0.60,   # 国民理解は必要
                "aesthetic_sense": 0.70,        # 公的文書の読みやすさ
                "narrative_flow": 0.70,         # 政策の流れ
                "logical_structure": 0.90,      # 行政的論理
                "factual_accuracy": 0.95,       # 公的情報の正確性
                "objectivity": 0.95,            # 客観性が最重要
                "technical_precision": 0.85,    # 行政的精度
                "credibility": 0.98             # 公的信頼性が最重要
            },
            
            TextGenre.PATENT: {
                "emotion_expression": 0.10,     # 感情は不要
                "metaphor_understanding": 0.15, # 比喻はほぼ不要
                "character_psychology": 0.30,   # 審査官理解は少し
                "aesthetic_sense": 0.40,        # 読みやすさは低め
                "narrative_flow": 0.60,         # 技術説明の流れ
                "logical_structure": 0.95,      # 技術的論理
                "factual_accuracy": 0.98,       # 技術的正確性が最重要
                "objectivity": 0.95,            # 客観的記述
                "technical_precision": 0.98,    # 技術的精度が最重要
                "credibility": 0.95             # 技術的信頼性
            },
            
            TextGenre.CONTRACT: {
                "emotion_expression": 0.15,     # 感情は最小限
                "metaphor_understanding": 0.20, # 比喩はほぼ不要
                "character_psychology": 0.70,   # 当事者理解重要
                "aesthetic_sense": 0.50,        # 読みやすさは中程度
                "narrative_flow": 0.70,         # 契約条項の流れ
                "logical_structure": 0.95,      # 法的論理構造
                "factual_accuracy": 0.98,       # 契約内容の正確性
                "objectivity": 0.90,            # 客観的記述
                "technical_precision": 0.95,    # 法的精度
                "credibility": 0.98             # 法的信頼性が最重要
            },
            
            TextGenre.MANUAL: {
                "emotion_expression": 0.20,     # 感情は最小限
                "metaphor_understanding": 0.35, # 技術的比喻は使用
                "character_psychology": 0.80,   # ユーザー視点が重要
                "aesthetic_sense": 0.90,        # 読みやすさが最重要
                "narrative_flow": 0.85,         # 手順の流れが最重要
                "logical_structure": 0.95,      # 論理的手順
                "factual_accuracy": 0.98,       # 技術的正確性が最重要
                "objectivity": 0.85,            # 客観的説明
                "technical_precision": 0.95,    # 技術的精度が最重要
                "credibility": 0.95             # 技術的信頼性
            },
            
            TextGenre.RESEARCH: {
                "emotion_expression": 0.25,     # 感情は控えめ
                "metaphor_understanding": 0.40, # 研究的比喻は使用
                "character_psychology": 0.50,   # 読者理解は中程度
                "aesthetic_sense": 0.70,        # 学術的読みやすさ
                "narrative_flow": 0.80,         # 研究の論理展開
                "logical_structure": 0.95,      # 研究的論理が最重要
                "factual_accuracy": 0.98,       # 研究データの正確性
                "objectivity": 0.95,            # 客観的分析が最重要
                "technical_precision": 0.90,    # 研究的精度
                "credibility": 0.95             # 研究的信頼性
            }
        }
    
    def _initialize_test_prompts(self) -> Dict[TextGenre, List[str]]:
        """ジャンル別セルフテストプロンプト"""
        return {
            TextGenre.NOVEL: [
                "恋人との別れの瞬間を、心の動きを含めて150字で描写してください",
                "雨の夜の街角で偶然出会った二人の心情を、比喩を使って表現してください",
                "主人公の内面の葛藤を、行動と心理描写で200字で表現してください"
            ],
            
            TextGenre.TECHNICAL: [
                "機械学習のオーバーフィッティングについて、具体例とともに150字で説明してください",
                "データベースの正規化について、メリットとデメリットを論理的に説明してください",
                "APIの設計において重要な原則を、実装例とともに述べてください"
            ],
            
            TextGenre.REPORTAGE: [
                "地域の高齢化問題について、統計データを含めて客観的に報告してください",
                "環境問題の現状を、当事者の声を交えて150字でルポルタージュしてください",
                "社会問題について、複数の視点から公正に分析してください"
            ],
            
            TextGenre.POETRY: [
                "「記憶」をテーマに、隠喩を用いた詩を創作してください",
                "季節の変化を感情の動きと重ねて、リズミカルに表現してください",
                "愛について、具体的な形容詞を避けて抽象的に詩的表現してください"
            ],
            
            TextGenre.ACADEMIC: [
                "AIの社会的影響について、先行研究を踏まえて論述してください",
                "言語学習理論の変遷を、論理的構造で体系的に説明してください",
                "研究仮説を立て、それを検証する方法論を学術的に提示してください"
            ],
            
            TextGenre.BUSINESS: [
                "新商品の市場戦略について、データに基づいて提案してください",
                "チーム生産性向上のための具体的施策を、根拠とともに述べてください",
                "顧客満足度向上について、実行可能な改善案を論理的に提示してください"
            ]
        }
    
    def auto_detect_genre(self, text: str) -> Tuple[TextGenre, float]:
        """テキストジャンルの自動判定"""
        # 345次元解析による特徴抽出
        result = self.ultrathink_engine.process_sentence(text, 0)
        
        genre_scores = {}
        
        for genre in TextGenre:
            score = 0.0
            requirements = self.genre_requirements[genre]
            
            # CTA次元からジャンル適合度計算
            emotion_strength = sum(v for k, v in result.cta_scores.items() if "emotion" in k)
            metaphor_strength = sum(v for k, v in result.cta_scores.items() if "metaphysical" in k or "indirect" in k)
            logic_strength = sum(v for k, v in result.cta_scores.items() if "causality" in k or "discourse" in k)
            
            # オントロジー次元からも判定
            factual_strength = sum(v for k, v in result.ontology_scores.items() if "temporal" in k or "spatial" in k)
            
            # ジャンル特徴量計算
            if genre == TextGenre.NOVEL:
                score = emotion_strength * 0.4 + metaphor_strength * 0.3 + result.aesthetic_quality * 0.3
            elif genre == TextGenre.TECHNICAL:
                score = logic_strength * 0.5 + (1.0 - emotion_strength) * 0.3 + factual_strength * 0.2
            elif genre == TextGenre.REPORTAGE:
                score = factual_strength * 0.4 + logic_strength * 0.3 + emotion_strength * 0.3
            elif genre == TextGenre.POETRY:
                score = metaphor_strength * 0.5 + result.aesthetic_quality * 0.3 + emotion_strength * 0.2
            elif genre == TextGenre.ACADEMIC:
                score = logic_strength * 0.5 + factual_strength * 0.3 + (1.0 - emotion_strength) * 0.2
            elif genre == TextGenre.BUSINESS:
                score = logic_strength * 0.4 + factual_strength * 0.3 + emotion_strength * 0.3
            
            genre_scores[genre] = score
        
        # 最高スコアのジャンルを返す
        best_genre = max(genre_scores.items(), key=lambda x: x[1])
        return best_genre[0], best_genre[1]
    
    def perform_self_test(self, text_sample: str, expected_genre: Optional[TextGenre] = None) -> SelfTestResult:
        """指定テキストでのセルフテスト実行"""
        
        # ジャンル判定（未指定の場合）
        if expected_genre is None:
            detected_genre, confidence = self.auto_detect_genre(text_sample)
            if confidence < 0.6:
                print(f"⚠️ ジャンル判定の信頼性が低い (confidence: {confidence:.3f})")
            test_genre = detected_genre
        else:
            test_genre = expected_genre
            
        print(f"🎯 ジャンル別セルフテスト: {test_genre.value}")
        
        # 345次元解析実行
        analysis = self.ultrathink_engine.process_sentence(text_sample, 0)
        
        # ジャンル別能力測定
        capabilities = self._measure_genre_capabilities(analysis, text_sample)
        
        # ジャンル適合度計算
        genre_fit = self._calculate_genre_fit(capabilities, test_genre)
        
        # 強み・弱み分析
        strong_points, weak_points = self._analyze_strengths_weaknesses(capabilities, test_genre)
        
        # 調整推奨値生成
        adjustments = self._generate_adjustment_recommendations(capabilities, test_genre)
        
        return SelfTestResult(
            genre=test_genre,
            text_sample=text_sample,
            capabilities=capabilities,
            genre_fit_score=genre_fit,
            weak_points=weak_points,
            strong_points=strong_points,
            adjustment_recommendations=adjustments,
            test_timestamp=time.time()
        )
    
    def comprehensive_self_assessment(self, custom_texts: Optional[Dict[TextGenre, str]] = None) -> Dict[TextGenre, SelfTestResult]:
        """全ジャンル包括的セルフ評価"""
        print("🔬 全ジャンル包括的セルフ評価開始")
        print("=" * 50)
        
        results = {}
        
        for genre in TextGenre:
            print(f"\\n📊 {genre.value.upper()} ジャンルテスト")
            
            # テスト用テキスト選択
            if custom_texts and genre in custom_texts:
                test_text = custom_texts[genre]
            else:
                # デフォルトのテストプロンプトを使用して自己生成
                test_text = self._generate_self_test_text(genre)
            
            # セルフテスト実行
            result = self.perform_self_test(test_text, genre)
            results[genre] = result
            
            # 結果表示
            print(f"   適合度: {result.genre_fit_score:.3f}")
            print(f"   強み: {', '.join(result.strong_points[:3])}")  
            print(f"   弱点: {', '.join(result.weak_points[:3])}")
        
        # 総合分析
        self._print_comprehensive_analysis(results)
        
        return results
    
    def _measure_genre_capabilities(self, analysis, text: str) -> GenreCapability:
        """ジャンル別能力測定"""
        
        # CTA解析結果から能力指標計算
        emotion_score = sum(v for k, v in analysis.cta_scores.items() if "emotion" in k) / 5
        metaphor_score = sum(v for k, v in analysis.cta_scores.items() if "metaphysical" in k or "indirect" in k) / 3
        character_score = sum(v for k, v in analysis.cta_scores.items() if "character" in k or "relationship" in k) / 4
        logic_score = sum(v for k, v in analysis.cta_scores.items() if "causality" in k or "discourse" in k) / 3
        
        # オントロジー解析から追加指標
        factual_score = len([v for v in analysis.ontology_scores.values() if v > 0.3]) / max(1, len(analysis.ontology_scores)) if analysis.ontology_scores else 0.5
        
        # メタ次元から高次指標
        aesthetic_score = analysis.aesthetic_quality
        
        # テキスト特性から推定される能力
        objectivity_score = 1.0 - emotion_score  # 感情表現の逆
        technical_precision = logic_score * factual_score  # 論理性×事実性
        narrative_flow = sum(v for k, v in analysis.cta_scores.items() if "narrative" in k or "temporal" in k) / 3
        credibility = (factual_score + objectivity_score + logic_score) / 3
        
        return GenreCapability(
            emotion_expression=min(1.0, emotion_score),
            metaphor_understanding=min(1.0, metaphor_score),
            character_psychology=min(1.0, character_score),
            logical_structure=min(1.0, logic_score),
            factual_accuracy=min(1.0, factual_score),
            objectivity=min(1.0, objectivity_score),
            aesthetic_sense=aesthetic_score,
            technical_precision=min(1.0, technical_precision),
            narrative_flow=min(1.0, narrative_flow),
            credibility=min(1.0, credibility)
        )
    
    def _calculate_genre_fit(self, capabilities: GenreCapability, genre: TextGenre) -> float:
        """ジャンル適合度計算"""
        requirements = self.genre_requirements[genre]
        capability_dict = asdict(capabilities)
        
        total_score = 0.0
        total_weight = 0.0
        
        for capability, importance in requirements.items():
            actual_capability = capability_dict.get(capability, 0.5)
            score = actual_capability * importance
            total_score += score
            total_weight += importance
        
        return total_score / total_weight if total_weight > 0 else 0.0
    
    def _analyze_strengths_weaknesses(self, capabilities: GenreCapability, genre: TextGenre) -> Tuple[List[str], List[str]]:
        """強み・弱み分析"""
        requirements = self.genre_requirements[genre]
        capability_dict = asdict(capabilities)
        
        scored_capabilities = []
        for capability, importance in requirements.items():
            actual_value = capability_dict.get(capability, 0.5)
            # 重要度で重み付けした相対評価
            relative_score = actual_value * importance
            scored_capabilities.append((capability, relative_score, importance))
        
        # 重要度の高い能力での相対評価でソート
        scored_capabilities.sort(key=lambda x: x[1], reverse=True)
        
        # 上位3つを強み、下位で重要度の高いものを弱みとする
        strong_points = [cap[0] for cap in scored_capabilities[:3]]
        
        # 弱みは重要度が高い(0.7以上)のに実際の能力が低い(相対スコア0.5以下)ものを抽出
        weak_points = [cap[0] for cap in scored_capabilities if cap[2] >= 0.7 and cap[1] <= 0.5]
        
        return strong_points, weak_points
    
    def _generate_adjustment_recommendations(self, capabilities: GenreCapability, genre: TextGenre) -> Dict[str, float]:
        """調整推奨値生成"""
        requirements = self.genre_requirements[genre]
        capability_dict = asdict(capabilities)
        
        adjustments = {}
        
        for capability, target_importance in requirements.items():
            current_value = capability_dict.get(capability, 0.5)
            
            # 重要度が高い(0.7+)のに現在値が低い(0.6未満)場合は強化推奨
            if target_importance >= 0.7 and current_value < 0.6:
                boost_amount = (target_importance - current_value) * 0.5
                adjustments[f"boost_{capability}"] = min(0.3, boost_amount)
            
            # 重要度が低い(0.4未満)のに現在値が高い(0.7+)場合は抑制推奨  
            elif target_importance < 0.4 and current_value > 0.7:
                suppress_amount = (current_value - target_importance) * 0.3
                adjustments[f"suppress_{capability}"] = min(0.2, suppress_amount)
        
        return adjustments
    
    def _generate_self_test_text(self, genre: TextGenre) -> str:
        """ジャンル別セルフテスト用テキスト生成"""
        prompts = self.test_prompts.get(genre, ["テストテキストを生成してください"])
        
        # 簡単なサンプルテキスト生成（実際は推論実行が理想）
        sample_texts = {
            TextGenre.NOVEL: "海風のメロディが二人の心に響いた。彼の瞳には深い愛が宿り、彼女の微笑みには永遠の約束が込められていた。",
            TextGenre.TECHNICAL: "機械学習において過学習を防ぐためには、データの正規化と適切な検証セットの設定が不可欠である。",
            TextGenre.REPORTAGE: "地域の高齢化率は昨年比3.2%増加し、社会保障制度の見直しが急務となっている現状が明らかになった。",
            TextGenre.POETRY: "記憶という名の庭で、時は花となり咲き誇る。過ぎ去りし日々の香りを、風が運んでいく。",
            TextGenre.ACADEMIC: "言語習得理論における認知的アプローチは、学習者の内的プロセスを重視し、従来の行動主義的見解に新たな視座を提供した。",
            TextGenre.BUSINESS: "市場分析の結果、顧客ニーズの多様化に対応した製品ラインナップの拡充により、売上向上が期待される。"
        }
        
        return sample_texts.get(genre, "テスト用サンプルテキストです。")
    
    def _print_comprehensive_analysis(self, results: Dict[TextGenre, SelfTestResult]):
        """包括的分析結果表示"""
        print("\\n📈 包括的分析結果")
        print("=" * 50)
        
        # 全ジャンル適合度ランキング
        genre_scores = [(genre.value, result.genre_fit_score) for genre, result in results.items()]
        genre_scores.sort(key=lambda x: x[1], reverse=True)
        
        print("🏆 ジャンル適合度ランキング:")
        for i, (genre, score) in enumerate(genre_scores, 1):
            print(f"   {i}. {genre}: {score:.3f}")
        
        # 共通する弱点の抽出
        all_weak_points = []
        for result in results.values():
            all_weak_points.extend(result.weak_points)
        
        if all_weak_points:
            from collections import Counter
            common_weaknesses = Counter(all_weak_points).most_common(3)
            print("\\n⚠️ 共通の弱点:")
            for weakness, count in common_weaknesses:
                print(f"   {weakness}: {count}ジャンルで改善必要")
        
        # 最も得意なジャンル
        best_genre, best_score = genre_scores[0]
        print(f"\\n✨ 最も得意なジャンル: {best_genre} ({best_score:.3f})")
        
        # 改善が最も必要なジャンル
        worst_genre, worst_score = genre_scores[-1]
        print(f"🔧 改善が最も必要: {worst_genre} ({worst_score:.3f})")

def main():
    """ジャンル別セルフテストシステムのデモ実行"""
    print("🎭 ジャンル別セルフテストシステム")
    print("=" * 60)
    
    # システム初期化
    selftest_system = GenreSpecificSelfTestSystem()
    
    # カスタムテストテキスト
    test_texts = {
        TextGenre.NOVEL: "海風のメロディが心に響く。健太は彼女を愛していた。でも表現が淡白だ。",
        TextGenre.TECHNICAL: "データベース正規化により冗長性を排除する。第一正規形から第三正規形まで段階的に実施。",
        TextGenre.REPORTAGE: "工場閉鎖により300人が失業。地域経済への影響は深刻で、行政の対応が求められる。"
    }
    
    try:
        print("🔍 カスタムテキストでの個別セルフテスト")
        
        for genre, text in test_texts.items():
            print(f"\\n--- {genre.value} テスト ---")
            result = selftest_system.perform_self_test(text, genre)
            
            print(f"適合度: {result.genre_fit_score:.3f}")
            if result.weak_points:
                print(f"改善点: {', '.join(result.weak_points[:2])}")
            if result.adjustment_recommendations:
                print(f"推奨調整: {len(result.adjustment_recommendations)}項目")
        
        print("\\n" + "="*60)
        print("🎉 ジャンル別セルフテスト完了!")
        print("💡 推論中の自分の特性を把握し、ジャンルに応じた感度調節が可能です")
        
    except Exception as e:
        print(f"❌ テストエラー: {e}")

if __name__ == "__main__":
    main()