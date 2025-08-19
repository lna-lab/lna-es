# LNA-ES v3.2 出力規格仕様書

## 1. 基本原則

### 1.1 デフォルト出力形式
- **自然な改行版**を標準とする
- 345次元データの変化に基づく段落分け
- 読みやすさと時短を重視した設計

### 1.2 改行判定アルゴリズム

#### 自動改行が挿入される条件：

1. **CTA次元の主要カテゴリ変化**
   - `narrative` → `temporal`（物語から時間へ）
   - `temporal` → `emotion`（時間から感情へ）
   - `emotion` → `spatial`（感情から空間へ）

2. **Ontology次元の主題変化**
   - `natural_水` → `natural_風`（水から風へ）
   - `natural` → `temporal`（自然から時間へ）
   - `temporal` → `existential`（時間から存在論へ）

3. **Meta次元の平均値変化（>0.1）**
   - 抽象度の急激な変化を検出
   - 哲学的深化のポイントを識別

4. **文長による調整**
   - 100文字超の文の後は改行
   - 50文字未満が3文続いたら結合

5. **時間的ギャップ（>10ms）**
   - ミリ秒タイムスタンプの差が大きい場合

## 2. UI表示用規格

### 2.1 テキストエリア設計
```css
.lna-output-container {
  font-family: "Noto Sans JP", sans-serif;
  font-size: 16px;
  line-height: 1.8;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.lna-paragraph {
  margin-bottom: 1.5em;
  text-indent: 1em;
}

.lna-meta-info {
  background: #f5f5f5;
  padding: 10px;
  border-left: 3px solid #4CAF50;
  margin-bottom: 2em;
  font-size: 14px;
  color: #666;
}
```

### 2.2 改行記号の扱い
- `\n\n`（ダブル改行）: 段落区切り
- `\n`（シングル改行）: 将来の拡張用（現在未使用）

### 2.3 メタ情報表示
```
【345次元解析による現代語再構築】
- 文数: XX
- 推定文字数: XXXX
- 美的品質: X.XXX
- 支配的認知パターン: [pattern_name, score]
- 支配的存在論: [ontology_name, score]
```

## 3. 出力サンプル

### 3.1 標準出力例（自然な改行版）
```
【345次元解析による現代語再構築】
～自然な改行版～

流れゆく川の水は絶えることがない。そこを流れる水は常に新しく、一瞬として同じものは留まらない。

水面に浮かぶ泡もまた、生まれては消え、消えては生まれ、その繰り返しの中で時は過ぎていく。人の世の営みもまた、この水の流れ、この泡のように、現れては消える定めを背負っている。

[以下、345次元の変化に応じて自動改行]
```

## 4. API出力仕様

### 4.1 JSON形式
```json
{
  "stage": 2,
  "graph_id": "xxxxxxxxxxxx_YYYYMMDD_milliseconds",
  "output_format": "natural_breaks",
  "content": {
    "meta": {
      "sentence_count": 66,
      "estimated_chars": 1500,
      "aesthetic_quality": 0.856,
      "dominant_patterns": {
        "cta": ["narrative_flow", 0.288],
        "ontology": ["natural_水", 1.0]
      }
    },
    "paragraphs": [
      {
        "index": 0,
        "text": "段落1のテキスト...",
        "break_reason": "cta_category_change"
      },
      {
        "index": 1,
        "text": "段落2のテキスト...",
        "break_reason": "meta_dimension_shift"
      }
    ]
  }
}
```

### 4.2 プレーンテキスト形式
- ヘッダー（メタ情報）
- ダブル改行
- 本文（自然な改行付き）
- ダブル改行
- フッター（技術的説明）※オプション

## 5. ユーザー設定可能パラメータ

### 5.1 改行感度
```python
break_sensitivity = {
    "low": 0.2,      # 大きな変化のみで改行
    "medium": 0.1,   # デフォルト
    "high": 0.05     # 細かい変化でも改行
}
```

### 5.2 段落長制御
```python
paragraph_length = {
    "short": 100,    # 最大100文字で改行
    "medium": 200,   # デフォルト
    "long": 300      # 最大300文字まで許容
}
```

### 5.3 メタ情報表示
```python
show_meta_info = True  # メタ情報の表示/非表示
show_technical_notes = False  # 技術的説明の表示/非表示
```

## 6. 実装ファイル

- **パイプライン**: `src/lna_es_pipeline.py`
  - `_format_with_natural_breaks()` メソッド
  - `_generate_modern_japanese_output()` メソッド

- **プロンプト**: `src/ai_restoration_prompt.md`
  - AI復元アルゴリズムの詳細仕様

- **出力例**: `out/yuki_seamless_with_breaks.txt`
  - 実際の出力サンプル

## 7. 今後の拡張予定

1. **音声読み上げ最適化**
   - 改行位置での自然なポーズ挿入
   - イントネーション指示タグ

2. **モバイル表示最適化**
   - スクロール位置の自動調整
   - スワイプによる段落送り

3. **インタラクティブ表示**
   - 段落ごとの345次元データ表示
   - 次元変化のビジュアライゼーション

---
*LNA-ES v3.2 Output Format Specification*
*Last Updated: 2025-08-19*