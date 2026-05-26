from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from config.universes import Universe
from domain.entities.player import Player


@dataclass
class Match:
    universe: Universe
    filter_key: str
    pool: list[str] = field(default_factory=list)
    players: list[Player] = field(default_factory=list)
    turn: int = 0
    current_char: Optional[str] = None

    @property
    def current_player(self) -> Player:
        return self.players[self.turn]

    @property
    def positions(self) -> list[str]:
        return self.universe.positions

    def next_turn(self) -> None:
        self.turn = 1 - self.turn
