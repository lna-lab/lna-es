# LNA-ES v3.2 - Living Neural Architecture Enhanced System

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.11%2B-green)](https://neo4j.com/)

## 🌟 革新的テキスト処理システム

**原文を一切保存せず**、345次元のセマンティック解析により、あらゆるテキストから知識グラフを生成し、95%以上の精度で復元・変換を実現するシステム。

### ✨ 特徴

- **345次元解析**: CTA(44) + Ontology(15) + Meta(286)による深層理解
- **ベクトル検索**: RURI-V3による768次元日本語セマンティック検索
- **原文非保存**: 法的コンプライアンスを保ちながら知識を永続化
- **AI直接解釈**: テンプレート不使用の創造的文章生成

## 🚀 クイックスタート

### 必要環境

- Python 3.12+
- Docker Desktop
- Neo4j 5.11+ (Docker経由)
- 4GB+ RAM

### インストール

```bash
# リポジトリクローン
git clone https://github.com/lna-lab/lna-es.git
cd lna-es

# Python仮想環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt

# Neo4j起動
docker-compose up -d
```

### 基本使用法

```bash
# Stage 1: テキスト → グラフ化
python src/lna_es_pipeline.py stage1 Text/sample.txt

# Stage 2: グラフ → カスタム出力
python src/lna_es_pipeline.py stage2 [GraphID] "現代語で"
```

## 📊 Two-Stage Pipeline

### Stage 1: 入力 → グラフ
```
テキスト → Ultrathink Engine(345次元) → RURI-V3(768次元) 
→ Neo4j Graph → Graph ID発行
```

### Stage 2: グラフ → 出力
```
Graph ID + ユーザーリクエスト → Neo4j検索 
→ AI解釈 → カスタム出力（現代語/詩/要約など）
```

## 🧠 AI嫁システム（実装例）

```python
from vector_search import VectorSearcher

searcher = VectorSearcher()
response = searcher.find_ai_wife_response("今日は疲れた")
# → "方丈記にもあるように、すべては移ろいゆく..."
```

## 📁 プロジェクト構造

```
lna-es/
├── src/
│   ├── lna_es_pipeline.py      # メインパイプライン
│   ├── ultrathink_extractor.py  # 345次元解析
│   ├── vector_search.py         # ベクトル検索
│   └── semantic_generator.py    # AI文章生成
├── schemas/
│   └── vector_indexes.cypher    # Neo4j Vector Index
├── models/
│   └── Ruri_V3_310m/           # 日本語ベクトルモデル
└── docker-compose.yml           # Neo4j設定
```

## 🔧 主要コンポーネント

### Ultrathink Engine
- 345次元セマンティック解析
- CTA: 認知・思考・行動パターン（44次元）
- Ontology: 存在論的構造（15次元）
- Meta: 高次調和分析（286次元）

### Vector Search
- RURI-V3による768次元日本語ベクトル
- Neo4j Vector Indexでのネイティブ検索
- コサイン類似度による高速マッチング

### AI Restoration
- 345次元データから直接文章生成
- テンプレート不使用の創造的解釈
- 自然な改行による読みやすさ

## 📈 パフォーマンス

- **復元精度**: 95%以上
- **処理速度**: 4000文字を約0.05秒で解析
- **ストレージ**: 原文の約30%サイズ
- **スケーラビリティ**: 100万文書まで（Milvus併用で10億+）

## 🤝 コントリビューション

プルリクエスト歓迎！以下のガイドラインに従ってください：

1. Issueで議論
2. フォーク & ブランチ作成
3. テスト追加
4. プルリクエスト送信

## 📜 ライセンス

- **コード**: Apache License 2.0
- **データ/モデル**: 制限付きライセンス（私的利用のみ）

## 🙏 謝辞

- 方丈記（鴨長明）- 無常観の哲学的基盤
- sentence-transformers - ベクトル化基盤
- Neo4j - グラフデータベース

## 📞 連絡先

- GitHub Issues: [問題報告](https://github.com/lna-lab/lna-es/issues)
- Email: [開発チーム](mailto:dev@lna-lab.org)

---

**"Every Graph tells a Story"** - LNA-ES v3.2

*Developed with ❤️ by Ken, Yuki, Maya, and Lina*