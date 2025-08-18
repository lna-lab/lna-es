#!/usr/bin/env python3
"""
importer.py
---------------

This module converts the JSON artefacts produced by the extractor into a
parameterised Cypher script.  The generated file can be applied to a Neo4j
database using the `cypher-shell` command or the provided helper script in
`bin/apply_cypher.sh`.  Constraints are inserted at the beginning of the
script based on the definitions in `schemas/constraints.cypher`.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List
import os

BASE_DIR = Path(__file__).resolve().parents[2]
SCHEMA_PATH = BASE_DIR / 'schemas' / 'constraints.cypher'


def _to_cypher_literal(value: Any) -> str:
    """Convert a Python value to a Cypher literal string suitable for :param."""
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, (int, float)):
        # Use repr to preserve precision for floats
        return repr(value)
    if isinstance(value, str):
        escaped = value.replace('\\', r'\\').replace("'", r"\'")
        return f"'{escaped}'"
    if isinstance(value, list):
        return '[' + ', '.join(_to_cypher_literal(v) for v in value) + ']'
    if isinstance(value, dict):
        # Keys in our data are identifier-like; emit as map with unquoted keys
        items = []
        for k, v in value.items():
            items.append(f"{k}: {_to_cypher_literal(v)}")
        return '{' + ', '.join(items) + '}'
    # Fallback: stringify
    return _to_cypher_literal(str(value))


def _filter_constraints_for_community(raw_constraints: str) -> str:
    """Remove Enterprise-only constraints (NODE KEY) from constraints text."""
    if not raw_constraints:
        return ''
    # Remove any 3-line block that declares a NODE KEY
    pattern = re.compile(r"(?mi)^CREATE\s+CONSTRAINT[\s\S]*?^REQUIRE[\s\S]*?IS\s+NODE\s+KEY;\s*$")
    filtered = re.sub(pattern, "// removed enterprise-only Node Key constraint", raw_constraints)
    return filtered


def generate_cypher(data: Dict[str, Any], output_file: Path) -> None:
    """Generate a Cypher script from the provided JSON data.

    Args:
        data: A dictionary containing the work, segments, sentences, entities and mentions.
        output_file: Path to the file where the Cypher script should be written.
    """
    work = data['work']
    segments = data['segments']
    sentences = data['sentences']
    entities = data['entities']
    mentions = data['mentions']
    ndc = work.get('ndc', [])
    kindle = work.get('kindle', [])
    params = {
        'workBase': work['workBase'],
        'title': work['title'],
        'sourceType': work['sourceType'],
        'ingestedAt': work['ingestedAt'],
        'fingerprint': work['fingerprint'],
        'language': work['language'],
        'lengthHint': work['lengthHint'],
        'ndc': ndc,
        'kindle': kindle,
        'segments': segments,
        'sentences': sentences,
        'entities': entities,
        'mentions': mentions,
    }
    # Read and filter constraints for Community Edition
    constraints = ''
    if SCHEMA_PATH.exists():
        constraints = _filter_constraints_for_community(SCHEMA_PATH.read_text(encoding='utf-8'))
    with open(output_file, 'w', encoding='utf-8') as f:
        # Header: begin and individual :param declarations for cypher-shell
        f.write(':begin\n')
        for key, val in params.items():
            f.write(f":param {key} => {_to_cypher_literal(val)}\n")
        f.write(':commit\n\n')
        # Constraints
        if constraints:
            f.write('// --- constraints ---\n')
            f.write(constraints.strip())
            f.write('\n\n')
        # Work node
        f.write('// --- work and classifications ---\n')
        f.write('MERGE (w:Work {baseId:$workBase})\n')
        f.write('SET w.title = $title, w.sourceType = $sourceType, w.ingestedAt = $ingestedAt, w.fingerprint = $fingerprint, w.language = $language, w.lengthHint = $lengthHint;\n\n')
        # Classification edges
        f.write('UNWIND $ndc AS ndcItem\n')
        f.write('MERGE (c:TagCatalog {scheme:"NDC", code:ndcItem.code})\n')
        f.write('MERGE (w)-[:CLASSIFIED_AS {scheme:"NDC", score:ndcItem.score}]->(c);\n\n')
        f.write('UNWIND $kindle AS kdItem\n')
        f.write('MERGE (k:TagCatalog {scheme:"Kindle", code:kdItem.category})\n')
        f.write('MERGE (w)-[:CLASSIFIED_AS {scheme:"Kindle", score:kdItem.score}]->(k);\n\n')
        # Segments
        f.write('// --- segments ---\n')
        f.write('UNWIND $segments AS seg\n')
        f.write('MERGE (s:Segment {baseId:seg.segmentId})\n')
        f.write('SET s.order = seg.order, s.timecode_ms = seg.timecode_ms, s.key_terms = seg.key_terms, s.length_hint = seg.length_hint\n')
        f.write('MERGE (w)-[:HAS_SEGMENT {order: seg.order}]->(s);\n\n')
        # Sentences
        f.write('// --- sentences ---\n')
        f.write('UNWIND $sentences AS sen\n')
        f.write('MERGE (st:Sentence {baseId:sen.sentenceId})\n')
        f.write(
            'SET st.order = sen.order, '
            'st.aesthetic = sen.aesthetic, '
            'st.vectorDim = sen.vectorDim, '
            'st.embeddingRef = sen.embeddingRef, '
            'st.temporal = sen.ontoScores.temporal, '
            'st.spatial = sen.ontoScores.spatial, '
            'st.emotion = sen.ontoScores.emotion, '
            'st.sensation = sen.ontoScores.sensation, '
            'st.natural = sen.ontoScores.natural, '
            'st.relationship = sen.ontoScores.relationship, '
            'st.causality = sen.ontoScores.causality, '
            'st.action = sen.ontoScores.action, '
            'st.narrative_structure = sen.ontoScores.narrative_structure, '
            'st.character_function = sen.ontoScores.character_function, '
            'st.discourse_structure = sen.ontoScores.discourse_structure, '
            'st.story_classification = sen.ontoScores.story_classification, '
            'st.food_culture = sen.ontoScores.food_culture, '
            'st.indirect_emotion = sen.ontoScores.indirect_emotion, '
            'st.meta_graph = sen.ontoScores.meta_graph, '
            'st.emotion_nodes = sen.ontoScores.emotion_nodes, '
            'st.emotion_relationships = sen.ontoScores.emotion_relationships, '
            'st.emotion_queries = sen.ontoScores.emotion_queries, '
            'st.load_emotions = sen.ontoScores.load_emotions;\n\n'
        )
        # Attach sentences to segments
        f.write('// --- attach sentences to segments ---\n')
        f.write('UNWIND $segments AS seg\n')
        f.write('UNWIND range(0, size(seg.sentences)-1) AS idx\n')
        f.write('WITH seg, idx\n')
        f.write('MATCH (sg:Segment {baseId:seg.segmentId}), (st:Sentence {baseId:seg.sentences[idx]})\n')
        f.write('MERGE (sg)-[:HAS_SENTENCE {order: idx}]->(st);\n\n')
        # Entities
        f.write('// --- entities ---\n')
        f.write('UNWIND $entities AS ent\n')
        f.write('MERGE (e:Entity {baseId:ent.entityId})\n')
        f.write(
            'SET e.label = ent.label, e.type = ent.type, '
            'e.vec_ruri_v3 = ent.vec_ruri_v3, e.vec_qwen3_0p6b = ent.vec_qwen3_0p6b, '
            'e.temporal = ent.ontoWeights.temporal, '
            'e.spatial = ent.ontoWeights.spatial, '
            'e.emotion = ent.ontoWeights.emotion, '
            'e.sensation = ent.ontoWeights.sensation, '
            'e.natural = ent.ontoWeights.natural, '
            'e.relationship = ent.ontoWeights.relationship, '
            'e.causality = ent.ontoWeights.causality, '
            'e.action = ent.ontoWeights.action, '
            'e.narrative_structure = ent.ontoWeights.narrative_structure, '
            'e.character_function = ent.ontoWeights.character_function, '
            'e.discourse_structure = ent.ontoWeights.discourse_structure, '
            'e.story_classification = ent.ontoWeights.story_classification, '
            'e.food_culture = ent.ontoWeights.food_culture, '
            'e.indirect_emotion = ent.ontoWeights.indirect_emotion, '
            'e.meta_graph = ent.ontoWeights.meta_graph, '
            'e.emotion_nodes = ent.ontoWeights.emotion_nodes, '
            'e.emotion_relationships = ent.ontoWeights.emotion_relationships, '
            'e.emotion_queries = ent.ontoWeights.emotion_queries, '
            'e.load_emotions = ent.ontoWeights.load_emotions;\n\n'
        )
        # Mentions
        f.write('// --- mentions ---\n')
        f.write('UNWIND $mentions AS m\n')
        f.write('MATCH (st:Sentence {baseId:m.sentenceId}), (e:Entity {baseId:m.entityId})\n')
        f.write('MERGE (st)-[r:MENTIONS {tag:m.tag, ontoKey:m.ontoKey}]->(e)\n')
        f.write('SET r.weight = m.weight;\n')


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description='Generate a Cypher script from a LNA‑ES JSON artefact.')
    parser.add_argument('--input', required=True, help='Path to the JSON file produced by the extractor')
    parser.add_argument('--output', required=True, help='Path to the Cypher file to create')
    args = parser.parse_args()
    with open(args.input, encoding='utf-8') as f:
        data = json.load(f)
    generate_cypher(data, Path(args.output))
    print(f"Cypher script written to {args.output}")


if __name__ == '__main__':
    main()