#!/usr/bin/env python3
"""
Minimal PromptBuilder stub for restoration pipeline fallback.
"""
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class DialSettings:
    soul: float
    editor: float
    fidelity: float


@dataclass
class LockSettings:
    identity: bool = True
    toponym: bool = True
    relation: bool = True
    pov: bool = True


@dataclass
class EditorBrief:
    audience: str
    shelf: str
    length: Dict[str, Any]


@dataclass
class Invariant:
    kind: str
    data: Dict[str, Any]


class PromptBuilder:
    def build_complete_prompt(
        self,
        dials: DialSettings,
        locks: LockSettings,
        brief: EditorBrief,
        graph_data: Dict[str, Any],
        style: str,
        invariants: List[Invariant],
        instruction: str,
    ) -> Dict[str, str]:
        # Build a simple context from graph nodes and brief
        chars = [n.get('name') for n in graph_data.get('nodes', []) if n.get('type') == 'Character']
        places = [n.get('place') for n in graph_data.get('nodes', []) if n.get('type') == 'Setting']
        ctx_lines = []
        if chars:
            ctx_lines.append(f"登場人物: {', '.join(filter(None, chars))}")
        if places:
            ctx_lines.append(f"舞台: {', '.join(filter(None, places))}")
        ctx_lines.append(f"読者: {brief.audience} / 棚: {brief.shelf}")
        ctx_lines.append(f"長さ: 目安 {brief.length.get('total_chars')} 文字")
        excerpt = (graph_data.get('meta', {}) or {}).get('excerpt')
        if excerpt:
            ctx_lines.append("--- 抜粋 ---")
            ctx_lines.append(excerpt)
        return {
            "system": f"You are a helpful literary editor. Style={style}",
            "instruction": instruction,
            "context": "\n".join(ctx_lines),
        }
