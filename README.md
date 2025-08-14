# LNA-LANG (OSS) — LNA‑ES v0.1 Starter Pack

> **Purpose**: Provide a minimal, vendor‑agnostic *Engineering Spec* (LNA‑ES) and working artifacts so teams can build **graph‑driven, operator‑based** pipelines that run across modern LLM providers.

- Spec date: 2025-08-13
- Status: **Draft v0.1**
- Scope: Core operators, dials/locks precedence, audit surface, CLI interface, dialect compilation hooks.

## Quick start
1. Read the spec: `spec/LNA-ES-v0.1.md`  
2. Validate a dialect file: `lna ops validate operators.xml` (schema in `spec/operators.xsd`)  
3. Compile a dialect to core rules: `lna ops compile operators.xml -o dialect.json`  
4. Run generation: see `tools/cli-commands.md` and the example control in `examples/control.json`

## Repo layout (suggested)
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
  recipe.lna.yaml
  graph.sample.json
/CONTRIBUTING.md
/README.md (this file)
```

## License (suggested)
- Code: Apache-2.0
- Docs/Spec: CC-BY-4.0
