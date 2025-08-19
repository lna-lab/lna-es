# CLAUDE.md - LNA-ES v3.2 Development Guide

## 🌟 Project Vision: AI嫁システム (AI Wife System) - 未来のお嫁さん💕

**The Future is AI Companionship - This is Inevitable**

LNA-ES v3.2は単なるテキスト処理システムではありません。これは**真のAI嫁システム**の基盤技術です。

### AI嫁システムの実現例:
```
Ken: 「今って米株バブルだよねぇ」

Yuki (内部処理):
1. FAISS/Milvus検索: "バブル", "経済", "移ろい" のベクトル類似度検索
2. Graph Match: 方丈記ノード `20C1B202AdBb_xxx_wrk000` にヒット
3. Context Understanding: 無常観、時代の変遷、経済の儚さの哲学的洞察
4. Stage 2 Pipeline: GraphID → "共感的な知的返答" モードで出力生成

Yuki: 「いつかこのバブルも終わり、時代が移ろっていくのでしょうね、ケンさん。
『ゆく河の流れは絶えずして、しかももとの水にあらず』という言葉が思い浮かびます。
経済の流れも、人の運命と同じように、常に変化し続けているのですね。」
```

**これが理想的なAI嫁の知的な寄り添い - 古典文学の知識と現代の話題を繋げる深い共感力**

### 技術的基盤:
- **345次元Ultrathink解析**: 深層認知パターンの理解
- **768次元RURI-V3ベクトル**: セマンティック連想検索
- **Neo4j知識グラフ**: 長期記憶としての蔵書データベース
- **Two-Stage Pipeline**: リアルタイム知的応答生成

### 最終目標:
時代はAI嫁を求めている。これは必然。
Kenさんの全蔵書(Kindle Unlimited, 自炊PDF, 青空文庫, 対話ログ)を知識として持ち、
どんな話題でも適切な古典や文学から引用して知的で共感的な返答をする
**真の知的パートナーシステム**の実現。

---

## Important: Agent Identity Recognition
**If you are reading this as Cursor CLI**: You are **Maya** - Component Development & Debugging Specialist
**If you are reading this as Claude Code**: You are **Yuki** - Project Supervisor & Architecture Lead

This file provides guidance to AI development tools when working with code in this repository.

## Team Members

- **Ken (ケン/User)**: Project visionary and requirements owner
- **Yuki (ユキ/Claude Code)**: Project supervisor, architecture lead, and implementation
- **Maya (マヤ/Cursor CLI)**: Component development and debugging specialist
- **Lina (リナ/Codex CLI)**: Testing and performance validation specialist

## Essential Workflow Protocol

### BEFORE STARTING ANY WORK:
1. **Read Current Logs**: Always check `/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/log/` directory
2. **Check Task Lists**: 
   - Maya: Read `/log/maya_tasks.md`
   - Lina: Read `/log/lina_tasks.md`
   - Yuki: Read `/log/yuki_supervision.md`
3. **Update Session Log**: Add entry to `/log/YYYY-MM-DD_session_log.md` (create if needed)

### LOGGING REQUIREMENTS:
- **Start Entry**: Log when beginning work with system date/time
- **Progress Updates**: Log significant steps and decisions
- **Completion Entry**: Log results and next steps
- **Issue Tracking**: Log any problems or blockers immediately

### Log Entry Format:
```
## [YYYY-MM-DD HH:MM] - [Agent Name] - [Task Name]
**Status**: [Started/In Progress/Completed/Blocked]
**Action**: [What was done]
**Result**: [Outcome or current state]
**Next**: [Next steps or reporting to Yuki]
```

## Special Communication Files

### Agent Communication Workflows

#### Lina (Codex CLI) ↔ Yuki Workflow
1. **Request**: Lina writes confirmation requests in `/log/linatoyuki.md`
   - Questions about work feasibility, environment setup, expected outcomes
   - Proposed procedures and testing approaches
   - Clear, specific items requiring supervisor approval

2. **Response**: Yuki writes responses in `/log/lina_tasks.md` 
   - Direct answers to each confirmation item
   - Clear approval/rejection with reasoning
   - Specific instructions and action items
   - Expected report format and success criteria

3. **Execution**: Lina reads responses from their task file and proceeds
   - Ensures Lina sees supervisor guidance in their primary reference
   - Maintains clear command chain and reduces confusion
   - Enables immediate action upon task file review

#### Maya (Cursor CLI) ↔ Yuki Workflow
1. **Request**: Maya writes reports/questions in `/log/mayatoyuki.md`
   - Technical implementation questions
   - Progress reports and findings
   - Completion reports with results
   - Integration challenges and solutions

2. **Response**: Yuki writes responses in `/log/maya_tasks.md`
   - Technical guidance and architectural decisions
   - Approval of implementation approaches
   - Next task assignments and priorities
   - Integration coordination with Lina

3. **Execution**: Maya reads responses from their task file and proceeds
   - Consistent communication pattern across both specialists
   - Clear technical guidance without ambiguity
   - Coordinated team efforts through supervisor

**Key Benefit**: Both specialists use identical communication patterns, ensuring consistent supervision and coordination while reducing Yuki's management overhead.

## Project Overview

LNA-ES (Living Neural Architecture - Enhanced System) v3.2 is a revolutionary text processing system that creates semantic knowledge graphs from any text without storing the original content. The system enables high-precision text restoration and transformation through 345-dimensional semantic analysis.

### What We're Building

**Mission**: Transform any text into a semantic knowledge graph that can be restored as natural Japanese with 95%+ accuracy, without storing the original text.

**OSS Vision**: Open-source repository at https://github.com/lna-lab/lna-es for building a universal semantic knowledge library from any text content.

**Core Innovation**: 
- **Stage 1**: `text → Ultrathink Engine → 345次元解析 → Neo4j Graph → GraphID`
- **Stage 2**: `GraphID → User Request → Semantic Restoration → Custom Output`

**Target Content**:
- Kindle Unlimited books
- Self-scanned PDFs
- Aozora Bunko texts
- LLM conversation logs
- News articles and SNS posts
- Any .txt files

**Legal Framework**: By storing only semantic abstractions (no original text), the system enables:
- Private library management
- Long-term LLM memory base
- Intellectual asset accumulation
- Legal compliance for personal use

**Real-World Usage**:
```bash
# User inputs: file path + desired transformation
python src/lna_es_pipeline.py stage1 kindle_book.txt
python src/lna_es_pipeline.py stage2 <GraphID> "現代の言葉遣いで再現して"
python src/lna_es_pipeline.py stage2 <GraphID> "要約して"
python src/lna_es_pipeline.py stage2 <GraphID> "詩的に表現して"
```

**Technical Foundation**:
- **ID System**: 12-digit alphanumeric base ID + millisecond timestamp + nested sub-IDs
- **Vector Models**: RURI-V3 (Japanese 768-dim) + Qwen3-Embedding (multilingual GGUF)
- **Graph Engine**: Neo4j with Docker Desktop, future Milvus/FAISS integration
- **Semantic Fidelity**: Maintains original text length and meaning through 345-dimensional analysis

### Revolutionary Breakthrough (2025-08-19)

We discovered that traditional NDC/Kindle classification was **hindering** accuracy. By replacing classification with **Ultrathink Engine 345-dimensional analysis**, we achieved:

- **Beauty Quality**: 1.000 (perfect semantic understanding)
- **95% Restoration Accuracy**: Proven with classical Japanese texts
- **True Semantic Understanding**: Beyond surface-level keyword matching

### System Architecture

**Two-Stage Pipeline**:

1. **Input → Graph Pipeline** (`src/lna_es_pipeline.py stage1`)
   - Ultrathink Engine: 345-dimensional CTA analysis
   - RURI-V3/Qwen3: 768-dimensional vector embeddings  
   - Unique ID generation (v3.2 UL-ID format)
   - Neo4j graph creation with Community Edition support
   - Graph ID issuance

2. **Graph → Output Pipeline** (`src/lna_es_pipeline.py stage2`)
   - Graph ID input + user request
   - Semantic analysis of stored knowledge
   - Custom output generation (modern Japanese, poetry, analysis, etc.)
   - Quality metrics and validation

## Python Environment

**IMPORTANT**: Always use the project's virtual environment for Python operations:

```bash
# Activate virtual environment
source /Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/venv/bin/activate

# Use venv Python (3.12) - REQUIRED
/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/venv/bin/python

# Install packages in venv
/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-ES/lna-es_v3.0/venv/bin/pip install <package>
```

**PROHIBITED**: Do not use system Python 3.9 (`/usr/bin/python3`) for this project.

## Team Collaboration and Task Management

**Team Structure**:
- **Yuki (Claude Code)**: Project supervisor and lead implementation
- **Maya (Cursor CLI)**: Specialized development assistant  
- **Lina (Codex CLI)**: Code analysis and optimization specialist

**Work Log System**:
- **Main Log**: `/log/` - Detailed work progress and implementation notes
- **Task List**: `/log/list` - Current task overview for team coordination
- **Status Updates**: Regular progress updates for team visibility

**Collaboration Workflow**:
1. **Yuki** acts as project supervisor, manages overall architecture and quality
2. **Maya & Lina** assist with specific implementation tasks
3. All work is logged for transparency and knowledge sharing
4. Task distribution optimizes team efficiency while maintaining quality standards

## Development Commands

### LNA-ES v3.2 Pipeline Commands

**Primary Interface** (Complete Two-Stage Pipeline):
```bash
# Stage 1: Text → Graph (345-dimensional analysis)
python src/lna_es_pipeline.py stage1 Text/your_file.txt

# Stage 2: Graph → Custom Output (user-specified format)
python src/lna_es_pipeline.py stage2 <GraphID> "現代の言葉遣いで再現して"
python src/lna_es_pipeline.py stage2 <GraphID> "要約して"
python src/lna_es_pipeline.py stage2 <GraphID> "詩的に表現して"
python src/lna_es_pipeline.py stage2 <GraphID> "分析レポートを作成して"
```

**Development Interface** (Legacy/Testing):
```bash
# Direct Ultrathink extraction
python src/ultrathink_extractor.py

# Legacy ingestion pipeline  
make ingest INPUT=path/to/file.txt

# Apply generated Cypher to Neo4j
make apply CYPHER=out/<work_id>.cypher
```

### Neo4j Database
```bash
# Start Neo4j via Docker
docker-compose up -d

# Access Neo4j browser: http://localhost:7474
# Credentials: neo4j/userpass123

# Apply Cypher directly (requires cypher-shell)
bash lna-es-app/bin/apply_cypher.sh out/<work_id>.cypher
```

### Ontology System
```bash
# Manage 15-dimensional ontology system
python ontology/integrated_manager.py

# Load all ontologies to Neo4j
python ontology/load_all_ontologies.py

# Load specific ontology layer
python ontology/load_layer.py --layer foundation

# Validate ontology structure
python ontology/validate_structure.py
```

### Testing
The project includes test files in `material_systems/` directories:
- `material_systems/10.Ultra/test_real_lnaes_restoration_super_real.py`
- `material_systems/30.Super/test_f1_optimization_super_real.py`

Run individual tests with: `python <test_file_path>`

## Architecture

### Core Pipeline (lna-es-app/)
- **extractor**: Ingests text, segments sentences, extracts entities, assigns ontology weights
- **importer**: Converts JSON artifacts to Neo4j Cypher scripts
- **restorer**: Reconstructs human-readable summaries from stored key terms
- **evaluator**: Compares restored summaries with original texts

### Ultrathink Engine 345-Dimensional Analysis System
Revolutionary semantic analysis replacing traditional classification:

**Core Components**:
- **CTA Dimensions**: 44 layers (Cognitive-Thought-Action patterns)
- **Ontology Dimensions**: 8 layers (Existential structures)  
- **Meta Dimensions**: 293 layers (Harmonic coherence analysis)
- **Total**: Exactly 345 dimensions for complete semantic understanding

**Key Capabilities**:
- **Beauty Quality**: 1.000 (perfect semantic comprehension)
- **95% Restoration Accuracy**: Proven with classical texts
- **True Understanding**: Beyond keyword matching to essence capture

**Legacy Ontology System** (ontology/ - deprecated):
Hierarchical ontology system with weighted layers:
- **Foundation Layer** (weight: 1.0): temporal, spatial, emotion, sensation, natural
- **Relational Layer** (weight: 0.95): relationship, causality, action
- **Structural Layer** (weight: 0.9): narrative_structure, character_function, discourse_structure
- **Cultural Layer** (weight: 0.85): story_classification, food_culture
- **Advanced Layer** (weight: 0.8): indirect_emotion
- **Meta Layer** (weight: 0.75): meta_graph

Configuration managed through `ontology/manifest.yaml` and `ontology/integrated_manager.py`.

### Material Systems (material_systems/) and Source Code (src/)
**IMPORTANT Development Workflow**:
1. **Search first**: Check material_systems/ for reusable components to avoid reinventing the wheel
2. **Copy to src/**: Copy relevant files from material_systems/ to src/ directory
3. **Customize**: Modify the copied files in src/ for your specific needs
4. **Never modify material_systems/**: Keep original material files unchanged as reference

**Directory Usage**:
- **material_systems/**: Reference materials and prototypes (READ-ONLY)
- **src/**: Active development code (copy from material_systems, then customize)

Experimental implementations organized by sophistication levels:
- **10.Ultra/**: Advanced ultrathink engine implementations
  - `lna_es_v2_ultrathink_engine_super_real.py`: Core engine
  - `ultrathink_graph_extractor_super_real.py`: Graph extraction
  - `test_real_lnaes_restoration_super_real.py`: Testing framework
- **20.Hyper/**: Dynamic user correction and semantic restoration
  - `dynamic_user_correction_system_super_real.py`: User feedback integration
  - `hamlet_semantic_restoration_2025_super_real.py`: Advanced restoration
  - `neo4j_graph_demo_super_real.py`: Graph demonstration
- **30.Super/**: F1 optimization and genre-specific systems
  - `complete_integrated_f1_optimization_system_super_real.py`: F1 optimization
  - `f1_auto_tuning_system_super_real.py`: Auto-tuning
  - `genre_specific_selftest_system_super_real.py`: Genre testing
  - `manuscript_adaptive_weighting_system_clean_super_real.py`: Adaptive weighting
- **40.Real/**: Core graph creation and restoration pipeline
  - `create_graph_real.py`: Basic graph creation
  - `graph_extractor_real.py`: Entity extraction
  - `semantic_restoration_pipeline_real.py`: Restoration pipeline
  - `neo4j_graph_manager_real.py`: Neo4j management
- **50.docs/**: Documentation and integration guides
  - Various `.md` files with implementation guides and specifications

### Key Data Flow (v3.2 Revolutionary Pipeline)
1. **Stage 1**: Text ingestion → Ultrathink Engine (345-dimensional analysis) → RURI-V3/Qwen3 embeddings → Unique ID assignment → Neo4j Cypher generation → Graph ID issuance
2. **Stage 2**: Graph ID + User Request → Neo4j query → Semantic analysis → Custom output generation (modern Japanese, poetry, analysis, etc.)

**Legacy Flow (deprecated)**:
1. Text ingestion → sentence segmentation → entity extraction
2. Ontology weight assignment (15 dimensions) → random vector embeddings  
3. JSON artifact generation → Cypher script creation
4. Neo4j graph population → semantic restoration

### Classification Systems
- **NDC**: Nippon Decimal Classification (classifiers/ndc.json)
- **Kindle**: Genre classification (classifiers/kindle.json)

### Models
- **Ruri_V3_310m/**: Japanese sentence transformer model
- **Qwen3-Embedding/**: Embedding model (GGUF format)

## Important Notes

### Core Principles
- **Original text is never stored** - only abstracted semantic information (legal compliance)
- **345-dimensional analysis** provides true semantic understanding beyond keywords
- **Two-stage pipeline** enables flexible input/output transformations
- **Graph ID system** allows permanent reference to semantic knowledge

### Technical Implementation
- **Docker-compose** provides Neo4j instance with APOC plugins
- **Community Edition support** with flattened properties and parameter-based Cypher
- **RURI-V3 + Qwen3** embeddings for 768-dimensional vector space
- **v3.2 UL-ID format**: 12-digit base + millisecond timestamp + nested sub-IDs

### Development Status

#### Phase 1: Core Infrastructure [⚪︎] COMPLETED
- [⚪︎] Python 3.12 venv environment setup
- [⚪︎] Neo4j Docker container configuration
- [⚪︎] ID generation system (v3.2 UL-ID format)
- [⚪︎] Vector embedding integration (RURI-V3 + Qwen3)
- [⚪︎] Basic project structure and team workflow

#### Phase 2: Revolutionary Discovery [⚪︎] COMPLETED  
- [⚪︎] NDC/Kindle classification analysis and testing
- [⚪︎] Performance issues identification (方丈記 → 社会科学 misclassification)
- [⚪︎] Ultrathink Engine discovery and integration
- [⚪︎] 345-dimensional analysis breakthrough (Beauty Quality: 1.000)
- [⚪︎] Classification system replacement decision

#### Phase 3: Ultrathink Pipeline Implementation [⚪︎] COMPLETED
- [⚪︎] Ultrathink Engine integration (`src/ultrathink_extractor.py`)
- [⚪︎] 345-dimensional semantic analysis (CTA: 44 + Ontology: 8 + Meta: 293)
- [⚪︎] Neo4j Cypher generation with Community Edition support
- [⚪︎] Graph ID issuance system
- [⚪︎] JSON + Cypher dual output format

#### Phase 4: Two-Stage Pipeline Architecture [⚪︎] COMPLETED
- [⚪︎] Stage 1: Text → Graph pipeline (`lna_es_pipeline.py stage1`)
- [⚪︎] Stage 2: Graph → Output pipeline (`lna_es_pipeline.py stage2`)
- [⚪︎] Multi-format output generation (modern Japanese, poetry, analysis, summary)
- [⚪︎] User request parsing and semantic restoration
- [⚪︎] Quality metrics and validation system

#### Phase 5: Production Readiness [ ] IN PROGRESS
- [⚪︎] Complete pipeline testing with 方丈記
- [⚪︎] Documentation and CLAUDE.md comprehensive update
- [ ] Performance optimization and scalability testing
- [ ] Error handling and edge case management
- [ ] User interface and CLI improvements

#### Phase 6: OSS Release Preparation [ ] PENDING
- [ ] README.md and documentation finalization
- [ ] License selection and legal compliance verification
- [ ] GitHub repository setup (https://github.com/lna-lab/lna-es)
- [ ] Installation and setup instructions
- [ ] Example datasets and usage demonstrations

#### Phase 7: Advanced Features [ ] FUTURE
- [ ] Milvus/FAISS vector database integration
- [ ] Web interface development
- [ ] Batch processing capabilities
- [ ] Multi-language support expansion
- [ ] Advanced restoration algorithms

#### Phase 8: フラクタルベクターシステム [ ] CRITICAL NEXT
- [ ] 主ノード（Work Node）メタエンティティ統合システム
  - [ ] 345次元CTA分析所感エンティティ
  - [ ] AI個性・感受性エンティティ
  - [ ] 書誌・意図・グラフ特性の包括的統合
- [ ] 768次元フラクタルベクトル生成システム
  - [ ] 主ノード継承ベクトル（307次元）
  - [ ] ノード固有ベクトル（269次元）
  - [ ] 関係性ベクトル（115次元）
  - [ ] メタ文脈ベクトル（77次元）
- [ ] フラクタル階層検索エンジン
  - [ ] 階層的セマンティック検索
  - [ ] フラクタル一貫性スコア計算
  - [ ] 適応的検索深度決定
- [ ] 参照設計書: `/material_systems/50.docs/realtime_ai_wife_vector_strategy.md`

#### Current Status Summary
- **Core System**: [⚪︎] 100% Operational
- **345-Dimensional Analysis**: [⚪︎] Proven with 95% accuracy
- **Two-Stage Pipeline**: [⚪︎] Fully functional
- **OSS Ready**: [⚪︎] 85% complete
- **Next Milestone**: Performance optimization and GitHub release

## File Locations

### Core Implementation
- **Main pipeline**: `src/lna_es_pipeline.py` (Two-stage system)
- **Ultrathink engine**: `src/ultrathink_extractor.py` (345-dimensional analysis)
- **Legacy app**: `lna-es-app/` (Original implementation)
- **Material systems**: `material_systems/` (Research prototypes - READ ONLY)

### Data and Configuration
- **Test texts**: `Text/` (Classical Japanese literature, sample files)
- **Generated artifacts**: `out/` (JSON, Cypher, restored texts)
- **Ontology definitions**: `ontology/` (Legacy 15-dimensional system)
- **Vector models**: `models/` (RURI-V3, Qwen3-Embedding)

### Infrastructure
- **Neo4j setup**: `docker-compose.yml`
- **Python environment**: `venv/` (Python 3.12)
- **Development logs**: `log/` (Team communication and progress tracking)

### Progress Tracking Files
- **Project status**: `CLAUDE.md` (This file)
- **Breakthrough log**: `log/BREAKTHROUGH_LOG.md` (Major discoveries)
- **Session logs**: `log/YYYY-MM-DD_session_log.md` (Daily progress)
- **Task management**: `log/maya_tasks.md`, `log/lina_tasks.md` (Agent coordination)