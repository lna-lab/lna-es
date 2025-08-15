.PHONY: setup fmt lint check precommit ab demo venv test ensure-python install-python

# Python/venv settings (use Python 3.12)
PYTHON ?= python3.12
VENV ?= .venv
VENVPY := $(VENV)/bin/python
PIP := $(VENVPY) -m pip

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
