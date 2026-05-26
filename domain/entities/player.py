from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Player:
    name: str
    slots: dict[str, Optional[str]] = field(default_factory=dict)
    skips_left: int = 1

    def init_slots(self, positions: list[str]) -> None:
        self.slots = {p: None for p in positions}

    def all_filled(self) -> bool:
        return all(v is not None for v in self.slots.values())
