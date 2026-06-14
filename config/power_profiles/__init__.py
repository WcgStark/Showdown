"""
Power profiles — the spoiler-safe knowledge base that drives the post-draft
battle analysis.

Design in three layers (see jujutsu.py for a worked example):

  1. ARCS          ordered list of reveal tiers for the universe (earliest →
                   latest). A fact's `reveal` is one of these strings.
  2. REVEAL_MAX    maps each filter_key (the chosen mode) to the latest arc that
                   is allowed to be referenced. The engine drops any ability
                   whose `reveal` comes after this — that's the hard spoiler gate.
  3. PROFILES      per-character data: position affinities, coarse stats, and a
                   list of abilities. Each ability carries:
                     reveal     — which arc it was shown in (gates visibility)
                     disclosure — how much may be SAID about it once visible:
                                    "full"  → describe the effect (text shown)
                                    "named" → name it, no effect
                                    "exists"→ only acknowledge it exists
                     tags       — drive the scoring engine (heal, tank, domain,
                                  domain_counter, buff, …); usable even at
                                  disclosure="exists" (we know Yuta can nullify a
                                  domain without knowing what his domain does).
                     text       — already written at the safe disclosure level.

To add a universe: write a module like jujutsu.py exposing a UniversePower and
register it in POWER_DATA below. Universes absent from POWER_DATA simply have no
analysis (the UI falls back to "debate your picks"), so this never breaks them.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class UniversePower:
    arcs: list[str]                  # ordered reveal tiers, earliest first
    reveal_max: dict[str, str]       # filter_key -> latest allowed arc
    profiles: dict[str, dict]        # character name -> profile dict
    default_reveal: str = ""         # fallback arc if a filter_key is unmapped

    def arc_index(self, arc: str) -> int:
        try:
            return self.arcs.index(arc)
        except ValueError:
            return len(self.arcs)  # unknown arc → treated as latest (hidden)

    def reveal_cut(self, filter_key: str) -> int:
        arc = self.reveal_max.get(filter_key, self.default_reveal or self.arcs[-1])
        return self.arc_index(arc)


# ──────────────────────────────────────────────────────────────────────────────
# Position role expectations — shared across universes that use POSITIONS_STANDARD.
# A slot "wants" certain ability tags; a character bringing them is far more
# influential in that slot (the "healer who actually heals" rule).
# ──────────────────────────────────────────────────────────────────────────────

POSITION_ROLE: dict[str, set[str]] = {
    "Captain":      {"leadership", "domain", "bruiser", "ace"},
    "Vice Captain": {"leadership", "versatility", "bruiser"},
    "Tank":         {"tank", "durability", "lockdown", "guard"},
    "Duelist":      {"bruiser", "burst", "aoe", "ace"},
    "Healer":       {"heal", "sustain", "revive"},
    "Support":      {"buff", "debuff", "utility", "versatility", "recon"},
    "Traitor":      {"sabotage", "betrayal", "manipulation"},
}


# ──────────────────────────────────────────────────────────────────────────────
# Registry — single source of truth, mirrors ALL_UNIVERSES keys.
# ──────────────────────────────────────────────────────────────────────────────

from config.power_profiles.jujutsu import JUJUTSU_POWER

POWER_DATA: dict[str, UniversePower] = {
    "jujutsu": JUJUTSU_POWER,
}
