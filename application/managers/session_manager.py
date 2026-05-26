from __future__ import annotations

from typing import Optional

from config.universes import Universe
from domain.entities.match import Match


class SessionManager:
    def __init__(self) -> None:
        self.universe: Optional[Universe] = None
        self.match: Optional[Match] = None
        self.undo_state: Optional[dict] = None

    def start_match(self, match: Match) -> None:
        self.match = match
        self.undo_state = None

    def clear(self) -> None:
        self.universe = None
        self.match = None
        self.undo_state = None

    def save_undo(self, char: str, pos: str, turn: int) -> None:
        self.undo_state = {"char": char, "pos": pos, "turn": turn}

    def pop_undo(self) -> Optional[dict]:
        state = self.undo_state
        self.undo_state = None
        return state
