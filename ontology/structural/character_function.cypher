// Golden AGI Character Function Ontology
// Based on Propp's 31 functions, Campbell's archetypes, and narratology
// Structure: Function Type (Level 0) → Role Category (Level 1) → Specific Function (Level 2)

// ========================================
// CORE CHARACTER FUNCTION TYPES (Level 0)
// ========================================

MERGE (:CharacterFunction {name_en: 'NARRATIVE_ROLE', name_ja: '物語役割', level: 0, core: true});
MERGE (:CharacterFunction {name_en: 'PROPP_FUNCTION', name_ja: 'プロップ機能', level: 0, core: true});
MERGE (:CharacterFunction {name_en: 'ARCHETYPE', name_ja: '原型', level: 0, core: true});

// ========================================
// NARRATIVE ROLES (Level 1)
// ========================================

// Primary Roles
MERGE (:CharacterFunction {name_en: 'Protagonist', name_ja: '主人公', level: 1, role_type: 'primary', core: false});
MERGE (:CharacterFunction {name_en: 'Antagonist', name_ja: '敵対者', level: 1, role_type: 'primary', core: false});
MERGE (:CharacterFunction {name_en: 'Deuteragonist', name_ja: '準主人公', level: 1, role_type: 'primary', core: false});
MERGE (:CharacterFunction {name_en: 'Tritagonist', name_ja: '第三の主要人物', level: 1, role_type: 'primary', core: false});

// Supporting Roles
MERGE (:CharacterFunction {name_en: 'Mentor', name_ja: '導師', level: 1, role_type: 'support', core: false});
MERGE (:CharacterFunction {name_en: 'Sidekick', name_ja: '相棒', level: 1, role_type: 'support', core: false});
MERGE (:CharacterFunction {name_en: 'Love Interest', name_ja: '恋愛対象', level: 1, role_type: 'support', core: false});
MERGE (:CharacterFunction {name_en: 'Comic Relief', name_ja: '道化役', level: 1, role_type: 'support', core: false});
MERGE (:CharacterFunction {name_en: 'Foil', name_ja: '対照的人物', level: 1, role_type: 'support', core: false});

// Functional Roles
MERGE (:CharacterFunction {name_en: 'Narrator', name_ja: '語り手', level: 1, role_type: 'functional', core: false});
MERGE (:CharacterFunction {name_en: 'Messenger', name_ja: '使者', level: 1, role_type: 'functional', core: false});
MERGE (:CharacterFunction {name_en: 'Guardian', name_ja: '守護者', level: 1, role_type: 'functional', core: false});
MERGE (:CharacterFunction {name_en: 'Tempter', name_ja: '誘惑者', level: 1, role_type: 'functional', core: false});

// ========================================
// PROPP'S 31 FUNCTIONS (Level 1)
// ========================================

// Initial Situation & Preparation
MERGE (:CharacterFunction {name_en: 'Absentation', name_ja: '不在', level: 1, propp_number: 1, core: false});
MERGE (:CharacterFunction {name_en: 'Interdiction', name_ja: '禁止', level: 1, propp_number: 2, core: false});
MERGE (:CharacterFunction {name_en: 'Violation', name_ja: '違反', level: 1, propp_number: 3, core: false});
MERGE (:CharacterFunction {name_en: 'Reconnaissance', name_ja: '偵察', level: 1, propp_number: 4, core: false});
MERGE (:CharacterFunction {name_en: 'Delivery', name_ja: '情報伝達', level: 1, propp_number: 5, core: false});
MERGE (:CharacterFunction {name_en: 'Trickery', name_ja: '策略', level: 1, propp_number: 6, core: false});
MERGE (:CharacterFunction {name_en: 'Complicity', name_ja: '幇助', level: 1, propp_number: 7, core: false});

// Complication
MERGE (:CharacterFunction {name_en: 'Villainy', name_ja: '加害', level: 1, propp_number: 8, core: false});
MERGE (:CharacterFunction {name_en: 'Lack', name_ja: '欠如', level: 1, propp_number: 8, core: false});
MERGE (:CharacterFunction {name_en: 'Mediation', name_ja: '仲介', level: 1, propp_number: 9, core: false});
MERGE (:CharacterFunction {name_en: 'Beginning Counter-action', name_ja: '対抗開始', level: 1, propp_number: 10, core: false});
MERGE (:CharacterFunction {name_en: 'Departure', name_ja: '出発', level: 1, propp_number: 11, core: false});

// Donor Sequence
MERGE (:CharacterFunction {name_en: 'First Donor Function', name_ja: '贈与者の第一機能', level: 1, propp_number: 12, core: false});
MERGE (:CharacterFunction {name_en: 'Hero Reaction', name_ja: '主人公の反応', level: 1, propp_number: 13, core: false});
MERGE (:CharacterFunction {name_en: 'Receipt of Agent', name_ja: '呪具の贈与', level: 1, propp_number: 14, core: false});

// Action Sequence
MERGE (:CharacterFunction {name_en: 'Spatial Transference', name_ja: '空間移動', level: 1, propp_number: 15, core: false});
MERGE (:CharacterFunction {name_en: 'Struggle', name_ja: '闘争', level: 1, propp_number: 16, core: false});
MERGE (:CharacterFunction {name_en: 'Branding', name_ja: '標付け', level: 1, propp_number: 17, core: false});
MERGE (:CharacterFunction {name_en: 'Victory', name_ja: '勝利', level: 1, propp_number: 18, core: false});
MERGE (:CharacterFunction {name_en: 'Liquidation', name_ja: '欠如の解消', level: 1, propp_number: 19, core: false});
MERGE (:CharacterFunction {name_en: 'Return', name_ja: '帰還', level: 1, propp_number: 20, core: false});
MERGE (:CharacterFunction {name_en: 'Pursuit', name_ja: '追跡', level: 1, propp_number: 21, core: false});
MERGE (:CharacterFunction {name_en: 'Rescue', name_ja: '救助', level: 1, propp_number: 22, core: false});

// Recognition Sequence
MERGE (:CharacterFunction {name_en: 'Unrecognized Arrival', name_ja: '気づかれぬ到着', level: 1, propp_number: 23, core: false});
MERGE (:CharacterFunction {name_en: 'Unfounded Claims', name_ja: '不当な要求', level: 1, propp_number: 24, core: false});
MERGE (:CharacterFunction {name_en: 'Difficult Task', name_ja: '難題', level: 1, propp_number: 25, core: false});
MERGE (:CharacterFunction {name_en: 'Solution', name_ja: '解決', level: 1, propp_number: 26, core: false});
MERGE (:CharacterFunction {name_en: 'Recognition', name_ja: '認知', level: 1, propp_number: 27, core: false});
MERGE (:CharacterFunction {name_en: 'Exposure', name_ja: '暴露', level: 1, propp_number: 28, core: false});
MERGE (:CharacterFunction {name_en: 'Transfiguration', name_ja: '変身', level: 1, propp_number: 29, core: false});
MERGE (:CharacterFunction {name_en: 'Punishment', name_ja: '処罰', level: 1, propp_number: 30, core: false});
MERGE (:CharacterFunction {name_en: 'Wedding', name_ja: '結婚', level: 1, propp_number: 31, core: false});

// ========================================
// ARCHETYPES (Level 1)
// ========================================

// Jungian Archetypes
MERGE (:CharacterFunction {name_en: 'The Hero', name_ja: '英雄', level: 1, archetype: 'jungian', core: false});
MERGE (:CharacterFunction {name_en: 'The Shadow', name_ja: '影', level: 1, archetype: 'jungian', core: false});
MERGE (:CharacterFunction {name_en: 'The Anima/Animus', name_ja: 'アニマ/アニムス', level: 1, archetype: 'jungian', core: false});
MERGE (:CharacterFunction {name_en: 'The Self', name_ja: '自己', level: 1, archetype: 'jungian', core: false});

// Campbell/Vogler Archetypes
MERGE (:CharacterFunction {name_en: 'The Shapeshifter', name_ja: '変化する者', level: 1, archetype: 'campbell', core: false});
MERGE (:CharacterFunction {name_en: 'The Threshold Guardian', name_ja: '門番', level: 1, archetype: 'campbell', core: false});
MERGE (:CharacterFunction {name_en: 'The Herald', name_ja: '使者', level: 1, archetype: 'campbell', core: false});
MERGE (:CharacterFunction {name_en: 'The Trickster', name_ja: 'トリックスター', level: 1, archetype: 'campbell', core: false});

// ========================================
// Level 2: Specific Character Types
// ========================================

// Hero Sub-types
MERGE (:CharacterFunction {name_en: 'Reluctant Hero', name_ja: '消極的英雄', level: 2, parent: 'Hero', core: false});
MERGE (:CharacterFunction {name_en: 'Anti-Hero', name_ja: 'アンチヒーロー', level: 2, parent: 'Hero', core: false});
MERGE (:CharacterFunction {name_en: 'Tragic Hero', name_ja: '悲劇的英雄', level: 2, parent: 'Hero', core: false});

// Mentor Sub-types
MERGE (:CharacterFunction {name_en: 'Wise Old Man', name_ja: '賢老', level: 2, parent: 'Mentor', core: false});
MERGE (:CharacterFunction {name_en: 'Fallen Mentor', name_ja: '堕落した師', level: 2, parent: 'Mentor', core: false});
MERGE (:CharacterFunction {name_en: 'Hidden Mentor', name_ja: '隠れた導師', level: 2, parent: 'Mentor', core: false});

// Antagonist Sub-types
MERGE (:CharacterFunction {name_en: 'Evil Overlord', name_ja: '暗黒の支配者', level: 2, parent: 'Antagonist', core: false});
MERGE (:CharacterFunction {name_en: 'Corrupted Hero', name_ja: '堕落した英雄', level: 2, parent: 'Antagonist', core: false});
MERGE (:CharacterFunction {name_en: 'Force of Nature', name_ja: '自然の脅威', level: 2, parent: 'Antagonist', core: false});

// Japanese-specific Roles
MERGE (:CharacterFunction {name_en: 'Tsundere', name_ja: 'ツンデレ', level: 2, parent: 'Love Interest', core: false});
MERGE (:CharacterFunction {name_en: 'Sensei', name_ja: '先生', level: 2, parent: 'Mentor', core: false});
MERGE (:CharacterFunction {name_en: 'Kohai', name_ja: '後輩', level: 2, parent: 'Sidekick', core: false});

// ========================================
// CREATE INDEXES
// ========================================

CREATE INDEX character_function_name_en IF NOT EXISTS FOR (c:CharacterFunction) ON (c.name_en);
CREATE INDEX character_function_level IF NOT EXISTS FOR (c:CharacterFunction) ON (c.level);
CREATE INDEX character_function_core IF NOT EXISTS FOR (c:CharacterFunction) ON (c.core);
CREATE INDEX character_function_propp IF NOT EXISTS FOR (c:CharacterFunction) ON (c.propp_number);
CREATE INDEX character_function_archetype IF NOT EXISTS FOR (c:CharacterFunction) ON (c.archetype);

// ========================================
// REFERENCES
// ========================================
// - Vladimir Propp: Morphology of the Folktale (31 functions)
// - Joseph Campbell: The Hero with a Thousand Faces
// - Christopher Vogler: The Writer's Journey
// - Carl Jung: Archetypes and the Collective Unconscious