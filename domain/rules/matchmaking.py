from __future__ import annotations

import random

from config.universes import Universe


def build_pool(universe: Universe, filter_key: str) -> list[str]:
    """Return a shuffled character pool with the filter's exclusions removed."""
    excluded = universe.filters[filter_key].exclude
    pool = [c for c in universe.characters if c not in excluded]
    random.shuffle(pool)
    return pool
