.PHONY: setup fmt lint check precommit ab demo

setup:
	python3 -m pip install -U pip || python -m pip install -U pip
	python3 -m pip install pre-commit commitizen black ruff mdformat || python -m pip install pre-commit commitizen black ruff mdformat
	python3 -m pre_commit install || python -m pre_commit install

fmt:
	python3 -m black . || python -m black .
	python3 -m ruff format . || python -m ruff format .
	python3 -m mdformat . || python -m mdformat .

lint:
	python3 -m pre_commit run --all-files || python -m pre_commit run --all-files

check: fmt lint

ab:
	python3 -m lna_es.cli abtest -A examples/control_A.json -B examples/control_B.json -g examples/graph.sample.json -o runs/ab/

demo:
	python3 -m lna_es.cli ops compile examples/recipe.lna.yaml -o runs/dialect.json || true
	python3 -m lna_es.cli generate -g examples/graph.sample.json -c examples/control_A.json -o runs/A/ || true
	python3 -m lna_es.cli verify -i runs/A/draft.txt -c examples/control_A.json -o runs/A/verify.json || true
	python3 -m lna_es.cli rewrite -i runs/A/draft.txt -v runs/A/verify.json -o runs/A/fixed.txt || true
