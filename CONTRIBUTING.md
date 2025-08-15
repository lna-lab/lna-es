# Contributing to LNA-ES

## Quick Start

1. Install dev tools
   ```bash
   pipx install pre-commit commitizen || pip install pre-commit commitizen
   pre-commit install
   ```
1. Format & lint before commit
   ```bash
   make fmt && make lint
   ```

## Commit & Branch

- Conventional Commits (feat/fix/docs/chore/refactor/test/ci/build)
- Branch prefixes: feat/*, fix/*, chore/*, docs/*
- PRs should include: rationale, before/after, and if generation changed, A/B outputs + audit card.

## Code Style

- Python 3.11+, black + ruff
- Keep CLI thin; put logic into `lna_es/`
- Add docstrings for public functions
- Avoid adding deps; prefer stdlib

## Tests

- Add tests under `tests/` when adding logic
- For generation, keep fixtures small and stable

## Security

- No secrets in repo. Use `.env` and document variables in `.env.example`.
