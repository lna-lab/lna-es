// Golden AGI Emotion Ontology - Useful Queries
// Collection of queries for analyzing and working with the emotion graph

// ========================================
// ANALYSIS QUERIES
// ========================================

// 1. Find all emotions with multiple parents (cross-categorized emotions)
MATCH (e:Emotion)<-[:HAS_SUBEMOTION]-(parent)
WITH e, collect(parent.name_en) as parents, count(parent) as parentCount
WHERE parentCount > 1
RETURN e.name_en as emotion, e.name_ja as japanese, parents, parentCount
ORDER BY parentCount DESC, e.name_en;

// 2. Show complete hierarchy for a specific core emotion
MATCH path = (core:Emotion {name_en: 'FEAR'})-[:HAS_SUBEMOTION*]->(descendant)
RETURN path;

// 3. Find all leaf emotions (no children)
MATCH (e:Emotion)
WHERE NOT (e)-[:HAS_SUBEMOTION]->()
RETURN e.level, e.name_en, e.name_ja
ORDER BY e.level DESC, e.name_en;

// 4. Count emotions by level
MATCH (e:Emotion)
RETURN e.level, count(e) as count
ORDER BY e.level;

// 5. Find shortest path between two emotions
MATCH path = shortestPath((e1:Emotion {name_en: 'Loving'})-[*]-(e2:Emotion {name_en: 'Hateful'}))
RETURN path;

// ========================================
// CHARACTER EMOTION ANALYSIS QUERIES
// ========================================

// 6. Tag a character with an emotion (example)
// First create a character:
// MERGE (c:Character {name: '鶴', story: 'tsuru_no_ongaeshi'})
// Then link to emotion:
// MATCH (c:Character {name: '鶴'}), (e:Emotion {name_en: 'Grateful'})
// CREATE (c)-[:FEELS {intensity: 85, scene: 'ending'}]->(e);

// 7. Find all emotions for a character
// MATCH (c:Character {name: '鶴'})-[f:FEELS]->(e:Emotion)
// RETURN c.name, e.name_en, e.name_ja, f.intensity, f.scene
// ORDER BY f.intensity DESC;

// 8. Find emotion journey for a character
// MATCH (c:Character {name: '鶴'})-[f:FEELS]->(e:Emotion)
// RETURN c.name, e.name_en, f.scene, f.intensity
// ORDER BY f.scene;

// ========================================
// EMOTION PATTERN QUERIES
// ========================================

// 9. Find common emotion combinations
// MATCH (c:Character)-[:FEELS]->(e1:Emotion),
//       (c)-[:FEELS]->(e2:Emotion)
// WHERE e1.name_en < e2.name_en
// WITH e1, e2, count(c) as cooccurrence
// WHERE cooccurrence > 1
// RETURN e1.name_en, e2.name_en, cooccurrence
// ORDER BY cooccurrence DESC
// LIMIT 20;

// 10. Find emotional opposites that appear together
// MATCH (c:Character)-[:FEELS]->(e1:Emotion),
//       (c)-[:FEELS]->(e2:Emotion),
//       (e1)-[:OPPOSITE_OF]-(e2)
// RETURN c.name, e1.name_en, e2.name_en;

// ========================================
// MAINTENANCE QUERIES
// ========================================

// 11. Check for orphaned emotions (no parent except multi-parent nodes)
MATCH (e:Emotion)
WHERE e.level > 0 AND NOT (e)<-[:HAS_SUBEMOTION]-()
RETURN e.name_en, e.name_ja, e.level;

// 12. Verify all core emotions exist
MATCH (e:Emotion {level: 0})
RETURN e.name_en, e.name_ja
ORDER BY e.name_en;

// 13. Find duplicate emotion names (should be empty)
MATCH (e1:Emotion), (e2:Emotion)
WHERE e1.name_en = e2.name_en AND id(e1) < id(e2)
RETURN e1.name_en, id(e1), id(e2);

// ========================================
// EXPORT QUERIES
// ========================================

// 14. Export full emotion hierarchy as JSON
MATCH (e:Emotion)
OPTIONAL MATCH (e)<-[:HAS_SUBEMOTION]-(parent)
WITH e, collect(parent.name_en) as parents
RETURN e.name_en as name, e.name_ja as japanese, e.level as level, parents
ORDER BY e.level, e.name_en;

// 15. Export emotion tree structure
MATCH path = (core:Emotion {level: 0})-[:HAS_SUBEMOTION*0..]->(e)
WITH core, e, length(path) as depth
RETURN core.name_en as core_emotion, 
       e.name_en as emotion, 
       e.name_ja as japanese,
       depth
ORDER BY core.name_en, depth, e.name_en;

// ========================================
// VISUALIZATION QUERIES
// ========================================

// 16. Get data for emotion wheel visualization
MATCH (core:Emotion {level: 0})
OPTIONAL MATCH (core)-[:HAS_SUBEMOTION]->(cat:Emotion {level: 1})
OPTIONAL MATCH (cat)-[:HAS_SUBEMOTION]->(specific:Emotion {level: 2})
RETURN core.name_en as core,
       collect(DISTINCT {
         category: cat.name_en,
         category_ja: cat.name_ja,
         emotions: collect(DISTINCT {
           name: specific.name_en,
           japanese: specific.name_ja
         })
       }) as structure;

// 17. Find emotions by Japanese name (partial match)
MATCH (e:Emotion)
WHERE e.name_ja CONTAINS '怒'
RETURN e.name_en, e.name_ja, e.level
ORDER BY e.level, e.name_en;

// ========================================
// ADVANCED ANALYSIS
// ========================================

// 18. Calculate emotion complexity (number of descendants)
MATCH (e:Emotion)
OPTIONAL MATCH (e)-[:HAS_SUBEMOTION*]->(descendant)
WITH e, count(DISTINCT descendant) as descendantCount
WHERE e.level <= 1
RETURN e.name_en, e.name_ja, e.level, descendantCount
ORDER BY descendantCount DESC;

// 19. Find emotion clusters (connected components)
CALL gds.graph.project(
  'emotion-graph',
  'Emotion',
  {
    HAS_SUBEMOTION: {orientation: 'UNDIRECTED'},
    OPPOSITE_OF: {orientation: 'UNDIRECTED'}
  }
)
YIELD graphName, nodeCount, relationshipCount;

// Then run community detection:
// CALL gds.louvain.stream('emotion-graph')
// YIELD nodeId, communityId
// RETURN gds.util.asNode(nodeId).name_en AS emotion, communityId
// ORDER BY communityId, emotion;

// 20. Emotion similarity based on shared ancestors
MATCH (e1:Emotion {name_en: 'Loving'})<-[:HAS_SUBEMOTION*]-(ancestor1),
      (e2:Emotion)<-[:HAS_SUBEMOTION*]-(ancestor2)
WHERE ancestor1 = ancestor2 AND e1 <> e2
WITH e1, e2, count(DISTINCT ancestor1) as sharedAncestors
RETURN e2.name_en, e2.name_ja, sharedAncestors
ORDER BY sharedAncestors DESC
LIMIT 10;