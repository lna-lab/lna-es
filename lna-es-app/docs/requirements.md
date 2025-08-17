# Requirements Specification

This directory is intended to hold documentation relating to the LNA‑ES project.  The **complete requirements specification** can be found at the root of this repository in the file `要件定義書_v3.2_100.md`.  To avoid duplication and possible divergence between documents, the full contents of that specification are not repeated here.  Please refer to the root‑level file for detailed design goals, data models, process flow and key performance indicators.

In summary, the system must:

* Ingest arbitrary plain text files (converted from PDF, Kindle, web content, chat logs, etc.) and break them into segments and sentences.
* Extract salient entities and relationships, classify documents against the Nippon Decimal Classification (NDC) and Kindle genre schemes, and assign ontology weights across fifteen semantic axes.
* Generate random vector embeddings for entities and sentences and persist only abstract information (no original text) to ensure compliance with copyright and privacy requirements.
* Produce Neo4j Cypher files that can be used to populate a graph database, including nodes for works, segments, sentences, entities and classification tags.
* Provide a simple restoration mechanism that reconstructs a human‑readable summary from the graph using only stored key terms, together with tools for evaluating the quality of the restoration relative to the original text.

See the project README for instructions on how to run the ingest, apply, restore and evaluate commands.