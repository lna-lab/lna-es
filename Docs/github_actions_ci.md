# GitHub Actions CI (Proposal)

This repository includes a minimal GitHub Actions workflow to validate core LNA-ES functions on every push/PR:

- File: `.github/workflows/lna-es-ci.yml`
- Python: 3.12 on `ubuntu-latest`
- Installs minimal deps (`requirements-ci.txt`): numpy, PyYAML
- Runs:
  - `python -m src.cli models --pretty` (model info; falls back if local models absent)
  - `python -m src.cli classify --text "吾輩は猫である…" --pretty` (classification smoke test)
  - `python lna-es-app/apps/extractor/extractor.py --input test_sample.txt --outdir out --datadir data` (pipeline smoke test)
- Uploads artefacts: `out/**`, `data/**`, and `out_classify.json`

Notes
- Embedding models are not fetched in CI; vector generation uses deterministic fallbacks.
- If ontology `index.yaml` is present, PyYAML enables optional mapping load.
- Extend with matrices (OS/Python versions), caching (pip), and timed metrics as needed.
- For Neo4j apply, inject secrets and gate behind an `if: github.ref == 'refs/heads/main'` condition.

Next steps (optional)
- Add `/usr/bin/time -l` benchmarks and parse into a JSON summary.
- Add a `make ci` script for local parity.
- Add separate workflow to lint/format (ruff/black) if adopted.
