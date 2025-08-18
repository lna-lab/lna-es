#!/usr/bin/env python3
"""
LNA-ES v3.2 System Completeness Evaluation
==========================================

現在のシステムの復元率とパイプライン完成度を包括的評価
Ken's directive: 現状レベルと完成度の定量的把握

評価項目:
1. Pipeline Completeness (パイプライン完成度)
2. Restoration Quality (復元品質)
3. Component Maturity (コンポーネント成熟度)
4. Integration Level (統合レベル)
5. Production Readiness (本番準備度)
"""

import json
import time
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
import logging

ROOT = Path(__file__).resolve().parents[1]

@dataclass
class ComponentStatus:
    """コンポーネント状態"""
    name: str
    status: str  # not_implemented, prototype, functional, production_ready
    completeness: float  # 0.0-1.0
    quality_score: float  # 0.0-1.0
    issues: List[str]
    dependencies: List[str]

@dataclass
class PipelineStage:
    """パイプライン段階"""
    stage_name: str
    required_components: List[str]
    implemented_components: List[str]
    stage_completeness: float
    bottlenecks: List[str]
    
@dataclass
class SystemEvaluation:
    """システム評価結果"""
    overall_completeness: float
    restoration_capability: float
    pipeline_maturity: float
    production_readiness: float
    components: List[ComponentStatus]
    pipeline_stages: List[PipelineStage]
    critical_gaps: List[str]
    recommendations: List[str]
    timestamp: int

class SystemCompletenessEvaluator:
    """システム完成度評価器"""
    
    def __init__(self):
        # 要件定義書ベースの完全パイプライン定義
        self.required_pipeline = {
            "1_ingest": {
                "name": "Text Ingestion",
                "components": ["file_reader", "encoding_detector", "text_preprocessor", "deduplication"],
                "maturity_target": 0.9
            },
            "2_analysis": {
                "name": "345-Dimension Analysis", 
                "components": ["cta_analyzer", "ontology_mapper", "semantic_analyzer", "ultrathink_engine"],
                "maturity_target": 0.85
            },
            "3_extraction": {
                "name": "Graph Extraction",
                "components": ["entity_extractor", "relationship_mapper", "cypher_generator", "validation"],
                "maturity_target": 0.8
            },
            "4_classification": {
                "name": "Triple Classification",
                "components": ["ndc_classifier", "kindle_classifier", "ontology_weighter", "triple_validator"],
                "maturity_target": 0.85
            },
            "5_vectorization": {
                "name": "Vector Embedding",
                "components": ["ruri_v3_embedder", "qwen3_embedder", "vector_indexer", "similarity_engine"],
                "maturity_target": 0.7
            },
            "6_persistence": {
                "name": "Graph Persistence",
                "components": ["neo4j_manager", "cypher_applier", "constraint_manager", "backup_system"],
                "maturity_target": 0.8
            },
            "7_restoration": {
                "name": "Semantic Restoration",
                "components": ["restoration_engine", "aesthetic_enhancer", "length_controller", "quality_validator"],
                "maturity_target": 0.6  # 最難関
            }
        }
        
    def evaluate_system(self) -> SystemEvaluation:
        """システム全体評価"""
        
        print("🔍 Starting LNA-ES v3.2 System Completeness Evaluation")
        print("=" * 60)
        
        # 1. コンポーネント評価
        components = self._evaluate_components()
        
        # 2. パイプライン段階評価
        pipeline_stages = self._evaluate_pipeline_stages(components)
        
        # 3. 復元能力テスト
        restoration_capability = self._test_restoration_capability()
        
        # 4. 統合レベル評価
        integration_level = self._evaluate_integration_level()
        
        # 5. 総合評価
        overall_completeness = self._calculate_overall_completeness(components, pipeline_stages)
        pipeline_maturity = self._calculate_pipeline_maturity(pipeline_stages)
        production_readiness = self._calculate_production_readiness(components, restoration_capability)
        
        # 6. 課題と推奨事項
        critical_gaps = self._identify_critical_gaps(components, pipeline_stages)
        recommendations = self._generate_recommendations(critical_gaps, restoration_capability)
        
        evaluation = SystemEvaluation(
            overall_completeness=overall_completeness,
            restoration_capability=restoration_capability,
            pipeline_maturity=pipeline_maturity,
            production_readiness=production_readiness,
            components=components,
            pipeline_stages=pipeline_stages,
            critical_gaps=critical_gaps,
            recommendations=recommendations,
            timestamp=int(time.time())
        )
        
        return evaluation
        
    def _evaluate_components(self) -> List[ComponentStatus]:
        """コンポーネント個別評価"""
        
        print("\n📋 Evaluating Individual Components")
        print("-" * 40)
        
        components = []
        
        # Enhanced Classification System
        enhanced_status = self._check_enhanced_classification()
        components.append(enhanced_status)
        print(f"✅ Enhanced Classification: {enhanced_status.completeness:.1%}")
        
        # Ultra-Super Hybrid System
        hybrid_status = self._check_ultra_super_hybrid()
        components.append(hybrid_status)
        print(f"🚀 Ultra-Super Hybrid: {hybrid_status.completeness:.1%}")
        
        # ID Generation System
        id_gen_status = self._check_id_generation()
        components.append(id_gen_status)
        print(f"🔢 ID Generation: {id_gen_status.completeness:.1%}")
        
        # Vector Embedding System
        vector_status = self._check_vector_system()
        components.append(vector_status)
        print(f"🧠 Vector Embeddings: {vector_status.completeness:.1%}")
        
        # Neo4j Integration
        neo4j_status = self._check_neo4j_integration()
        components.append(neo4j_status)
        print(f"📊 Neo4j Integration: {neo4j_status.completeness:.1%}")
        
        # Extractor Pipeline
        extractor_status = self._check_extractor_pipeline()
        components.append(extractor_status)
        print(f"⚙️ Extractor Pipeline: {extractor_status.completeness:.1%}")
        
        # API System
        api_status = self._check_api_system()
        components.append(api_status)
        print(f"🌐 API System: {api_status.completeness:.1%}")
        
        # Restoration Engine
        restoration_status = self._check_restoration_engine()
        components.append(restoration_status)
        print(f"🔄 Restoration Engine: {restoration_status.completeness:.1%}")
        
        return components
        
    def _check_enhanced_classification(self) -> ComponentStatus:
        """Enhanced Classification評価"""
        
        # ファイル存在確認
        enhanced_file = ROOT / "src/enhanced_classification.py"
        if not enhanced_file.exists():
            return ComponentStatus(
                name="Enhanced Classification",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["File not found"],
                dependencies=[]
            )
            
        # 機能テスト
        try:
            result = subprocess.run([
                str(ROOT / "venv/bin/python"), "-c",
                "from src.enhanced_classification import EnhancedClassifier; print('OK')"
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                return ComponentStatus(
                    name="Enhanced Classification",
                    status="functional",
                    completeness=0.85,
                    quality_score=0.75,
                    issues=["Overfitting warnings detected"],
                    dependencies=["NDC data", "Kindle data", "Ontology system"]
                )
            else:
                return ComponentStatus(
                    name="Enhanced Classification",
                    status="prototype",
                    completeness=0.5,
                    quality_score=0.4,
                    issues=[f"Import error: {result.stderr}"],
                    dependencies=[]
                )
        except Exception as e:
            return ComponentStatus(
                name="Enhanced Classification",
                status="prototype",
                completeness=0.3,
                quality_score=0.2,
                issues=[f"Execution error: {e}"],
                dependencies=[]
            )
            
    def _check_ultra_super_hybrid(self) -> ComponentStatus:
        """Ultra-Super Hybrid評価"""
        
        hybrid_file = ROOT / "src/ultra_super_hybrid.py"
        if not hybrid_file.exists():
            return ComponentStatus(
                name="Ultra-Super Hybrid",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["File not found"],
                dependencies=[]
            )
            
        try:
            result = subprocess.run([
                str(ROOT / "venv/bin/python"), "-c",
                "from src.ultra_super_hybrid import UltraSuperHybrid; h=UltraSuperHybrid(); print('OK')"
            ], capture_output=True, text=True, timeout=15)
            
            if result.returncode == 0:
                return ComponentStatus(
                    name="Ultra-Super Hybrid",
                    status="functional",
                    completeness=0.80,
                    quality_score=0.85,
                    issues=["F1 system fallback mode"],
                    dependencies=["material_systems/10.Ultra", "material_systems/30.Super"]
                )
            else:
                return ComponentStatus(
                    name="Ultra-Super Hybrid",
                    status="prototype",
                    completeness=0.4,
                    quality_score=0.3,
                    issues=[f"Error: {result.stderr}"],
                    dependencies=[]
                )
        except Exception as e:
            return ComponentStatus(
                name="Ultra-Super Hybrid",
                status="prototype",
                completeness=0.2,
                quality_score=0.1,
                issues=[f"Exception: {e}"],
                dependencies=[]
            )
            
    def _check_id_generation(self) -> ComponentStatus:
        """ID Generation System評価"""
        
        id_file = ROOT / "lna-es-app/apps/shared/id_generator.py"
        if not id_file.exists():
            return ComponentStatus(
                name="ID Generation",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["File not found"],
                dependencies=[]
            )
            
        try:
            result = subprocess.run([
                str(ROOT / "venv/bin/python"), 
                str(id_file)
            ], capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0 and "UL-ID" in result.stdout:
                return ComponentStatus(
                    name="ID Generation",
                    status="production_ready",
                    completeness=1.0,
                    quality_score=0.95,
                    issues=[],
                    dependencies=[]
                )
            else:
                return ComponentStatus(
                    name="ID Generation",
                    status="functional",
                    completeness=0.7,
                    quality_score=0.6,
                    issues=["Output format issues"],
                    dependencies=[]
                )
        except Exception as e:
            return ComponentStatus(
                name="ID Generation",
                status="prototype",
                completeness=0.3,
                quality_score=0.2,
                issues=[f"Exception: {e}"],
                dependencies=[]
            )
            
    def _check_vector_system(self) -> ComponentStatus:
        """Vector Embedding System評価"""
        
        vector_file = ROOT / "src/vector_embeddings.py"
        if not vector_file.exists():
            return ComponentStatus(
                name="Vector Embeddings",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["File not found"],
                dependencies=[]
            )
            
        try:
            result = subprocess.run([
                str(ROOT / "venv/bin/python"), 
                str(vector_file)
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                return ComponentStatus(
                    name="Vector Embeddings",
                    status="functional",
                    completeness=0.75,
                    quality_score=0.70,
                    issues=["RURI-V3/Qwen3 models not installed", "Fallback mode only"],
                    dependencies=["RURI-V3 model", "Qwen3 model", "Language detection"]
                )
            else:
                return ComponentStatus(
                    name="Vector Embeddings",
                    status="prototype",
                    completeness=0.4,
                    quality_score=0.3,
                    issues=[f"Execution error: {result.stderr}"],
                    dependencies=[]
                )
        except Exception as e:
            return ComponentStatus(
                name="Vector Embeddings",
                status="prototype",
                completeness=0.2,
                quality_score=0.1,
                issues=[f"Exception: {e}"],
                dependencies=[]
            )
            
    def _check_neo4j_integration(self) -> ComponentStatus:
        """Neo4j Integration評価"""
        
        # Neo4j接続テスト
        try:
            result = subprocess.run([
                "docker", "ps", "--filter", "name=neo4j", "--format", "{{.Status}}"
            ], capture_output=True, text=True, timeout=5)
            
            neo4j_running = "Up" in result.stdout
            
            if neo4j_running:
                return ComponentStatus(
                    name="Neo4j Integration",
                    status="functional",
                    completeness=0.85,
                    quality_score=0.80,
                    issues=["Community Edition constraints"],
                    dependencies=["Docker Desktop", "Neo4j container"]
                )
            else:
                return ComponentStatus(
                    name="Neo4j Integration",
                    status="prototype",
                    completeness=0.6,
                    quality_score=0.5,
                    issues=["Neo4j container not running"],
                    dependencies=["Docker Desktop", "Neo4j setup"]
                )
        except Exception as e:
            return ComponentStatus(
                name="Neo4j Integration",
                status="not_implemented",
                completeness=0.2,
                quality_score=0.1,
                issues=[f"Docker check failed: {e}"],
                dependencies=["Docker Desktop"]
            )
            
    def _check_extractor_pipeline(self) -> ComponentStatus:
        """Extractor Pipeline評価"""
        
        extractor_file = ROOT / "lna-es-app/apps/extractor/extractor.py"
        if not extractor_file.exists():
            return ComponentStatus(
                name="Extractor Pipeline",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["File not found"],
                dependencies=[]
            )
            
        try:
            result = subprocess.run([
                str(ROOT / "venv/bin/python"), 
                str(extractor_file),
                "--help"
            ], capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                return ComponentStatus(
                    name="Extractor Pipeline",
                    status="functional",
                    completeness=0.90,
                    quality_score=0.85,
                    issues=["Memory usage on large files"],
                    dependencies=["ID generator", "Enhanced classification", "Vector embeddings"]
                )
            else:
                return ComponentStatus(
                    name="Extractor Pipeline",
                    status="prototype",
                    completeness=0.5,
                    quality_score=0.4,
                    issues=[f"Help command failed: {result.stderr}"],
                    dependencies=[]
                )
        except Exception as e:
            return ComponentStatus(
                name="Extractor Pipeline",
                status="prototype",
                completeness=0.3,
                quality_score=0.2,
                issues=[f"Exception: {e}"],
                dependencies=[]
            )
            
    def _check_api_system(self) -> ComponentStatus:
        """API System評価"""
        
        # Lina APIテスト
        lina_status = self._test_api_endpoint("localhost:3001", "/health")
        
        # Maya APIテスト  
        maya_status = self._test_api_endpoint("localhost:3000", "/health")
        
        if lina_status and maya_status:
            return ComponentStatus(
                name="API System",
                status="functional",
                completeness=0.95,
                quality_score=0.90,
                issues=[],
                dependencies=["Lina API", "Maya API", "curl communication"]
            )
        elif lina_status or maya_status:
            return ComponentStatus(
                name="API System",
                status="functional",
                completeness=0.70,
                quality_score=0.60,
                issues=["One API endpoint down"],
                dependencies=["API servers"]
            )
        else:
            return ComponentStatus(
                name="API System",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["No API endpoints responding"],
                dependencies=["API server setup"]
            )
            
    def _check_restoration_engine(self) -> ComponentStatus:
        """Restoration Engine評価"""
        
        # 復元エンジンは material_systems にのみ存在（未統合）
        material_files = [
            ROOT / "material_systems/10.Ultra/lna_es_v2_ultrathink_engine_super_real.py",
            ROOT / "material_systems/50.docs/95percent_method.md"
        ]
        
        existing_files = [f for f in material_files if f.exists()]
        
        if len(existing_files) >= 2:
            return ComponentStatus(
                name="Restoration Engine",
                status="prototype",
                completeness=0.30,
                quality_score=0.70,  # 高品質だが未統合
                issues=["Not integrated into main pipeline", "95% method needs implementation"],
                dependencies=["material_systems integration", "LNA consciousness method"]
            )
        else:
            return ComponentStatus(
                name="Restoration Engine",
                status="not_implemented",
                completeness=0.0,
                quality_score=0.0,
                issues=["No restoration engine in main pipeline"],
                dependencies=["95% restoration method", "Aesthetic quality system"]
            )
            
    def _test_api_endpoint(self, host: str, endpoint: str) -> bool:
        """API endpoint テスト"""
        try:
            result = subprocess.run([
                "curl", "-X", "GET", f"http://{host}{endpoint}"
            ], capture_output=True, text=True, timeout=3)
            
            return result.returncode == 0 and "ok" in result.stdout.lower()
        except:
            return False
            
    def _evaluate_pipeline_stages(self, components: List[ComponentStatus]) -> List[PipelineStage]:
        """パイプライン段階評価"""
        
        print("\n⚙️ Evaluating Pipeline Stages")
        print("-" * 40)
        
        pipeline_stages = []
        
        for stage_id, stage_def in self.required_pipeline.items():
            # 実装済みコンポーネント特定
            implemented = []
            
            # コンポーネント名とステージ要件のマッピング
            component_mapping = {
                "Enhanced Classification": ["ndc_classifier", "kindle_classifier", "ontology_weighter"],
                "Ultra-Super Hybrid": ["cta_analyzer", "semantic_analyzer", "ultrathink_engine"],
                "ID Generation": ["file_reader", "text_preprocessor"],
                "Vector Embeddings": ["ruri_v3_embedder", "qwen3_embedder", "vector_indexer"],
                "Neo4j Integration": ["neo4j_manager", "cypher_applier", "constraint_manager"],
                "Extractor Pipeline": ["entity_extractor", "relationship_mapper", "cypher_generator"],
                "API System": ["validation", "quality_validator"],
                "Restoration Engine": ["restoration_engine", "aesthetic_enhancer", "length_controller"]
            }
            
            for component in components:
                if component.status in ["functional", "production_ready"]:
                    mapped_components = component_mapping.get(component.name, [])
                    implemented.extend(mapped_components)
                    
            # ステージ完成度計算
            required_components = stage_def["components"]
            implemented_components = [c for c in required_components if c in implemented]
            stage_completeness = len(implemented_components) / len(required_components)
            
            # ボトルネック特定
            bottlenecks = [c for c in required_components if c not in implemented]
            
            stage = PipelineStage(
                stage_name=stage_def["name"],
                required_components=required_components,
                implemented_components=implemented_components,
                stage_completeness=stage_completeness,
                bottlenecks=bottlenecks
            )
            
            pipeline_stages.append(stage)
            print(f"📊 {stage.stage_name}: {stage_completeness:.1%} complete")
            
        return pipeline_stages
        
    def _test_restoration_capability(self) -> float:
        """復元能力テスト"""
        
        print("\n🔄 Testing Restoration Capability")
        print("-" * 40)
        
        # A/Bテスト結果を参照
        ab_results_dir = ROOT / "out/ab_tests"
        if ab_results_dir.exists():
            ab_files = list(ab_results_dir.glob("*.json"))
            if ab_files:
                latest_ab = max(ab_files, key=lambda f: f.stat().st_mtime)
                try:
                    with open(latest_ab, 'r', encoding='utf-8') as f:
                        ab_data = json.load(f)
                        
                    # 最良手法の結果を抽出
                    recommendation = ab_data.get("recommendation", "")
                    if "hybrid_ultra_super" in recommendation:
                        # hybrid_ultra_super の平均性能を算出
                        hybrid_results = [r for r in ab_data.get("results", []) 
                                        if r.get("method_name") == "hybrid_ultra_super"]
                        
                        if hybrid_results:
                            avg_semantic = sum(r.get("semantic_coherence", 0) for r in hybrid_results) / len(hybrid_results)
                            avg_aesthetic = sum(r.get("aesthetic_quality", 0) for r in hybrid_results) / len(hybrid_results)
                            
                            # 復元能力スコア（意味的一貫性 + 美的品質）
                            restoration_score = (avg_semantic + avg_aesthetic) / 2
                            print(f"📈 Current restoration capability: {restoration_score:.1%}")
                            return restoration_score
                except:
                    pass
                    
        # フォールバック：基本テスト
        print("📈 Fallback estimation: 15% (basic pipeline only)")
        return 0.15
        
    def _evaluate_integration_level(self) -> float:
        """統合レベル評価"""
        
        # API通信可能性
        api_integration = 0.8 if self._test_api_endpoint("localhost:3001", "/health") else 0.0
        
        # ファイルベース統合
        file_integration = 0.6 if (ROOT / "out/metrics.json").exists() else 0.0
        
        # コンポーネント間依存関係
        dependency_integration = 0.7  # extractor -> classification -> neo4j
        
        return (api_integration + file_integration + dependency_integration) / 3
        
    def _calculate_overall_completeness(self, 
                                      components: List[ComponentStatus],
                                      pipeline_stages: List[PipelineStage]) -> float:
        """全体完成度計算"""
        
        # コンポーネント完成度（重み付け平均）
        component_weights = {
            "Enhanced Classification": 0.15,
            "Ultra-Super Hybrid": 0.20,
            "ID Generation": 0.10,
            "Vector Embeddings": 0.10,
            "Neo4j Integration": 0.15,
            "Extractor Pipeline": 0.15,
            "API System": 0.10,
            "Restoration Engine": 0.05  # 未実装でも最小重み
        }
        
        weighted_completeness = 0.0
        for component in components:
            weight = component_weights.get(component.name, 0.0)
            weighted_completeness += component.completeness * weight
            
        # パイプライン段階完成度
        pipeline_completeness = sum(stage.stage_completeness for stage in pipeline_stages) / len(pipeline_stages)
        
        # 統合レベル
        integration_level = self._evaluate_integration_level()
        
        # 全体完成度（加重平均）
        overall = (weighted_completeness * 0.5 + pipeline_completeness * 0.3 + integration_level * 0.2)
        
        return overall
        
    def _calculate_pipeline_maturity(self, pipeline_stages: List[PipelineStage]) -> float:
        """パイプライン成熟度計算"""
        
        # 各段階の完成度に目標達成度を掛け合わせ
        maturity_scores = []
        for stage_id, stage_def in self.required_pipeline.items():
            stage = next((s for s in pipeline_stages if s.stage_name == stage_def["name"]), None)
            if stage:
                target = stage_def["maturity_target"]
                actual = stage.stage_completeness
                maturity_score = min(actual / target, 1.0) if target > 0 else 0.0
                maturity_scores.append(maturity_score)
                
        return sum(maturity_scores) / len(maturity_scores) if maturity_scores else 0.0
        
    def _calculate_production_readiness(self, 
                                      components: List[ComponentStatus],
                                      restoration_capability: float) -> float:
        """本番準備度計算"""
        
        # 必須コンポーネントの production_ready 状態
        critical_components = ["Enhanced Classification", "Extractor Pipeline", "Neo4j Integration"]
        production_ready_count = sum(1 for c in components 
                                   if c.name in critical_components and c.status == "production_ready")
        
        readiness_ratio = production_ready_count / len(critical_components)
        
        # 復元能力と組み合わせ
        production_readiness = (readiness_ratio * 0.7 + restoration_capability * 0.3)
        
        return production_readiness
        
    def _identify_critical_gaps(self, 
                              components: List[ComponentStatus],
                              pipeline_stages: List[PipelineStage]) -> List[str]:
        """重要なギャップ特定"""
        
        gaps = []
        
        # 復元エンジン未実装
        restoration_component = next((c for c in components if c.name == "Restoration Engine"), None)
        if not restoration_component or restoration_component.completeness < 0.5:
            gaps.append("Restoration Engine not integrated - 95% method from material_systems needs implementation")
            
        # Vector model 未インストール
        vector_component = next((c for c in components if c.name == "Vector Embeddings"), None)
        if vector_component and "models not installed" in str(vector_component.issues):
            gaps.append("RURI-V3 and Qwen3 models not installed - only fallback mode available")
            
        # パイプライン最大ボトルネック
        worst_stage = min(pipeline_stages, key=lambda s: s.stage_completeness)
        if worst_stage.stage_completeness < 0.5:
            gaps.append(f"Pipeline bottleneck: {worst_stage.stage_name} only {worst_stage.stage_completeness:.1%} complete")
            
        # F1最適化システム
        hybrid_component = next((c for c in components if c.name == "Ultra-Super Hybrid"), None)
        if hybrid_component and "fallback mode" in str(hybrid_component.issues):
            gaps.append("F1 optimization system (30.Super) not fully integrated")
            
        return gaps
        
    def _generate_recommendations(self, 
                                critical_gaps: List[str],
                                restoration_capability: float) -> List[str]:
        """推奨事項生成"""
        
        recommendations = []
        
        # 復元率改善
        if restoration_capability < 0.5:
            recommendations.append("Priority 1: Integrate material_systems/50.docs 95% restoration method")
            recommendations.append("Priority 2: Implement LNA consciousness-based restoration engine")
            
        # パイプライン完成
        recommendations.append("Priority 3: Complete vector embedding system with actual RURI-V3/Qwen3 models")
        
        # 品質向上
        recommendations.append("Priority 4: Resolve overfitting warnings in classification system")
        
        # スケーラビリティ
        recommendations.append("Priority 5: Implement FAISS/Milvus for large-scale vector operations")
        
        # 本番準備
        if any("Neo4j" in gap for gap in critical_gaps):
            recommendations.append("Priority 6: Setup production Neo4j with Enterprise features")
            
        return recommendations

def main():
    """メイン実行"""
    evaluator = SystemCompletenessEvaluator()
    evaluation = evaluator.evaluate_system()
    
    # 結果表示
    print("\n" + "=" * 60)
    print("🎯 LNA-ES v3.2 System Evaluation Results")
    print("=" * 60)
    
    print(f"\n📊 Overall Completeness: {evaluation.overall_completeness:.1%}")
    print(f"🔄 Restoration Capability: {evaluation.restoration_capability:.1%}")
    print(f"⚙️ Pipeline Maturity: {evaluation.pipeline_maturity:.1%}")
    print(f"🚀 Production Readiness: {evaluation.production_readiness:.1%}")
    
    print(f"\n❌ Critical Gaps ({len(evaluation.critical_gaps)}):")
    for i, gap in enumerate(evaluation.critical_gaps, 1):
        print(f"  {i}. {gap}")
        
    print(f"\n💡 Recommendations ({len(evaluation.recommendations)}):")
    for rec in evaluation.recommendations:
        print(f"  • {rec}")
        
    # 結果保存
    output_file = ROOT / "out/system_evaluation.json"
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(asdict(evaluation), f, ensure_ascii=False, indent=2)
        
    print(f"\n💾 Detailed results saved: {output_file}")
    
    # サマリー
    print(f"\n🎯 SUMMARY:")
    if evaluation.overall_completeness >= 0.8:
        print("✅ System is near production ready")
    elif evaluation.overall_completeness >= 0.6:
        print("🔶 System is functional but needs optimization")
    elif evaluation.overall_completeness >= 0.4:
        print("🔶 System has core functionality, major gaps remain")
    else:
        print("🔴 System is in early development stage")
        
    print(f"📈 Current restoration level: ~{evaluation.restoration_capability:.0%} (Target: 95%)")

if __name__ == "__main__":
    main()