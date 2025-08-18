#!/usr/bin/env python3
"""
id_generator.py
---------------

LNA-ES v3.2 ID Generation System
Implements BASE12 + millisecond timestamp + subID specification

Based on material_systems/10.Ultra/lna_es_v2_ultrathink_engine_super_real.py
Adapted to v3.2 requirements: A1b2C3d4E5f6_1723862400123_ent001
"""

import time
import random
import string
import hashlib
from typing import Optional
from dataclasses import dataclass


@dataclass
class ULIDConfig:
    """Configuration for UL-ID generation"""
    base_length: int = 12
    use_semantic_hash: bool = True
    counter_digits: int = 4


class LNAESv32IDGenerator:
    """
    LNA-ES v3.2 ID Generator
    
    Generates UL-IDs in format: BASE12_TIMESTAMP_SUBID
    Example: A1b2C3d4E5f6_1723862400123_ent001
    """
    
    def __init__(self, config: Optional[ULIDConfig] = None):
        self.config = config or ULIDConfig()
        self.counter = 0
        
    def generate_base_id(self, context: str = "") -> str:
        """
        Generate BASE12 identifier
        
        Args:
            context: Optional context for semantic generation
            
        Returns:
            12-character alphanumeric base ID
        """
        if context and self.config.use_semantic_hash:
            # Semantic BASE12 from context hash
            base_hash = hashlib.md5(context.encode()).hexdigest()[:12]
            # Ensure proper case mixing for BASE12
            return self._to_base12_format(base_hash)
        else:
            # Random BASE12
            chars = string.ascii_letters + string.digits
            return ''.join(random.choices(chars, k=self.config.base_length))
    
    def _to_base12_format(self, hex_string: str) -> str:
        """Convert hex string to BASE12 format with proper case mixing"""
        result = ""
        for i, char in enumerate(hex_string):
            if char.isdigit():
                result += char
            else:
                # Alternate between upper and lower case for letters
                if i % 2 == 0:
                    result += char.upper()
                else:
                    result += char.lower()
        return result
    
    def generate_timestamp_ms(self) -> int:
        """Generate millisecond timestamp"""
        return int(time.time() * 1000)
    
    def generate_sub_id(self, prefix: str, index: Optional[int] = None) -> str:
        """
        Generate sub-ID for entities, tags, etc.
        
        Args:
            prefix: Type prefix (e.g., 'ent', 'tag', 'seg')
            index: Optional specific index
            
        Returns:
            Sub-ID in format: prefix + 3-digit number
        """
        if index is not None:
            return f"{prefix}{index:03d}"
        else:
            self.counter += 1
            return f"{prefix}{self.counter:03d}"
    
    def generate_ul_id(self, context: str = "", sub_prefix: str = "ent", 
                       sub_index: Optional[int] = None) -> str:
        """
        Generate complete UL-ID
        
        Args:
            context: Context for semantic base ID generation
            sub_prefix: Prefix for sub-ID
            sub_index: Optional specific sub-index
            
        Returns:
            Complete UL-ID: BASE12_TIMESTAMP_SUBID
        """
        base_id = self.generate_base_id(context)
        timestamp = self.generate_timestamp_ms()
        sub_id = self.generate_sub_id(sub_prefix, sub_index)
        
        return f"{base_id}_{timestamp}_{sub_id}"
    
    def generate_work_id(self, title: str = "", file_path: str = "") -> str:
        """Generate work-level ID"""
        context = f"work_{title}_{file_path}"
        return self.generate_ul_id(context, "wrk", 0)
    
    def generate_segment_id(self, work_context: str, segment_index: int) -> str:
        """Generate segment ID"""
        context = f"segment_{work_context}_{segment_index}"
        return self.generate_ul_id(context, "seg", segment_index)
    
    def generate_sentence_id(self, segment_context: str, sentence_index: int) -> str:
        """Generate sentence ID"""
        context = f"sentence_{segment_context}_{sentence_index}"
        return self.generate_ul_id(context, "sen", sentence_index)
    
    def generate_entity_id(self, sentence_context: str, entity_type: str, 
                          entity_index: int) -> str:
        """Generate entity ID"""
        context = f"entity_{sentence_context}_{entity_type}_{entity_index}"
        prefix = entity_type[:3].lower()
        return self.generate_ul_id(context, prefix, entity_index)
    
    def generate_tag_id(self, context: str, tag_type: str, tag_index: int) -> str:
        """Generate tag ID"""
        tag_context = f"tag_{context}_{tag_type}_{tag_index}"
        prefix = f"t{tag_type[:2].lower()}"
        return self.generate_ul_id(tag_context, prefix, tag_index)


class LegacyIDAdapter:
    """
    Adapter for existing ID systems in material_systems
    Provides compatibility with 10.Ultra ID generation
    """
    
    def __init__(self):
        self.v32_generator = LNAESv32IDGenerator()
        self.ultra_counter = 0
    
    def adapt_ultra_id(self, ultra_id: str) -> str:
        """
        Convert 10.Ultra ID format to v3.2 format
        
        Args:
            ultra_id: ID from 10.Ultra system
            
        Returns:
            v3.2 compatible UL-ID
        """
        # Parse ultra format and convert
        parts = ultra_id.split('_')
        if len(parts) >= 2:
            base_part = parts[0][:12]
            timestamp = int(time.time() * 1000)
            sub_id = f"adp{self.ultra_counter:03d}"
            self.ultra_counter += 1
            return f"{base_part}_{timestamp}_{sub_id}"
        else:
            # Fallback to new generation
            return self.v32_generator.generate_ul_id("legacy_ultra", "leg")


# Convenience functions for direct usage
def generate_work_id(title: str = "", file_path: str = "") -> str:
    """Generate work ID - convenience function"""
    generator = LNAESv32IDGenerator()
    return generator.generate_work_id(title, file_path)


def generate_entity_id(context: str, entity_type: str, index: int = 0) -> str:
    """Generate entity ID - convenience function"""
    generator = LNAESv32IDGenerator()
    return generator.generate_entity_id(context, entity_type, index)


# Global instance for consistent counter management
_global_generator = LNAESv32IDGenerator()


def get_global_generator() -> LNAESv32IDGenerator:
    """Get global ID generator instance"""
    return _global_generator


if __name__ == "__main__":
    # Example usage and testing
    generator = LNAESv32IDGenerator()
    
    print("=== LNA-ES v3.2 ID Generator Examples ===")
    print()
    
    # Work ID
    work_id = generator.generate_work_id("吾輩は猫である", "wagahai_cat.txt")
    print(f"Work ID: {work_id}")
    
    # Segment ID
    segment_id = generator.generate_segment_id("wagahai_cat", 0)
    print(f"Segment ID: {segment_id}")
    
    # Sentence ID
    sentence_id = generator.generate_sentence_id("wagahai_cat_seg0", 0)
    print(f"Sentence ID: {sentence_id}")
    
    # Entity IDs
    entity_id1 = generator.generate_entity_id("wagahai_sentence", "person", 0)
    entity_id2 = generator.generate_entity_id("wagahai_sentence", "location", 0)
    print(f"Person Entity ID: {entity_id1}")
    print(f"Location Entity ID: {entity_id2}")
    
    # Tag ID
    tag_id = generator.generate_tag_id("wagahai_context", "emotion", 0)
    print(f"Tag ID: {tag_id}")
    
    print()
    print("=== Format Verification ===")
    sample_id = generator.generate_ul_id("test_context", "ent", 1)
    parts = sample_id.split('_')
    print(f"Sample ID: {sample_id}")
    print(f"Parts: BASE12='{parts[0]}' ({len(parts[0])} chars), TIMESTAMP='{parts[1]}', SUBID='{parts[2]}'")
    print(f"Matches v3.2 spec: {len(parts) == 3 and len(parts[0]) == 12 and parts[1].isdigit() and len(parts[2]) >= 4}")