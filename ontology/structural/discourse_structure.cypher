// Golden AGI Discourse Structure Ontology
// Based on Rhetorical Structure Theory (RST) and discourse analysis
// Structure: Relation Type (Level 0) → Specific Relation (Level 1) → Sub-patterns (Level 2)

// ========================================
// CORE DISCOURSE RELATION TYPES (Level 0)
// ========================================

MERGE (:DiscourseStructure {name_en: 'NUCLEUS_SATELLITE', name_ja: '核-衛星', level: 0, core: true});
MERGE (:DiscourseStructure {name_en: 'MULTINUCLEAR', name_ja: '多核', level: 0, core: true});
MERGE (:DiscourseStructure {name_en: 'SCHEMA', name_ja: 'スキーマ', level: 0, core: true});

// ========================================
// NUCLEUS-SATELLITE RELATIONS (Level 1)
// ========================================

// Presentational Relations (intended to increase reader's positive regard)
MERGE (:DiscourseStructure {name_en: 'Motivation', name_ja: '動機付け', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Antithesis', name_ja: '対照法', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Background', name_ja: '背景', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Enablement', name_ja: '可能化', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Evidence', name_ja: '証拠', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Justify', name_ja: '正当化', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Preparation', name_ja: '準備', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Restatement', name_ja: '言い換え', level: 1, rst_type: 'presentational', core: false});
MERGE (:DiscourseStructure {name_en: 'Summary', name_ja: '要約', level: 1, rst_type: 'presentational', core: false});

// Subject Matter Relations (intended to inform)
MERGE (:DiscourseStructure {name_en: 'Circumstance', name_ja: '状況', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Condition', name_ja: '条件', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Elaboration', name_ja: '詳述', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Evaluation', name_ja: '評価', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Interpretation', name_ja: '解釈', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Means', name_ja: '手段', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Non-volitional Cause', name_ja: '非意志的原因', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Non-volitional Result', name_ja: '非意志的結果', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Otherwise', name_ja: 'さもなければ', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Purpose', name_ja: '目的', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Solutionhood', name_ja: '解決策', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Unless', name_ja: 'でない限り', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Volitional Cause', name_ja: '意志的原因', level: 1, rst_type: 'subject_matter', core: false});
MERGE (:DiscourseStructure {name_en: 'Volitional Result', name_ja: '意志的結果', level: 1, rst_type: 'subject_matter', core: false});

// ========================================
// MULTINUCLEAR RELATIONS (Level 1)
// ========================================

MERGE (:DiscourseStructure {name_en: 'Conjunction', name_ja: '連結', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'Contrast', name_ja: '対比', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'Disjunction', name_ja: '選言', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'Joint', name_ja: '結合', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'List', name_ja: '列挙', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'Restatement-MN', name_ja: '多核言い換え', level: 1, rst_type: 'multinuclear', core: false});
MERGE (:DiscourseStructure {name_en: 'Sequence', name_ja: '連続', level: 1, rst_type: 'multinuclear', core: false});

// ========================================
// SCHEMA RELATIONS (Level 1)
// ========================================

// Problem-Solution Schema
MERGE (:DiscourseStructure {name_en: 'Problem', name_ja: '問題', level: 1, schema_type: 'problem_solution', core: false});
MERGE (:DiscourseStructure {name_en: 'Solution', name_ja: '解決', level: 1, schema_type: 'problem_solution', core: false});

// Question-Answer Schema
MERGE (:DiscourseStructure {name_en: 'Question', name_ja: '質問', level: 1, schema_type: 'question_answer', core: false});
MERGE (:DiscourseStructure {name_en: 'Answer', name_ja: '回答', level: 1, schema_type: 'question_answer', core: false});

// Claim-Evidence Schema
MERGE (:DiscourseStructure {name_en: 'Claim', name_ja: '主張', level: 1, schema_type: 'claim_evidence', core: false});
MERGE (:DiscourseStructure {name_en: 'Support', name_ja: '支持', level: 1, schema_type: 'claim_evidence', core: false});

// ========================================
// Level 2: Specific Discourse Patterns
// ========================================

// Elaboration sub-types
MERGE (:DiscourseStructure {name_en: 'General-Specific', name_ja: '一般-具体', level: 2, parent: 'Elaboration', core: false});
MERGE (:DiscourseStructure {name_en: 'Part-Whole', name_ja: '部分-全体', level: 2, parent: 'Elaboration', core: false});
MERGE (:DiscourseStructure {name_en: 'Process-Step', name_ja: 'プロセス-ステップ', level: 2, parent: 'Elaboration', core: false});
MERGE (:DiscourseStructure {name_en: 'Object-Attribute', name_ja: '対象-属性', level: 2, parent: 'Elaboration', core: false});
MERGE (:DiscourseStructure {name_en: 'Set-Member', name_ja: '集合-要素', level: 2, parent: 'Elaboration', core: false});

// Contrast sub-types
MERGE (:DiscourseStructure {name_en: 'Concession', name_ja: '譲歩', level: 2, parent: 'Contrast', core: false});
MERGE (:DiscourseStructure {name_en: 'Antithesis', name_ja: '正反対', level: 2, parent: 'Contrast', core: false});
MERGE (:DiscourseStructure {name_en: 'Comparison', name_ja: '比較', level: 2, parent: 'Contrast', core: false});

// Cause-Effect sub-types
MERGE (:DiscourseStructure {name_en: 'Direct Cause', name_ja: '直接原因', level: 2, parent: 'Volitional Cause', core: false});
MERGE (:DiscourseStructure {name_en: 'Indirect Cause', name_ja: '間接原因', level: 2, parent: 'Volitional Cause', core: false});
MERGE (:DiscourseStructure {name_en: 'Enabling Cause', name_ja: '可能化原因', level: 2, parent: 'Volitional Cause', core: false});

// Temporal sub-types
MERGE (:DiscourseStructure {name_en: 'Before', name_ja: '前', level: 2, parent: 'Sequence', core: false});
MERGE (:DiscourseStructure {name_en: 'After', name_ja: '後', level: 2, parent: 'Sequence', core: false});
MERGE (:DiscourseStructure {name_en: 'Simultaneous', name_ja: '同時', level: 2, parent: 'Sequence', core: false});

// Japanese-specific discourse markers
MERGE (:DiscourseStructure {name_en: 'Demo (but)', name_ja: 'でも', level: 2, parent: 'Contrast', core: false});
MERGE (:DiscourseStructure {name_en: 'Shikashi (however)', name_ja: 'しかし', level: 2, parent: 'Contrast', core: false});
MERGE (:DiscourseStructure {name_en: 'Tsumari (in other words)', name_ja: 'つまり', level: 2, parent: 'Restatement', core: false});
MERGE (:DiscourseStructure {name_en: 'Tatoeba (for example)', name_ja: '例えば', level: 2, parent: 'Evidence', core: false});
MERGE (:DiscourseStructure {name_en: 'Dakara (therefore)', name_ja: 'だから', level: 2, parent: 'Volitional Result', core: false});

// ========================================
// CREATE INDEXES
// ========================================

CREATE INDEX discourse_structure_name_en IF NOT EXISTS FOR (d:DiscourseStructure) ON (d.name_en);
CREATE INDEX discourse_structure_level IF NOT EXISTS FOR (d:DiscourseStructure) ON (d.level);
CREATE INDEX discourse_structure_core IF NOT EXISTS FOR (d:DiscourseStructure) ON (d.core);
CREATE INDEX discourse_structure_rst IF NOT EXISTS FOR (d:DiscourseStructure) ON (d.rst_type);
CREATE INDEX discourse_structure_schema IF NOT EXISTS FOR (d:DiscourseStructure) ON (d.schema_type);

// ========================================
// REFERENCES
// ========================================
// - Mann, W. C., & Thompson, S. A. (1988). Rhetorical Structure Theory
// - Taboada, M., & Mann, W. C. (2006). RST Website
// - Marcu, D. (2000). The Theory and Practice of Discourse Parsing
// - Japanese discourse markers from linguistic research