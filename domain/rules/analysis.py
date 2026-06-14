"""
Battle-analysis engine.

Given a finished draft (two players' position→character maps), the chosen mode
(filter_key) and the universe, produce a spoiler-safe, position-by-position
tally of both teams: each slot's score, the winner, and intra-team synergy.

Every fact surfaced here passes through `_visible_abilities`, which drops
anything revealed after the mode's boundary — that's the single spoiler gate.

TRAITOR RULE: the character a player drops into the "Traitor" slot is a wildcard
that fights for the ENEMY. They are scored at their BEST-FIT position (their
highest non-Traitor affinity) and their points are credited to the opponent.
"""

from __future__ import annotations

from config.power_profiles import POWER_DATA, POSITION_ROLE, UniversePower


# Neutral baseline (0–100 scale) for characters with no authored profile yet.
_DEFAULT_STATS = {"power": 50, "durability": 50, "speed": 50, "utility": 50}
_DEFAULT_POS_FIT = 0.45

TRAITOR = "Traitor"


def _visible_abilities(profile: dict, cut: int, power: UniversePower) -> list[dict]:
    """Abilities revealed at or before the mode boundary. `text` is already
    written at a safe disclosure level, so visible == safe to show."""
    return [ab for ab in profile.get("abilities", [])
            if power.arc_index(ab.get("reveal", "")) <= cut]


def _ability_tags(abilities: list[dict]) -> set[str]:
    tags: set[str] = set()
    for ab in abilities:
        tags.update(ab.get("tags", ()))
    return tags


def _stat_mean(stats: dict) -> float:
    vals = list(stats.values()) or [50]
    return sum(vals) / len(vals)


def _best_position(profile: dict) -> str | None:
    """Highest-affinity position, ignoring the Traitor slot itself."""
    pos = {p: v for p, v in (profile.get("positions") or {}).items() if p != TRAITOR}
    return max(pos, key=pos.get) if pos else None


def _score_char(char: str, position: str, power: UniversePower, cut: int) -> dict:
    """Score one character played at one position.

    placement = base · (0.5 + 0.5·fit) · (1 + 0.25·roleMatches)
    where roleMatches = how many of the character's visible tags the slot wants.
    """
    profile = power.profiles.get(char)
    has_profile = profile is not None
    prof = profile or {}
    abilities = _visible_abilities(prof, cut, power) if has_profile else []

    base = _stat_mean(prof.get("stats", _DEFAULT_STATS))
    fit = prof.get("positions", {}).get(position, _DEFAULT_POS_FIT)
    wanted = POSITION_ROLE.get(position, set())
    tags = _ability_tags(abilities)
    # The domain tag is still SHOWN in the Healer slot, but it grants no points:
    # it isn't in the Healer's wanted set (no role-match points) and the +28
    # domain advantage already excludes the Healer slot (see the tally below).
    matches = tags & wanted
    score = base * (0.5 + 0.5 * fit) * (1 + 0.25 * len(matches))

    return {
        "char": char,
        "score": round(score, 1),
        "tags": sorted(tags),
        "abilities": [ab["text"] for ab in abilities],
        "hasProfile": has_profile,
    }


def _synergy_bonus(tags: set[str]) -> tuple[float, list[str]]:
    """Intra-team combos, scored on the team that actually ends up fighting
    together (own slots + any enemy traitor that defected in)."""
    bonus = 0.0
    lines: list[str] = []
    if {"heal", "sustain"} & tags and {"tank", "guard"} & tags:
        bonus += 30
        lines.append("Cura protegida por uma linha de frente — sustentação sólida.")
    if {"buff", "debuff"} & tags and {"bruiser", "burst", "ace"} & tags:
        bonus += 20
        lines.append("Suporte amplifica os atacantes principais.")
    return bonus, lines


def _interactions(p1_tags: set[str], p2_tags: set[str]) -> list[str]:
    """Cross-team callouts (spoiler-safe — driven only by visible tags)."""
    out: list[str] = []
    if "domain_counter" in p1_tags and "domain" in p2_tags:
        out.append("P1 tem como anular a expansão de domínio adversária.")
    if "domain_counter" in p2_tags and "domain" in p1_tags:
        out.append("P2 tem como anular a expansão de domínio adversária.")
    return out


def analyze_match(universe_key: str, filter_key: str,
                  p1_slots: dict, p2_slots: dict) -> dict:
    power = POWER_DATA.get(universe_key)
    if power is None:
        return {"available": False}

    cut = power.reveal_cut(filter_key)
    positions = list(p1_slots.keys())

    # One row per position; the Traitor slot's occupant is a defector.
    rows: list[dict] = []
    for pos in positions:
        entry: dict = {"position": pos}
        for side, slots in (("p1", p1_slots), ("p2", p2_slots)):
            char = slots.get(pos)
            if not char:
                entry[side] = None
                continue
            defects = (pos == TRAITOR)
            role = pos
            if defects:
                role = _best_position(power.profiles.get(char) or {}) or "Duelist"
            entry[side] = {"role": role, "defects": defects,
                           **_score_char(char, role, power, cut)}
        rows.append(entry)

    # Anti-domain presence per side (combat slots only). An anti-domain technique
    # (Simple Domain, Domain Amplification, …) neutralizes the enemy's domains.
    p1_anti = p2_anti = False
    for entry in rows:
        pos = entry["position"]
        for side in ("p1", "p2"):
            e = entry[side]
            if not e:
                continue
            to_p1 = (side == "p1") != e["defects"]
            if pos != "Healer" and "anti_domain" in e["tags"]:
                if to_p1: p1_anti = True
                else: p2_anti = True

    # Tally: defectors contribute to the OTHER side (and bring their tags there).
    # A domain only projects from a combat slot (a Healer is busy healing); and a
    # combat domain user facing an enemy anti-domain loses HALF its score.
    p1_total = p2_total = 0.0
    p1_tags: set[str] = set()
    p2_tags: set[str] = set()
    p1_dom_adv = p2_dom_adv = False
    for entry in rows:
        pos = entry["position"]
        for side in ("p1", "p2"):
            e = entry[side]
            if not e:
                continue
            to_p1 = (side == "p1") != e["defects"]   # xor: defector flips sides
            tags = set(e["tags"])
            is_domain_combat = pos != "Healer" and "domain" in tags
            if to_p1:
                p1_total += e["score"]; p1_tags |= tags
                if is_domain_combat: p1_dom_adv = True
            else:
                p2_total += e["score"]; p2_tags |= tags
                if is_domain_combat: p2_dom_adv = True

    b1, l1 = _synergy_bonus(p1_tags)
    b2, l2 = _synergy_bonus(p2_tags)

    # A domain is a decisive edge against a team with no domain in combat. An
    # enemy anti-domain doesn't cancel it — it HALVES it (the character's own
    # score is untouched), so the +28 edge becomes +14.
    DOMAIN_ADV = 28
    cut_by_p1 = cut_by_p2 = False   # did this side's anti-domain halve the edge?
    if p1_dom_adv and not p2_dom_adv:
        if p2_anti:
            b1 += DOMAIN_ADV // 2; cut_by_p2 = True
            l1.append(f"Vantagem de domínio +{DOMAIN_ADV // 2} (anti-domínio do oponente reduziu pela metade).")
        else:
            b1 += DOMAIN_ADV
            l1.append(f"Vantagem de domínio +{DOMAIN_ADV} — oponente sem expansão.")
    if p2_dom_adv and not p1_dom_adv:
        if p1_anti:
            b2 += DOMAIN_ADV // 2; cut_by_p1 = True
            l2.append(f"Vantagem de domínio +{DOMAIN_ADV // 2} (anti-domínio do oponente reduziu pela metade).")
        else:
            b2 += DOMAIN_ADV
            l2.append(f"Vantagem de domínio +{DOMAIN_ADV} — oponente sem expansão.")

    p1_total += b1
    p2_total += b2

    margin = p1_total - p2_total
    tie_band = 0.04 * max(p1_total, p2_total, 1)   # tie if within 4% of the leader
    verdict = "tie" if abs(margin) < tie_band else ("p1" if margin > 0 else "p2")

    interactions = _interactions(p1_tags, p2_tags)
    if cut_by_p1:
        interactions.append("P1 cortou pela metade a vantagem de domínio do oponente (anti-domínio).")
    if cut_by_p2:
        interactions.append("P2 cortou pela metade a vantagem de domínio do oponente (anti-domínio).")

    return {
        "available": True,
        "positions": positions,
        "rows": rows,
        "p1": {"total": round(p1_total, 1), "bonus": round(b1, 1), "synergy": l1},
        "p2": {"total": round(p2_total, 1), "bonus": round(b2, 1), "synergy": l2},
        "verdict": verdict,
        "margin": round(margin, 1),
        "interactions": interactions,
    }
