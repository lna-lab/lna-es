// Golden AGI Meta Ontology Graph
// Represents dependencies and relationships between ontologies
// This graph helps manage ontology loading order and granularity levels

// ========================================
// ONTOLOGY NODES
// ========================================

// Core Ontologies
MERGE (spatial:Ontology {name: 'spatial', name_ja: '空間', priority: 1, type: 'core'});
MERGE (temporal:Ontology {name: 'temporal', name_ja: '時間', priority: 1, type: 'core'});
MERGE (relationship:Ontology {name: 'relationship', name_ja: '関係性', priority: 2, type: 'core'});
MERGE (emotion:Ontology {name: 'emotion', name_ja: '感情', priority: 3, type: 'core'});
MERGE (causality:Ontology {name: 'causality', name_ja: '因果関係', priority: 2, type: 'core'});

// Structural Ontologies
MERGE (narrative:Ontology {name: 'narrative', name_ja: '物語構造', priority: 4, type: 'structural'});
MERGE (character:Ontology {name: 'character', name_ja: 'キャラクター機能', priority: 4, type: 'structural'});
MERGE (discourse:Ontology {name: 'discourse', name_ja: '談話構造', priority: 4, type: 'structural'});

// Advanced Ontologies
MERGE (indirect_emotion:Ontology {name: 'indirect_emotion', name_ja: '間接感情', priority: 5, type: 'advanced'});
MERGE (metaphysical:Ontology {name: 'metaphysical', name_ja: '形而上', priority: 5, type: 'advanced'});

// ========================================
// DEPENDENCY RELATIONSHIPS
// ========================================

// Basic dependencies (no dependencies)
// spatial -> none
// temporal -> none

// Relationship dependencies
MERGE (relationship)-[:DEPENDS_ON]->(temporal);

// Emotion dependencies
MERGE (emotion)-[:DEPENDS_ON]->(relationship);

// Causality dependencies
MERGE (causality)-[:DEPENDS_ON]->(temporal);

// Narrative dependencies
MERGE (narrative)-[:DEPENDS_ON]->(temporal);
MERGE (narrative)-[:DEPENDS_ON]->(causality);

// Character dependencies
MERGE (character)-[:DEPENDS_ON]->(relationship);

// Discourse dependencies
MERGE (discourse)-[:DEPENDS_ON]->(causality);

// Indirect emotion dependencies
MERGE (indirect_emotion)-[:DEPENDS_ON]->(emotion);
MERGE (indirect_emotion)-[:DEPENDS_ON]->(spatial);

// Metaphysical dependencies
MERGE (metaphysical)-[:DEPENDS_ON]->(spatial);
MERGE (metaphysical)-[:DEPENDS_ON]->(temporal);
MERGE (metaphysical)-[:DEPENDS_ON]->(causality);

// ========================================
// GRANULARITY LEVELS
// ========================================

MERGE (overview:GranularityLevel {name: 'overview', name_ja: '概要', level: 1});
MERGE (detailed:GranularityLevel {name: 'detailed', name_ja: '詳細', level: 2});
MERGE (exhaustive:GranularityLevel {name: 'exhaustive', name_ja: '網羅的', level: 3});

// ========================================
// GRANULARITY REQUIREMENTS
// ========================================

// Overview level requirements
MERGE (overview)-[:REQUIRES {status: 'required'}]->(temporal);
MERGE (overview)-[:REQUIRES {status: 'required'}]->(spatial);
MERGE (overview)-[:REQUIRES {status: 'required'}]->(relationship);
MERGE (overview)-[:REQUIRES {status: 'optional'}]->(emotion);

// Detailed level requirements
MERGE (detailed)-[:REQUIRES {status: 'required'}]->(temporal);
MERGE (detailed)-[:REQUIRES {status: 'required'}]->(spatial);
MERGE (detailed)-[:REQUIRES {status: 'required'}]->(relationship);
MERGE (detailed)-[:REQUIRES {status: 'required'}]->(causality);
MERGE (detailed)-[:REQUIRES {status: 'required'}]->(narrative);
MERGE (detailed)-[:REQUIRES {status: 'optional'}]->(emotion);
MERGE (detailed)-[:REQUIRES {status: 'optional'}]->(character);
MERGE (detailed)-[:REQUIRES {status: 'optional'}]->(discourse);

// Exhaustive level requirements (all ontologies)
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(spatial);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(temporal);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(relationship);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(emotion);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(causality);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(narrative);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(character);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(discourse);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(indirect_emotion);
MERGE (exhaustive)-[:REQUIRES {status: 'required'}]->(metaphysical);

// ========================================
// ONTOLOGY GROUPS (for visualization)
// ========================================

MERGE (core_group:OntologyGroup {name: 'Core Ontologies', name_ja: 'コアオントロジー'});
MERGE (structural_group:OntologyGroup {name: 'Structural Ontologies', name_ja: '構造オントロジー'});
MERGE (advanced_group:OntologyGroup {name: 'Advanced Ontologies', name_ja: '高度なオントロジー'});

// Group memberships
MERGE (spatial)-[:BELONGS_TO]->(core_group);
MERGE (temporal)-[:BELONGS_TO]->(core_group);
MERGE (relationship)-[:BELONGS_TO]->(core_group);
MERGE (emotion)-[:BELONGS_TO]->(core_group);
MERGE (causality)-[:BELONGS_TO]->(core_group);

MERGE (narrative)-[:BELONGS_TO]->(structural_group);
MERGE (character)-[:BELONGS_TO]->(structural_group);
MERGE (discourse)-[:BELONGS_TO]->(structural_group);

MERGE (indirect_emotion)-[:BELONGS_TO]->(advanced_group);
MERGE (metaphysical)-[:BELONGS_TO]->(advanced_group);

// ========================================
// CREATE INDEXES
// ========================================

CREATE INDEX ontology_name IF NOT EXISTS FOR (o:Ontology) ON (o.name);
CREATE INDEX ontology_priority IF NOT EXISTS FOR (o:Ontology) ON (o.priority);
CREATE INDEX ontology_type IF NOT EXISTS FOR (o:Ontology) ON (o.type);
CREATE INDEX granularity_name IF NOT EXISTS FOR (g:GranularityLevel) ON (g.name);
CREATE INDEX ontology_group_name IF NOT EXISTS FOR (g:OntologyGroup) ON (g.name);

// ========================================
// USEFUL QUERIES
// ========================================

// Query 1: Get loading order for a granularity level
// MATCH (g:GranularityLevel {name: 'detailed'})-[:REQUIRES]->(o:Ontology)
// OPTIONAL MATCH path = (o)-[:DEPENDS_ON*]->(dep:Ontology)
// WITH o, COLLECT(DISTINCT dep) AS deps
// RETURN o.name AS ontology, 
//        [d IN deps | d.name] AS dependencies,
//        o.priority AS priority
// ORDER BY o.priority, SIZE(deps)

// Query 2: Check circular dependencies
// MATCH path = (o:Ontology)-[:DEPENDS_ON*]->(o)
// RETURN path

// Query 3: Get ontologies by group
// MATCH (g:OntologyGroup)<-[:BELONGS_TO]-(o:Ontology)
// RETURN g.name AS group, COLLECT(o.name) AS ontologies