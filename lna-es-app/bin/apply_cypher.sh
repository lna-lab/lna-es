#!/usr/bin/env bash

# Helper script to apply a Cypher file to a Neo4j instance.
#
# Usage:
#   ./bin/apply_cypher.sh path/to/file.cypher
#
# Environment variables:
#   NEO4J_URI  - Bolt URI of the Neo4j instance (default: bolt://localhost:7687)
#   NEO4J_USER - Username (default: neo4j)
#   NEO4J_PASS - Password (default: password)

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <cypher-file>" >&2
    exit 1
fi

FILE="$1"
if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE" >&2
    exit 1
fi

NEO4J_URI="${NEO4J_URI:-bolt://localhost:7687}"
NEO4J_USER="${NEO4J_USER:-neo4j}"
NEO4J_PASS="${NEO4J_PASS:-password}"

if command -v cypher-shell >/dev/null 2>&1; then
    echo "Applying $FILE to Neo4j at $NEO4J_URI as user $NEO4J_USER…"
    cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASS" < "$FILE"
    echo "Done."
else
    echo "WARNING: cypher-shell not found in PATH." >&2
    echo "You can manually apply the file using Neo4j Desktop or docker exec, for example:" >&2
    echo "  docker exec -it <neo4j-container> cypher-shell -u $NEO4J_USER -p <password> -f /path/inside/container/$(basename "$FILE")" >&2
fi