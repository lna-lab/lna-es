"""
LNA-LANG Graph Extractor
Enhanced version supporting UI-Min graph format and LNA-LANG requirements
Author: Yuki (covering for sleeping Lina)
"""

from typing import Dict, List, Any, Optional, Tuple
import json
import re
from dataclasses import dataclass

from src.utils.extractors import extract_mentions_entities_events, extract_events_with_roles


# ------------------------------
# Deep extraction primitives
# ------------------------------

KANJI = r"一-龯"  # Basic CJK Unified Ideographs
HIRAGANA = r"ぁ-ゖ"  # includes small kana
KATAKANA = r"ァ-ヺ"  # includes small kana
PROLONG = r"ー"      # chōonpu


@dataclass
class CandidateEntity:
    surface: str
    ent_type: str  # Character | Setting | Attribute | Motif | Unknown
    start: int
    end: int
    confidence: float = 0.0
    gender: Optional[str] = None
    kind: Optional[str] = None
    reasons: Optional[List[str]] = None


@dataclass 
class Character:
    name: str
    gender: Optional[str] = None
    kind: str = "human"  # "human", "android", "AI", etc.
    role: Optional[str] = None


@dataclass
class Setting:
    place: str
    time: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Relation:
    source: str
    relation_type: str  # "LOVES", "FRIENDS", "ENEMY", etc.
    target: str
    strength: float = 1.0


@dataclass
class Motif:
    symbol: str
    category: str = "theme"  # "theme", "object", "concept"
    description: Optional[str] = None


class GraphExtractor:
    """Enhanced graph extraction for LNA-LANG"""
    
    def __init__(self):
        # Name-cue patterns (fixed): honorifics, conjunction + subject, bare subject (guarded)
        name_core = rf"([{KANJI}{{2,4}}|[{KATAKANA}{PROLONG}]{{2,12}}])"
        # Honorific attachment, e.g., 麗華さん / タロウ君
        self.pattern_name_honorific = re.compile(
            rf"([{KANJI}][{KANJI}]{{1,3}}|[{KATAKANA}{PROLONG}]{{2,12}})(さん|くん|ちゃん|氏|君|先輩|先生)"
        )
        # Conjunction subject, e.g., 健太と麗華が / 太郎と花子は
        self.pattern_name_conj_subject = re.compile(
            rf"([{KANJI}]{{2,4}}|[{KATAKANA}{PROLONG}]{{2,12}})と([{KANJI}]{{2,4}}|[{KATAKANA}{PROLONG}]{{2,12}})(が|は)"
        )
        # Bare subject (guarded by stoplists), e.g., 麗華が / 健太は
        self.pattern_name_bare_subject = re.compile(
            rf"(^|[^{KANJI}{HIRAGANA}{KATAKANA}{PROLONG}])([{KANJI}]{{2,4}}|[{KATAKANA}{PROLONG}]{{2,12}})(が|は)"
        )

        # Lexicons and cues
        self.pronouns = {"彼", "彼女", "僕", "私", "俺", "あたし", "わたし"}
        self.place_names = {
            "防波堤", "海", "浜辺", "公園", "学校", "家", "駅", "街", "砂浜", "港", "川", "橋", "海岸", "渚",
            "湘南", "東京", "大阪", "京都", "横浜", "神戸", "新宿", "渋谷", "池袋",
        }
        self.generic_nouns = {
            "空", "風", "雲", "星", "月", "太陽", "夕陽", "夕焼け", "手", "声", "髪", "心", "世界", "端", "橋",
            "金属肌", "涙", "笑み", "光", "静けさ",
        }
        self.attribute_phrases_android = {"金属肌", "機械", "機械なのに", "アンドロイド", "ロボット", "人工知能", "AI"}
        self.gender_indicators = {
            "male": ["彼", "男性", "男の子", "少年", "青年", "兄", "父", "息子"],
            "female": ["彼女", "女性", "女の子", "少女", "姉", "母", "娘"],
        }
        self.kind_indicators = {
            "android": ["アンドロイド", "ロボット", "人工知能", "AI", "機械", "金属肌"],
            "human": ["人間", "人", "ヒト"],
        }
        
        self.setting_patterns = {
            "places": re.compile(r"(湘南|防波堤|海|浜辺|公園|学校|家|駅|街|[一-龥]{2,6}市|[一-龥]{2,6}町)"),
            "times": re.compile(r"(夕暮れ|朝|昼|夜|夕方|深夜|早朝|午前|午後|[0-9]{1,2}時)")
        }
        
        self.relation_patterns = {
            "love": re.compile(r"(愛して|好き|恋|愛情|恋人|カップル|付き合)"),
            "friendship": re.compile(r"(友達|友人|親友|仲間|友情)"),
            "family": re.compile(r"(家族|兄弟|姉妹|親子|父母|夫婦)")
        }
        
        self.motif_patterns = {
            "nature": ["海", "空", "風", "雲", "星", "月", "太陽", "夕陽"],
            "emotion": ["愛", "喜び", "悲しみ", "怒り", "恐怖", "希望", "絶望"],
            "abstract": ["時間", "永遠", "記憶", "夢", "現実", "命", "死"]
        }
    
    def extract_from_text(self, 
                         text: str, 
                         doc_prefix: str = "DOC",
                         run_id: str = "001") -> Dict[str, Any]:
        """テキストから完全なグラフ構造を抽出"""
        
        # 基本エンティティ抽出
        base_nodes, base_edges, graph_seq = extract_mentions_entities_events(
            text=text,
            global_start=0,
            doc_prefix=doc_prefix,
            run_id=run_id,
            graph_seq=0
        )
        
        # イベント抽出
        event_nodes, event_edges, graph_seq = extract_events_with_roles(
            text=text,
            global_start=0, 
            doc_prefix=doc_prefix,
            run_id=run_id,
            graph_seq=graph_seq
        )
        
        # LNA-LANG専用構造抽出
        characters = self._extract_characters(text)
        settings = self._extract_settings(text)
        relations = self._extract_relations(text, characters)
        motifs = self._extract_motifs(text)
        
        # UI-Min形式に変換
        ui_min_graph = self._convert_to_ui_min_format(
            characters, settings, relations, motifs,
            base_nodes + event_nodes,
            base_edges + event_edges
        )
        
        return ui_min_graph
    
    def _extract_characters(self, text: str) -> List[Character]:
        """キャラクター抽出（多段階フィルタ＋信頼度判定）"""
        candidates: Dict[str, CandidateEntity] = {}

        # Stage 1: honorific cues
        for m in self.pattern_name_honorific.finditer(text):
            name = m.group(1)
            if name in self.pronouns or name in self.place_names or name in self.generic_nouns:
                continue
            start, end = m.span(1)
            ce = candidates.get(name) or CandidateEntity(surface=name, ent_type="Character", start=start, end=end, reasons=[])
            ce.confidence = max(ce.confidence, 0.8)
            ce.reasons.append("honorific")
            candidates[name] = ce

        # Stage 2: coordination + subject (強い手掛かり)
        for m in self.pattern_name_conj_subject.finditer(text):
            n1, n2 = m.group(1), m.group(2)
            for name in (n1, n2):
                if name in self.pronouns or name in self.place_names or name in self.generic_nouns:
                    continue
                start = text.find(name, m.start(), m.end())
                end = start + len(name)
                ce = candidates.get(name) or CandidateEntity(surface=name, ent_type="Character", start=start, end=end, reasons=[])
                ce.confidence = max(ce.confidence, 0.75)
                ce.reasons.append("conj+subject")
                candidates[name] = ce

        # Stage 3: guarded bare subject
        for m in self.pattern_name_bare_subject.finditer(text):
            name = m.group(2)
            # Guard with stop-lists and attribute/place exclusion
            if name in self.pronouns or name in self.place_names or name in self.generic_nouns:
                continue
            # Exclude if immediately followed by "の" (名詞連体) more likely attribute/場所
            tail_index = m.end(2)
            if tail_index < len(text) and text[tail_index:tail_index+1] == "の":
                continue
            start = m.start(2)
            end = m.end(2)
            ce = candidates.get(name) or CandidateEntity(surface=name, ent_type="Character", start=start, end=end, reasons=[])
            ce.confidence = max(ce.confidence, 0.55)
            ce.reasons.append("bare-subject")
            candidates[name] = ce

        # Stage 4: gender/kind cues in context
        for name, ce in list(candidates.items()):
            ce.gender = self._infer_gender(text, name)
            ce.kind = self._infer_kind(text, name)
            # Confidence bumps
            if ce.gender:
                ce.confidence = max(ce.confidence, 0.7)
                ce.reasons.append(f"gender:{ce.gender}")
            if ce.kind and ce.kind != "human":
                ce.confidence = max(ce.confidence, 0.75)
                ce.reasons.append(f"kind:{ce.kind}")

        # Stage 4.5: pronoun and possessive attribute binding override (precision pass)
        self._bind_pronoun_and_attributes(text, candidates)

        # Stage 5: final filtering by confidence and output as Character objects
        characters: List[Character] = []
        for ce in candidates.values():
            if ce.confidence >= 0.6:
                role = self._infer_role(text, ce.surface)
                characters.append(Character(name=ce.surface, gender=ce.gender, kind=ce.kind or "human", role=role))

        # Stage 6: simple gender completion heuristic
        # If exactly two characters and one is explicitly female, the other defaults to male unless set
        if len(characters) == 2:
            genders = [c.gender for c in characters]
            if genders.count("female") == 1 and genders.count(None) == 1:
                for c in characters:
                    if c.gender is None:
                        c.gender = "male"
                        break
        return characters

    def _bind_pronoun_and_attributes(self, text: str, candidates: Dict[str, CandidateEntity]) -> None:
        """Pronoun coreference and possessive attribute binding (precision-focused).

        - Binds "彼女"/"彼" to the nearest preceding candidate name within 60 chars.
        - If "彼女の/彼の" is directly followed by strong attribute phrases (e.g., 金属肌),
          set the bound candidate's kind to android.
        """
        # Build list of candidate spans
        cand_list: List[CandidateEntity] = sorted(candidates.values(), key=lambda c: c.start)
        # Pronoun occurrences
        for m in re.finditer(r"(彼女|彼)(の)?", text):
            pron = m.group(1)
            has_no = m.group(2) is not None
            pos = m.start()
            # Find nearest preceding candidate within window
            nearest: Optional[CandidateEntity] = None
            nearest_dist = 10**9
            for ce in cand_list:
                if ce.end <= pos:
                    dist = pos - ce.end
                    if dist < nearest_dist and dist <= 60:
                        nearest = ce
                        nearest_dist = dist
                else:
                    break
            if not nearest:
                continue
            # Assign gender based on pronoun
            if pron == "彼女":
                nearest.gender = "female"
                nearest.confidence = max(nearest.confidence, 0.72)
                if nearest.reasons is not None:
                    nearest.reasons.append("pronoun:彼女->gender")
            elif pron == "彼":
                # Avoid mis-binding when "彼女" exists (this branch only triggers on isolated 彼)
                nearest.gender = nearest.gender or "male"
                if nearest.reasons is not None:
                    nearest.reasons.append("pronoun:彼->gender?")

            # Attribute possession binding
            if has_no:
                lookahead = text[m.end(): m.end() + 24]
                if any(attr in lookahead for attr in self.attribute_phrases_android):
                    nearest.kind = "android"
                    nearest.confidence = max(nearest.confidence, 0.78)
                    if nearest.reasons is not None:
                        nearest.reasons.append("possessive->android")
    
    def _infer_gender(self, text: str, name: str) -> Optional[str]:
        """性別推定: 周辺100-120文字の指示語などから推定。
        注意: 「彼」は「彼女」に含まれるため、まず女性系の長い指標を優先する。
        """
        context_window = 120
        # Exclude ambiguous pronouns here; pronoun-based inference is handled by _bind_pronoun_and_attributes
        female_cues = [c for c in sorted(self.gender_indicators["female"], key=len, reverse=True) if c not in ("彼女",)]
        male_cues = [c for c in sorted(self.gender_indicators["male"], key=len, reverse=True) if c not in ("彼",)]
        for match in re.finditer(re.escape(name), text):
            start = max(0, match.start() - context_window)
            end = min(len(text), match.end() + context_window)
            context = text[start:end]
            # Prefer explicit female cues (non-pronoun)
            if any(cue in context for cue in female_cues):
                return "female"
            # Male cues (non-pronoun)
            if any(cue in context for cue in male_cues):
                return "male"
        return None
    
    def _infer_kind(self, text: str, name: str) -> str:
        """種別推定: 近接パターン優先の文脈一致。
        - 強い属性句（例: 金属肌）は、直近文脈に「<name>の」または性別代名詞所有「彼女の/彼の」がある場合にのみ紐付ける。
        - 一般指示語（アンドロイド等）は単純近接。
        """
        context_window = 120
        inferred: Optional[str] = None
        name_pos = [m for m in re.finditer(re.escape(name), text)]
        for match in name_pos:
            start = max(0, match.start() - context_window)
            end = min(len(text), match.end() + context_window)
            context = text[start:end]
            local = text[max(0, match.start() - 40): min(len(text), match.end() + 40)]

            # Strong attribute phrases: require possessive binding
            has_attr = None
            for ph in self.attribute_phrases_android:
                if ph in local:
                    has_attr = ph
                    break
            if has_attr:
                owner_ok = (f"{name}の" in local) or ("彼女の" in local and (self._infer_gender(text, name) == "female")) or ("彼の" in local and (self._infer_gender(text, name) == "male"))
                if owner_ok:
                    return "android"

            # Generic kind indicators near the name
            for kind, indicators in self.kind_indicators.items():
                if any(ind in local for ind in indicators):
                    inferred = kind
        return inferred or "human"
    
    def _infer_role(self, text: str, name: str) -> Optional[str]:
        """役割推定"""
        # 簡易実装：主人公、相手役など
        first_occurrence = text.find(name)
        if first_occurrence < len(text) * 0.3:
            return "protagonist"
        return "supporting"
    
    def _extract_settings(self, text: str) -> List[Setting]:
        """設定抽出: 固定辞書＋素朴な場所句抽出。"""
        settings: List[Setting] = []
        places: set[str] = set()

        # Predefined places
        for p in self.place_names:
            if p in text:
                places.add(p)

        # Regex for place-like Kanji compounds ending with 地名/場所っぽい接尾辞
        place_like = re.compile(rf"([{KANJI}]{{2,6}})(?:の)?(海岸|港|駅|公園|橋|岬|川|市|町|村)")
        for m in place_like.finditer(text):
            places.add(m.group(1) + m.group(2))

        # Times
        times: set[str] = set()
        times_pattern = re.compile(r"(夕暮れ|朝|昼|夜|夕方|深夜|早朝|午前|午後|[0-9]{1,2}時|夕陽|夕焼け)")
        for m in times_pattern.finditer(text):
            times.add(m.group(1))

        for place in sorted(places):
            time = next(iter(times), None) if times else None
            settings.append(Setting(place=place, time=time))
        return settings
    
    def _extract_relations(self, text: str, characters: List[Character]) -> List[Relation]:
        """関係性抽出"""
        relations = []
        
        if len(characters) < 2:
            return relations
        
        # キャラクター間の関係性を推定
        for i, char1 in enumerate(characters):
            for char2 in characters[i+1:]:
                relation_type = self._infer_relation_type(text, char1.name, char2.name)
                if relation_type:
                    relations.append(Relation(
                        source=char1.name,
                        relation_type=relation_type,
                        target=char2.name,
                        strength=0.8
                    ))
        
        return relations
    
    def _infer_relation_type(self, text: str, name1: str, name2: str) -> Optional[str]:
        """関係性タイプ推定"""
        # 両名前が近くに出現する箇所を分析
        for match1 in re.finditer(re.escape(name1), text):
            for match2 in re.finditer(re.escape(name2), text):
                distance = abs(match1.start() - match2.start())
                if distance < 100:  # 100文字以内
                    context_start = min(match1.start(), match2.start()) - 20
                    context_end = max(match1.end(), match2.end()) + 20
                    context = text[max(0, context_start):min(len(text), context_end)]
                    
                    for relation, pattern in self.relation_patterns.items():
                        if pattern.search(context):
                            return relation.upper()
        
        return "KNOWS"  # デフォルト関係
    
    def _extract_motifs(self, text: str) -> List[Motif]:
        """モチーフ抽出"""
        motifs = []
        
        for category, symbols in self.motif_patterns.items():
            for symbol in symbols:
                if symbol in text:
                    motifs.append(Motif(
                        symbol=symbol,
                        category=category,
                        description=f"{category}系のモチーフ"
                    ))
        
        return motifs
    
    def _convert_to_ui_min_format(self,
                                characters: List[Character],
                                settings: List[Setting], 
                                relations: List[Relation],
                                motifs: List[Motif],
                                base_nodes: List[Dict],
                                base_edges: List[Dict]) -> Dict[str, Any]:
        """UI-Min形式への変換"""
        
        nodes = []
        edges = []
        
        # キャラクターノード
        for char in characters:
            nodes.append({
                "id": char.name.lower(),
                "type": "Character",
                "name": char.name,
                "gender": char.gender,
                "kind": char.kind,
                "role": char.role
            })
        
        # 設定ノード
        for i, setting in enumerate(settings):
            setting_id = f"setting_{i}"
            nodes.append({
                "id": setting_id,
                "type": "Setting", 
                "place": setting.place,
                "time": setting.time
            })
        
        # モチーフノード
        for i, motif in enumerate(motifs):
            motif_id = f"motif_{i}"
            nodes.append({
                "id": motif_id,
                "type": "Motif",
                "symbol": motif.symbol,
                "category": motif.category
            })
        
        # 関係エッジ
        for relation in relations:
            edges.append({
                "src": relation.source.lower(),
                "rel": relation.relation_type,
                "dst": relation.target.lower(),
                "strength": relation.strength
            })
        
        return {
            "nodes": nodes,
            "edges": edges,
            "metadata": {
                "extraction_method": "lna_lang_enhanced",
                "character_count": len(characters),
                "setting_count": len(settings),
                "relation_count": len(relations),
                "motif_count": len(motifs)
            }
        }


# テスト関数
def test_graph_extractor():
    """Graph Extractorのテスト"""
    extractor = GraphExtractor()
    
    # サンプルテキスト（防波堤シーン）
    text = """夕焼けは血のように赤く、防波堤の端で健太と麗華が並ぶ。彼女の金属肌は光を吸い込み、わずかに震える。風が髪を掻きむしった――それは人間らしい、でも彼女にはない、儚い美しさだった。

「今日も、私、あなたと一緒に暮れを見られましたね」と麗華が微笑む。声は機械なのに、心臓の音のように胸に響く。

健太は黙って、その手をそっと握った。夕陽が二人を溶かし、世界は静けさの中、もう一つの未来へと歩き出す。"""
    
    result = extractor.extract_from_text(text)
    
    print("=== GRAPH EXTRACTION TEST ===")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    return result


if __name__ == "__main__":
    test_graph_extractor()