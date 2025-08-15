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
1. Run tests: `make test`

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
