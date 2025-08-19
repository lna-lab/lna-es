"""
Enhanced ID Generator for LNA-ES v3.2
階層構造と時系列を明確にするID生成システム

ID Format:
- Work: base12_YYYYMMDD_millisec(13digits)
- Sentence: base12_YYYYMMDD_millisec_S001
- Entity: base12_YYYYMMDD_millisec_S001_a001
- Tag: base12_YYYYMMDD_millisec_S001_b001
"""

import time
import random
import string
from datetime import datetime
from typing import Dict, List, Optional


class EnhancedIDGenerator:
    """
    改良版ID生成システム
    - 12桁英数字ベースID
    - 日付（YYYYMMDD）
    - ミリ秒タイムスタンプ（13桁のUNIXタイムスタンプ）
    - 階層的な子ID（S001, a001, b001）
    """
    
    def __init__(self):
        self.work_counter = {}  # Work IDごとのカウンター管理
        self.base_id_cache = None
        self.date_cache = None
        
    def generate_base_id(self) -> str:
        """12桁の英数字ベースIDを生成"""
        # 小文字英字と数字を組み合わせて読みやすいIDを生成
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choices(chars, k=12))
    
    def get_current_date(self) -> str:
        """現在日付をYYYYMMDD形式で取得"""
        return datetime.now().strftime('%Y%m%d')
    
    def get_milliseconds(self) -> str:
        """現在のミリ秒タイムスタンプを取得（13桁のUNIXタイムスタンプ）"""
        # time.time()をミリ秒単位で取得（13桁）
        ms = int(time.time() * 1000)
        return str(ms)
    
    def generate_work_id(self, title: str = None, filename: str = None) -> str:
        """
        Work（主ノード）のID生成
        Format: base12_YYYYMMDD_millisec
        Example: 3ji4ghidtfa5_20250119_1737261986236
        """
        base = self.generate_base_id()
        date = self.get_current_date()
        ms = self.get_milliseconds()
        
        work_id = f"{base}_{date}_{ms}"
        
        # このWork IDのカウンターを初期化
        self.work_counter[work_id] = {
            'sentence': 0,
            'entities': {},
            'tags': {}
        }
        
        return work_id
    
    def generate_sentence_id(self, work_id: str, sentence_index: Optional[int] = None) -> str:
        """
        Sentence（子ノード）のID生成
        各センテンスごとに新しいミリ秒タイムスタンプを生成
        Format: base12_YYYYMMDD_millisec_S001
        Example: 3ji4ghidtfa5_20250119_1737261986237_S001
        """
        # Work IDからベースIDと日付を抽出
        parts = work_id.split('_')
        base_id = parts[0]
        date = parts[1]
        
        # 新しいミリ秒タイムスタンプを生成（各センテンスごとにユニーク）
        ms = self.get_milliseconds()
        
        if work_id not in self.work_counter:
            self.work_counter[work_id] = {
                'sentence': 0,
                'entities': {},
                'tags': {}
            }
        
        if sentence_index is None:
            self.work_counter[work_id]['sentence'] += 1
            sentence_index = self.work_counter[work_id]['sentence']
        
        sentence_id = f"{base_id}_{date}_{ms}_S{sentence_index:03d}"
        
        # この文のエンティティ・タグカウンターを初期化
        self.work_counter[work_id]['entities'][sentence_id] = 0
        self.work_counter[work_id]['tags'][sentence_id] = 0
        
        return sentence_id
    
    def generate_entity_id(self, sentence_id: str, entity_type: str = None, 
                          entity_index: Optional[int] = None) -> str:
        """
        Entity（孫ノード）のID生成
        各エンティティごとに新しいミリ秒タイムスタンプを生成
        Format: base12_YYYYMMDD_millisec_S001_a001
        Example: 3ji4ghidtfa5_20250119_1737261986238_S049_a003
        """
        # Sentence IDからベースIDと日付、文番号を抽出
        parts = sentence_id.split('_')
        base_id = parts[0]
        date = parts[1]
        sentence_num = parts[3] if len(parts) > 3 else "S000"
        
        # 新しいミリ秒タイムスタンプを生成（各エンティティごとにユニーク）
        ms = self.get_milliseconds()
        
        # Work IDを構築（カウンター管理用）
        work_id = f"{base_id}_{date}_{parts[2]}"
        
        if work_id not in self.work_counter:
            self.work_counter[work_id] = {
                'sentence': 0,
                'entities': {},
                'tags': {}
            }
        
        if sentence_id not in self.work_counter[work_id]['entities']:
            self.work_counter[work_id]['entities'][sentence_id] = 0
        
        if entity_index is None:
            self.work_counter[work_id]['entities'][sentence_id] += 1
            entity_index = self.work_counter[work_id]['entities'][sentence_id]
        
        return f"{base_id}_{date}_{ms}_{sentence_num}_a{entity_index:03d}"
    
    def generate_tag_id(self, sentence_id: str, tag_type: str = None,
                       tag_index: Optional[int] = None) -> str:
        """
        Tag（エッジ属性）のID生成
        各タグごとに新しいミリ秒タイムスタンプを生成
        Format: base12_YYYYMMDD_millisec_S001_b001
        Example: 3ji4ghidtfa5_20250119_1737261986239_S001_b001
        """
        # Sentence IDからベースIDと日付、文番号を抽出
        parts = sentence_id.split('_')
        base_id = parts[0]
        date = parts[1]
        sentence_num = parts[3] if len(parts) > 3 else "S000"
        
        # 新しいミリ秒タイムスタンプを生成（各タグごとにユニーク）
        ms = self.get_milliseconds()
        
        # Work IDを構築（カウンター管理用）
        work_id = f"{base_id}_{date}_{parts[2]}"
        
        if work_id not in self.work_counter:
            self.work_counter[work_id] = {
                'sentence': 0,
                'entities': {},
                'tags': {}
            }
        
        if sentence_id not in self.work_counter[work_id]['tags']:
            self.work_counter[work_id]['tags'][sentence_id] = 0
        
        if tag_index is None:
            self.work_counter[work_id]['tags'][sentence_id] += 1
            tag_index = self.work_counter[work_id]['tags'][sentence_id]
        
        return f"{base_id}_{date}_{ms}_{sentence_num}_b{tag_index:03d}"
    
    def parse_id(self, id_string: str) -> Dict[str, str]:
        """
        IDを解析して構成要素を返す
        """
        parts = id_string.split('_')
        
        result = {
            'base_id': parts[0] if len(parts) > 0 else None,
            'date': parts[1] if len(parts) > 1 else None,
            'millisec': parts[2] if len(parts) > 2 else None,
            'sentence': None,
            'entity': None,
            'tag': None,
            'type': 'unknown'
        }
        
        if len(parts) >= 3:
            result['type'] = 'work'
            
        if len(parts) >= 4 and parts[3].startswith('S'):
            result['sentence'] = parts[3]
            result['type'] = 'sentence'
            
        if len(parts) >= 5:
            if parts[4].startswith('a'):
                result['entity'] = parts[4]
                result['type'] = 'entity'
            elif parts[4].startswith('b'):
                result['tag'] = parts[4]
                result['type'] = 'tag'
        
        return result
    
    def get_hierarchy_level(self, id_string: str) -> int:
        """
        IDの階層レベルを返す
        Work: 0, Sentence: 1, Entity/Tag: 2
        """
        parsed = self.parse_id(id_string)
        
        if parsed['type'] == 'work':
            return 0
        elif parsed['type'] == 'sentence':
            return 1
        elif parsed['type'] in ['entity', 'tag']:
            return 2
        else:
            return -1
    
    def get_sentence_order(self, id_string: str) -> int:
        """
        文の順序番号を返す（復元時の順序決定用）
        """
        parsed = self.parse_id(id_string)
        
        if parsed['sentence']:
            # S001 -> 1, S002 -> 2, etc.
            return int(parsed['sentence'][1:])
        
        return -1
    
    def is_related(self, id1: str, id2: str) -> bool:
        """
        2つのIDが同じWork配下にあるかチェック
        """
        parsed1 = self.parse_id(id1)
        parsed2 = self.parse_id(id2)
        
        # ベースID、日付、ミリ秒が同じなら関連している
        return (parsed1['base_id'] == parsed2['base_id'] and 
                parsed1['date'] == parsed2['date'] and 
                parsed1['millisec'] == parsed2['millisec'])


# テスト用コード
if __name__ == "__main__":
    generator = EnhancedIDGenerator()
    
    # Work ID生成
    work_id = generator.generate_work_id("方丈記", "hojoki.txt")
    print(f"Work ID: {work_id}")
    
    # Sentence ID生成
    sentence_ids = []
    for i in range(3):
        sid = generator.generate_sentence_id(work_id)
        sentence_ids.append(sid)
        print(f"Sentence {i+1}: {sid}")
    
    # Entity ID生成
    for sid in sentence_ids[:2]:
        for j in range(2):
            eid = generator.generate_entity_id(sid, "person")
            print(f"  Entity: {eid}")
    
    # Tag ID生成
    for sid in sentence_ids[:1]:
        for j in range(2):
            tid = generator.generate_tag_id(sid, "emotion")
            print(f"  Tag: {tid}")
    
    # ID解析テスト
    print("\n=== ID解析テスト ===")
    test_id = sentence_ids[0] + "_a001"
    parsed = generator.parse_id(test_id)
    print(f"ID: {test_id}")
    print(f"Parsed: {parsed}")
    print(f"Hierarchy Level: {generator.get_hierarchy_level(test_id)}")
    print(f"Sentence Order: {generator.get_sentence_order(test_id)}")