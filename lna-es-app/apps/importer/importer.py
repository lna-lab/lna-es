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
from pathlib import Path
from typing import Dict, Any, List
import os

BASE_DIR = Path(__file__).resolve().parents[2]
SCHEMA_PATH = BASE_DIR / 'schemas' / 'constraints.cypher'


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
    # Read constraints
    constraints = ''
    if SCHEMA_PATH.exists():
        constraints = SCHEMA_PATH.read_text(encoding='utf-8')
    with open(output_file, 'w', encoding='utf-8') as f:
        # Header: begin and params
        f.write(':begin\n')
        # Write params as JSON inside :params
        json_params = json.dumps(params, ensure_ascii=False)
        f.write(f":params {json_params}\n")
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
        f.write('SET st.order = sen.order, st.ontoScores = sen.ontoScores, st.aesthetic = sen.aesthetic, st.vectorDim = sen.vectorDim, st.embeddingRef = sen.embeddingRef;\n\n')
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
        f.write('SET e.label = ent.label, e.type = ent.type, e.ontoWeights = ent.ontoWeights, e.vec_ruri_v3 = ent.vec_ruri_v3, e.vec_qwen3_0p6b = ent.vec_qwen3_0p6b;\n\n')
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