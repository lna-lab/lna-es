# Graph export (openCypher / CSV / Gremlin)

LNA-ES keeps the in-memory graph as JSON (`{nodes, edges}`) and provides vendor-neutral export options.

## Choose backend

- Preferred via `graph.backend` file in repo root:

```
# BACKEND=cypher
# BACKEND=csv
# BACKEND=gremlin
```

Uncomment one line, or override per-run: `make export-graph BACKEND=csv GRAPH=runs/A/metrics.json`.

## Export command

```
make export-graph GRAPH=runs/recon/aibrain_onto.json          # uses default BACKEND (cypher)
make export-graph GRAPH=runs/recon/aibrain_onto.json BACKEND=csv
make export-graph GRAPH=runs/recon/aibrain_onto.json BACKEND=gremlin
```

- cypher: writes `runs/export/cypher/export.cypher`
- csv: writes `runs/export/csv/{nodes.csv,edges.csv}`
- gremlin: writes `runs/export/gremlin/export.gremlin.groovy`

## Minimal import recipes

- Neo4j / Memgraph (openCypher):

  - Start DB, then run the cypher file (client/Browser)
  - Example: `:source runs/export/cypher/export.cypher`

- AWS Neptune (Gremlin):

  - Use `export.gremlin.groovy` with a Gremlin console connected to Neptune endpoint
  - Or load CSV to S3 and run Neptune Bulk Loader (align CSV headers accordingly)

- AgensGraph / other Cypher systems:

  - Most accept openCypher `MERGE` syntax; run `export.cypher`

Notes:

- The exporter uses conservative property typing (strings/numbers/bools)
- Index/constraints are not emitted by default; add them manually per system
