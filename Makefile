.PHONY: setup fmt lint check precommit ab demo

setup:
	pip install -U pip
	pip install pre-commit commitizen
	pre-commit install

fmt:
	black .
	ruff format .
	mdformat .

lint:
	pre-commit run --all-files

check: fmt lint

ab:
	python -m lna_es.cli abtest -A examples/control_A.json -B examples/control_B.json -g examples/graph.sample.json -o runs/ab/

demo:
    lna ops compile examples/recipe.lna.yaml -o runs/dialect.json || true
	lna generate -g examples/graph.sample.json -c examples/control_A.json -o runs/A/ || true
