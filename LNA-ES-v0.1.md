# LNA‑ES v0.1 — Engineering Spec (Draft)

**Goal**: Turn *prompts* into a portable **protocol** for graph‑conditioned generation.

## 0. Terms

- **Graph**: Neo4j‑compatible JSON (`nodes`, `edges`, attributes).
- **Operator**: A declarative step with typed I/O and side effects.
- **Dialect**: A pack of high‑level (often aesthetic) operators compiled to Core.
- **Dials**: Numeric controls — `soul`, `editor`, `fidelity` (0..1).
- **Locks**: Hard constraints — `identity`, `toponym`, `relation`, `pov` (bool).
- **Invariants**: HARD (must keep) / SOFT (prefer to keep).

## 1. Core Operators (required by LNA‑ES)

Each operator conforms to `spec/operator.schema.json` (JSON Schema).

### 1.1 EXTRACT

- **In**: `text`, optional `ontology_version`
- **Out**: `graph_candidates` (nodes/edges with confidence)
- **Side effects**: `prompt_inject` (optional notes)

### 1.2 RESOLVE

- **In**: `graph_candidates`
- **Out**: `graph` (deduped, coref‑resolved)

### 1.3 WEIGHT

- **In**: `graph`
- **Out**: `graph` (with weights: occurrence/causality/contrast)

### 1.4 LOCK

- **In**: `graph`, `invariants` (`HARD`/`SOFT`), `locks`
- **Out**: `graph_locked`
- **Rule**: Locks override all other operator effects.

### 1.5 STYLE

- **In**: `author_vector` (style/doctrine/symbol), `dials`
- **Out**: `style_signal` (provider‑agnostic structure)

### 1.6 VERIFY

- **In**: `draft`, `graph_locked`, `editor_brief`, `style_targets`
- **Out**: `violations` (array), `metrics` (style/market/invariant)

### 1.7 REWRITE

- **In**: `draft`, `violations`
- **Out**: `draft_fixed` (apply **minimal** edits only)

## 2. Dials & Locks Precedence

1. **Locks(HARD)** → 2. VERIFY (HARD rules) → 3. REWRITE → 4. Editor targets → 5. Style → 6. SOFT invariants

## 3. I/O Contracts

- All operators accept an `input` object and return an `output` object.
- Errors must be typed: `InvalidInput`, `RuleConflict`, `ProviderError`.

## 4. Audit Surface

- Persist `audit_card` (JSON + Markdown) with: inputs (hashes), dials, locks, metrics, violations, diffs.

## 5. Provider Adapters

- Provide `openai`, `anthropic`, `qwen`, `llama` adapters. Map `style_signal` to provider prompts, stop tokens, decoding params.

## 6. Compliance Hooks

- Forbidden content rules (basic), redaction, and “soul‑mode disclosure” tag in audit.

## 7. Versioning

- **SemVer**: MAJOR.MINOR.PATCH
- **Stability**: `stable`, `experimental`, `deprecated` per operator or field.

## 8. Compatibility

- An LNA‑ES implementation MUST:
  - Implement all 7 Core operators.
  - Honor Locks precedence.
  - Support `audit_card`.
  - Provide at least one provider adapter.
