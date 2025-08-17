#!/usr/bin/env python3
"""
高度ローカライゼーションシステム
=================================

文学作品・文書の徹底的な地域適応変換システム
- 登場人物名の完全日本人化
- 地名・文化要素の日本適応
- 文体・表現の日本語ネイティブ調整
- カスタムローカライズルール対応

Based on Ken's insight: "カラマーゾフの兄弟の名前を全部日本人の名前にしたらめっちゃわかりやすくなる"
"""

import json
import re
import time
import random
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import logging

@dataclass
class LocalizationRule:
    """ローカライゼーションルール"""
    rule_id: str
    rule_type: str  # "name", "place", "culture", "expression"
    source_pattern: str
    target_replacement: str
    context_condition: Optional[str] = None
    confidence_threshold: float = 0.8

@dataclass
class NameMappingEntry:
    """名前マッピングエントリ"""
    original_name: str
    japanese_name: str
    gender: str
    character_type: str  # "protagonist", "supporting", "minor"
    personality_traits: List[str]
    name_reasoning: str

@dataclass
class LocalizationResult:
    """ローカライゼーション結果"""
    original_text: str
    localized_text: str
    applied_rules: List[Dict[str, Any]]
    name_conversions: List[NameMappingEntry]
    place_conversions: List[Dict[str, str]]
    cultural_adaptations: List[Dict[str, str]]
    localization_quality_score: float
    processing_time: float
    created_timestamp: float

class AdvancedLocalizationSystem:
    """
    高度ローカライゼーションシステム
    文学作品の完全日本適応変換
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # 日本人名データベース
        self.japanese_names = self._initialize_japanese_names()
        
        # ローカライゼーションルール
        self.localization_rules = self._initialize_localization_rules()
        
        # 文学作品別特殊マッピング
        self.literary_mappings = self._initialize_literary_mappings()
        
        # 帰化機能システム
        self.naturalization_engine = self._initialize_naturalization_engine()
        
        print("🌸 高度ローカライゼーションシステム初期化完了")
        print("   日本適応変換準備完了")
        
    def _initialize_japanese_names(self) -> Dict[str, Dict[str, List[str]]]:
        """日本人名データベース初期化"""
        return {
            "male_names": {
                "strong_character": ["大輔", "健太", "剛志", "武志", "力也", "勇介", "強志"],
                "intellectual": ["哲也", "賢一", "聡志", "智彦", "学", "文彦", "博之"],
                "gentle": ["優人", "和也", "穏", "温志", "慎一", "静也", "安司"],
                "artistic": ["雅彦", "美男", "詩人", "文雄", "芸志", "創作", "美郎"],
                "religious": ["信一", "聖志", "神司", "仁", "慈雄", "救", "愛也"],
                "rebellious": ["反", "荒太", "暴志", "破", "狂介", "乱", "逆志"]
            },
            "female_names": {
                "elegant": ["美紀", "雅子", "麗華", "優美", "清香", "純子", "典子"],
                "strong": ["剛子", "勇子", "強美", "毅子", "凛", "颯子", "雄美"],
                "gentle": ["和子", "温美", "穏香", "慎子", "静香", "安美", "柔子"],
                "mysterious": ["謎子", "神秘", "幽香", "影美", "闇子", "秘美", "奥香"],
                "tragic": ["悲美", "涙子", "憂香", "哀美", "愁子", "嘆美", "苦香"]
            },
            "surnames": {
                "noble": ["高田", "上杉", "藤原", "橘", "源", "平", "足利"],
                "common": ["田中", "佐藤", "鈴木", "高橋", "渡辺", "山田", "中村"],
                "regional": ["北野", "南川", "東山", "西田", "中島", "大谷", "小林"],
                "occupational": ["大工", "農", "商人", "職人", "学者", "医者", "僧"]
            }
        }
    
    def _initialize_localization_rules(self) -> List[LocalizationRule]:
        """ローカライゼーションルール初期化"""
        rules = []
        
        # ロシア名→日本名パターン
        russian_names = [
            ("ドミートリー", "大輔", "male_strong"),
            ("イワン", "伊万", "male_intellectual"), 
            ("アリョーシャ", "有朝", "male_gentle"),
            ("フョードル", "文太郎", "male_elder"),
            ("カテリーナ", "香帝", "female_elegant"),
            ("グルーシェンカ", "久留子", "female_mysterious"),
            ("スメルジャコフ", "墨田", "male_servant"),
            ("ゾシマ", "蔵馬", "male_religious"),
        ]
        
        for original, japanese, character_type in russian_names:
            rules.append(LocalizationRule(
                rule_id=f"name_{original}",
                rule_type="name",
                source_pattern=original,
                target_replacement=japanese,
                confidence_threshold=0.9
            ))
        
        # 地名変換ルール
        place_names = [
            ("モスクワ", "武蔵野"),
            ("ペテルブルグ", "江戸"),
            ("シベリア", "蝦夷"),
            ("ヴォルガ川", "利根川"),
            ("ウラル山脈", "富士山系"),
            ("バイカル湖", "琵琶湖"),
        ]
        
        for original, japanese in place_names:
            rules.append(LocalizationRule(
                rule_id=f"place_{original}",
                rule_type="place",
                source_pattern=original,
                target_replacement=japanese,
                confidence_threshold=0.8
            ))
        
        # 文化要素変換ルール
        cultural_elements = [
            ("正教会", "禅寺"),
            ("ウォッカ", "日本酒"),
            ("ボルシチ", "味噌汁"),
            ("サモワール", "茶釜"),
            ("イコン", "仏像"),
            ("修道院", "寺院"),
        ]
        
        for original, japanese in cultural_elements:
            rules.append(LocalizationRule(
                rule_id=f"culture_{original}",
                rule_type="culture",
                source_pattern=original,
                target_replacement=japanese,
                confidence_threshold=0.7
            ))
        
        return rules
    
    def _initialize_literary_mappings(self) -> Dict[str, Dict]:
        """文学作品別特殊マッピング"""
        return {
            "karamazov_brothers": {
                "title": "加楽真象夫の兄弟",
                "setting": "明治時代の武蔵野",
                "theme_adaptations": {
                    "Orthodox_Christianity": "禅仏教",
                    "Russian_soul": "大和魂",
                    "Nihilism": "無常観",
                    "Faith_vs_Reason": "信仰と理性"
                },
                "character_relationships": {
                    "父子関係": "家督相続問題",
                    "兄弟対立": "家業跡継ぎ争い",
                    "恋愛関係": "許嫁制度下の恋愛"
                }
            },
            
            "war_and_peace": {
                "title": "戦争と平和 - 幕末動乱記",
                "setting": "幕末から明治維新",
                "theme_adaptations": {
                    "Napoleonic_Wars": "黒船来航・戊辰戦争",
                    "Russian_nobility": "幕府旗本・諸藩主",
                    "French_invasion": "外国勢力の介入"
                }
            },
            
            "crime_and_punishment": {
                "title": "罪と罰 - 明治維新後の心象",
                "setting": "明治初期の東京",
                "theme_adaptations": {
                    "Guilt_and_redemption": "罪悪感と贖罪",
                    "Poverty_and_crime": "士族没落と犯罪",
                    "Psychological_analysis": "心理分析"
                }
            },
            
            # 中国文学シリーズ
            "journey_to_west": {
                "title": "西遊記 - 天空への旅路",
                "setting": "古代日本・山岳地帯",
                "theme_adaptations": {
                    "Buddhist_pilgrimage": "仏教巡礼",
                    "Monkey_King": "猿王",
                    "Heaven_rebellion": "天への反逆",
                    "Enlightenment_journey": "悟りの旅"
                }
            },
            
            "romance_three_kingdoms": {
                "title": "三国志 - 戦国三分記",
                "setting": "戦国時代",
                "theme_adaptations": {
                    "Han_Dynasty": "平安朝廷",
                    "Three_Kingdoms": "三大勢力",
                    "Military_strategy": "軍事戦略",
                    "Loyalty_betrayal": "忠義と裏切り"
                }
            },
            
            "dream_red_chamber": {
                "title": "紅楼夢 - 華族没落記", 
                "setting": "江戸時代後期",
                "theme_adaptations": {
                    "Aristocratic_decline": "華族没落",
                    "Forbidden_love": "禁断の恋",
                    "Family_honor": "家名の誇り",
                    "Social_hierarchy": "身分制度"
                }
            },
            
            # 西洋文学追加
            "mario_series": {
                "title": "真理央の大冒険",
                "setting": "現代日本・ゲーム世界",
                "theme_adaptations": {
                    "Princess_rescue": "姫君救出",
                    "Kingdom_adventure": "王国冒険",
                    "Good_vs_evil": "正義vs悪"
                }
            }
        }
    
    def _initialize_naturalization_engine(self) -> Dict[str, Any]:
        """帰化機能エンジン初期化 - ケン氏発案「マリオ→真理央」システム"""
        return {
            # 音韻ベース帰化パターン
            "phonetic_naturalization": {
                # イタリア系
                "mario": "真理央",
                "luigi": "留意義", 
                "giuseppe": "十瀬平",
                "giovanni": "上万二",
                "francesco": "古蘭千郎",
                
                # 英語系
                "john": "樹音",
                "mary": "真理",
                "david": "大維人",
                "michael": "美仮流",
                "sarah": "佐羅",
                "james": "十夢須",
                "william": "上利雨無",
                
                # ドイツ系
                "wilhelm": "上留夢",
                "friedrich": "不利井道",
                "wolfgang": "上夫岡",
                "gretchen": "玲釣陳",
                
                # フランス系
                "pierre": "比恵留",
                "marie": "真理恵",
                "jean": "樹安",
                "claude": "蔵憂出",
                "antoine": "安十院",
                
                # 中国系（音読み＋意訳混合）
                "liu_bei": "劉部太郎",
                "guan_yu": "関雄",
                "zhang_fei": "張飛雄",
                "zhuge_liang": "諸川明",
                "cao_cao": "曹操",
                "sun_quan": "孫権三",
                "wukong": "悟空",
                "xuanzang": "玄蔵",
                "bajie": "八戒",
                "wujing": "悟浄",
                "baoyu": "宝雄",
                "daiyu": "代雄",
                "baochai": "宝茶"
            },
            
            # 意味ベース帰化パターン
            "semantic_naturalization": {
                # 職業・役職ベース
                "king": "王様",
                "queen": "女王様", 
                "prince": "王子",
                "princess": "姫様",
                "knight": "騎士",
                "wizard": "魔法使い",
                "warrior": "戦士",
                "monk": "僧侶",
                "scholar": "学者",
                "merchant": "商人",
                
                # 性格・特徴ベース
                "wise": "賢",
                "brave": "勇",
                "gentle": "優",
                "strong": "剛",
                "beautiful": "美",
                "clever": "智"
            },
            
            # 文化的帰化パターン
            "cultural_naturalization": {
                # 食べ物
                "pizza": "ピザ焼き",
                "pasta": "麺類",
                "wine": "葡萄酒",
                "bread": "パン",
                "cheese": "乳製品",
                
                # 建物・場所
                "castle": "城",
                "cathedral": "大聖堂",
                "village": "村",
                "forest": "森",
                "mountain": "山",
                "river": "川"
            },
            
            # 特殊変換ルール
            "special_rules": {
                # 複合名前の処理
                "compound_names": True,
                "title_preservation": True,  # 敬称保持
                "family_name_generation": True,  # 苗字自動生成
                "regional_variation": True  # 地方変種対応
            }
        }
    
    def localize_text(self, text: str, work_title: str = None, 
                     custom_rules: List[LocalizationRule] = None) -> LocalizationResult:
        """
        テキストの完全ローカライゼーション実行
        """
        print(f"🌸 ローカライゼーション開始: {work_title or '汎用文書'}")
        print("=" * 60)
        
        start_time = time.time()
        
        # === Phase 1: 作品特定・ルール選択 ===
        selected_mapping = self._detect_literary_work(text, work_title)
        print(f"📚 作品判定: {selected_mapping.get('title', '汎用作品')}")
        
        # === Phase 2: 登場人物名抽出・マッピング ===
        print("\n👥 Phase 2: 登場人物名分析・マッピング")
        name_conversions = self._generate_character_name_mappings(text, selected_mapping)
        print(f"✅ 登場人物マッピング: {len(name_conversions)}件")
        
        # === Phase 3: 地名・文化要素マッピング ===
        print("\n🏞️ Phase 3: 地名・文化要素適応")
        place_conversions = self._generate_place_mappings(text, selected_mapping)
        cultural_adaptations = self._generate_cultural_mappings(text, selected_mapping)
        print(f"✅ 地名変換: {len(place_conversions)}件, 文化適応: {len(cultural_adaptations)}件")
        
        # === Phase 4: テキスト変換実行 ===
        print("\n🔄 Phase 4: テキスト変換実行")
        localized_text, applied_rules = self._apply_all_conversions(
            text, name_conversions, place_conversions, cultural_adaptations, custom_rules
        )
        
        # === Phase 5: 品質評価 ===
        quality_score = self._evaluate_localization_quality(text, localized_text, applied_rules)
        
        processing_time = time.time() - start_time
        
        result = LocalizationResult(
            original_text=text,
            localized_text=localized_text,
            applied_rules=applied_rules,
            name_conversions=name_conversions,
            place_conversions=place_conversions,
            cultural_adaptations=cultural_adaptations,
            localization_quality_score=quality_score,
            processing_time=processing_time,
            created_timestamp=time.time()
        )
        
        print(f"\n📊 ローカライゼーション結果:")
        print(f"   適用ルール数: {len(applied_rules)}")
        print(f"   名前変換: {len(name_conversions)}")
        print(f"   品質スコア: {quality_score:.3f}")
        print(f"   処理時間: {processing_time:.3f}秒")
        
        print("\n🎉 ローカライゼーション完了!")
        
        return result
    
    def _detect_literary_work(self, text: str, work_title: str = None) -> Dict:
        """文学作品の特定"""
        if work_title and "カラマーゾフ" in work_title:
            return self.literary_mappings["karamazov_brothers"]
        
        # テキスト内容による判定
        if "ドミートリー" in text and "イワン" in text and "アリョーシャ" in text:
            return self.literary_mappings["karamazov_brothers"]
        elif "ナターシャ" in text and "ピエール" in text:
            return self.literary_mappings["war_and_peace"]
        elif "ラスコーリニコフ" in text:
            return self.literary_mappings["crime_and_punishment"]
        
        # デフォルトマッピング
        return {"title": "汎用日本適応", "setting": "現代日本"}
    
    def _generate_character_name_mappings(self, text: str, mapping: Dict) -> List[NameMappingEntry]:
        """登場人物名マッピング生成"""
        name_mappings = []
        
        # 既知のパターンマッチング
        known_characters = {
            "ドミートリー": ("大輔", "male", "protagonist", ["情熱的", "衝動的"], "情熱的な長男"),
            "イワン": ("伊万", "male", "protagonist", ["知的", "懐疑的"], "理知的な次男"),
            "アリョーシャ": ("有朝", "male", "protagonist", ["温和", "信仰深い"], "純真な三男"),
            "フョードル": ("文太郎", "male", "supporting", ["放蕩", "好色"], "放蕩な父親"),
            "カテリーナ": ("香帝", "female", "supporting", ["高慢", "美しい"], "誇り高い令嬢"),
            "グルーシェンカ": ("久留子", "female", "supporting", ["魅惑的", "複雑"], "魅惑的な女性"),
            "ゾシマ": ("蔵馬", "male", "supporting", ["聖人", "導師"], "精神的指導者")
        }
        
        for original_name, (japanese_name, gender, char_type, traits, reasoning) in known_characters.items():
            if original_name in text:
                name_mappings.append(NameMappingEntry(
                    original_name=original_name,
                    japanese_name=japanese_name,
                    gender=gender,
                    character_type=char_type,
                    personality_traits=traits,
                    name_reasoning=reasoning
                ))
        
        # 未知の名前の自動マッピング（帰化機能使用）
        unknown_names = self._extract_unknown_names(text, [nm.original_name for nm in name_mappings])
        for unknown_name in unknown_names:
            # ケン式帰化機能を使用
            japanese_name = self.naturalize_name(unknown_name, text)
            name_mappings.append(NameMappingEntry(
                original_name=unknown_name,
                japanese_name=japanese_name,
                gender="unknown",
                character_type="minor",
                personality_traits=[],
                name_reasoning="ケン式帰化機能による自動変換"
            ))
        
        return name_mappings
    
    def _extract_unknown_names(self, text: str, known_names: List[str]) -> List[str]:
        """未知の人名抽出"""
        # カタカナ名前パターン（ロシア系）
        russian_name_pattern = r'[ァ-ヴー]{3,}(?=[さんは、。！？])'
        matches = re.findall(russian_name_pattern, text)
        
        unknown_names = []
        for match in set(matches):
            if match not in known_names and len(match) >= 3:
                unknown_names.append(match)
        
        return unknown_names
    
    def naturalize_name(self, original_name: str, context: str = "") -> str:
        """
        帰化機能による名前変換 - ケン氏発案システム
        マリオ→真理央 のような音韻＋漢字適用
        """
        original_lower = original_name.lower()
        
        # 1. 直接マッピングチェック
        phonetic_map = self.naturalization_engine["phonetic_naturalization"]
        if original_lower in phonetic_map:
            return phonetic_map[original_lower]
        
        # 2. 部分マッチング（複合名前対応）
        for foreign_name, japanese_name in phonetic_map.items():
            if foreign_name in original_lower:
                return japanese_name
        
        # 3. 音韻ベース自動変換
        japanese_name = self._phonetic_conversion(original_name)
        
        # 4. 意味的強化（文脈考慮）
        if context:
            japanese_name = self._enhance_with_context(japanese_name, context)
        
        return japanese_name
    
    def _phonetic_conversion(self, name: str) -> str:
        """音韻変換エンジン"""
        # 音韻マッピングテーブル
        sound_map = {
            'ma': '真', 'ri': '理', 'o': '央',  # Mario → 真理央
            'lu': '留', 'i': '意', 'gi': '義',  # Luigi → 留意義
            'pi': '比', 'e': '恵', 'r': '留',   # Pierre → 比恵留
            'jo': '樹', 'hn': '音',            # John → 樹音
            'da': '大', 'vi': '維', 'd': '人',  # David → 大維人
            'mi': '美', 'cha': '茶', 'el': '恵流', # Michael → 美茶恵流
            'an': '安', 'to': '十', 'ine': '院', # Antoine → 安十院
        }
        
        # 簡易的な音韻変換
        result = ""
        i = 0
        while i < len(name.lower()):
            matched = False
            # 3文字マッチング
            if i + 2 < len(name) and name.lower()[i:i+3] in sound_map:
                result += sound_map[name.lower()[i:i+3]]
                i += 3
                matched = True
            # 2文字マッチング
            elif i + 1 < len(name) and name.lower()[i:i+2] in sound_map:
                result += sound_map[name.lower()[i:i+2]]
                i += 2
                matched = True
            # 1文字マッチング
            elif name.lower()[i] in sound_map:
                result += sound_map[name.lower()[i]]
                i += 1
                matched = True
            
            if not matched:
                # 未マッピング文字の処理
                char = name[i]
                if char.isalpha():
                    # アルファベットを適当な漢字に変換
                    fallback_map = {
                        'a': '亜', 'b': '部', 'c': '千', 'd': '大', 'e': '恵',
                        'f': '富', 'g': '義', 'h': '春', 'i': '意', 'j': '樹',
                        'k': '京', 'l': '留', 'm': '真', 'n': '那', 'o': '央',
                        'p': '平', 'q': '九', 'r': '理', 's': '佐', 't': '太',
                        'u': '雄', 'v': '美', 'w': '和', 'x': '幸', 'y': '由', 'z': '蔵'
                    }
                    result += fallback_map.get(char.lower(), char)
                else:
                    result += char
                i += 1
        
        return result or name  # 変換失敗時は元の名前
    
    def _enhance_with_context(self, base_name: str, context: str) -> str:
        """文脈による名前強化"""
        # 文脈キーワードによる調整
        if "王" in context or "king" in context.lower():
            return base_name + "王"
        elif "姫" in context or "princess" in context.lower():
            return base_name + "姫"
        elif "騎士" in context or "knight" in context.lower():
            return base_name + "騎士"
        elif "魔法" in context or "magic" in context.lower():
            return base_name + "法師"
        
        return base_name
    
    def _generate_japanese_name_for_character(self, original_name: str, context: str) -> str:
        """文字に基づく日本名生成"""
        # 音韻近似変換
        sound_mappings = {
            'ア': 'あ', 'イ': 'い', 'ウ': 'う', 'エ': 'え', 'オ': 'お',
            'カ': 'か', 'キ': 'き', 'ク': 'く', 'ケ': 'け', 'コ': 'こ',
            'サ': 'さ', 'シ': 'し', 'ス': 'す', 'セ': 'せ', 'ソ': 'そ',
            'タ': 'た', 'チ': 'ち', 'ツ': 'つ', 'テ': 'て', 'ト': 'と',
            'ナ': 'な', 'ニ': 'に', 'ヌ': 'ぬ', 'ネ': 'ね', 'ノ': 'の',
            'ハ': 'は', 'ヒ': 'ひ', 'フ': 'ふ', 'ヘ': 'へ', 'ホ': 'ほ',
            'マ': 'ま', 'ミ': 'み', 'ム': 'む', 'メ': 'め', 'モ': 'も',
            'ヤ': 'や', 'ユ': 'ゆ', 'ヨ': 'よ',
            'ラ': 'ら', 'リ': 'り', 'ル': 'る', 'レ': 'れ', 'ロ': 'ろ',
            'ワ': 'わ', 'ヲ': 'を', 'ン': 'ん'
        }
        
        # 簡易的な音韻変換
        japanese_sound = ""
        for char in original_name[:3]:  # 最初の3文字
            if char in sound_mappings:
                japanese_sound += sound_mappings[char]
        
        # 日本名らしい漢字に変換
        if japanese_sound.startswith('あ'):
            return random.choice(["有朝", "明", "安司"])
        elif japanese_sound.startswith('い'):
            return random.choice(["伊万", "一郎", "勇"])
        elif japanese_sound.startswith('え'):
            return random.choice(["恵美", "栄子", "英志"])
        else:
            return random.choice(["太郎", "花子", "次郎"])
    
    def _generate_place_mappings(self, text: str, mapping: Dict) -> List[Dict[str, str]]:
        """地名マッピング生成"""
        place_mappings = []
        
        place_rules = [rule for rule in self.localization_rules if rule.rule_type == "place"]
        
        for rule in place_rules:
            if rule.source_pattern in text:
                place_mappings.append({
                    "original": rule.source_pattern,
                    "japanese": rule.target_replacement,
                    "rule_id": rule.rule_id
                })
        
        return place_mappings
    
    def _generate_cultural_mappings(self, text: str, mapping: Dict) -> List[Dict[str, str]]:
        """文化要素マッピング生成"""
        cultural_mappings = []
        
        cultural_rules = [rule for rule in self.localization_rules if rule.rule_type == "culture"]
        
        for rule in cultural_rules:
            if rule.source_pattern in text:
                cultural_mappings.append({
                    "original": rule.source_pattern,
                    "japanese": rule.target_replacement,
                    "rule_id": rule.rule_id,
                    "adaptation_type": "cultural_element"
                })
        
        return cultural_mappings
    
    def _apply_all_conversions(self, text: str, name_conversions: List[NameMappingEntry],
                             place_conversions: List[Dict], cultural_adaptations: List[Dict],
                             custom_rules: List[LocalizationRule] = None) -> Tuple[str, List[Dict]]:
        """全変換の適用"""
        localized_text = text
        applied_rules = []
        
        # 名前変換
        for name_mapping in name_conversions:
            count = localized_text.count(name_mapping.original_name)
            if count > 0:
                localized_text = localized_text.replace(
                    name_mapping.original_name, 
                    name_mapping.japanese_name
                )
                applied_rules.append({
                    "type": "name_conversion",
                    "original": name_mapping.original_name,
                    "replacement": name_mapping.japanese_name,
                    "count": count,
                    "reasoning": name_mapping.name_reasoning
                })
        
        # 地名変換
        for place_mapping in place_conversions:
            count = localized_text.count(place_mapping["original"])
            if count > 0:
                localized_text = localized_text.replace(
                    place_mapping["original"],
                    place_mapping["japanese"]
                )
                applied_rules.append({
                    "type": "place_conversion", 
                    "original": place_mapping["original"],
                    "replacement": place_mapping["japanese"],
                    "count": count
                })
        
        # 文化要素変換
        for cultural_mapping in cultural_adaptations:
            count = localized_text.count(cultural_mapping["original"])
            if count > 0:
                localized_text = localized_text.replace(
                    cultural_mapping["original"],
                    cultural_mapping["japanese"]
                )
                applied_rules.append({
                    "type": "cultural_conversion",
                    "original": cultural_mapping["original"],
                    "replacement": cultural_mapping["japanese"],
                    "count": count
                })
        
        # カスタムルール適用
        if custom_rules:
            for rule in custom_rules:
                count = localized_text.count(rule.source_pattern)
                if count > 0:
                    localized_text = localized_text.replace(
                        rule.source_pattern,
                        rule.target_replacement
                    )
                    applied_rules.append({
                        "type": f"custom_{rule.rule_type}",
                        "original": rule.source_pattern,
                        "replacement": rule.target_replacement,
                        "count": count,
                        "rule_id": rule.rule_id
                    })
        
        return localized_text, applied_rules
    
    def _evaluate_localization_quality(self, original: str, localized: str, 
                                     applied_rules: List[Dict]) -> float:
        """ローカライゼーション品質評価"""
        base_score = 0.7
        
        # 変換率による加点
        total_changes = sum(rule["count"] for rule in applied_rules)
        change_rate = total_changes / max(1, len(original.split()))
        change_bonus = min(0.2, change_rate * 0.5)
        
        # 変換種類による加点
        rule_types = set(rule["type"] for rule in applied_rules)
        diversity_bonus = len(rule_types) * 0.03
        
        # 文字数変化による調整（大きく変わりすぎない方が良い）
        length_ratio = len(localized) / len(original)
        length_penalty = abs(length_ratio - 1.0) * 0.1
        
        quality_score = base_score + change_bonus + diversity_bonus - length_penalty
        
        return max(0.0, min(1.0, quality_score))
    
    def create_localization_summary(self, result: LocalizationResult) -> str:
        """ローカライゼーション結果サマリー作成"""
        summary = f"""
🌸 **ローカライゼーション完了レポート**

📊 **変換統計**
- 適用ルール数: {len(result.applied_rules)}
- 登場人物変換: {len(result.name_conversions)}名
- 地名変換: {len(result.place_conversions)}箇所
- 文化適応: {len(result.cultural_adaptations)}要素
- 品質スコア: {result.localization_quality_score:.1%}

👥 **主な登場人物変換**
"""
        
        for name_conv in result.name_conversions[:5]:  # 最大5名表示
            summary += f"• {name_conv.original_name} → **{name_conv.japanese_name}** ({name_conv.name_reasoning})\n"
        
        if len(result.name_conversions) > 5:
            summary += f"• ...他{len(result.name_conversions) - 5}名\n"
        
        summary += "\n🏞️ **地名・文化要素変換**\n"
        
        all_conversions = result.place_conversions + result.cultural_adaptations
        for conv in all_conversions[:5]:  # 最大5要素表示
            summary += f"• {conv['original']} → **{conv['japanese']}**\n"
        
        if len(all_conversions) > 5:
            summary += f"• ...他{len(all_conversions) - 5}要素\n"
        
        summary += f"\n⏱️ 処理時間: {result.processing_time:.3f}秒"
        
        return summary.strip()

def main():
    """高度ローカライゼーションシステムのデモ実行"""
    print("🌸 高度ローカライゼーションシステム")
    print("=" * 60)
    
    # システム初期化
    localization_system = AdvancedLocalizationSystem()
    
    # 革命的ローカライゼーションテストセット
    test_cases = {
        "karamazov_brothers": """
ドミートリーは情熱的で衝動的な性格の長男である。イワンは知的で懐疑的な次男で、
アリョーシャは純真で信仰深い三男だった。父親のフョードルは放蕩な生活を送っており、
カテリーナという美しい令嬢と、グルーシェンカという魅惑的な女性の間で揺れ動いていた。
ゾシマ長老は精神的な指導者として、アリョーシャに大きな影響を与えた。
物語の舞台はモスクワ近郊の小さな町で、正教会の教えが人々の生活に深く根ざしていた。
登場人物たちはウォッカを飲みながら人生について語り合い、
サモワールで沸かした茶を飲みながら哲学的な議論を交わした。
        """,
        
        "mario_adventure": """
Marioは勇敢な配管工で、Luigiという弟と一緒にKingdom of Mushroomで冒険していた。
Princess Peachが邪悪なBowserにさらわれてしまい、Marioは彼女を救うために旅立った。
途中でToadという小さな助手に出会い、様々な試練を乗り越えていく。
Marioはfire flowerを手に入れて強くなり、最終的にBowserの城でPrincess Peachを救出した。
        """,
        
        "three_kingdoms": """
劉備は仁徳ある指導者で、関羽と張飛という義兄弟と共に天下統一を目指していた。
諸葛亮という天才軍師が劉備に仕え、数々の戦略で敵を打ち破った。
一方、曹操は冷徹で計算高い政治家として北方を支配し、
孫権は若いながらも賢明な君主として江南の地を治めていた。
三国が鼎立する中、英雄たちは己の信念をかけて戦い続けた。
        """,
        
        "western_literature": """
John は勇敢な騎士で、Mary という美しい姫君を愛していた。
悪い魔法使い David が Mary をさらって Dark Castle に監禁してしまった。
John は Michael という仲間と共に、姫君を救うための冒険に出発した。
途中で賢者 William に出会い、魔法の剣を授けられる。
最後に John は David を倒し、Mary と結ばれて幸せに暮らした。
        """
    }
    
    try:
        print("📚 カラマーゾフの兄弟ローカライゼーションテスト")
        
        # ローカライゼーション実行
        result = localization_system.localize_text(
            test_text, 
            work_title="カラマーゾフの兄弟"
        )
        
        print(f"\n📖 **変換結果:**")
        print("=" * 50)
        print(result.localized_text)
        print("=" * 50)
        
        # サマリー表示
        summary = localization_system.create_localization_summary(result)
        print(f"\n{summary}")
        
        print("\n🎉 高度ローカライゼーションシステム実行完了!")
        
    except Exception as e:
        print(f"❌ 実行エラー: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main()