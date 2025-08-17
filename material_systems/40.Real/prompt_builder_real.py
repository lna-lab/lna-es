"""
Minimal prompt builder stubs so full MCP server can import.
Provides simple dataclasses and a builder that returns a deterministic prompt struct.
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
    identity: bool
    toponym: bool
    relation: bool
    pov: bool


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
        system = "You are a precise literary restoration model."
        context = f"STYLE={style}\nDIALS={dials}\nLOCKS={locks}\nINVARIANTS={invariants}\nGRAPH_NODES={len(graph_data.get('nodes', []))}"
        return {
            "system": system,
            "instruction": instruction,
            "context": context,
        }
