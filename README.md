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

## Design philosophy: Core vs. Dialects (AI-brain as a dialect)

LNA‑ES keeps the Core minimal and stable, while allowing rich expression via Dialects.

- Core (portable contract)

  - 7 required operators: EXTRACT, RESOLVE, WEIGHT, LOCK, STYLE, VERIFY, REWRITE
  - Dials/Locks precedence、I/O契約（typed errors）、Audit surface
  - Provider-agnostic outputs（例: style_signal）をアダプタで各LLMへマッピング

- Dialects (your customization)

  - ドメイン/美学/「AI脳」などの概念は方言で表現
  - `operators.xml`（`spec/operators.xsd`）で演算子を定義し、`effect_map` で Core へ落とし込む
  - `lna ops compile operators.xml -o dialect.json` で決定的にCoreへコンパイル
  - 安定性と進化管理: `stability` フラグと SemVer を運用

- Why dialects for “AI脳”?

  - Coreを痩せた契約のまま保つことで互換性と移植性を確保
  - Axis系（例: `packages/instant_dialogue/lna_axis0_sonnet4.xml`）は方言パックとして管理
  - ユーザーは用途に応じて独自方言を定義/差し替え可能（ベンダー非依存のまま）

Start here if you want your own dialect:

1. Copy `examples/operators.sample.xml` and extend it
1. Validate with `lna ops validate your_operators.xml`
1. Compile with `lna ops compile your_operators.xml -o your_dialect.json`
1. Use it with `lna generate ... --dialect your_dialect.json`（adapter側でのマッピング想定）

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
