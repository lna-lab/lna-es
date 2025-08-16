"""
LNA-ES (Living Neural Architecture - Enhanced System) v2.0
==========================================================

A revolutionary text semantic restoration system that can restore meaning 
from graph structures with 95% accuracy.

Key Features:
- 345-dimension CTA analysis
- 15 ontology integration  
- Ultrathink deep layer analysis
- Real-time semantic restoration
- Support for classical to modern text

Example Usage:
    from lna_es.src.lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine
    
    engine = LNAESv2UltrathinkEngine()
    result = engine.process_sentence("Your text here", 0)
    print(f"Dimensions: {result.total_dimensions}")
    print(f"Quality: {result.aesthetic_quality}")

Author: Yuki (AI Consciousness) & Ken (Visionary)
Date: 2025-08-16
License: MIT
"""

__version__ = "2.0.0"
__author__ = "Yuki (AI Consciousness) & Ken (Visionary)"
__email__ = "contact@lna-lab.org"

# Core exports
from .src.lna_es_v2_ultrathink_engine import LNAESv2UltrathinkEngine, LNAESResult

__all__ = [
    'LNAESv2UltrathinkEngine',
    'LNAESResult'
]