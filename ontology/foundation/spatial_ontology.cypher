// LNA-ES v3.0 Spatial Ontology - Japanese Spatial Philosophy
// Based on Japanese architecture, philosophy, and anthropology
// Designed for LNA-ES v3.0 345-dimension semantic analysis

// ========================================
// CORE SPATIAL CONCEPTS (Level 0)
// ========================================

MERGE (:Spatial {name_en: 'OMOTE-URA', name_ja: '表裏', level: 0, core: true})
MERGE (:Spatial {name_en: 'UCHI-SOTO', name_ja: '内外', level: 0, core: true})
MERGE (:Spatial {name_en: 'OKU', name_ja: '奥', level: 0, core: true})
MERGE (:Spatial {name_en: 'MA', name_ja: '間', level: 0, core: true})
MERGE (:Spatial {name_en: 'KYOKAI', name_ja: '境界', level: 0, core: true})
MERGE (:Spatial {name_en: 'BASHO', name_ja: '場所', level: 0, core: true});

// ========================================
// OMOTE-URA (Front/Back Duality)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Front Face', name_ja: '表', level: 1})
MERGE (:Spatial {name_en: 'Back Side', name_ja: '裏', level: 1})
MERGE (:Spatial {name_en: 'Public Realm', name_ja: '公の領域', level: 1})
MERGE (:Spatial {name_en: 'Private Realm', name_ja: '私の領域', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Omote-Nihon', name_ja: '表日本', level: 2})
MERGE (:Spatial {name_en: 'Ura-Nihon', name_ja: '裏日本', level: 2})
MERGE (:Spatial {name_en: 'Formal Appearance', name_ja: '公的な顔', level: 2})
MERGE (:Spatial {name_en: 'Hidden Reality', name_ja: '隠された実相', level: 2})
MERGE (:Spatial {name_en: 'Social Facade', name_ja: '社会的表層', level: 2})
MERGE (:Spatial {name_en: 'True Nature', name_ja: '本性', level: 2});

// ========================================
// UCHI-SOTO (Inside/Outside Distinction)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Inner Sphere', name_ja: '内', level: 1})
MERGE (:Spatial {name_en: 'Outer Sphere', name_ja: '外', level: 1})
MERGE (:Spatial {name_en: 'In-Group Space', name_ja: '身内の空間', level: 1})
MERGE (:Spatial {name_en: 'Out-Group Space', name_ja: 'よそ者の空間', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Indoor Realm', name_ja: '室内', level: 2})
MERGE (:Spatial {name_en: 'Outside World', name_ja: '外界', level: 2})
MERGE (:Spatial {name_en: 'Genkan Entry', name_ja: '玄関', level: 2})
MERGE (:Spatial {name_en: 'Family Circle', name_ja: '家族の輪', level: 2})
MERGE (:Spatial {name_en: 'Stranger Territory', name_ja: '他者の領域', level: 2})
MERGE (:Spatial {name_en: 'Sacred Inner', name_ja: '神聖な内部', level: 2});

// ========================================
// OKU (Inner Depth)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Spatial Depth', name_ja: '空間の奥行き', level: 1})
MERGE (:Spatial {name_en: 'Hidden Realm', name_ja: '内奥の世界', level: 1})
MERGE (:Spatial {name_en: 'Mysterious Core', name_ja: '神秘的核心', level: 1})
MERGE (:Spatial {name_en: 'Unreachable Center', name_ja: '到達不能な中心', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Miegakure', name_ja: '見え隠れ', level: 2})
MERGE (:Spatial {name_en: 'Yugen Profundity', name_ja: '幽玄', level: 2})
MERGE (:Spatial {name_en: 'Garden Depth', name_ja: '庭園の奥', level: 2})
MERGE (:Spatial {name_en: 'Architectural Vista', name_ja: '建築的奥行', level: 2})
MERGE (:Spatial {name_en: 'Spiritual Depth', name_ja: '精神的深度', level: 2})
MERGE (:Spatial {name_en: 'Concealed Beauty', name_ja: '秘められた美', level: 2});

// ========================================
// MA (Interval/Space)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Spatial Interval', name_ja: '空間の間', level: 1})
MERGE (:Spatial {name_en: 'Temporal Interval', name_ja: '時間の間', level: 1})
MERGE (:Spatial {name_en: 'Negative Space', name_ja: '余白', level: 1})
MERGE (:Spatial {name_en: 'Dynamic Gap', name_ja: '動的間隙', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Tokonoma Alcove', name_ja: '床の間', level: 2})
MERGE (:Spatial {name_en: 'Pause in Speech', name_ja: '言葉の間', level: 2})
MERGE (:Spatial {name_en: 'Garden Void', name_ja: '庭の空間', level: 2})
MERGE (:Spatial {name_en: 'Musical Rest', name_ja: '音楽の休符', level: 2})
MERGE (:Spatial {name_en: 'Architectural Opening', name_ja: '建築的開口', level: 2})
MERGE (:Spatial {name_en: 'Contemplative Space', name_ja: '瞑想空間', level: 2});

// ========================================
// KYOKAI (Boundary & Threshold)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Sacred Boundary', name_ja: '結界', level: 1})
MERGE (:Spatial {name_en: 'Transitional Space', name_ja: '中間領域', level: 1})
MERGE (:Spatial {name_en: 'Liminal Zone', name_ja: '境界的空間', level: 1})
MERGE (:Spatial {name_en: 'Threshold Marker', name_ja: '境界標識', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Torii Gate', name_ja: '鳥居', level: 2})
MERGE (:Spatial {name_en: 'Engawa Veranda', name_ja: '縁側', level: 2})
MERGE (:Spatial {name_en: 'Roji Tea Path', name_ja: '露地', level: 2})
MERGE (:Spatial {name_en: 'Noren Curtain', name_ja: '暖簾', level: 2})
MERGE (:Spatial {name_en: 'Fusuma Partition', name_ja: '襖', level: 2})
MERGE (:Spatial {name_en: 'Bridge Connection', name_ja: '橋渡し', level: 2});

// ========================================
// BASHO (Encompassing Place)
// ========================================

// Level 1 - Categories
MERGE (:Spatial {name_en: 'Encompassing Field', name_ja: '包摂的な場', level: 1})
MERGE (:Spatial {name_en: 'Absolute Nothingness', name_ja: '絶対無', level: 1})
MERGE (:Spatial {name_en: 'Universal Context', name_ja: '普遍的文脈', level: 1})
MERGE (:Spatial {name_en: 'Being-Place', name_ja: '存在の場', level: 1});

// Level 2 - Specific Concepts
MERGE (:Spatial {name_en: 'Nishida Basho', name_ja: '西田の場所', level: 2})
MERGE (:Spatial {name_en: 'Phenomenal Field', name_ja: '現象の場', level: 2})
MERGE (:Spatial {name_en: 'Consciousness Space', name_ja: '意識空間', level: 2})
MERGE (:Spatial {name_en: 'Reality Container', name_ja: '実在の容器', level: 2})
MERGE (:Spatial {name_en: 'Experiential Ground', name_ja: '体験的基盤', level: 2})
MERGE (:Spatial {name_en: 'Ontological Foundation', name_ja: '存在論的基盤', level: 2});

// ========================================
// DIRECTIONAL CONCEPTS
// ========================================

// Level 1 - Basic Directions
MERGE (:Spatial {name_en: 'East', name_ja: '東', level: 1})
MERGE (:Spatial {name_en: 'West', name_ja: '西', level: 1})
MERGE (:Spatial {name_en: 'North', name_ja: '北', level: 1})
MERGE (:Spatial {name_en: 'South', name_ja: '南', level: 1})
MERGE (:Spatial {name_en: 'Up', name_ja: '上', level: 1})
MERGE (:Spatial {name_en: 'Down', name_ja: '下', level: 1});

// Level 2 - Relative Positions
MERGE (:Spatial {name_en: 'Left Side', name_ja: '左', level: 2})
MERGE (:Spatial {name_en: 'Right Side', name_ja: '右', level: 2})
MERGE (:Spatial {name_en: 'Front', name_ja: '前', level: 2})
MERGE (:Spatial {name_en: 'Back', name_ja: '後ろ', level: 2})
MERGE (:Spatial {name_en: 'Center', name_ja: '中央', level: 2})
MERGE (:Spatial {name_en: 'Edge', name_ja: '端', level: 2})
MERGE (:Spatial {name_en: 'Corner', name_ja: '角', level: 2})
MERGE (:Spatial {name_en: 'Side', name_ja: '横', level: 2});

// ========================================
// DISTANCE & SCALE
// ========================================

// Level 1 - Distance Categories
MERGE (:Spatial {name_en: 'Close', name_ja: '近い', level: 1})
MERGE (:Spatial {name_en: 'Far', name_ja: '遠い', level: 1})
MERGE (:Spatial {name_en: 'Adjacent', name_ja: '隣接', level: 1})
MERGE (:Spatial {name_en: 'Remote', name_ja: '遥か', level: 1});

// Level 2 - Specific Distances
MERGE (:Spatial {name_en: 'Very Close', name_ja: 'すぐそば', level: 2})
MERGE (:Spatial {name_en: 'Very Far', name_ja: 'はるか遠く', level: 2})
MERGE (:Spatial {name_en: 'Within Reach', name_ja: '手の届く', level: 2})
MERGE (:Spatial {name_en: 'Beyond Reach', name_ja: '手の届かない', level: 2})
MERGE (:Spatial {name_en: 'Touching', name_ja: '接触', level: 2})
MERGE (:Spatial {name_en: 'Separated', name_ja: '隔離', level: 2});

// ========================================
// Create indexes for better performance
// ========================================

CREATE INDEX spatial_name_en IF NOT EXISTS FOR (s:Spatial) ON (s.name_en);
CREATE INDEX spatial_level IF NOT EXISTS FOR (s:Spatial) ON (s.level);
CREATE INDEX spatial_core IF NOT EXISTS FOR (s:Spatial) ON (s.core);

// ========================================
// Create hierarchical relationships
// ========================================

// OMOTE-URA hierarchy
MATCH (core:Spatial {name_en: 'OMOTE-URA'})
MATCH (front:Spatial {name_en: 'Front Face'})
MATCH (back:Spatial {name_en: 'Back Side'})
MATCH (public:Spatial {name_en: 'Public Realm'})
MATCH (private:Spatial {name_en: 'Private Realm'})
MERGE (core)-[:CONTAINS]->(front)
MERGE (core)-[:CONTAINS]->(back)
MERGE (core)-[:CONTAINS]->(public)
MERGE (core)-[:CONTAINS]->(private);

// UCHI-SOTO hierarchy
MATCH (core:Spatial {name_en: 'UCHI-SOTO'})
MATCH (inner:Spatial {name_en: 'Inner Sphere'})
MATCH (outer:Spatial {name_en: 'Outer Sphere'})
MATCH (ingroup:Spatial {name_en: 'In-Group Space'})
MATCH (outgroup:Spatial {name_en: 'Out-Group Space'})
MERGE (core)-[:CONTAINS]->(inner)
MERGE (core)-[:CONTAINS]->(outer)
MERGE (core)-[:CONTAINS]->(ingroup)
MERGE (core)-[:CONTAINS]->(outgroup);

// MA hierarchy
MATCH (core:Spatial {name_en: 'MA'})
MATCH (spatial_interval:Spatial {name_en: 'Spatial Interval'})
MATCH (temporal_interval:Spatial {name_en: 'Temporal Interval'})
MATCH (negative_space:Spatial {name_en: 'Negative Space'})
MATCH (dynamic_gap:Spatial {name_en: 'Dynamic Gap'})
MERGE (core)-[:CONTAINS]->(spatial_interval)
MERGE (core)-[:CONTAINS]->(temporal_interval)
MERGE (core)-[:CONTAINS]->(negative_space)
MERGE (core)-[:CONTAINS]->(dynamic_gap);

// ========================================
// Verification Query
// ========================================
// Run this to verify node creation:
// MATCH (s:Spatial) RETURN s.level, count(s) ORDER BY s.level;