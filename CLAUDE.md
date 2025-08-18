# CLAUDE.md - LNA-ES v3.2 Development Guide

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

LNA-ES (Living Neural Architecture - Enhanced System) v3.0 is a text processing pipeline that ingests arbitrary text files, classifies them using NDC (Nippon Decimal Classification) and Kindle genre schemes, extracts entities and relationships, assigns 15-dimensional ontology weights, and generates Neo4j graph databases. The system abstracts text into knowledge graphs without storing original content, enabling semantic restoration and analysis.

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

### Core Pipeline Commands
```bash
# Text ingestion pipeline
make ingest INPUT=path/to/file.txt

# Apply generated Cypher to Neo4j
make apply CYPHER=out/<work_id>.cypher

# Restore text summary from graph
make restore DOC=<work_id>

# Evaluate restoration quality
make eval ORIG=path/to/original.txt REST=out/restored_<work_id>.txt
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

### 15-Dimensional Ontology System (ontology/)
Hierarchical ontology system with weighted layers:
- **Foundation Layer** (weight: 1.0): temporal, spatial, emotion, sensation, natural
- **Relational Layer** (weight: 0.95): relationship, causality, action
- **Structural Layer** (weight: 0.9): narrative_structure, character_function, discourse_structure
- **Cultural Layer** (weight: 0.85): story_classification, food_culture
- **Advanced Layer** (weight: 0.8): indirect_emotion
- **Meta Layer** (weight: 0.75): meta_graph
- **Emotions Layer** (weight: 0.85): emotion_nodes, emotion_relationships, etc.

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

### Key Data Flow
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

- Original text is never stored - only abstracted semantic information
- System uses random embeddings in reference implementation (replace with real models in production)
- Docker-compose provides Neo4j instance with APOC plugins
- Cypher constraints defined in `schemas/constraints.cypher`
- Material systems contain experimental code for advanced features

## File Locations

- Main app: `lna-es-app/`
- Ontology definitions: `ontology/foundation/`, `ontology/relational/`, etc.
- Test texts: `Text/` (classical Japanese literature)
- Generated artifacts: `lna-es-app/data/`, `lna-es-app/out/`
- Neo4j setup: `docker-compose.yml`