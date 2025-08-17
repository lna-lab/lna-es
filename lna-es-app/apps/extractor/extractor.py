#!/usr/bin/env python3
"""
extractor.py
---------------

This module implements the ingestion pipeline for the LNA‑ES system.  It reads a plain
text file, segments it into sentences and groups of sentences (segments), extracts
simple entities based on salient keywords, assigns random ontology weights, classifies
the document according to the NDC and Kindle schemes and produces both a JSON
artefact and a parameterised Cypher script.  The original text is never stored.

Note that this is a reference implementation intended for demonstration purposes
only.  In production it should be replaced by calls to sophisticated natural
language models and embedding services.
"""

import argparse
import sys
import json
import os
import random
import re
import string
import time
import hashlib
from pathlib import Path
from collections import Counter

# Directory of this script
BASE_DIR = Path(__file__).resolve().parents[2]

# Ensure the project root is on sys.path so that the `apps` package can be found when
# running this module as a script.  Without this adjustment, Python cannot
# resolve absolute package imports when invoked via `python apps/extractor/extractor.py`.
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Load classification dictionaries
NDC_PATH = BASE_DIR / 'classifiers' / 'ndc.json'
KINDLE_PATH = BASE_DIR / 'classifiers' / 'kindle.json'

with open(NDC_PATH, encoding='utf-8') as f:
    NDC_CATEGORIES = json.load(f)

with open(KINDLE_PATH, encoding='utf-8') as f:
    KINDLE_CATEGORIES = json.load(f)

# Define ontology categories (15 dimensions)
ONTOLOGY_CATEGORIES = [
    "philosophy", "history", "science", "technology", "arts",
    "literature", "language", "geography", "education", "psychology",
    "economics", "politics", "culture", "religion", "society"
]

# A very small list of English stopwords.  Extend as needed.
STOPWORDS = {
    'the', 'and', 'for', 'are', 'with', 'that', 'this', 'from', 'have', 'has',
    'were', 'was', 'been', 'their', 'which', 'such', 'into', 'there', 'here',
    'also', 'these', 'some', 'when', 'than', 'then', 'over', 'under', 'while',
    'each', 'other', 'they', 'them', 'our', 'your', 'what', 'where', 'who',
    'will', 'shall', 'would', 'could', 'should'
}

def generate_base_id(length: int = 12) -> str:
    """Generate a random base identifier consisting of alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def tokenize(text: str) -> list:
    """Simple word tokenizer returning lowercase alphanumeric tokens."""
    return re.findall(r"\b\w+\b", text.lower())


def segment_sentences(text: str) -> list:
    """Split raw text into a list of sentences using punctuation and newlines as boundaries."""
    # Replace newlines with spaces to avoid empty tokens
    cleaned = text.replace('\r', ' ').replace('\n', ' ')
    # Split on Japanese full stop, full stop, question mark and exclamation mark
    parts = re.split(r'[。\.\!\?]+\s*', cleaned)
    sentences = [p.strip() for p in parts if p.strip()]
    return sentences


def group_segments(sentences: list, sentences_per_segment: int = 5) -> list:
    """Group sentences into segments of fixed size."""
    segments = []
    for i in range(0, len(sentences), sentences_per_segment):
        segment = sentences[i:i + sentences_per_segment]
        segments.append(segment)
    return segments


def extract_key_terms(text: str, top_n: int = 3) -> list:
    """Extract key terms by simple frequency analysis, ignoring stopwords."""
    tokens = tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    if not tokens:
        return []
    counts = Counter(tokens)
    return [word for word, _ in counts.most_common(top_n)]


def classify_document(tokens: list, categories: list, key_field: str, label_field: str) -> list:
    """Compute weighted classification scores based on keyword overlaps.

    Args:
        tokens: list of tokens from the document
        categories: list of category dicts containing a label and keywords
        key_field: name of the field containing the category code/label
        label_field: name of the field containing the list of keywords

    Returns:
        A list of the top three categories with normalised scores.
    """
    scores = {}
    total = 0
    token_set = set(tokens)
    for item in categories:
        name = item[key_field]
        keywords = item['keywords']
        # Count how many category keywords appear in the document
        score = sum(1 for kw in keywords if kw.lower() in token_set)
        scores[name] = score
        total += score
    # Normalise; if total is zero assign uniform weights
    if total == 0:
        n = len(scores)
        for k in scores:
            scores[k] = 1.0 / n
    else:
        for k in scores:
            scores[k] = scores[k] / total
    # Select top 3
    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    return [{key_field: code, 'score': weight} for code, weight in top3]


def assign_ontology_weights() -> dict:
    """Assign a random distribution across the 15 ontology categories."""
    weights = [random.random() for _ in ONTOLOGY_CATEGORIES]
    total = sum(weights)
    return {ONTOLOGY_CATEGORIES[i]: weights[i] / total for i in range(len(ONTOLOGY_CATEGORIES))}


def embed_vector(dim: int) -> list:
    """Return a random embedding vector of given dimension."""
    return [random.random() for _ in range(dim)]


def ingest_file(input_path: str, out_dir: str, data_dir: str, vector_dim: int = 16) -> str:
    """Top level ingestion function.  Returns the generated work base id."""
    with open(input_path, encoding='utf-8', errors='ignore') as f:
        text = f.read()
    # Compute fingerprint (SHA256) of original text
    fingerprint = hashlib.sha256(text.encode('utf-8')).hexdigest()
    # Tokenise entire document for classification
    tokens = tokenize(text)
    ndc_results = classify_document(tokens, NDC_CATEGORIES, key_field='code', label_field='keywords')
    kindle_results = classify_document(tokens, KINDLE_CATEGORIES, key_field='category', label_field='keywords')
    # Generate base id for the work
    work_base = generate_base_id()
    # Segment sentences and group into segments
    sentences = segment_sentences(text)
    sentence_groups = group_segments(sentences, sentences_per_segment=5)
    # Prepare structures
    segments_data = []
    sentences_data = []
    entity_map = {}  # keyed by lower case label
    mentions_data = []
    sentence_index = 0
    # Process each segment
    for seg_idx, group in enumerate(sentence_groups):
        segment_id = f"{work_base}_seg{seg_idx:03d}"
        # Compute key terms for the segment (using all sentences in the group)
        key_terms = extract_key_terms(' '.join(group), top_n=5)
        # Prepare list of sentence ids for this segment
        sent_ids = []
        for local_idx, sentence in enumerate(group):
            sentence_id = f"{work_base}_sen{sentence_index:04d}"
            sent_ids.append(sentence_id)
            # Random ontology scores for the sentence
            onto_scores = assign_ontology_weights()
            # Sentence record (we do not keep original text) – onto scores only
            sentences_data.append({
                'sentenceId': sentence_id,
                'order': sentence_index,
                'ontoScores': onto_scores,
                'aesthetic': None,
                'vectorDim': vector_dim,
                'embeddingRef': '',
            })
            # Extract simple entities: top 3 terms from this sentence
            ent_terms = extract_key_terms(sentence, top_n=3)
            for term in ent_terms:
                key = term.lower()
                if key not in entity_map:
                    ent_id = f"{work_base}_ent{len(entity_map):04d}"
                    entity_map[key] = {
                        'entityId': ent_id,
                        'label': term,
                        'type': 'concept',
                        'ontoWeights': assign_ontology_weights(),
                        'vec_ruri_v3': embed_vector(vector_dim),
                        'vec_qwen3_0p6b': embed_vector(vector_dim),
                    }
                entity = entity_map[key]
                # Determine ontoKey as the maximum weight key
                onto_key = max(entity['ontoWeights'], key=lambda k: entity['ontoWeights'][k])
                mentions_data.append({
                    'sentenceId': sentence_id,
                    'entityId': entity['entityId'],
                    'tag': term,
                    'ontoKey': onto_key,
                    'weight': 1.0
                })
            sentence_index += 1
        # Add segment data
        segments_data.append({
            'segmentId': segment_id,
            'order': seg_idx,
            'timecode_ms': seg_idx * 1000,
            'key_terms': key_terms,
            'length_hint': len(group),
            'sentences': sent_ids
        })
    # Note: Dominant ontology per segment is not computed in this reference implementation.
    # Write JSON artefact to data directory
    os.makedirs(data_dir, exist_ok=True)
    data_path = Path(data_dir) / f"{work_base}.json"
    json_data = {
        'work': {
            'workBase': work_base,
            'title': os.path.basename(input_path),
            'sourceType': 'local',
            'ingestedAt': int(time.time() * 1000),
            'fingerprint': fingerprint,
            'language': 'unknown',
            'lengthHint': len(tokens),
            'ndc': ndc_results,
            'kindle': kindle_results
        },
        'segments': segments_data,
        'sentences': sentences_data,
        'entities': list(entity_map.values()),
        'mentions': mentions_data
    }
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    # Produce Cypher file
    out_path = Path(out_dir)
    os.makedirs(out_path, exist_ok=True)
    cypher_file = out_path / f"{work_base}.cypher"
    from apps.importer.importer import generate_cypher
    generate_cypher(json_data, cypher_file)
    return work_base


def main() -> None:
    parser = argparse.ArgumentParser(description='Ingest a text file and produce graph artefacts.')
    parser.add_argument('--input', required=True, help='Path to the input .txt file')
    parser.add_argument('--outdir', default='out', help='Directory for Cypher output')
    parser.add_argument('--datadir', default='data', help='Directory for JSON artefacts')
    parser.add_argument('--vector-dim', type=int, default=16, help='Embedding dimension (default: 16)')
    args = parser.parse_args()
    work_id = ingest_file(args.input, args.outdir, args.datadir, vector_dim=args.vector_dim)
    print(f"Ingestion complete. Work ID: {work_id}")


if __name__ == '__main__':
    main()