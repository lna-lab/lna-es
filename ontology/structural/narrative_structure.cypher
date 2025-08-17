// Golden AGI Narrative Structure Ontology
// Based on narratology, story theory, and literary analysis
// Structure: Type (Level 0) → Category (Level 1) → Specific Pattern (Level 2)

// ========================================
// NARRATIVE UNITS (Level 0)
// ========================================

MERGE (:NarrativeStructure {name_en: 'NARRATIVE_UNIT', name_ja: '物語単位', level: 0, core: true});
MERGE (:NarrativeStructure {name_en: 'PLOT_DEVICE', name_ja: 'プロット装置', level: 0, core: true});
MERGE (:NarrativeStructure {name_en: 'STORY_ARC', name_ja: '物語の弧', level: 0, core: true});

// ========================================
// NARRATIVE UNITS - Traditional Structures (Level 1)
// ========================================

// Kishōtenketsu (起承転結) - Japanese 4-act structure
MERGE (:NarrativeStructure {name_en: 'Introduction (Ki)', name_ja: '起', level: 1, stage: 'ki', core: false});
MERGE (:NarrativeStructure {name_en: 'Development (Sho)', name_ja: '承', level: 1, stage: 'sho', core: false});
MERGE (:NarrativeStructure {name_en: 'Twist (Ten)', name_ja: '転', level: 1, stage: 'ten', core: false});
MERGE (:NarrativeStructure {name_en: 'Conclusion (Ketsu)', name_ja: '結', level: 1, stage: 'ketsu', core: false});

// Three-Act Structure
MERGE (:NarrativeStructure {name_en: 'Setup', name_ja: '設定', level: 1, act: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Confrontation', name_ja: '対立', level: 1, act: 2, core: false});
MERGE (:NarrativeStructure {name_en: 'Resolution', name_ja: '解決', level: 1, act: 3, core: false});

// Freytag's Pyramid
MERGE (:NarrativeStructure {name_en: 'Exposition', name_ja: '導入', level: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Rising Action', name_ja: '上昇', level: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Climax', name_ja: 'クライマックス', level: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Falling Action', name_ja: '下降', level: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Denouement', name_ja: '結末', level: 1, core: false});

// ========================================
// PLOT DEVICES (Level 1)
// ========================================

// Narrative Techniques
MERGE (:NarrativeStructure {name_en: 'Foreshadowing', name_ja: '伏線', level: 1, device_type: 'foreshadow', core: false});
MERGE (:NarrativeStructure {name_en: 'Flashback', name_ja: '回想', level: 1, device_type: 'flashback', core: false});
MERGE (:NarrativeStructure {name_en: 'Flash-forward', name_ja: '未来予示', level: 1, device_type: 'flash_forward', core: false});
MERGE (:NarrativeStructure {name_en: 'Plot Twist', name_ja: 'どんでん返し', level: 1, device_type: 'twist', core: false});
MERGE (:NarrativeStructure {name_en: 'Cliffhanger', name_ja: 'クリフハンガー', level: 1, device_type: 'cliffhanger', core: false});
MERGE (:NarrativeStructure {name_en: 'Red Herring', name_ja: 'ミスリード', level: 1, device_type: 'red_herring', core: false});
MERGE (:NarrativeStructure {name_en: 'Deus Ex Machina', name_ja: '機械仕掛けの神', level: 1, device_type: 'deus_ex_machina', core: false});
MERGE (:NarrativeStructure {name_en: 'MacGuffin', name_ja: 'マクガフィン', level: 1, device_type: 'macguffin', core: false});

// Turning Points
MERGE (:NarrativeStructure {name_en: 'Inciting Incident', name_ja: '発端', level: 1, device_type: 'inciting_incident', core: false});
MERGE (:NarrativeStructure {name_en: 'Point of No Return', name_ja: '引き返せない点', level: 1, device_type: 'point_of_no_return', core: false});
MERGE (:NarrativeStructure {name_en: 'Crisis', name_ja: '危機', level: 1, device_type: 'crisis', core: false});
MERGE (:NarrativeStructure {name_en: 'Catharsis', name_ja: 'カタルシス', level: 1, device_type: 'catharsis', core: false});

// ========================================
// STORY ARCS (Level 1)
// ========================================

// Hero's Journey (Campbell/Vogler)
MERGE (:NarrativeStructure {name_en: 'Ordinary World', name_ja: '日常世界', level: 1, journey_stage: 1, core: false});
MERGE (:NarrativeStructure {name_en: 'Call to Adventure', name_ja: '冒険への呼びかけ', level: 1, journey_stage: 2, core: false});
MERGE (:NarrativeStructure {name_en: 'Refusal of Call', name_ja: '呼びかけの拒否', level: 1, journey_stage: 3, core: false});
MERGE (:NarrativeStructure {name_en: 'Meeting Mentor', name_ja: '賢者との出会い', level: 1, journey_stage: 4, core: false});
MERGE (:NarrativeStructure {name_en: 'Crossing Threshold', name_ja: '第一関門', level: 1, journey_stage: 5, core: false});
MERGE (:NarrativeStructure {name_en: 'Tests and Trials', name_ja: '試練', level: 1, journey_stage: 6, core: false});
MERGE (:NarrativeStructure {name_en: 'Approach', name_ja: '最も危険な場所への接近', level: 1, journey_stage: 7, core: false});
MERGE (:NarrativeStructure {name_en: 'Ordeal', name_ja: '最大の試練', level: 1, journey_stage: 8, core: false});
MERGE (:NarrativeStructure {name_en: 'Reward', name_ja: '報酬', level: 1, journey_stage: 9, core: false});
MERGE (:NarrativeStructure {name_en: 'The Road Back', name_ja: '帰路', level: 1, journey_stage: 10, core: false});
MERGE (:NarrativeStructure {name_en: 'Resurrection', name_ja: '復活', level: 1, journey_stage: 11, core: false});
MERGE (:NarrativeStructure {name_en: 'Return with Elixir', name_ja: '宝を持っての帰還', level: 1, journey_stage: 12, core: false});

// ========================================
// Level 2: Specific Examples and Patterns
// ========================================

// Ki (起) sub-types
MERGE (:NarrativeStructure {name_en: 'Setting Introduction', name_ja: '舞台設定', level: 2, parent: 'Introduction', core: false});
MERGE (:NarrativeStructure {name_en: 'Character Introduction', name_ja: '人物紹介', level: 2, parent: 'Introduction', core: false});
MERGE (:NarrativeStructure {name_en: 'Status Quo', name_ja: '現状描写', level: 2, parent: 'Introduction', core: false});

// Sho (承) sub-types
MERGE (:NarrativeStructure {name_en: 'Deepening', name_ja: '深化', level: 2, parent: 'Development', core: false});
MERGE (:NarrativeStructure {name_en: 'Expansion', name_ja: '展開', level: 2, parent: 'Development', core: false});
MERGE (:NarrativeStructure {name_en: 'Complication', name_ja: '複雑化', level: 2, parent: 'Development', core: false});

// Ten (転) sub-types
MERGE (:NarrativeStructure {name_en: 'Major Twist', name_ja: '大転換', level: 2, parent: 'Twist', core: false});
MERGE (:NarrativeStructure {name_en: 'Revelation', name_ja: '真相開示', level: 2, parent: 'Twist', core: false});
MERGE (:NarrativeStructure {name_en: 'Reversal', name_ja: '逆転', level: 2, parent: 'Twist', core: false});

// Ketsu (結) sub-types
MERGE (:NarrativeStructure {name_en: 'Resolution', name_ja: '解決', level: 2, parent: 'Conclusion', core: false});
MERGE (:NarrativeStructure {name_en: 'New Equilibrium', name_ja: '新たな均衡', level: 2, parent: 'Conclusion', core: false});
MERGE (:NarrativeStructure {name_en: 'Open Ending', name_ja: '開かれた結末', level: 2, parent: 'Conclusion', core: false});

// ========================================
// CREATE INDEXES
// ========================================

CREATE INDEX narrative_structure_name_en IF NOT EXISTS FOR (n:NarrativeStructure) ON (n.name_en);
CREATE INDEX narrative_structure_level IF NOT EXISTS FOR (n:NarrativeStructure) ON (n.level);
CREATE INDEX narrative_structure_core IF NOT EXISTS FOR (n:NarrativeStructure) ON (n.core);
CREATE INDEX narrative_structure_stage IF NOT EXISTS FOR (n:NarrativeStructure) ON (n.stage);
CREATE INDEX narrative_structure_device IF NOT EXISTS FOR (n:NarrativeStructure) ON (n.device_type);

// ========================================
// REFERENCES
// ========================================
// - Kishōtenketsu: Traditional Japanese/Chinese narrative structure
// - Three-Act Structure: Syd Field's screenplay paradigm
// - Freytag's Pyramid: Gustav Freytag's dramatic structure
// - Hero's Journey: Joseph Campbell's monomyth
// - Plot devices: Various narratological sources