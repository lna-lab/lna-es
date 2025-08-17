// Temporal Ontology - Time Expressions Across Genres
// Collected from AI collaborators - based on linguistics, narratology, philosophy, and cognitive psychology
// 3-level hierarchy following emotion ontology structure

// ========================================
// Level 0: Core time concepts (fundamental temporal categories)
// ========================================

MERGE (:TimeConcept { name_en: "Moment", name_ja: "瞬間", level: 0, core: true });
MERGE (:TimeConcept { name_en: "Duration", name_ja: "期間", level: 0, core: true });
MERGE (:TimeConcept { name_en: "Cycle", name_ja: "循環", level: 0, core: true });
MERGE (:TimeConcept { name_en: "Qualitative Time", name_ja: "質的時間", level: 0, core: true });

// ========================================
// Level 1: Categories and sub-concepts for each core concept
// ========================================

// Moment (瞬間) - Points in time and instants
MERGE (:TimeConcept { name_en: "Present Moment", name_ja: "現在", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Instant", name_ja: "瞬時", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Significant Moment", name_ja: "重要な瞬間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Transitional Moment", name_ja: "境界の瞬間", level: 1, core: false });

// Duration (期間) - Linear time and spans
MERGE (:TimeConcept { name_en: "Chronological Time", name_ja: "直線的時間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Short Duration", name_ja: "短期間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Eternal Time", name_ja: "永遠の時間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Historical Time", name_ja: "歴史的時間", level: 1, core: false });

// Cycle (循環) - Cyclical and repeating time
MERGE (:TimeConcept { name_en: "Natural Cycle", name_ja: "自然の循環", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Life Cycle", name_ja: "生命の循環", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Cosmic Cycle", name_ja: "宇宙の循環", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Time Loop", name_ja: "時間ループ", level: 1, core: false });

// Qualitative Time (質的時間) - Subjective and experiential time
MERGE (:TimeConcept { name_en: "Subjective Time", name_ja: "主観的時間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Sacred/Mythic Time", name_ja: "聖なる時間", level: 1, core: false });
MERGE (:TimeConcept { name_en: "Non-linear Time", name_ja: "非線形時間", level: 1, core: false });

// ========================================
// Level 2: Concrete expressions and specific examples
// ========================================

// Moment examples
MERGE (:TimeConcept { name_en: "Now", name_ja: "今", level: 2, core: false });
MERGE (:TimeConcept { name_en: "In an instant", name_ja: "瞬く間に", level: 2, core: false });
MERGE (:TimeConcept { name_en: "At that moment", name_ja: "その瞬間", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Moment of truth", name_ja: "真実の瞬間", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Climactic moment", name_ja: "クライマックスの瞬間", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Dawn", name_ja: "夜明け", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Midnight", name_ja: "真夜中", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Just then", name_ja: "ちょうどその時", level: 2, core: false });

// Duration examples
MERGE (:TimeConcept { name_en: "Past", name_ja: "過去", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Future", name_ja: "未来", level: 2, core: false });
MERGE (:TimeConcept { name_en: "For a while", name_ja: "しばらく", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Fleeting moment", name_ja: "束の間", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Eternity", name_ja: "永遠", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Once upon a time", name_ja: "昔々", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Ancient times", name_ja: "古代", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Golden Age", name_ja: "黄金時代", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Eventually", name_ja: "やがて", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Before long", name_ja: "程なく", level: 2, core: false });

// Cycle examples
MERGE (:TimeConcept { name_en: "Day and night", name_ja: "昼夜", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Four seasons", name_ja: "四季", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Every day", name_ja: "毎日", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Reincarnation", name_ja: "輪廻転生", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Eternal return", name_ja: "永劫回帰", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Groundhog Day loop", name_ja: "繰り返す一日", level: 2, core: false });
MERGE (:TimeConcept { name_en: "History repeats", name_ja: "歴史は繰り返す", level: 2, core: false });

// Qualitative Time examples
MERGE (:TimeConcept { name_en: "Time flies", name_ja: "光陰矢の如し", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Time drags", name_ja: "時間が長く感じる", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Dreamtime", name_ja: "夢の時間", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Kairos (opportune moment)", name_ja: "好機", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Flashback", name_ja: "回想", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Flash-forward", name_ja: "未来への跳躍", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Time travel", name_ja: "タイムトラベル", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Parallel timeline", name_ja: "並行時間軸", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Sacred ritual time", name_ja: "儀式的時間", level: 2, core: false });

// Additional Japanese temporal expressions
MERGE (:TimeConcept { name_en: "Gradually", name_ja: "いつしか", level: 2, core: false });
MERGE (:TimeConcept { name_en: "In those days", name_ja: "その頃", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Someday", name_ja: "いつか", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Just now", name_ja: "たった今", level: 2, core: false });
MERGE (:TimeConcept { name_en: "Long ago", name_ja: "ずっと前", level: 2, core: false });

// ========================================
// Create indexes for better performance
// ========================================

CREATE INDEX time_concept_name_en IF NOT EXISTS FOR (t:TimeConcept) ON (t.name_en);
CREATE INDEX time_concept_level IF NOT EXISTS FOR (t:TimeConcept) ON (t.level);
CREATE INDEX time_concept_core IF NOT EXISTS FOR (t:TimeConcept) ON (t.core);

// ========================================
// References
// ========================================
// Based on:
// - Narratology: Genette's narrative time theory (order, duration, frequency)
// - Philosophy: Chronos vs Kairos distinction, Bergson's durée
// - Psychology: Subjective time perception and flow states
// - Mythology: Eliade's sacred vs profane time, cyclical time concepts
// - Linguistics: Tense, aspect, and temporal expressions
// - Science Fiction: Time loops, time travel, alternate timelines