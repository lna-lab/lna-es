.PHONY: setup fmt lint check precommit ab demo venv test

# Python/venv settings (use Python 3.12)
PYTHON ?= python3.12
VENV ?= .venv
VENVPY := $(VENV)/bin/python
PIP := $(VENVPY) -m pip

venv:
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
