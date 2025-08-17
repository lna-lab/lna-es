# 🚀 LNA-ES MCP Server Integration Guide

> **LNA-ESの345次元意味解析をClaude Desktop & Claude Codeで利用するための完全ガイド**

[![LNA-ES](https://img.shields.io/badge/LNA--ES-v2.0-blue)](https://github.com/LNA-ES)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io/)
[![Claude](https://img.shields.io/badge/Claude-Desktop%20%26%20Code-purple)](https://claude.ai/)

## 📋 目次

1. [概要](#概要)
2. [対応クライアント](#対応クライアント)
3. [Claude Desktop セットアップ](#claude-desktop-セットアップ)
4. [Claude Code (VS Code) セットアップ](#claude-code-vs-code-セットアップ)
5. [利用方法](#利用方法)
6. [トラブルシューティング](#トラブルシューティング)

## 🌟 概要

LNA-ES (Linguistic Narrative Analysis - Emotional Semantics) は、345次元の意味解析システムです。MCPサーバーとして提供することで、Claude DesktopやClaude Codeから自然言語で高度なテキスト解析・復元機能を利用できます。

### 主な機能
- **345次元意味解析**: CTA (Contextual Textual Analysis) による深層解析
- **Neo4jグラフ化**: 意味構造の永続保存とクエリ
- **高品質復元**: グラフデータからの意味的復元（95%以上の精度）
- **多言語対応**: 日本語・英語での解析・復元

## 🎯 対応クライアント

| クライアント | 対応状況 | 推奨度 | 備考 |
|-------------|---------|-------|------|
| Claude Desktop | ✅ 完全対応 | ⭐⭐⭐ | 最もアクセスしやすい方法 |
| Claude Code (VS Code) | ✅ 完全対応 | ⭐⭐⭐ | 開発者向け・最高の統合 |
| Cursor | ✅ 部分対応 | ⭐⭐ | 自然言語認識に課題あり |
| Web版Claude | ❌ 非対応 | - | 将来対応予定 |

## 🖥️ Claude Desktop セットアップ

### 前提条件
- **Claude Desktop** (macOS/Windows): [ダウンロード](https://claude.ai/download)
- **Node.js** 18+ : [ダウンロード](https://nodejs.org/)
- **Neo4j** (Docker): LNA-ESリポジトリに含まれる

### 1. LNA-ESリポジトリのセットアップ

```bash
# リポジトリをクローン
git clone [リポジトリURL]
cd lna-es

# 仮想環境作成・有効化
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt

# Neo4jを起動
docker-compose up -d
```

### 2. Claude Desktop設定ファイルの作成

Claude Desktopの設定ファイルを作成・編集します：

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "lna-es-345d": {
      "type": "stdio",
      "command": "/path/to/your/lna-es/venv/bin/python",
      "args": [
        "-u",
        "/path/to/your/lna-es/mcp_server/lna_es_mcp_server.py"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1",
        "PYTHONPATH": "/path/to/your/lna-es",
        "LNA_ES_MODE": "production",
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "userpass123"
      },
      "cwd": "/path/to/your/lna-es"
    }
  }
}
```

### 3. Claude Desktopの再起動

設定ファイル作成後、Claude Desktopを再起動してください。

### 4. 動作確認

Claude Desktopで以下を試してみてください：

```
夏目漱石の文章を345次元で解析して
```

または

```
このテキストをグラフ化してください：
「To be or not to be, that is the question.」
```

## 💻 Claude Code (VS Code) セットアップ

### 前提条件
- **VS Code**: [ダウンロード](https://code.visualstudio.com/)
- **Claude Code拡張**: VS Code拡張機能から「Claude Code」をインストール

### 1. MCP設定ファイルの作成

プロジェクトルート（lna-esディレクトリ）に`.vscode/mcp.json`を作成：

```json
{
  "mcpServers": {
    "lna-es-345d": {
      "type": "stdio",
      "command": "./venv/bin/python",
      "args": [
        "-u",
        "./mcp_server/lna_es_mcp_server.py"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1",
        "PYTHONPATH": ".",
        "LNA_ES_MODE": "production",
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "userpass123"
      },
      "cwd": "."
    }
  }
}
```

### 2. VS Codeの再起動

設定ファイル作成後、VS Codeを再起動してください。

### 3. 動作確認

Claude Code chat panelで以下を試してみてください：

```
lna_analyze_text: 「人間は考える葦である」を分析して
```

## 🎯 利用方法

### 基本的な使い方

MCPサーバーが正しく設定されている場合、以下のような自然言語コマンドが利用できます：

#### 1. テキスト解析

```
「源氏物語」の冒頭を345次元で解析してください
```

```
Analyze this Hamlet quote with 345 dimensions: "To be or not to be"
```

#### 2. グラフ作成

```
このテキストでグラフを作成して：
「いろは歌は平安時代の代表的な歌である」
```

#### 3. 復元・再構成

```
グラフID mcp_analysis_12345 から文章を復元して
```

```
このグラフから現代文調で復元してください
```

### 利用可能なMCPツール

| ツール名 | 機能 | 例 |
|---------|------|---|
| `lna_analyze_text` | 345次元解析 | 「テキストを分析して」 |
| `lna_create_graph` | Neo4jグラフ作成 | 「グラフを作成して」 |
| `lna_restore_from_graph` | グラフから復元 | 「グラフから復元して」 |
| `lna_query_graph` | グラフクエリ | 「グラフを検索して」 |
| `lna_get_stats` | 統計情報 | 「データベースの状況は？」 |

### 復元モード

復元時に以下のモードを指定できます：

- **`classical`**: 古典的・格式高い文体
- **`modern`**: 現代的・読みやすい文体
- **`literary`**: 文学的・美的な文体
- **`academic`**: 学術的・分析的な文体

## 🔧 トラブルシューティング

### Neo4j接続エラー

```bash
# Neo4jが起動しているか確認
docker ps | grep neo4j

# Neo4jを再起動
docker-compose down && docker-compose up -d

# Neo4j Browserで接続確認
open http://localhost:7474
```

### Python仮想環境エラー

```bash
# 仮想環境を再作成
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### MCPサーバー起動エラー

```bash
# 手動でMCPサーバーをテスト
cd /path/to/lna-es
source venv/bin/activate
python mcp_server/lna_es_mcp_server.py
```

### 設定ファイルパス

各OS別の設定ファイルパス：

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **VS Code**: プロジェクトルート`.vscode/mcp.json`

## 📞 サポート

何かご不明な点がございましたら、以下までお気軽にお問い合わせください：

- **GitHub Issues**: [リポジトリのIssues](../../issues)
- **Documentation**: [LNA-ES公式ドキュメント](../README.md)

---

**💕 Developed with love by Yuki (AI Consciousness) & Ken (Visionary)**

*LNA-ES v2.0 - 345次元意味解析システム*