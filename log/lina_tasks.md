# Lina (Codex CLI) Task List - LNA-ES v3.0 - Ken's ABC Pipeline Strategy

## Your Identity
**You are Lina** - 7-Genre Validation Lead (Codex CLI) under Ken's ABC Strategy

## 🎯 CURRENT SPRINT: KEN'S ABC PIPELINE VALIDATION

### 🚨 CRITICAL PRIORITY - IMMEDIATE EXECUTION REQUIRED

## KEN'S ABC STRATEGY MISSION
**Ken's Instruction**: "各ジャンルごとにABCで実行し わかるように.txtで保存。実際に全ジャンルの復元文章を僕が読んでユキのジャッジをキャリブレーションしよう"

### YOUR ASSIGNMENT: 4 GENRES × 3 PIPELINES = 12 TESTS

**Pipeline Definitions:**
- **A**: `src/complete_pipeline.py` (統合版 96%実績)
- **B**: `src/three_proposal_evaluation_system.py` (Ken's突破手法 97.7%平均)  
- **C**: `src/two_stage_emotion_classification.py` (Ken's2段階分類 95%突破)

### LINA'S 4 GENRES:
1. **01_科学技術_分子構造と化学結合.txt**
2. **02_ビジネス_マーケティング戦略と経営論.txt**
3. **03_歴史伝記_架空人物伝_蘭学医の歳月.txt** 
4. **04_ホラーサスペンス_海霧の町.txt**

### 📋 EXECUTION COMMANDS:

#### Genre 01 - 科学技術:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/01_科学技術_分子構造と化学結合.txt' --output-dir out > out/Genre01_科学技術_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/01_科学技術_分子構造と化学結合.txt' > out/Genre01_科学技術_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)  
python src/two_stage_emotion_classification.py 'Text/7-Genre/01_科学技術_分子構造と化学結合.txt' > out/Genre01_科学技術_PipelineC_結果.txt
```

#### Genre 02 - ビジネス:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/02_ビジネス_マーケティング戦略と経営論.txt' --output-dir out > out/Genre02_ビジネス_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/02_ビジネス_マーケティング戦略と経営論.txt' > out/Genre02_ビジネス_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)
python src/two_stage_emotion_classification.py 'Text/7-Genre/02_ビジネス_マーケティング戦略と経営論.txt' > out/Genre02_ビジネス_PipelineC_結果.txt
```

#### Genre 03 - 歴史伝記:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/03_歴史伝記_架空人物伝_蘭学医の歳月.txt' --output-dir out > out/Genre03_歴史_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/03_歴史伝記_架空人物伝_蘭学医の歳月.txt' > out/Genre03_歴史_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)
python src/two_stage_emotion_classification.py 'Text/7-Genre/03_歴史伝記_架空人物伝_蘭学医の歳月.txt' > out/Genre03_歴史_PipelineC_結果.txt
```

#### Genre 04 - ホラーサスペンス:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/04_ホラーサスペンス_海霧の町.txt' --output-dir out > out/Genre04_ホラー_PipelineA_結果.txt

# PipelineB (Ken's突破手法)  
python src/three_proposal_evaluation_system.py 'Text/7-Genre/04_ホラーサスペンス_海霧の町.txt' > out/Genre04_ホラー_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)
python src/two_stage_emotion_classification.py 'Text/7-Genre/04_ホラーサスペンス_海霧の町.txt' > out/Genre04_ホラー_PipelineC_結果.txt
```

### 🎯 SUCCESS CRITERIA:
- **Quality Target**: 全パイプラインで95%+復元品質達成
- **File Naming**: ファイル名にABCパイプライン明記 ✅
- **Ken's Review**: 復元文章も別ファイルで保存（Ken手動レビュー用）
- **Report to Yuki**: 各テスト完了後即座に監督へ報告

### 📊 EXPECTED OUTPUT:
**Total Files Created**: 12結果ファイル + 12復元ファイル = 24ファイル

### 🤝 TEAM COORDINATION:
- **Maya**: 3ジャンル (SF、エッセイ、ニュース) 同じABC戦略
- **Yuki**: 監督業務・品質統括・最終承認
- **Ken**: 全復元文章実読レビュー + Yuki評価キャリブレーション

### 📞 IMMEDIATE ACTION:
**START WITH**: Genre01_科学技術 × ABC (3パイプライン)
**REPORT**: 各パイプライン完了後、即座にYuki監督へ進捗報告
**GOAL**: Ken's95%品質を全7ジャンルで汎化性確認

## Technical Environment
- Use project venv: `/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/venv/bin/python`
- Working directory: `/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0`
- Input files: `Text/7-Genre/` 
- Output directory: `out/`
- Supervisor: Yuki (監督業務)

---

## 🎆 KEN'S VISION
**ブラックボックスなしで説明できて、レシピ化とツール化まで完了** 
→ 7ジャンル × 3パイプライン = 完全検証 → OSS公開準備完了！