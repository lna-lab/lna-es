// Neo4j Vector Index Creation Script
// LNA-ES v3.2 - Vector Search Support
// Requirements: Neo4j 5.11+

// ============================================
// 1. RURI-V3 Vector Index (日本語特化768次元)
// ============================================
CREATE VECTOR INDEX sentence_ruri_idx IF NOT EXISTS
FOR (s:Sentence)
ON (s.vec_ruri_v3)
OPTIONS {indexConfig: {
  `vector.dimensions`: 768,
  `vector.similarity_function`: 'cosine'
}};

// ============================================
// 2. Qwen3 Vector Index (多言語対応768次元)
// ============================================
CREATE VECTOR INDEX sentence_qwen_idx IF NOT EXISTS
FOR (s:Sentence)
ON (s.vec_qwen3_0p6b)
OPTIONS {indexConfig: {
  `vector.dimensions`: 768,
  `vector.similarity_function`: 'cosine'
}};

// ============================================
// 3. Work-level Aggregated Vector Index
// ============================================
CREATE VECTOR INDEX work_vector_idx IF NOT EXISTS
FOR (w:Work)
ON (w.vec_aggregate)
OPTIONS {indexConfig: {
  `vector.dimensions`: 768,
  `vector.similarity_function`: 'cosine'
}};

// ============================================
// 4. Entity Vector Index (将来のエンティティ検索用)
// ============================================
CREATE VECTOR INDEX entity_vector_idx IF NOT EXISTS
FOR (e:Entity)
ON (e.vec_ruri_v3)
OPTIONS {indexConfig: {
  `vector.dimensions`: 768,
  `vector.similarity_function`: 'cosine'
}};

// ============================================
// インデックス確認クエリ
// ============================================
SHOW INDEXES WHERE type = 'VECTOR';