from __future__ import annotations

import pathlib
import random
import sys

from config.settings import QUICK_NAMES
from config.universes import ALL_UNIVERSES
from application.services.game_service import GameService
from application.managers.session_manager import SessionManager
import updater as _updater


def _get_base() -> pathlib.Path:
    if getattr(sys, "frozen", False):
        return pathlib.Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return pathlib.Path(__file__).parent.parent


_BASE_DIR = _get_base()
_DIST_DIR = _BASE_DIR / "dist"


class GameAPI:
    def __init__(self) -> None:
        self._service = GameService()
        self._session = SessionManager()
        self._history: list[dict] = []
        self._ext_map: dict[str, str] = {}

    # ── Config ────────────────────────────────────────────────────────────────

    def get_config(self) -> dict:
        universes = []
        for key, u in ALL_UNIVERSES.items():
            filters = [
                {"key": fk, "label": fs.label}
                for fk, fs in u.filters.items()
            ]
            universes.append({
                "id": key,
                "name": u.name,
                "tag": u.name.upper(),
                "positions": u.positions,
                "filters": filters,
                "defaultFilter": u.default_filter,
                "assetFolder": u.asset_folder,
            })
        return {"universes": universes, "quickNames": QUICK_NAMES, "version": _updater.APP_VERSION}

    # ── Match lifecycle ───────────────────────────────────────────────────────

    def start_match(
        self,
        universe_id: str,
        filter_key: str,
        p1_name: str,
        p2_name: str,
    ) -> dict:
        universe = ALL_UNIVERSES[universe_id]
        self._ext_map = {}
        # Assets live in dist/<folder_name>/ after Vite build
        folder_name = pathlib.Path(universe.asset_folder).name
        asset_dir = _DIST_DIR / folder_name
        if asset_dir.exists():
            for f in asset_dir.iterdir():
                if f.suffix.lower() == ".gif":
                    self._ext_map[f.stem] = "gif"
        match = self._service.create_match(
            universe,
            filter_key,
            [p1_name or "Player 1", p2_name or "Player 2"],
        )
        self._session.universe = universe
        self._session.start_match(match)
        self._history = []
        return self._game_state()

    def toggle_fullscreen(self) -> None:
        import webview
        for w in webview.windows:
            w.toggle_fullscreen()

    def reset(self) -> dict:
        self._session.clear()
        self._history = []
        return {"reset": True}

    # ── Game actions ──────────────────────────────────────────────────────────

    def gacha(self) -> dict:
        self._service.draw_character(self._session.match)
        return self._game_state()

    def assign(self, position: str) -> dict:
        m = self._session.match
        old_turn = m.turn
        if m.current_char and m.current_player.slots.get(position) is None:
            self._session.save_undo(m.current_char, position, old_turn)
            positions = self._session.universe.positions
            self._history.append({
                "posIdx": positions.index(position),
                "turn": "p1" if old_turn == 0 else "p2",
            })
            self._service.assign_character(m, position)
        return self._game_state()

    def skip(self) -> dict:
        self._service.skip_character(self._session.match)
        return self._game_state()

    def pass_turn(self) -> dict:
        m = self._session.match
        m.turn = 1 - m.turn
        return self._game_state()

    def switch_positions(self, pos_a: str, pos_b: str) -> dict:
        self._service.switch_positions(self._session.match, pos_a, pos_b)
        return self._game_state()

    def undo(self) -> dict:
        state = self._session.pop_undo()
        if state:
            m = self._session.match
            m.turn = state["turn"]
            m.current_player.slots[state["pos"]] = None
            m.pool.append(state["char"])
            m.current_char = state["char"]
            if self._history:
                self._history.pop()
        return self._game_state()

    # ── Update ────────────────────────────────────────────────────────────────

    def check_update(self) -> dict:
        info = _updater.check_for_update()
        if info is None:
            return {"hasUpdate": False, "currentVersion": _updater.APP_VERSION}
        return {"hasUpdate": True, **info}

    def start_download_update(self, url: str) -> None:
        _updater.start_download(url)

    def get_update_progress(self) -> dict:
        return _updater.get_progress()

    def apply_update(self) -> bool:
        success = _updater.apply_update()
        if success:
            import webview as _wv
            for w in _wv.windows:
                w.destroy()
        return success

    # ── Internal ──────────────────────────────────────────────────────────────

    def _char_obj(self, name: str) -> dict:
        return {"name": name, "ext": self._ext_map.get(name, "jpeg")}

    def _game_state(self) -> dict:
        m = self._session.match
        u = self._session.universe
        assignments = []
        for pos in u.positions:
            p1_char = m.players[0].slots.get(pos)
            p2_char = m.players[1].slots.get(pos)
            assignments.append({
                "p1": self._char_obj(p1_char) if p1_char else None,
                "p2": self._char_obj(p2_char) if p2_char else None,
            })
        pool_sample = random.sample(m.pool, min(40, len(m.pool))) if m.pool else []
        return {
            "turn": "p1" if m.turn == 0 else "p2",
            "currentChar": self._char_obj(m.current_char) if m.current_char else None,
            "assignments": assignments,
            "skipsP1": m.players[0].skips_left,
            "skipsP2": m.players[1].skips_left,
            "history": self._history,
            "undoAvailable": self._session.undo_state is not None,
            "poolSample": pool_sample,
        }
