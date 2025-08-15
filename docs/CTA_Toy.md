# CTA Toy (demo-only)

This repo ships a tiny demonstration of a "CTA-like" pipeline to show how ontologies can influence analysis without prescribing any particular engine.

- Goal: illustrate the direction only. Do not rely on the toy for production quality.
- In LNA-ES core, ontologies are optional and engine-agnostic. Real CTA/Extractor implementations live outside the core (dialects/engines).

## Sample ontology

We provide a minimal sample ontology file to make the demo tangible:

- `ontology/local_geo_nature.yaml` — contains handful of terms like 湘南/海/夕暮れ and light associations

You are expected to replace it with your own domain ontologies in real projects.

## Commands

1. Analyze text with ontology-assisted scoring (toy):

```bash
python -m lna_es.cli cta analyze -i runs/sample_text.txt -o runs/cta.json --ontology-dir ontology
```

2. Convert scores to a toy graph of Segment nodes at a threshold:

```bash
python -m lna_es.cli cta to-graph -i runs/cta.json -o runs/cta_graph.json --threshold 0.2
```

Result: segments whose score >= threshold become Segment nodes. No edges are created in the toy.

## Why this design

- Keep LNA-ES core minimal and provider-neutral
- Let dialects and engines implement the real CTA/Extractor logic (co-reference, relation induction, ontology weighting)
- Offer only a tiny sample ontology + toy CTA here so users can see the knobs without being constrained
