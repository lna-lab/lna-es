"""
create_graph.py
=================

This script reads a UTF‑8 text file and converts its contents into a set of
Cypher statements suitable for import into graph databases such as Neo4j.
Each Japanese sentence becomes a node labelled `Sentence`, with an `id` and
`text` property.  A `NEXT` relationship connects each sentence to the one
that follows it.  This representation preserves the original order of the
manuscript and allows the text to be reconstructed verbatim by traversing
the `NEXT` relationships in order.

Usage:
    python create_graph.py --input seaside_love_story.txt --output graph.cypher

The resulting `graph.cypher` file will contain Cypher `CREATE` statements for
all nodes and relationships.  You can load this file into Neo4j by pasting
its contents into the Neo4j browser or by using the `neo4j-admin import` tool.
"""

import argparse
import json
import re
from typing import List, Tuple, Dict, Optional, Union


def read_text(path: str) -> str:
    """Read a UTF-8 encoded text file and return its content as a string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_into_sentences(text: str) -> List[str]:
    """
    Split Japanese text into sentences by looking for the full stop
    character (。).  The delimiter is kept at the end of each sentence to
    preserve punctuation in the graph representation.

    We also handle newlines: continuous lines are joined before splitting so
    that sentences spanning multiple lines remain intact.  Empty lines are
    ignored.
    """
    # Normalize newlines
    normalized = text.replace("\r\n", "\n").strip()
    # Remove blank lines and join the remaining lines without separators
    lines = [line.strip() for line in normalized.split("\n") if line.strip()]
    joined = "".join(lines)
    # Split on Japanese full stop while keeping the delimiter
    parts = re.split(r"(。)", joined)
    sentences: List[str] = []
    for i in range(0, len(parts), 2):
        fragment = parts[i].strip()
        delimiter = parts[i + 1] if i + 1 < len(parts) else ""
        if fragment or delimiter:
            sentences.append(fragment + delimiter)
    return sentences


def generate_cypher(
    sentences: List[str], extra_props: Optional[List[Dict[str, Union[str, float]]]] = None
) -> Tuple[str, str]:
    """
    Generate Cypher statements to create sentence nodes and NEXT relationships.

    If `extra_props` is provided, it should be a list of dictionaries of the
    same length as `sentences`.  Each dictionary will be merged into the
    properties of the corresponding sentence node.

    Returns a tuple of two strings: the node statements and the relationship
    statements.  The statements are separated because Neo4j expects all
    nodes to be created before relationships referencing them.
    """
    node_statements: List[str] = []
    rel_statements: List[str] = []
    for idx, sentence in enumerate(sentences, start=1):
        # Escape single quotes by doubling them per Cypher syntax
        escaped = sentence.replace("'", "''")
        # Start building property assignments with id and text
        props_list = [f"id: {idx}", f"text: '{escaped}'"]
        if extra_props and idx - 1 < len(extra_props):
            for key, value in extra_props[idx - 1].items():
                # Escape value if string
                if isinstance(value, str):
                    escaped_val = value.replace("'", "''")
                    props_list.append(f"{key}: '{escaped_val}'")
                else:
                    props_list.append(f"{key}: {value}")
        props_str = ", ".join(props_list)
        node_statements.append(
            f"CREATE (s{idx}:Sentence {{{props_str}}});"
        )
        if idx > 1:
            rel_statements.append(
                f"CREATE (s{idx - 1})-[:NEXT]->(s{idx});"
            )
    return "\n".join(node_statements), "\n".join(rel_statements)


def load_characters(path: str) -> Dict[str, Dict[str, str]]:
    """
    Load a JSON file containing character definitions.

    The JSON should be a mapping from character names to a dictionary of
    properties, for example:

        {
          "健太": {"type": "human"},
          "麗華": {"type": "android"}
        }

    Returns the parsed dictionary.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Ensure each value is a dict
    for name, props in data.items():
        if not isinstance(props, dict):
            data[name] = {"type": str(props)}
    return data


def load_emotions(path: str) -> Dict[str, str]:
    """
    Load a JSON file containing emotion definitions.

    The JSON should map emotion keywords (words or phrases) to a category
    label.  For example:

        {
          "愛": "love",
          "恥じらい": "embarrassment",
          "心配": "worry"
        }

    Returns the parsed dictionary.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_character_statements(
    sentences: List[str], characters: Dict[str, Dict[str, str]]
) -> Tuple[List[str], List[str], Dict[str, str]]:
    """
    Generate Cypher statements for Character nodes and APPEARS_IN relationships.

    For each character in the provided dictionary, a `Character` node is
    created.  For each sentence containing the character's name, an
    `APPEARS_IN` relationship is created from the character to that sentence.
    """
    char_nodes: List[str] = []
    rels: List[str] = []
    var_map: Dict[str, str] = {}
    # Assign unique variable names to characters (c1, c2, ...)
    for idx, (name, props) in enumerate(characters.items(), start=1):
        alias = f"c{idx}"
        var_map[name] = alias
        # Escape single quotes in name and any properties
        escaped_name = name.replace("'", "''")
        prop_pairs: List[str] = []
        for key, value in props.items():
            val_str = str(value).replace("'", "''")
            prop_pairs.append(f"{key}: '{val_str}'")
        props_str = ", ".join(prop_pairs)
        char_nodes.append(
            f"CREATE ({alias}:Character {{name: '{escaped_name}', {props_str}}});"
        )
        # For each sentence, check if name appears
        for s_idx, sentence in enumerate(sentences, start=1):
            if name in sentence:
                rels.append(
                    f"CREATE ({alias})-[:APPEARS_IN]->(s{s_idx});"
                )
    return char_nodes, rels, var_map


def generate_emotion_statements(
    sentences: List[str],
    emotions: Dict[str, str],
    char_var_map: Dict[str, str],
) -> Tuple[List[str], List[str]]:
    """
    Generate Cypher statements for Emotion nodes and their relationships.

    For each unique emotion keyword in the mapping, an `Emotion` node is
    created with properties `word` (the keyword) and `category` (the mapped
    category name).  When an emotion keyword appears in a sentence, a
    `HAS_EMOTION` relationship is created from the sentence node to the
    emotion node.  Additionally, for each character appearing in the same
    sentence (based on `char_var_map`), a `FEELS` relationship is created
    from the character node to the emotion node.
    """
    emotion_nodes: List[str] = []
    rels: List[str] = []
    # Map emotion keyword to variable alias
    emotion_alias_map: Dict[str, str] = {}
    next_emotion_id = 1

    for word, category in emotions.items():
        # Assign variable name for this emotion
        alias = f"e{next_emotion_id}"
        next_emotion_id += 1
        emotion_alias_map[word] = alias
        # Escape properties
        escaped_word = word.replace("'", "''")
        escaped_category = str(category).replace("'", "''")
        emotion_nodes.append(
            f"CREATE ({alias}:Emotion {{word: '{escaped_word}', category: '{escaped_category}'}});"
        )
    # For each sentence, check if it contains any emotion keyword
    for s_idx, sentence in enumerate(sentences, start=1):
        for word, alias in emotion_alias_map.items():
            if word in sentence:
                # Relationship from sentence to emotion
                rels.append(f"CREATE (s{s_idx})-[:HAS_EMOTION]->({alias});")
                # For each character that appears in this sentence, create FEELS relationship
                for name, char_alias in char_var_map.items():
                    if name in sentence:
                        rels.append(f"CREATE ({char_alias})-[:FEELS]->({alias});")
    return emotion_nodes, rels


def tokenize_japanese(text: str) -> List[str]:
    """
    A naive tokenizer for Japanese text used to approximate semantic similarity.
    This function extracts sequences of Kanji, Hiragana, Katakana, and Latin letters
    as tokens using a regular expression.  It is not a full morphological
    analyzer but provides a simple basis for Jaccard similarity.
    """
    import re

    # Match sequences of Japanese characters or ASCII letters
    return re.findall(r"[一-龯ぁ-んァ-ンーa-zA-Z]+", text)


def generate_semantic_relations(
    sentences: List[str], threshold: float = 0.3
) -> List[str]:
    """
    Generate Cypher statements for semantic relationships between sentences.

    For each pair of sentences, compute a Jaccard similarity between token
    sets.  If the similarity exceeds `threshold`, create a `SEMANTIC_RELATES`
    relationship with a `strength` property equal to the similarity score
    rounded to three decimals and `type` set to 'similarity'.
    """
    rels: List[str] = []
    # Pre-tokenize all sentences
    token_sets = [set(tokenize_japanese(s)) for s in sentences]
    n = len(sentences)
    for i in range(n):
        for j in range(i + 1, n):
            tokens_i = token_sets[i]
            tokens_j = token_sets[j]
            if not tokens_i or not tokens_j:
                continue
            intersection = tokens_i & tokens_j
            union = tokens_i | tokens_j
            score = len(intersection) / len(union)
            if score >= threshold:
                rels.append(
                    f"CREATE (s{i + 1})-[:SEMANTIC_RELATES {{strength: {round(score, 3)}, type: 'similarity'}}]->(s{j + 1});"
                )
    return rels


def analyze_cta_layers(sentence: str) -> Dict[str, float]:
    """
    Perform a simplified Contextual Textual Analysis (CTA) across multiple layers.

    The analysis uses predefined keyword patterns and weights to compute a
    normalized score for each layer.  The algorithm normalizes the score by
    sentence length and applies additional boosts based on the number of
    matching keywords and the layer's importance.

    Returns a dictionary mapping layer names to scores between 0.0 and 1.2.
    """
    import re

    analysis_patterns = {
        # Foundation Layer (基盤レイヤー)
        "temporal": {
            "keywords": ["時", "瞬間", "永遠", "昔", "今", "未来", "朝", "夜", "春", "秋"],
            "weight": 2.5,
        },
        "spatial": {
            "keywords": ["海", "空", "庭", "部屋", "街", "道", "橋", "山", "川"],
            "weight": 2.0,
        },
        "emotion": {
            "keywords": ["愛", "悲しみ", "喜び", "怒り", "恐れ", "驚き", "恥じらい"],
            "weight": 3.5,
        },
        # Relational Layer (関係レイヤー)
        "relationship": {
            "keywords": ["彼", "彼女", "二人", "一緒", "別れ", "出会い", "友達", "恋人"],
            "weight": 3.5,
        },
        "causality": {
            "keywords": ["だから", "なぜなら", "ため", "結果", "原因", "理由"],
            "weight": 2.8,
        },
        "action": {
            "keywords": ["歩く", "見る", "話す", "触れる", "抱く", "笑う", "泣く"],
            "weight": 3.5,
        },
        # Structural Layer (構造レイヤー)
        "narrative": {
            "keywords": ["物語", "話", "語る", "伝える", "思い出", "記憶", "夢"],
            "weight": 2.2,
        },
        "character": {
            "keywords": ["性格", "心", "魂", "人格", "個性", "本質"],
            "weight": 2.8,
        },
        "discourse": {
            "keywords": ["言葉", "声", "語り", "表現", "意味", "象徴"],
            "weight": 2.0,
        },
        # Cultural Layer (文化レイヤー)
        "linguistic_style": {
            "keywords": ["美しい", "優雅", "繊細", "上品", "古風", "現代的"],
            "weight": 1.8,
        },
        "story_classification": {
            "keywords": ["恋愛", "悲劇", "喜劇", "ドラマ", "ファンタジー", "現実"],
            "weight": 1.5,
        },
        # Advanced Layer (高度レイヤー)
        "indirect_emotion": {
            "keywords": ["雰囲気", "気配", "予感", "余韻", "微妙", "奥深い"],
            "weight": 4.0,
        },
        "metaphysical": {
            "keywords": ["存在", "真実", "現実", "幻想", "意識", "精神", "魂"],
            "weight": 5.0,
        },
    }

    scores: Dict[str, float] = {}
    sentence_length = len(sentence)
    for layer, config in analysis_patterns.items():
        raw_score = 0.0
        keyword_count = 0
        for keyword in config["keywords"]:
            if keyword in sentence:
                # context boost: if punctuation around keyword
                context_boost = 1.0
                if re.search(f"[。、]{keyword}|{keyword}[。、]", sentence):
                    context_boost = 1.3
                raw_score += config["weight"] * context_boost
                keyword_count += 1
        # Normalize by sentence length and apply aesthetic boosts
        if sentence_length > 0:
            normalized_score = (raw_score / sentence_length) * 100
            # Boost for multiple keywords
            if keyword_count > 1:
                normalized_score *= 1.2
            # Boost for deep layers
            if layer in ["metaphysical", "indirect_emotion"]:
                normalized_score *= 1.1
            scores[layer] = min(round(normalized_score, 3), 1.2)
        else:
            scores[layer] = 0.0
    return scores


def calculate_aesthetic_beauty(sentence: str, cta_scores: Dict[str, float]) -> float:
    """
    Compute an aesthetic quality score based on CTA layer scores and sentence
    properties.  This function applies weighted combinations and booster
    conditions inspired by the "文芸界最強AI" aesthetics.
    """
    # Base factors
    beauty_factors = {
        "metaphysical_depth": cta_scores.get("metaphysical", 0.0) * 0.3,
        "emotional_resonance": cta_scores.get("emotion", 0.0) * 0.25,
        "indirect_subtlety": cta_scores.get("indirect_emotion", 0.0) * 0.2,
        "narrative_elegance": cta_scores.get("narrative", 0.0) * 0.15,
        "relational_harmony": cta_scores.get("relationship", 0.0) * 0.1,
    }
    base_beauty = sum(beauty_factors.values())
    # Aesthetic boosts
    if "美しい" in sentence or "愛" in sentence:
        base_beauty *= 1.15
    # Optimal length boost
    if 30 < len(sentence) < 100:
        base_beauty *= 1.1
    return min(round(base_beauty, 3), 1.0)


def write_cypher_file(statements: List[str], out_path: str) -> None:
    """Write a list of Cypher statements to the given output path."""
    with open(out_path, "w", encoding="utf-8") as f:
        for stmt in statements:
            if stmt:
                f.write(stmt)
                if not stmt.endswith("\n"):
                    f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a text file into a Cypher graph.")
    parser.add_argument("--input", required=True, help="Path to the input text file (UTF-8).")
    parser.add_argument("--output", required=True, help="Path to the output Cypher file.")
    parser.add_argument(
        "--characters",
        help="Optional path to a JSON file defining characters. Adds Character nodes and APPEARS_IN relationships.",
    )
    parser.add_argument(
        "--emotions",
        help="Optional path to a JSON file defining emotions. Adds Emotion nodes and relationships.",
    )
    parser.add_argument(
        "--semantic",
        action="store_true",
        help="If set, compute semantic similarity relations between sentences.",
    )

    parser.add_argument(
        "--cta",
        action="store_true",
        help=(
            "If set, perform CTA (Contextual Textual Analysis) on each sentence "
            "and embed the resulting layer scores, dominant layer and aesthetic "
            "quality as properties on Sentence nodes."
        ),
    )
    args = parser.parse_args()

    text = read_text(args.input)
    sentences = split_into_sentences(text)
    if not sentences:
        raise SystemExit("No sentences were found in the input text.")

    # Prepare extra properties for sentences (emotion metrics) if needed
    extra_props: List[Dict[str, str | float]] = [{} for _ in sentences]
    loaded_emotions: Dict[str, str] = {}
    if args.emotions:
        loaded_emotions = load_emotions(args.emotions)
        # Analyze each sentence for emotion strength and dominant emotion
        for idx, sentence in enumerate(sentences):
            counts: Dict[str, int] = {}
            total_occurrences = 0
            for word, category in loaded_emotions.items():
                if word in sentence:
                    counts[category] = counts.get(category, 0) + 1
                    total_occurrences += 1
            if total_occurrences > 0:
                dominant = max(counts.items(), key=lambda x: x[1])[0]
                strength = total_occurrences / max(len(sentence), 1)
                extra_props[idx]["emotion_strength"] = round(strength, 3)
                extra_props[idx]["dominant_emotion"] = dominant
            else:
                extra_props[idx]["emotion_strength"] = 0.0
                extra_props[idx]["dominant_emotion"] = "none"

    # If CTA flag is set, compute CTA layer scores and attach them to sentences
    if getattr(args, "cta", False):
        for idx, sentence in enumerate(sentences):
            cta_scores = analyze_cta_layers(sentence)
            if cta_scores:
                dominant_layer, max_score = max(cta_scores.items(), key=lambda item: item[1])
            else:
                dominant_layer, max_score = ("none", 0.0)
            aesthetic_quality = calculate_aesthetic_beauty(sentence, cta_scores)
            for layer_name, score in cta_scores.items():
                extra_props[idx][f"cta_{layer_name}"] = score
            extra_props[idx]["dominant_layer"] = dominant_layer
            extra_props[idx]["layer_strength"] = max_score
            extra_props[idx]["aesthetic_quality"] = aesthetic_quality

    # Generate sentence nodes and NEXT relationships with extra properties
    node_str, rel_str = generate_cypher(sentences, extra_props)
    # Split node and rel strings into lists for easier combination
    nodes = [line for line in node_str.split("\n") if line.strip()]
    rels = [line for line in rel_str.split("\n") if line.strip()]

    # If character definitions are provided, load and generate their nodes and relationships
    char_var_map: Dict[str, str] = {}
    if args.characters:
        characters = load_characters(args.characters)
        char_nodes, char_rels, char_var_map = generate_character_statements(sentences, characters)
        nodes.extend(char_nodes)
        rels.extend(char_rels)

    # If emotion definitions are provided, generate emotion nodes and relationships
    if args.emotions:
        emotion_nodes, emotion_rels = generate_emotion_statements(sentences, loaded_emotions, char_var_map)
        nodes.extend(emotion_nodes)
        rels.extend(emotion_rels)

    # If semantic flag is set, compute semantic relations
    if getattr(args, "semantic", False):
        semantic_rels = generate_semantic_relations(sentences)
        rels.extend(semantic_rels)

    # Combine all statements: nodes first, then relationships
    all_statements = nodes + rels
    write_cypher_file(all_statements, args.output)
    print(f"Graph with {len(sentences)} sentences created at {args.output}")


if __name__ == "__main__":
    main()