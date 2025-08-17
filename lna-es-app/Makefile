PYTHON := python3

# Default directories
OUTDIR ?= out
DATADIR ?= data

.PHONY: ingest apply restore eval

##
## Ingest: convert a text file into JSON and Cypher artefacts
## Usage: make ingest INPUT=path/to/file.txt
ingest:
	@if [ -z "$(INPUT)" ]; then \
		echo "Usage: make ingest INPUT=path/to/file.txt"; exit 1; \
	fi
	@mkdir -p $(OUTDIR) $(DATADIR)
	$(PYTHON) apps/extractor/extractor.py --input "$(INPUT)" --outdir "$(OUTDIR)" --datadir "$(DATADIR)"

##
## Apply: send a generated Cypher script to Neo4j using bin/apply_cypher.sh
## Usage: make apply CYPHER=out/<id>.cypher
apply:
	@if [ -z "$(CYPHER)" ]; then \
		echo "Usage: make apply CYPHER=path/to/file.cypher"; exit 1; \
	fi
	@bash bin/apply_cypher.sh "$(CYPHER)"

##
## Restore: reconstruct a summary using only stored key terms
## Usage: make restore DOC=<work_id>
restore:
	@if [ -z "$(DOC)" ]; then \
		echo "Usage: make restore DOC=<work_id>"; exit 1; \
	fi
	@mkdir -p $(OUTDIR)
	$(PYTHON) apps/restorer/restorer.py --doc "$(DOC)" --datadir "$(DATADIR)" --output "$(OUTDIR)/restored_$(DOC).txt"

##
## Eval: compare original and restored texts
## Usage: make eval ORIG=path/to/orig.txt REST=out/restored_<id>.txt
eval:
	@if [ -z "$(ORIG)" ] || [ -z "$(REST)" ]; then \
		echo "Usage: make eval ORIG=path/to/original.txt REST=path/to/restored.txt"; exit 1; \
	fi
	$(PYTHON) apps/evaluator/evaluator.py --orig "$(ORIG)" --rest "$(REST)"