from __future__ import annotations

import random
from typing import Optional

from config.universes import Universe
from domain.entities.match import Match
from domain.entities.player import Player
from domain.rules.matchmaking import build_pool


class GameService:
    def create_match(
        self,
        universe: Universe,
        filter_key: str,
        player_names: list[str],
    ) -> Match:
        pool = build_pool(universe, filter_key)
        players = [Player(name) for name in player_names]
        for p in players:
            p.init_slots(universe.positions)
        return Match(
            universe=universe,
            filter_key=filter_key,
            pool=pool,
            players=players,
        )

    def draw_character(self, match: Match) -> Optional[str]:
        """Pick a random character from the pool. Returns None if not drawable."""
        if match.current_char or match.current_player.all_filled():
            return None
        char = random.choice(match.pool)
        match.current_char = char
        return char

    def assign_character(self, match: Match, position: str) -> bool:
        """Place the current character into a slot and advance the turn."""
        player = match.current_player
        if not match.current_char or player.slots.get(position) is not None:
            return False
        player.slots[position] = match.current_char
        match.pool.remove(match.current_char)
        match.current_char = None
        match.next_turn()
        return True

    def skip_character(self, match: Match) -> bool:
        """Discard the current character and consume a skip."""
        p = match.current_player
        if not match.current_char or p.skips_left <= 0:
            return False
        match.pool.remove(match.current_char)
        match.current_char = None
        p.skips_left -= 1
        return True

    def switch_positions(self, match: Match, pos_a: str, pos_b: str) -> bool:
        """Swap two filled positions for the current player, consuming a skip."""
        player = match.current_player
        if player.skips_left <= 0:
            return False
        player.slots[pos_a], player.slots[pos_b] = (
            player.slots[pos_b],
            player.slots[pos_a],
        )
        player.skips_left -= 1
        return True
