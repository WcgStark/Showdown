"""Tests for the core draft logic in GameService."""
from __future__ import annotations

import random

import pytest

from application.services.game_service import GameService
from config.universes import ONEPIECE, BLEACH, JOJO

TESTE_POOL_OP = {"Monkey D. Luffy", "Edward Newgate"}

TESTE_POOL_BLEACH = {
    "Ichigo Kurosaki", "Sousuke Aizen", "Yhwach",
    "Genryūsai Shigekuni Yamamoto",
}

TESTE_POOL_JOJO = {
    "Giorno", "Yoshikage Kira", "Diavolo", "Pucci",
    "Joseph Joestar", "Jotaro Kujo", "Dio Brando",
}


@pytest.fixture
def service() -> GameService:
    return GameService()


@pytest.fixture
def match(service: GameService):
    random.seed(0)
    return service.create_match(ONEPIECE, "teste", ["P1", "P2"])


@pytest.fixture
def match_bleach(service: GameService):
    random.seed(0)
    return service.create_match(BLEACH, "teste", ["P1", "P2"])


@pytest.fixture
def match_jojo(service: GameService):
    random.seed(0)
    return service.create_match(JOJO, "teste", ["P1", "P2"])


# ── create_match ────────────────────────────────────────────────────────────

def test_create_match_applies_filter(match):
    assert set(match.pool) == TESTE_POOL_OP


def test_create_match_bleach_applies_filter(match_bleach):
    assert set(match_bleach.pool) == TESTE_POOL_BLEACH


def test_create_match_jojo_applies_filter(match_jojo):
    assert set(match_jojo.pool) == TESTE_POOL_JOJO


def test_create_match_initializes_players(match):
    assert [p.name for p in match.players] == ["P1", "P2"]
    for p in match.players:
        assert set(p.slots) == set(ONEPIECE.positions)
        assert all(v is None for v in p.slots.values())
        assert p.skips_left == 1
    assert match.turn == 0


# ── draw_character ──────────────────────────────────────────────────────────

def test_draw_character_sets_current(service, match):
    char = service.draw_character(match)
    assert char in TESTE_POOL_OP
    assert match.current_char == char


def test_draw_character_returns_none_when_already_drawn(service, match):
    service.draw_character(match)
    assert service.draw_character(match) is None


def test_draw_character_returns_none_when_player_full(service, match):
    for pos in ONEPIECE.positions:
        match.current_player.slots[pos] = "x"
    assert service.draw_character(match) is None


# ── assign_character ────────────────────────────────────────────────────────

def test_assign_places_char_and_advances_turn(service, match):
    char = service.draw_character(match)
    pos = ONEPIECE.positions[0]
    assert service.assign_character(match, pos) is True
    assert match.players[0].slots[pos] == char
    assert char not in match.pool
    assert match.current_char is None
    assert match.turn == 1


def test_assign_fails_without_current_char(service, match):
    assert service.assign_character(match, ONEPIECE.positions[0]) is False


def test_assign_fails_on_occupied_slot(service, match):
    service.draw_character(match)
    pos = ONEPIECE.positions[0]
    match.current_player.slots[pos] = "taken"
    assert service.assign_character(match, pos) is False


# ── skip_character ──────────────────────────────────────────────────────────

def test_skip_consumes_skip_and_discards(service, match):
    char = service.draw_character(match)
    assert service.skip_character(match) is True
    assert match.current_char is None
    assert char not in match.pool
    assert match.current_player.skips_left == 0


def test_skip_fails_without_skips_left(service, match):
    service.draw_character(match)
    match.current_player.skips_left = 0
    assert service.skip_character(match) is False


def test_skip_fails_without_current_char(service, match):
    assert service.skip_character(match) is False


# ── switch_positions ────────────────────────────────────────────────────────

def test_switch_swaps_and_consumes_skip(service, match):
    a, b = ONEPIECE.positions[0], ONEPIECE.positions[1]
    match.current_player.slots[a] = "A"
    match.current_player.slots[b] = "B"
    assert service.switch_positions(match, a, b) is True
    assert match.current_player.slots[a] == "B"
    assert match.current_player.slots[b] == "A"
    assert match.current_player.skips_left == 0


def test_switch_fails_without_skips_left(service, match):
    match.current_player.skips_left = 0
    a, b = ONEPIECE.positions[0], ONEPIECE.positions[1]
    assert service.switch_positions(match, a, b) is False
