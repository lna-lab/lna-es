// Golden AGI Emotion Ontology - CSV Import Script
// This script loads emotions from CSV file

// First, clear existing emotion data (optional - uncomment if needed)
// MATCH (e:Emotion) DETACH DELETE e;

// ========================================
// LOAD EMOTIONS FROM CSV
// ========================================

// Note: Update the file path to match your Neo4j import directory
// The CSV file should be placed in the Neo4j import folder

// Load all emotion nodes first
LOAD CSV WITH HEADERS FROM 'file:///emotions.csv' AS row
MERGE (e:Emotion {name_en: row.name_en})
SET e.name_ja = row.name_ja,
    e.level = toInteger(row.level);

// Add core flag to level 0 emotions
MATCH (e:Emotion {level: 0})
SET e.core = true;

// Create relationships based on parent column
LOAD CSV WITH HEADERS FROM 'file:///emotions.csv' AS row
WHERE row.parent IS NOT NULL AND row.parent <> ''
MATCH (child:Emotion {name_en: row.name_en})
MATCH (parent:Emotion {name_en: row.parent})
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// LOAD EMOTIONS WITH MULTIPLE PARENTS
// ========================================

// If using the multi-parent CSV format:
// This handles comma-separated parent lists

// LOAD CSV WITH HEADERS FROM 'file:///emotions_with_multiple_parents.csv' AS row
// MERGE (e:Emotion {name_en: row.name_en})
// SET e.name_ja = row.name_ja,
//     e.level = toInteger(row.level)
// WITH e, row
// WHERE row.parents IS NOT NULL AND row.parents <> ''
// WITH e, split(row.parents, ',') AS parentList
// UNWIND parentList AS parentName
// WITH e, trim(parentName) AS parentName
// MATCH (parent:Emotion {name_en: parentName})
// MERGE (parent)-[:HAS_SUBEMOTION]->(e);

// ========================================
// CREATE OPPOSITE RELATIONSHIPS
// ========================================

// Create core emotion opposites
MATCH (happy:Emotion {name_en: 'HAPPY'}), (sad:Emotion {name_en: 'SAD'})
MERGE (happy)-[:OPPOSITE_OF]->(sad)
MERGE (sad)-[:OPPOSITE_OF]->(happy);

// ========================================
// CREATE INDEXES
// ========================================

CREATE INDEX emotion_name_en IF NOT EXISTS FOR (e:Emotion) ON (e.name_en);
CREATE INDEX emotion_name_ja IF NOT EXISTS FOR (e:Emotion) ON (e.name_ja);
CREATE INDEX emotion_level IF NOT EXISTS FOR (e:Emotion) ON (e.level);
CREATE INDEX emotion_core IF NOT EXISTS FOR (e:Emotion) ON (e.core);

// ========================================
// VERIFICATION
// ========================================

// Verify import results
MATCH (e:Emotion)
RETURN e.level, count(e) as count
ORDER BY e.level;

// Check for multi-parent nodes
MATCH (e:Emotion)<-[:HAS_SUBEMOTION]-(parent)
WITH e, count(parent) as parentCount
WHERE parentCount > 1
RETURN e.name_en, e.name_ja, parentCount
ORDER BY parentCount DESC;