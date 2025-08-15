.PHONY: setup fmt lint check precommit ab demo venv test ensure-python install-python export-graph

# Python/venv settings (use Python 3.12)
PYTHON ?= python3.12
VENV ?= .venv
VENVPY := $(VENV)/bin/python
PIP := $(VENVPY) -m pip

# Graph export backend selection
# You can override BACKEND here or in ./graph.backend (uncomment one)
# BACKEND=cypher
# BACKEND=csv
# BACKEND=gremlin
-include graph.backend
BACKEND ?= cypher

ensure-python:
	@if command -v $(PYTHON) >/dev/null 2>&1; then \
		echo "Found $(PYTHON): $$($(PYTHON) -V)"; \
	else \
		echo "ERROR: $(PYTHON) not found in PATH."; \
		echo ""; \
		echo "Install options:"; \
		echo "  - pyenv:   pyenv install -s 3.12.x  && export PYTHON=$$(pyenv which python3.12)"; \
		echo "  - Homebrew: brew install python@3.12 && brew link python@3.12 --force"; \
		echo "  - Or override: make PYTHON=$$(which python3.12) setup"; \
		exit 2; \
	fi

install-python:
	@if command -v pyenv >/dev/null 2>&1; then \
		echo "Using pyenv to install Python 3.12 (if needed)..."; \
		pyenv install -s 3.12.0 || true; \
		echo "Tip: set PYTHON=$$(pyenv which python3.12) for subsequent make targets."; \
	elif command -v brew >/dev/null 2>&1; then \
		echo "Using Homebrew to install python@3.12..."; \
		brew install python@3.12 || true; \
		echo "If needed: brew link python@3.12 --force"; \
	else \
		echo "Please install Python 3.12 manually and re-run make setup."; \
		exit 2; \
	fi

venv: ensure-python
	@# Create venv with Python 3.12
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip

setup: venv
	$(PIP) install pre-commit commitizen black ruff mdformat jsonschema xmlschema pytest
	$(VENVPY) -m pre_commit install

fmt:
	$(VENVPY) -m black .
	$(VENVPY) -m ruff format .
	$(VENVPY) -m mdformat .

lint:
	$(VENVPY) -m pre_commit run --all-files

test:
	$(VENVPY) -m pytest -q

check: fmt lint test

ab:
	$(VENVPY) -m lna_es.cli abtest -A examples/control_A.json -B examples/control_B.json -g examples/graph.sample.json -o runs/ab/

demo:
	$(VENVPY) -m lna_es.cli ops compile examples/recipe.lna.yaml -o runs/dialect.json || true
	$(VENVPY) -m lna_es.cli ops validate examples/operators.sample.xml || true
	$(VENVPY) -m lna_es.cli ops validate examples/operator.sample.json || true
	$(VENVPY) -m lna_es.cli generate -g examples/graph.sample.json -c examples/control_A.json -o runs/A/ || true
	$(VENVPY) -m lna_es.cli verify -i runs/A/draft.txt -c examples/control_A.json -o runs/A/verify.json || true
	$(VENVPY) -m lna_es.cli rewrite -i runs/A/draft.txt -v runs/A/verify.json -o runs/A/fixed.txt || true
	$(VENVPY) -m lna_es.cli audit -m runs/A/metrics.json -v runs/A/verify.json -o runs/A/audit_card.md || true

init:
	$(VENVPY) -m lna_es.cli preset load packages/instant_dialogue/lna_axis0_sonnet4.xml -o runs/cache/axis0_index.json

bench-graphs:
	@mkdir -p runs/recon
	$(VENVPY) -m lna_es.cli graph-reconstruct -c examples/control_A.json -o runs/recon/core.json
	$(VENVPY) -m lna_es.cli graph-reconstruct -c examples/control_A.json -o runs/recon/aibrain.json --ai-brain --ai-threshold 0.7
	$(VENVPY) -m lna_es.cli graph-reconstruct -c examples/control_A.json -o runs/recon/aibrain_onto.json --ai-brain --ai-threshold 0.6 --ontology-dir ontology
	$(VENVPY) -m lna_es.cli graph-eval -g examples/graph.sample.json -p runs/recon/core.json -o runs/recon/core_eval.json
	$(VENVPY) -m lna_es.cli graph-eval -g examples/graph.sample.json -p runs/recon/aibrain.json -o runs/recon/aibrain_eval.json
	$(VENVPY) -m lna_es.cli graph-eval -g examples/graph.sample.json -p runs/recon/aibrain_onto.json -o runs/recon/aibrain_onto_eval.json
	@echo "method\tnodes_f1\tedges_f1" > runs/recon/bench.tsv
	@printf "core\t" >> runs/recon/bench.tsv; jq -r '(.nodes.f1|tostring)+"\t"+(.edges.f1|tostring)' runs/recon/core_eval.json >> runs/recon/bench.tsv
	@printf "ai-brain(th=0.7)\t" >> runs/recon/bench.tsv; jq -r '(.nodes.f1|tostring)+"\t"+(.edges.f1|tostring)' runs/recon/aibrain_eval.json >> runs/recon/bench.tsv
	@printf "ai+onto(th=0.6)\t" >> runs/recon/bench.tsv; jq -r '(.nodes.f1|tostring)+"\t"+(.edges.f1|tostring)' runs/recon/aibrain_onto_eval.json >> runs/recon/bench.tsv
	@echo "\nBench results written to runs/recon/bench.tsv" && cat runs/recon/bench.tsv

export-graph:
	@if [ -z "$(GRAPH)" ]; then echo "Usage: make export-graph GRAPH=path/to/graph.json [BACKEND=cypher|csv|gremlin]"; exit 2; fi
	@mkdir -p runs/export/$(BACKEND)
	$(VENVPY) -m lna_es.cli graph-export -g $(GRAPH) -f $(BACKEND) -o runs/export/$(BACKEND)
	@echo "Exported to runs/export/$(BACKEND)/"
