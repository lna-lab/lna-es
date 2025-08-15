# LNA-LANG (OSS) — LNA‑ES v0.1 Starter Pack

> **Purpose**: Provide a minimal, vendor‑agnostic *Engineering Spec* (LNA‑ES) and working artifacts so teams can build **graph‑driven, operator‑based** pipelines that run across modern LLM providers.

- Spec date: 2025-08-13
- Status: **Draft v0.1**
- Scope: Core operators, dials/locks precedence, audit surface, CLI interface, dialect compilation hooks.

## Quick start

1. Read the spec: `spec/LNA-ES-v0.1.md`
1. Setup tools: `make setup`
1. Validate a dialect file: `python3 -m lna_es.cli ops validate examples/operators.sample.xml`
1. Compile a dialect to core rules: `python3 -m lna_es.cli ops compile examples/recipe.lna.yaml -o runs/dialect.json`
1. Run demo pipeline: `make demo` (generate → verify → rewrite → audit)

### Use Python 3.12 in a venv

This repo is configured to use Python 3.12 via a local virtual environment `./.venv`.

- Create venv and install tools: `make setup`
- Run commands inside venv automatically via Make targets (they use `./.venv/bin/python`)
- If `python3.12` is not found on your system, install it (e.g., via `pyenv` or Homebrew) or override `PYTHON` when creating the venv:

```bash
make PYTHON=$(which python3.12) setup
# Or try: make install-python  # attempts pyenv/brew installation helpers
```

1. Run tests: `make test`

## CI (GitHub Actions)

This repo includes a basic CI workflow at `.github/workflows/ci.yml` that runs on every push and pull request:

- Set up Python 3.12
- Install dev tools (`pre-commit`, `black`, `ruff`, `mdformat`, `pytest`, `jsonschema`, `xmlschema`)
- Run `pre-commit` on all files (format + lint)
- Run `pytest`
- Run a quick CLI sanity check (`python -m lna_es.cli --help`)

How to use:

- Push your branch to GitHub; the workflow auto-runs
- Check the “Actions” tab for status and logs
- To speed up linting, the workflow caches pre-commit hooks

## Repo layout

```
/spec
  LNA-ES-v0.1.md
  operator.schema.json
  operators.xsd
  RFC-Process.md
/tools
  cli-commands.md
/examples
  control.json
  control_A.json
  control_B.json
  recipe.lna.yaml
  graph.sample.json
  operators.sample.xml
  operator.sample.json
/CONTRIBUTING.md
/README.md (this file)
```

## License (suggested)

- Code: Apache-2.0
- Docs/Spec: CC-BY-4.0
