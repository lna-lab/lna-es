// Golden AGI Causality Ontology - Node Creation Script
// Based on narrative causality research and philosophical traditions:
// - Hu & Walker 2017: Narrative Causality typology
// - Aristotle's Four Causes
// - Literary studies of chance and coincidence
// - Classical/Stoic conceptions of fate
// Structure: Causal Mode (Level 0) → Causal Type (Level 1) → Specific Pattern (Level 2)

// ========================================
// CORE CAUSAL MODES (Level 0)
// ========================================

MERGE (:Causality {name_en: 'NECESSITY', name_ja: '必然', level: 0, core: true});
MERGE (:Causality {name_en: 'CONTINGENCY', name_ja: '偶然', level: 0, core: true});
MERGE (:Causality {name_en: 'FATE', name_ja: '運命', level: 0, core: true});

// ========================================
// NECESSITY (Level 1)
// Based on Hu & Walker's 4 types of narrative causality
// ========================================

MERGE (:Causality {name_en: 'Physical', name_ja: '物理因果', level: 1, core: false});
MERGE (:Causality {name_en: 'Motivational', name_ja: '動機因果', level: 1, core: false});
MERGE (:Causality {name_en: 'Psychological', name_ja: '心理因果', level: 1, core: false});
MERGE (:Causality {name_en: 'Enabling', name_ja: '条件因果', level: 1, core: false});

// Level 2 - Physical sub-types (Aristotelian causes)
MERGE (:Causality {name_en: 'Material Cause', name_ja: '質料因', level: 2, core: false});
MERGE (:Causality {name_en: 'Efficient Cause', name_ja: '作用因', level: 2, core: false});
MERGE (:Causality {name_en: 'Natural Law', name_ja: '自然法則', level: 2, core: false});
MERGE (:Causality {name_en: 'Mechanical', name_ja: '機械的因果', level: 2, core: false});

// Level 2 - Motivational sub-types
MERGE (:Causality {name_en: 'Goal-Driven', name_ja: '目的追求', level: 2, core: false});
MERGE (:Causality {name_en: 'Revenge', name_ja: '復讐動機', level: 2, core: false});
MERGE (:Causality {name_en: 'Love-Driven', name_ja: '愛情動機', level: 2, core: false});
MERGE (:Causality {name_en: 'Duty-Bound', name_ja: '義務遂行', level: 2, core: false});

// Level 2 - Psychological sub-types
MERGE (:Causality {name_en: 'Fear-Induced', name_ja: '恐怖誘発', level: 2, core: false});
MERGE (:Causality {name_en: 'Desire-Induced', name_ja: '欲望誘発', level: 2, core: false});
MERGE (:Causality {name_en: 'Trauma-Driven', name_ja: 'トラウマ起因', level: 2, core: false});
MERGE (:Causality {name_en: 'Belief-Based', name_ja: '信念基盤', level: 2, core: false});

// Level 2 - Enabling sub-types
MERGE (:Causality {name_en: 'Opportunity', name_ja: '機会創出', level: 2, core: false});
MERGE (:Causality {name_en: 'Resource Flow', name_ja: '資源供与', level: 2, core: false});
MERGE (:Causality {name_en: 'Permission', name_ja: '許可付与', level: 2, core: false});
MERGE (:Causality {name_en: 'Removal of Obstacle', name_ja: '障害除去', level: 2, core: false});

// ========================================
// CONTINGENCY (Level 1)
// ========================================

MERGE (:Causality {name_en: 'Chance', name_ja: 'ランダム', level: 1, core: false});
MERGE (:Causality {name_en: 'Coincidence', name_ja: '偶然の一致', level: 1, core: false});
MERGE (:Causality {name_en: 'Serendipity', name_ja: '僥倖', level: 1, core: false});
MERGE (:Causality {name_en: 'Accident', name_ja: '事故', level: 1, core: false});

// Level 2 - Chance sub-types
MERGE (:Causality {name_en: 'Random Event', name_ja: '無作為事象', level: 2, core: false});
MERGE (:Causality {name_en: 'Chaos Effect', name_ja: 'バタフライ効果', level: 2, core: false});
MERGE (:Causality {name_en: 'Stochastic', name_ja: '確率的事象', level: 2, core: false});

// Level 2 - Coincidence sub-types
MERGE (:Causality {name_en: 'Meet-Cute', name_ja: '偶然の出会い', level: 2, core: false});
MERGE (:Causality {name_en: 'Convergence', name_ja: '収束偶然', level: 2, core: false});
MERGE (:Causality {name_en: 'Synchronicity', name_ja: '共時性', level: 2, core: false});

// Level 2 - Serendipity sub-types
MERGE (:Causality {name_en: 'Happy Accident', name_ja: '幸福な偶然', level: 2, core: false});
MERGE (:Causality {name_en: 'Fortunate Mistake', name_ja: '幸運な誤り', level: 2, core: false});
MERGE (:Causality {name_en: 'Lucky Find', name_ja: '思いがけない発見', level: 2, core: false});

// Level 2 - Accident sub-types
MERGE (:Causality {name_en: 'Mishap', name_ja: '不慮の事故', level: 2, core: false});
MERGE (:Causality {name_en: 'Error', name_ja: '過失', level: 2, core: false});
MERGE (:Causality {name_en: 'Unintended Consequence', name_ja: '意図せぬ結果', level: 2, core: false});

// ========================================
// FATE (Level 1)
// ========================================

MERGE (:Causality {name_en: 'Prophecy', name_ja: '予言', level: 1, core: false});
MERGE (:Causality {name_en: 'Destiny', name_ja: '宿命', level: 1, core: false});
MERGE (:Causality {name_en: 'Divine Will', name_ja: '神意', level: 1, core: false});
MERGE (:Causality {name_en: 'Karma', name_ja: '因果応報', level: 1, core: false});

// Level 2 - Prophecy sub-types
MERGE (:Causality {name_en: 'Foretold Event', name_ja: '定められた啓示', level: 2, core: false});
MERGE (:Causality {name_en: 'Self-Fulfilling', name_ja: '自己成就予言', level: 2, core: false});
MERGE (:Causality {name_en: 'Oracle', name_ja: '神託', level: 2, core: false});

// Level 2 - Destiny sub-types
MERGE (:Causality {name_en: 'Chosen One', name_ja: '選ばれし者', level: 2, core: false});
MERGE (:Causality {name_en: 'Inescapable End', name_ja: '逃れられぬ結末', level: 2, core: false});
MERGE (:Causality {name_en: 'Fated Meeting', name_ja: '運命の出会い', level: 2, core: false});

// Level 2 - Divine Will sub-types
MERGE (:Causality {name_en: 'Providence', name_ja: '摂理', level: 2, core: false});
MERGE (:Causality {name_en: 'Divine Intervention', name_ja: '神の介入', level: 2, core: false});
MERGE (:Causality {name_en: 'Curse', name_ja: '呪い', level: 2, core: false});
MERGE (:Causality {name_en: 'Blessing', name_ja: '祝福', level: 2, core: false});

// Level 2 - Karma sub-types
MERGE (:Causality {name_en: 'Reward', name_ja: '報償', level: 2, core: false});
MERGE (:Causality {name_en: 'Retribution', name_ja: '報い', level: 2, core: false});
MERGE (:Causality {name_en: 'Karmic Cycle', name_ja: '業の循環', level: 2, core: false});
MERGE (:Causality {name_en: 'Poetic Justice', name_ja: '因果応報的正義', level: 2, core: false});

// ========================================
// ADDITIONAL JAPANESE CAUSALITY CONCEPTS
// ========================================

// Level 1 - Japanese-specific causality
MERGE (:Causality {name_en: 'En (Connection)', name_ja: '縁', level: 1, core: false});

// Level 2 - En sub-types
MERGE (:Causality {name_en: 'Musubi', name_ja: '結び', level: 2, core: false});
MERGE (:Causality {name_en: 'Kizuna', name_ja: '絆', level: 2, core: false});
MERGE (:Causality {name_en: 'Innen', name_ja: '因縁', level: 2, core: false});

// ========================================
// INDEXES (query performance)
// ========================================

CREATE INDEX causality_name_en IF NOT EXISTS FOR (c:Causality) ON (c.name_en);
CREATE INDEX causality_level IF NOT EXISTS FOR (c:Causality) ON (c.level);
CREATE INDEX causality_core IF NOT EXISTS FOR (c:Causality) ON (c.core);

// ========================================
// VERIFICATION QUERY
// ========================================
// Run this to verify node creation:
// MATCH (c:Causality) RETURN c.level, count(c) ORDER BY c.level;

// ========================================
// REFERENCES
// ========================================
// - Hu & Walker (2017). How (not) to generate a story: A computational and cognitive perspective
// - Aristotle's Four Causes (Material, Efficient, Formal, Final)
// - Literary theory on chance and coincidence
// - Classical philosophy on fate and determinism
// - Eastern philosophy on karma and causality (縁起)