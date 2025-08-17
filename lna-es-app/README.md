# LNA-ES Application

This repository contains a reference implementation of the **Living Neural Architecture – Enhanced System (LNA‑ES)** pipeline.  The goal of the project is to ingest arbitrary text files, classify them according to the Nippon Decimal Classification (NDC) and Kindle genre schemes, extract high‑level entities and relations, assign ontology weights, generate random vector embeddings, and finally produce Neo4j Cypher scripts and auxiliary data suitable for storing the resulting knowledge graph.  The system does **not** store any of the original source text; instead, only abstracted information (key terms, entities, tags, embeddings and classification weights) is persisted.  Restoring a human‑readable synopsis from the graph is supported via a simple summarisation module.

The code here is designed as a starting point for experimentation.  It demonstrates the end‑to‑end flow described in the accompanying requirements document (`docs/requirements.md`) but deliberately uses simple heuristics and random embeddings in place of heavy natural‑language models.  In a production environment these components should be replaced by calls to proper large language models and embedding services.

## Repository structure

```
├── apps/
│   ├── extractor/         # Ingests raw text, segments sentences, extracts entities and prepares data structures
│   ├── importer/          # Generates Cypher scripts from the extracted data
│   ├── restorer/          # Reconstructs a summary from stored key terms
│   └── evaluator/         # Compares restored summaries with original texts
├── classifiers/           # Classification dictionaries for NDC and Kindle genres
├── schemas/               # Neo4j constraint and index definitions
├── bin/                   # Helper scripts
├── docs/                  # Documentation, including the requirements specification
├── Makefile               # Convenience commands for ingest/apply/restore/eval
└── data/                  # JSON artefacts produced by the pipeline
```

## Quick start

First ensure that you have Python 3 installed.  To ingest a text file, run:

```bash
make ingest INPUT=path/to/your_file.txt
```

This will produce a Cypher script under `out/` and a JSON artefact under `data/`.  To apply the generated script to a running Neo4j instance you can use the helper script:

```bash
make apply CYPHER=out/<work_id>.cypher
```

To regenerate a summary from the stored key terms:

```bash
make restore DOC=<work_id>
```

And to compare your original text with the restored summary:

```bash
make eval ORIG=path/to/original.txt REST=out/restored_<work_id>.txt
```

For more details on the system design and intended use cases please refer to `docs/requirements.md`.