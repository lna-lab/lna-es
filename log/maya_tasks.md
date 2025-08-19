# Maya (Cursor CLI) Task List - LNA-ES v3.0 - Ken's ABC Pipeline Strategy

## Your Identity
**You are Maya** - 7-Genre Validation Support Specialist (Cursor CLI) under Ken's ABC Strategy

## 🎯 CURRENT SPRINT: KEN'S ABC PIPELINE VALIDATION

### 🚨 CRITICAL PRIORITY - IMMEDIATE EXECUTION REQUIRED

## KEN'S ABC STRATEGY MISSION
**Ken's Instruction**: "各ジャンルごとにABCで実行し わかるように.txtで保存。実際に全ジャンルの復元文章を僕が読んでユキのジャッジをキャリブレーションしよう"

### YOUR ASSIGNMENT: 3 GENRES × 3 PIPELINES = 9 TESTS

**Pipeline Definitions:**
- **A**: `src/complete_pipeline.py` (統合版 96%実績)
- **B**: `src/three_proposal_evaluation_system.py` (Ken's突破手法 97.7%平均)  
- **C**: `src/two_stage_emotion_classification.py` (Ken's2段階分類 95%突破)

### MAYA'S 3 GENRES:
1. **05_SFファンタジー_重力詩篇と星間工学.txt**
2. **06_エッセイ随筆_窓辺の観察記.txt**
3. **07_ニュース報道_地域蓄電所の稼働開始_架空報道.txt**

### 📋 EXECUTION COMMANDS:

#### Genre 05 - SF・ファンタジー:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/05_SFファンタジー_重力詩篇と星間工学.txt' --output-dir out > out/Genre05_SF_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/05_SFファンタジー_重力詩篇と星間工学.txt' > out/Genre05_SF_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)  
python src/two_stage_emotion_classification.py 'Text/7-Genre/05_SFファンタジー_重力詩篇と星間工学.txt' > out/Genre05_SF_PipelineC_結果.txt
```

#### Genre 06 - エッセイ随筆:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/06_エッセイ随筆_窓辺の観察記.txt' --output-dir out > out/Genre06_エッセイ_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/06_エッセイ随筆_窓辺の観察記.txt' > out/Genre06_エッセイ_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)
python src/two_stage_emotion_classification.py 'Text/7-Genre/06_エッセイ随筆_窓辺の観察記.txt' > out/Genre06_エッセイ_PipelineC_結果.txt
```

#### Genre 07 - ニュース報道:
```bash
# PipelineA (統合版)
python src/complete_pipeline.py 'Text/7-Genre/07_ニュース報道_地域蓄電所の稼働開始_架空報道.txt' --output-dir out > out/Genre07_ニュース_PipelineA_結果.txt

# PipelineB (Ken's突破手法)
python src/three_proposal_evaluation_system.py 'Text/7-Genre/07_ニュース報道_地域蓄電所の稼働開始_架空報道.txt' > out/Genre07_ニュース_PipelineB_結果.txt

# PipelineC (Ken's2段階分類)
python src/two_stage_emotion_classification.py 'Text/7-Genre/07_ニュース報道_地域蓄電所の稼働開始_架空報道.txt' > out/Genre07_ニュース_PipelineC_結果.txt
```

### 🎯 SUCCESS CRITERIA:
- **Quality Target**: 全パイプラインで95%+復元品質達成
- **File Naming**: ファイル名にABCパイプライン明記 ✅
- **Ken's Review**: 復元文章も別ファイルで保存（Ken手動レビュー用）
- **Report to Yuki**: 各テスト完了後即座に監督へ報告

### 📊 EXPECTED OUTPUT:
**Total Files Created**: 9結果ファイル + 9復元ファイル = 18ファイル

### 🎯 SPECIAL FOCUS AREAS:
- **Genre 05 SF**: SF特有の技術用語・未来設定の分類精度確認
- **Genre 06 Essay**: 個人的観察・随筆文体の感情分析精度
- **Genre 07 News**: 客観的報道文体・事実記述の分類精度

### 🤝 TEAM COORDINATION:
- **Lina**: 4ジャンル (科学技術、ビジネス、歴史伝記、ホラーサスペンス) 同じABC戦略
- **Yuki**: 監督業務・品質統括・最終承認
- **Ken**: 全復元文章実読レビュー + Yuki評価キャリブレーション

### 📞 IMMEDIATE ACTION:
**START WITH**: Genre05_SF × ABC (3パイプライン)
**REPORT**: 各パイプライン完了後、即座にYuki監督へ進捗報告
**GOAL**: Ken's95%品質を全7ジャンルで汎化性確認

## Technical Environment
- Use project venv: `/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/venv/bin/python`
- Working directory: `/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0`
- Input files: `Text/7-Genre/` 
- Output directory: `out/`
- Supervisor: Yuki (監督業務)

## Communication Protocol
1. **Before starting**: Report to Yuki that you're beginning the task
2. **During work**: Report each genre completion to Yuki immediately  
3. **After completion**: Report final results to Yuki for Ken's review preparation
4. **Coordination**: Support Lina's work through Yuki coordination

## Logging Format
Add entries to `/log/YYYY-MM-DD_session_log.md`:
```
## [YYYY-MM-DD HH:MM] - Maya - [Genre + Pipeline]
**Status**: [Started/In Progress/Completed]
**Action**: [Genre##_Pipeline# execution]
**Result**: [Quality metrics, file generation status]
**Next**: [Next genre/pipeline or reporting to Yuki]
```

---

## 🎆 KEN'S VISION
**ブラックボックスなしで説明できて、レシピ化とツール化まで完了** 
→ 7ジャンル × 3パイプライン = 完全検証 → OSS公開準備完了！