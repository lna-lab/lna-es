// Neo4j constraint definitions

// Ensure that each Work has a unique base identifier
CREATE CONSTRAINT work_baseId_unique IF NOT EXISTS
FOR (w:Work)
REQUIRE w.baseId IS UNIQUE;

// Ensure that each Segment has a unique base identifier
CREATE CONSTRAINT segment_baseId_unique IF NOT EXISTS
FOR (s:Segment)
REQUIRE s.baseId IS UNIQUE;

// Ensure that each Sentence has a unique base identifier
CREATE CONSTRAINT sentence_baseId_unique IF NOT EXISTS
FOR (s:Sentence)
REQUIRE s.baseId IS UNIQUE;

// Ensure that each Entity has a unique base identifier
CREATE CONSTRAINT entity_baseId_unique IF NOT EXISTS
FOR (e:Entity)
REQUIRE e.baseId IS UNIQUE;

// Ensure uniqueness on TagCatalog entries by scheme and code/category
CREATE CONSTRAINT tagCatalog_scheme_code_unique IF NOT EXISTS
FOR (t:TagCatalog)
REQUIRE (t.scheme, t.code) IS NODE KEY;