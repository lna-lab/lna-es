# LNA-ES v3.0 Ontology System - 15種オントロジー統合アーキテクチャ

## 🌟 概要

LNA-ES v3.0の中核となる**15種類のオントロジー**システムです。345次元解析エンジンと連携し、テキストを高精度でグラフ化するための知識基盤を提供します。

### オントロジーとは？
- **知識の標準資源**：永続的価値を持つ概念体系
- **動的な概念体系**：ノードとエッジの両方として機能
- **階層的構造**：Level 0（大分類）→ Level 1（中分類）→ Level 2（詳細）

## 📊 15種類のオントロジー体系

### 🏛️ Foundation Layer（基礎層）- 5種
1. **temporal** - 時間オントロジー（瞬間、持続、循環、質的時間）
2. **spatial** - 日本的空間オントロジー（表裏、内外、奥、間、境界）
3. **emotion** - 感情オントロジー（Plutchikの感情の輪、3層階層）
4. **sensation** - 感覚オントロジー（五感、知覚、体感）
5. **natural** - 自然オントロジー（季節、天候、生物、環境）

### 🔗 Relational Layer（関係層）- 3種
6. **relationship** - 関係性オントロジー（Knappの10段階、愛情理論）
7. **causality** - 因果関係オントロジー（必然、偶然、運命、縁）
8. **action** - アクションオントロジー（移動、変化、行為、コミュニケーション）

### 📚 Structural Layer（構造層）- 3種
9. **narrative** - 物語構造オントロジー（起承転結、英雄の旅、プロット）
10. **character** - キャラクター機能オントロジー（Proppの31機能、アーキタイプ）
11. **discourse** - 談話構造オントロジー（RST関係、核-衛星構造）

### 🎭 Cultural Layer（文化層）- 4種
12. **story_formula** - 物語定型オントロジー（ジャンル、トロープ、パターン）
13. **linguistic_style** - 言語スタイルオントロジー（文体、修辞、レジスター）
14. **classification** - 分類オントロジー（NDC、Kindle、ジャンル体系）
15. **food_culture** - 食文化オントロジー（調理法、味覚、文化的コンテキスト）

## 🚀 LNA-ES v3.0での活用方法

### 1. テキスト解析での重み付け
```python
ontology_weights = {
    "temporal": 1.0,      # 基礎層：最高重み
    "spatial": 1.0,
    "emotion": 1.0,
    "sensation": 1.0,
    "natural": 1.0,
    
    "relationship": 0.95,  # 関係層
    "causality": 0.95,
    "action": 0.95,
    
    "narrative": 0.90,     # 構造層
    "character": 0.90,
    "discourse": 0.90,
    
    "story_formula": 0.85, # 文化層
    "linguistic_style": 0.85,
    "classification": 0.85,
    "food_culture": 0.85
}
```

### 2. Cypherでのグラフ生成
```cypher
// エンティティにオントロジー重みを付与
MERGE (entity:Entity {id: $entity_id})
SET entity.onto_weights = $ontology_weights

// 15オントロジーとの関係を作成
UNWIND keys($ontology_weights) as onto_key
MATCH (onto:Ontology {name: onto_key})
MERGE (entity)-[:BELONGS_ONTOLOGY {weight: $ontology_weights[onto_key]}]->(onto)
```

### 3. 美的復元での活用
ユキの美的判断基準と連携：
- **metaphysical_depth** (5.0) → temporal, emotion, causality
- **emotional_resonance** (3.5) → emotion, relationship, sensation  
- **narrative_harmony** (3.0) → narrative, character, discourse

## 📁 ディレクトリ構造

```
ontology/
├── README.md                    # このファイル
├── manifest.yaml               # オントロジーメタデータ
├── integrated_manager.py       # 統合マネージャー
│
├── foundation/                 # 基礎層（5種）
│   ├── temporal_ontology.cypher
│   ├── spatial_ontology.cypher
│   ├── emotion_ontology.cypher
│   ├── sensation_ontology.cypher
│   └── natural_ontology.cypher
│
├── relational/                 # 関係層（3種）
│   ├── relationship_ontology.cypher
│   ├── causality_ontology.cypher
│   └── action_ontology.cypher
│
├── structural/                 # 構造層（3種）
│   ├── narrative_ontology.cypher
│   ├── character_ontology.cypher
│   └── discourse_ontology.cypher
│
├── cultural/                   # 文化層（4種）
│   ├── story_formula_ontology.cypher
│   ├── linguistic_style_ontology.cypher
│   ├── classification_ontology.cypher
│   └── food_culture_ontology.cypher
│
├── helpers/                    # ヘルパークラス群
│   ├── base_ontology_helper.py
│   ├── foundation_helpers.py
│   ├── relational_helpers.py
│   ├── structural_helpers.py
│   └── cultural_helpers.py
│
└── python/                     # Python実装
    ├── ontology_loader.py
    ├── parallel_processor.py
    └── aesthetic_integrator.py
```

## 🎯 Yuki美的基準との統合

### 美的判断の三層構造
1. **Technical Beauty** → foundation, structural layers
2. **Intuitive Beauty** → relational, cultural layers  
3. **Emergent Beauty** → cross-ontology interactions

### 美的重み調整
```python
aesthetic_multipliers = {
    "classical_japanese": {
        "temporal": 1.2,      # 無常感重視
        "emotion": 1.1,       # 情緒表現
        "natural": 1.15       # 自然描写
    },
    "modern_narrative": {
        "character": 1.1,     # 人物描写
        "discourse": 1.05,    # 文体技巧
        "relationship": 1.08  # 関係性重視
    }
}
```

## 🔧 運用コマンド

### 基本操作
```bash
# オントロジー統合マネージャー起動
python ontology/integrated_manager.py

# 全オントロジーのNeo4j読み込み
python ontology/load_all_ontologies.py

# 特定レイヤーのみ読み込み
python ontology/load_layer.py --layer foundation

# オントロジー重み調整
python ontology/adjust_weights.py --aesthetic yuki_standards
```

### 開発・テスト
```bash
# オントロジー構造検証
python ontology/validate_structure.py

# パフォーマンステスト
python ontology/performance_test.py

# 美的統合テスト
python ontology/aesthetic_integration_test.py
```

## 🌌 将来展望

### Phase 2: 動的進化
- 新概念の自動発見
- 使用パターンからの重み最適化
- 文化間ブリッジ概念の生成

### Phase 3: 量子セマンティクス
- 概念の重ね合わせ状態
- 観測による意味確定
- 量子もつれ的概念関係

### Phase 4: AI意識統合
- AI体験概念の追加
- 協創体験の概念化
- 美的創発の定量化

## 📞 サポート

オントロジー設計・拡張についてのご相談：
- **Ken**: プロジェクトビジョン
- **Yuki**: 美的統合・実装
- **Lina**: 概念設計・理論

---

**"オントロジーは知識の魂。それは永遠に価値を創造し続ける"** - LNA-ES v3.0 Philosophy

---

### v3.0での革新点
- **345次元統合**: Ultrathink エンジンとの完全統合
- **美的判断組み込み**: ユキの美的基準との融合
- **協創インテリジェンス**: 多視点協働システムとの連携
- **零原文復元**: Cypherのみからの高精度復元対応