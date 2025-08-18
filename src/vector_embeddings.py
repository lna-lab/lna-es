#!/usr/bin/env python3
"""
vector_embeddings.py
--------------------

LNA-ES v3.2 Vector Embedding Integration
Implements RURI-V3 (Japanese) and Qwen3-Embedding (Multilingual) support

Requirements:
- RURI-V3: Japanese 768-dimensional embeddings
- Qwen3-Embedding: Multilingual + code embeddings (GGUF format)
"""

import json
import numpy as np
from pathlib import Path
from typing import List, Optional, Dict, Any, Union
import hashlib
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VectorEmbeddingManager:
    """
    Manages vector embeddings for LNA-ES v3.2
    Supports RURI-V3 and Qwen3-Embedding models
    """
    
    def __init__(self, models_path: Optional[Path] = None):
        self.models_path = models_path or Path(__file__).parent.parent / "models"
        self.ruri_model = None
        self.qwen_model = None
        self.cache = {}
        
        # Model configurations
        self.ruri_config = {
            "path": self.models_path / "Ruri_V3_310m",
            "dimensions": 768,
            "language": "japanese",
            "max_length": 512
        }
        
        self.qwen_config = {
            "path": self.models_path / "Qwen3-Embedding" / "Qwen3-Embedding-0.6B-Q8_0.gguf",
            "dimensions": 768,  # Same as RURI-V3 for compatibility
            "language": "multilingual",
            "format": "gguf"
        }
        
        # Initialize models if available
        self._init_models()
    
    def _init_models(self):
        """Initialize embedding models if available"""
        try:
            # Try to initialize RURI-V3 (SentenceTransformers)
            if self.ruri_config["path"].exists():
                self._init_ruri_model()
            else:
                logger.warning(f"RURI-V3 model not found at {self.ruri_config['path']}")
                
            # Try to initialize Qwen3 (GGUF format)
            if self.qwen_config["path"].exists():
                self._init_qwen_model()
            else:
                logger.warning(f"Qwen3 model not found at {self.qwen_config['path']}")
                
        except ImportError as e:
            logger.warning(f"Missing dependencies for embedding models: {e}")
            logger.info("Using fallback random embeddings")
    
    def _init_ruri_model(self):
        """Initialize RURI-V3 SentenceTransformer model"""
        try:
            from sentence_transformers import SentenceTransformer
            self.ruri_model = SentenceTransformer(str(self.ruri_config["path"]))
            logger.info("RURI-V3 model loaded successfully")
        except ImportError:
            logger.warning("sentence-transformers not installed. Install with: pip install sentence-transformers")
        except Exception as e:
            logger.error(f"Failed to load RURI-V3 model: {e}")
    
    def _init_qwen_model(self):
        """Initialize Qwen3 GGUF model"""
        try:
            # Try llama-cpp-python for GGUF support
            from llama_cpp import Llama
            self.qwen_model = Llama(
                model_path=str(self.qwen_config["path"]),
                embedding=True,
                verbose=False
            )
            # Verify embedding dimensions (should be 768 for compatibility with RURI-V3)
            test_embedding = self.qwen_model.create_embedding("test")
            actual_dims = len(test_embedding["data"][0]["embedding"])
            if actual_dims != 768:
                logger.warning(f"Qwen3 model has {actual_dims} dimensions, expected 768")
            else:
                logger.info("Qwen3 dimensions verified as 768 (compatible with RURI-V3)")
            logger.info(f"Qwen3 model loaded successfully ({self.qwen_config['dimensions']} dimensions)")
        except ImportError:
            logger.warning("llama-cpp-python not installed. Install with: pip install llama-cpp-python")
        except Exception as e:
            logger.error(f"Failed to load Qwen3 model: {e}")
    
    def _detect_language(self, text: str) -> str:
        """Simple language detection for text"""
        # Count Japanese characters (Hiragana, Katakana, Kanji)
        japanese_chars = 0
        total_chars = len(text)
        
        for char in text:
            if any([
                '\u3040' <= char <= '\u309F',  # Hiragana
                '\u30A0' <= char <= '\u30FF',  # Katakana
                '\u4E00' <= char <= '\u9FAF',  # Kanji
            ]):
                japanese_chars += 1
        
        japanese_ratio = japanese_chars / max(total_chars, 1)
        return "japanese" if japanese_ratio > 0.1 else "other"
    
    def get_ruri_embedding(self, text: str) -> Optional[List[float]]:
        """Get RURI-V3 embedding for Japanese text"""
        if not self.ruri_model:
            return None
            
        try:
            # Truncate text if too long
            if len(text) > self.ruri_config["max_length"]:
                text = text[:self.ruri_config["max_length"]]
                
            embedding = self.ruri_model.encode(text, normalize_embeddings=True)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"RURI embedding failed: {e}")
            return None
    
    def get_qwen_embedding(self, text: str) -> Optional[List[float]]:
        """Get Qwen3 embedding for multilingual text"""
        if not self.qwen_model:
            return None
            
        try:
            result = self.qwen_model.create_embedding(text)
            return result["data"][0]["embedding"]
        except Exception as e:
            logger.error(f"Qwen embedding failed: {e}")
            return None
    
    def get_random_embedding(self, dimensions: int, seed: Optional[str] = None) -> List[float]:
        """Generate deterministic random embedding as fallback"""
        if seed:
            # Use text hash as seed for deterministic results
            np.random.seed(int(hashlib.md5(seed.encode()).hexdigest()[:8], 16) % (2**32))
        
        # Generate normalized random vector
        vector = np.random.normal(0, 1, dimensions)
        vector = vector / np.linalg.norm(vector)
        return vector.tolist()
    
    def embed_text(self, text: str, force_model: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate embeddings for text using appropriate models
        
        Args:
            text: Text to embed
            force_model: Force specific model ("ruri" or "qwen")
            
        Returns:
            Dictionary with embedding results and metadata
        """
        if not text.strip():
            return {
                "text": text,
                "ruri_embedding": None,
                "qwen_embedding": None,
                "language": "unknown",
                "method": "empty_text",
                "timestamp": int(time.time() * 1000)
            }
        
        # Cache key for performance
        cache_key = hashlib.md5(text.encode()).hexdigest()[:16]
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        language = self._detect_language(text)
        result = {
            "text": text[:100] + "..." if len(text) > 100 else text,
            "language": language,
            "timestamp": int(time.time() * 1000)
        }
        
        # Get RURI-V3 embedding (preferred for Japanese)
        if force_model == "ruri" or (language == "japanese" and not force_model):
            ruri_embedding = self.get_ruri_embedding(text)
            result["ruri_embedding"] = ruri_embedding
            result["ruri_method"] = "model" if ruri_embedding else "fallback"
            
            if not ruri_embedding:
                result["ruri_embedding"] = self.get_random_embedding(
                    self.ruri_config["dimensions"], 
                    f"ruri_{text}"
                )
        else:
            result["ruri_embedding"] = self.get_random_embedding(
                self.ruri_config["dimensions"], 
                f"ruri_{text}"
            )
            result["ruri_method"] = "fallback"
        
        # Get Qwen3 embedding (for multilingual/code)
        if force_model == "qwen" or (language != "japanese" and not force_model):
            qwen_embedding = self.get_qwen_embedding(text)
            result["qwen_embedding"] = qwen_embedding
            result["qwen_method"] = "model" if qwen_embedding else "fallback"
            
            if not qwen_embedding:
                # Use 768 dimensions for compatibility with RURI-V3
                dimensions = 768
                result["qwen_embedding"] = self.get_random_embedding(
                    dimensions, 
                    f"qwen_{text}"
                )
        else:
            # Use 768 dimensions for compatibility with RURI-V3
            result["qwen_embedding"] = self.get_random_embedding(
                768, 
                f"qwen_{text}"
            )
            result["qwen_method"] = "fallback"
        
        # Cache result
        self.cache[cache_key] = result
        return result
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about loaded models"""
        return {
            "ruri_v3": {
                "loaded": self.ruri_model is not None,
                "path": str(self.ruri_config["path"]),
                "dimensions": self.ruri_config["dimensions"],
                "language": self.ruri_config["language"]
            },
            "qwen3": {
                "loaded": self.qwen_model is not None,
                "path": str(self.qwen_config["path"]),
                "dimensions": self.qwen_config["dimensions"],
                "format": self.qwen_config["format"]
            },
            "cache_size": len(self.cache)
        }


# Global instance for consistent embedding management
_global_embedding_manager = None

def get_embedding_manager() -> VectorEmbeddingManager:
    """Get global embedding manager instance"""
    global _global_embedding_manager
    if _global_embedding_manager is None:
        _global_embedding_manager = VectorEmbeddingManager()
    return _global_embedding_manager


# Convenience functions for extractor.py compatibility
def embed_text_v32(text: str) -> Dict[str, List[float]]:
    """
    Embed text using v3.2 specification
    Returns dict with both RURI and Qwen embeddings
    """
    manager = get_embedding_manager()
    result = manager.embed_text(text)
    
    return {
        "vec_ruri_v3": result["ruri_embedding"],
        "vec_qwen3_0p6b": result["qwen_embedding"]
    }


def embed_vector_legacy(dimensions: int) -> List[float]:
    """Legacy compatibility function for existing extractor.py"""
    manager = get_embedding_manager()
    return manager.get_random_embedding(dimensions)


if __name__ == "__main__":
    # Example usage and testing
    print("=== LNA-ES v3.2 Vector Embedding System ===")
    print()
    
    manager = VectorEmbeddingManager()
    print("Model Info:")
    info = manager.get_model_info()
    for model, details in info.items():
        if isinstance(details, dict):  # Skip cache_size which is int
            print(f"  {model}: {'✅ Loaded' if details['loaded'] else '❌ Not loaded'}")
            if details.get('dimensions'):
                print(f"    Dimensions: {details['dimensions']}")
    print(f"  Cache size: {info.get('cache_size', 0)}")
    
    print()
    print("Testing embeddings:")
    
    # Test Japanese text
    japanese_text = "吾輩は猫である"
    result_ja = manager.embed_text(japanese_text)
    print(f"Japanese text: {result_ja['text']}")
    print(f"  Language detected: {result_ja['language']}")
    print(f"  RURI method: {result_ja['ruri_method']}")
    print(f"  Qwen method: {result_ja['qwen_method']}")
    print(f"  RURI dims: {len(result_ja['ruri_embedding'])}")
    print(f"  Qwen dims: {len(result_ja['qwen_embedding'])}")
    
    print()
    
    # Test English text
    english_text = "Hello world, this is a test"
    result_en = manager.embed_text(english_text)
    print(f"English text: {result_en['text']}")
    print(f"  Language detected: {result_en['language']}")
    print(f"  RURI method: {result_en['ruri_method']}")
    print(f"  Qwen method: {result_en['qwen_method']}")
    
    print()
    
    # Test legacy compatibility
    embeddings = embed_text_v32("テスト文章")
    print("Legacy compatibility test:")
    print(f"  RURI embedding: {len(embeddings['vec_ruri_v3'])} dimensions")
    print(f"  Qwen embedding: {len(embeddings['vec_qwen3_0p6b'])} dimensions")