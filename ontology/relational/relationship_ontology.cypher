// Golden AGI Relationship Ontology – Node Creation Script
// Based on social psychology theories:
// - Knapp & Vangelisti: Coming Together/Coming Apart 10 stages
// - Altman & Taylor: Social Penetration Theory 5 stages  
// - Sternberg: Triangular Theory of Love 7 love styles
// Structure: Type (Level 0) → Stage (Level 1) → State (Level 2)

// ========================================
// CORE RELATIONSHIP TYPES (Level 0)
// ========================================

MERGE (:Relation {name_en: 'FAMILY', name_ja: '家族', level: 0, core: true});
MERGE (:Relation {name_en: 'FRIENDSHIP', name_ja: '友情', level: 0, core: true});
MERGE (:Relation {name_en: 'ROMANTIC', name_ja: '恋愛', level: 0, core: true});
MERGE (:Relation {name_en: 'PROFESSIONAL', name_ja: '職業的関係', level: 0, core: true});
MERGE (:Relation {name_en: 'COMMUNITY', name_ja: '共同体', level: 0, core: true});
MERGE (:Relation {name_en: 'RIVALRY', name_ja: '敵対', level: 0, core: true});

// ========================================
// RELATIONSHIP DEVELOPMENT – COMING TOGETHER
// ========================================

// Level 1 – Category
MERGE (:Relation {name_en: 'Coming Together', name_ja: '関係形成', level: 1, core: false});

// Level 2 – Specific stages (Knapp's model)
MERGE (:Relation {name_en: 'Initiating', name_ja: '開始', level: 2, core: false});
MERGE (:Relation {name_en: 'Experimenting', name_ja: '試行', level: 2, core: false});
MERGE (:Relation {name_en: 'Intensifying', name_ja: '深化', level: 2, core: false});
MERGE (:Relation {name_en: 'Integrating', name_ja: '統合', level: 2, core: false});
MERGE (:Relation {name_en: 'Bonding', name_ja: '結束', level: 2, core: false});

// ========================================
// RELATIONSHIP DEVELOPMENT – MAINTENANCE
// ========================================

MERGE (:Relation {name_en: 'Relational Maintenance', name_ja: '関係維持', level: 1, core: false});

// Level 2 – Illustrative maintenance states
MERGE (:Relation {name_en: 'Routine Support', name_ja: '日常的支援', level: 2, core: false});
MERGE (:Relation {name_en: 'Conflict Management', name_ja: '葛藤調整', level: 2, core: false});
MERGE (:Relation {name_en: 'Rituals & Traditions', name_ja: '儀礼・伝統', level: 2, core: false});

// ========================================
// RELATIONSHIP DEVELOPMENT – COMING APART
// ========================================

MERGE (:Relation {name_en: 'Coming Apart', name_ja: '関係解消', level: 1, core: false});

// Level 2 – Specific stages (Knapp's model)
MERGE (:Relation {name_en: 'Differentiating', name_ja: '差別化', level: 2, core: false});
MERGE (:Relation {name_en: 'Circumscribing', name_ja: '限定化', level: 2, core: false});
MERGE (:Relation {name_en: 'Stagnating', name_ja: '停滞', level: 2, core: false});
MERGE (:Relation {name_en: 'Avoiding', name_ja: '回避', level: 2, core: false});
MERGE (:Relation {name_en: 'Terminating', name_ja: '終結', level: 2, core: false});

// ========================================
// INTIMACY DEPTH (Social Penetration Theory)
// ========================================

MERGE (:Relation {name_en: 'Intimacy Depth', name_ja: '親密度段階', level: 1, core: false});

// Level 2 – Altman & Taylor's stages
MERGE (:Relation {name_en: 'Orientation', name_ja: 'オリエンテーション', level: 2, core: false});
MERGE (:Relation {name_en: 'Exploratory Affective Exchange', name_ja: '探求的感情交換', level: 2, core: false});
MERGE (:Relation {name_en: 'Affective Exchange', name_ja: '感情交換', level: 2, core: false});
MERGE (:Relation {name_en: 'Stable Exchange', name_ja: '安定交換', level: 2, core: false});
MERGE (:Relation {name_en: 'Depenetration', name_ja: '親密度低下', level: 2, core: false});

// ========================================
// LOVE STYLE TYPOLOGY (Triangular Theory)
// ========================================

MERGE (:Relation {name_en: 'Love Styles', name_ja: '愛のスタイル', level: 1, core: false});

// Level 2 – Sternberg's 7 love types
MERGE (:Relation {name_en: 'Liking', name_ja: '友情的好意', level: 2, core: false});
MERGE (:Relation {name_en: 'Infatuation', name_ja: '恋い焦がれ', level: 2, core: false});
MERGE (:Relation {name_en: 'Empty Love', name_ja: '空虚な愛', level: 2, core: false});
MERGE (:Relation {name_en: 'Romantic Love', name_ja: 'ロマンティックラブ', level: 2, core: false});
MERGE (:Relation {name_en: 'Companionate Love', name_ja: '友愛的愛情', level: 2, core: false});
MERGE (:Relation {name_en: 'Fatuous Love', name_ja: '愚かな愛', level: 2, core: false});
MERGE (:Relation {name_en: 'Consummate Love', name_ja: '完全な愛', level: 2, core: false});

// ========================================
// ADDITIONAL JAPANESE RELATIONSHIP CONCEPTS
// ========================================

// Level 1 – Japanese-specific relationship dynamics
MERGE (:Relation {name_en: 'Japanese Social Relations', name_ja: '日本的関係性', level: 1, core: false});

// Level 2 – Specific Japanese concepts
MERGE (:Relation {name_en: 'Senpai-Kohai', name_ja: '先輩後輩', level: 2, core: false});
MERGE (:Relation {name_en: 'On-Giri', name_ja: '恩義', level: 2, core: false});
MERGE (:Relation {name_en: 'Ninjo', name_ja: '人情', level: 2, core: false});
MERGE (:Relation {name_en: 'Tatemae-Honne', name_ja: '建前本音', level: 2, core: false});
MERGE (:Relation {name_en: 'Amae', name_ja: '甘え', level: 2, core: false});

// ========================================
// PERFORMANCE INDEXES
// ========================================

CREATE INDEX relation_name_en IF NOT EXISTS FOR (r:Relation) ON (r.name_en);
CREATE INDEX relation_level IF NOT EXISTS FOR (r:Relation) ON (r.level);
CREATE INDEX relation_core IF NOT EXISTS FOR (r:Relation) ON (r.core);

// ========================================
// VERIFICATION QUERY
// ========================================
// Run this to verify node creation:
// MATCH (r:Relation) RETURN r.level, count(r) ORDER BY r.level;

// ========================================
// REFERENCES
// ========================================
// - Knapp, M. L., & Vangelisti, A. L. (2005). Interpersonal Communication and Human Relationships
// - Altman, I., & Taylor, D. A. (1973). Social Penetration Theory
// - Sternberg, R. J. (1986). A Triangular Theory of Love
// - Additional Japanese relationship concepts from cultural anthropology