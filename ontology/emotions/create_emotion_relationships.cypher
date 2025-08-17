// Golden AGI Emotion Ontology - Relationship Creation Script
// This script creates HAS_SUBEMOTION relationships between emotion nodes
// Note: Some emotions have multiple parents due to cross-categorization

// ========================================
// HAPPY RELATIONSHIPS
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'HAPPY'}), (cat:Emotion)
WHERE cat.name_en IN ['Peaceful', 'Powerful', 'Accepted', 'Proud', 'Interested', 'Joyful']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Peaceful to its children
MATCH (parent:Emotion {name_en: 'Peaceful'}), (child:Emotion)
WHERE child.name_en IN ['Loving', 'Hopeful', 'Sensitive', 'Playful']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Powerful to its children
MATCH (parent:Emotion {name_en: 'Powerful'}), (child:Emotion)
WHERE child.name_en IN ['Courageous', 'Provocative']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Accepted to its children
MATCH (parent:Emotion {name_en: 'Accepted'}), (child:Emotion)
WHERE child.name_en IN ['Fulfilled', 'Respected']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Proud to its children
MATCH (parent:Emotion {name_en: 'Proud'}), (child:Emotion)
WHERE child.name_en IN ['Confident', 'Important']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Interested to its children
MATCH (parent:Emotion {name_en: 'Interested'}), (child:Emotion)
WHERE child.name_en IN ['Inquisitive', 'Amused']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Joyful to its children
MATCH (parent:Emotion {name_en: 'Joyful'}), (child:Emotion)
WHERE child.name_en IN ['Ecstatic', 'Liberated', 'Energetic', 'Eager']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// SURPRISE RELATIONSHIPS
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'SURPRISE'}), (cat:Emotion)
WHERE cat.name_en IN ['Excited', 'Amazed', 'Confused', 'Startled']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Excited to its children
MATCH (parent:Emotion {name_en: 'Excited'}), (child:Emotion)
WHERE child.name_en IN ['Awe', 'Astonished']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Amazed to its children
MATCH (parent:Emotion {name_en: 'Amazed'}), (child:Emotion)
WHERE child.name_en IN ['Perplexed', 'Disillusioned']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Confused to its children
MATCH (parent:Emotion {name_en: 'Confused'}), (child:Emotion)
WHERE child.name_en IN ['Dismayed', 'Shocked']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Startled to its children
MATCH (parent:Emotion {name_en: 'Startled'}), (child:Emotion)
WHERE child.name_en IN ['Terrified', 'Frightened']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// FEAR RELATIONSHIPS (Complex due to duplicates)
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'FEAR'}), (cat:Emotion)
WHERE cat.name_en IN ['Scared', 'Anxious', 'Insecure', 'Submissive', 'Rejected', 'Humiliated']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Scared to its children
MATCH (parent:Emotion {name_en: 'Scared'}), (child:Emotion)
WHERE child.name_en IN ['Overwhelmed', 'Worried']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Anxious to its children
MATCH (parent:Emotion {name_en: 'Anxious'}), (child:Emotion)
WHERE child.name_en IN ['Inadequate', 'Inferior']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Insecure to its children (Note: Insecure also appears under ANGER)
MATCH (parent:Emotion {name_en: 'Insecure'}), (child:Emotion)
WHERE child.name_en IN ['Worthless', 'Insignificant']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Submissive to its children (including Rejected and Humiliated as Level 2)
MATCH (parent:Emotion {name_en: 'Submissive'}), (child:Emotion)
WHERE child.name_en IN ['Rejected', 'Humiliated']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Rejected as Level 1 to its children
MATCH (parent:Emotion {name_en: 'Rejected'}), (child:Emotion)
WHERE child.name_en IN ['Alienated', 'Disrespected']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Humiliated as Level 1 to its children
MATCH (parent:Emotion {name_en: 'Humiliated'}), (child:Emotion)
WHERE child.name_en IN ['Ridiculed', 'Embarrassed']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// ANGER RELATIONSHIPS
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'ANGER'}), (cat:Emotion)
WHERE cat.name_en IN ['Hurt', 'Threatened', 'Hateful', 'Mad', 'Aggressive', 'Frustrated']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Hurt to its children (including Insecure which is shared with FEAR)
MATCH (parent:Emotion {name_en: 'Hurt'}), (child:Emotion)
WHERE child.name_en IN ['Devastated', 'Insecure']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Threatened to its children
MATCH (parent:Emotion {name_en: 'Threatened'}), (child:Emotion)
WHERE child.name_en IN ['Jealous', 'Resentful']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Hateful to its children
MATCH (parent:Emotion {name_en: 'Hateful'}), (child:Emotion)
WHERE child.name_en IN ['Violated', 'Furious']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Mad to its children
MATCH (parent:Emotion {name_en: 'Mad'}), (child:Emotion)
WHERE child.name_en IN ['Enraged', 'Provoked']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Aggressive to its children
MATCH (parent:Emotion {name_en: 'Aggressive'}), (child:Emotion)
WHERE child.name_en IN ['Hostile', 'Infuriated']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Frustrated to its children
MATCH (parent:Emotion {name_en: 'Frustrated'}), (child:Emotion)
WHERE child.name_en IN ['Irritated', 'Withdrawn']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// DISGUST RELATIONSHIPS
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'DISGUST'}), (cat:Emotion)
WHERE cat.name_en IN ['Critical', 'Distant', 'Disapproval', 'Disappointed', 'Awful', 'Avoidance']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Critical to its children
MATCH (parent:Emotion {name_en: 'Critical'}), (child:Emotion)
WHERE child.name_en IN ['Suspicious', 'Skeptical']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Distant to its children
MATCH (parent:Emotion {name_en: 'Distant'}), (child:Emotion)
WHERE child.name_en IN ['Sarcastic', 'Judgmental']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Disapproval to its children
MATCH (parent:Emotion {name_en: 'Disapproval'}), (child:Emotion)
WHERE child.name_en IN ['Loathing', 'Repugnant']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Disappointed to its children
MATCH (parent:Emotion {name_en: 'Disappointed'}), (child:Emotion)
WHERE child.name_en IN ['Revolted', 'Revulsion']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Awful to its children
MATCH (parent:Emotion {name_en: 'Awful'}), (child:Emotion)
WHERE child.name_en IN ['Detestable', 'Aversion']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Avoidance to its children
MATCH (parent:Emotion {name_en: 'Avoidance'}), (child:Emotion)
WHERE child.name_en IN ['Hesitant', 'Remorseful']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// SAD RELATIONSHIPS (Complex due to Abandoned duplicate)
// ========================================

// Core to Level 1
MATCH (core:Emotion {name_en: 'SAD'}), (cat:Emotion)
WHERE cat.name_en IN ['Guilty', 'Abandoned', 'Despair', 'Depressed', 'Lonely', 'Bored']
MERGE (core)-[:HAS_SUBEMOTION]->(cat);

// Guilty to its children
MATCH (parent:Emotion {name_en: 'Guilty'}), (child:Emotion)
WHERE child.name_en IN ['Ashamed', 'Ignored']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Abandoned as Level 1 to its children
MATCH (parent:Emotion {name_en: 'Abandoned'}), (child:Emotion)
WHERE child.name_en IN ['Victimized', 'Powerless']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Despair to its children (including Inferior which is shared with FEAR)
MATCH (parent:Emotion {name_en: 'Despair'}), (child:Emotion)
WHERE child.name_en IN ['Vulnerable', 'Inferior']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Depressed to its children (including Abandoned as Level 2)
MATCH (parent:Emotion {name_en: 'Depressed'}), (child:Emotion)
WHERE child.name_en IN ['Empty', 'Abandoned']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Lonely to its children
MATCH (parent:Emotion {name_en: 'Lonely'}), (child:Emotion)
WHERE child.name_en IN ['Isolated', 'Apathetic']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// Bored to its children
MATCH (parent:Emotion {name_en: 'Bored'}), (child:Emotion)
WHERE child.name_en IN ['Indifferent', 'Inspired']
MERGE (parent)-[:HAS_SUBEMOTION]->(child);

// ========================================
// OPPOSITE RELATIONSHIPS (Core emotions)
// ========================================

// Create bidirectional opposite relationships
MATCH (happy:Emotion {name_en: 'HAPPY'}), (sad:Emotion {name_en: 'SAD'})
MERGE (happy)-[:OPPOSITE_OF]->(sad)
MERGE (sad)-[:OPPOSITE_OF]->(happy);

// Optional: Add more opposite relationships based on Plutchik's wheel
// MATCH (fear:Emotion {name_en: 'FEAR'}), (anger:Emotion {name_en: 'ANGER'})
// MERGE (fear)-[:OPPOSITE_OF]->(anger)
// MERGE (anger)-[:OPPOSITE_OF]->(fear);

// MATCH (surprise:Emotion {name_en: 'SURPRISE'}), (anticipation:Emotion {name_en: 'ANTICIPATION'})
// MERGE (surprise)-[:OPPOSITE_OF]->(anticipation)
// MERGE (anticipation)-[:OPPOSITE_OF]->(surprise);

// ========================================
// VERIFICATION QUERIES
// ========================================

// Check multi-parent nodes:
// MATCH (e:Emotion)<-[:HAS_SUBEMOTION]-(parent)
// WITH e, count(parent) as parentCount
// WHERE parentCount > 1
// RETURN e.name_en, e.name_ja, parentCount
// ORDER BY parentCount DESC;

// Visualize full hierarchy:
// MATCH path = (core:Emotion {level: 0})-[:HAS_SUBEMOTION*]->(leaf)
// WHERE NOT (leaf)-[:HAS_SUBEMOTION]->()
// RETURN path;

// Count emotions by level:
// MATCH (e:Emotion)
// RETURN e.level, count(e) as count
// ORDER BY e.level;