from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import urllib.request

APP_VERSION = "1.0.3"
# ─── Configure your GitHub repo here ─────────────────────────────────────────
GITHUB_OWNER = "WcgStark"   # ← substituir pelo seu usuário do GitHub
GITHUB_REPO  = "Showdown"      # ← substituir pelo nome do repositório
# ─────────────────────────────────────────────────────────────────────────────

_API_URL = f"https://api.github.com/repos/WcgStark/Showdown/releases/latest"

_state: dict = {"status": "idle", "value": 0, "tmp_path": ""}
_lock = threading.Lock()


def _set(status: str, value: int = 0, tmp_path: str = "") -> None:
    with _lock:
        _state["status"]   = status
        _state["value"]    = value
        if tmp_path:
            _state["tmp_path"] = tmp_path


def get_progress() -> dict:
    with _lock:
        return dict(_state)


def _version_tuple(v: str) -> tuple:
    try:
        return tuple(int(x) for x in v.lstrip("v").split("."))
    except Exception:
        return (0,)


def check_for_update() -> dict | None:
    """Returns update info dict or None (no update / no internet / error)."""
    try:
        req = urllib.request.Request(
            _API_URL,
            headers={
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "ShowdownDraftApp",
            },
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())

        latest = data["tag_name"].lstrip("v")
        if _version_tuple(latest) <= _version_tuple(APP_VERSION):
            return None

        exe_url = next(
            (a["browser_download_url"] for a in data.get("assets", []) if a["name"].endswith(".exe")),
            None,
        )
        if not exe_url:
            return None

        return {
            "latestVersion": latest,
            "currentVersion": APP_VERSION,
            "downloadUrl": exe_url,
            "notes": data.get("body", ""),
        }
    except Exception:
        return None


def _download_thread(url: str) -> None:
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as tmp:
            tmp_path = tmp.name

        def reporthook(block: int, block_size: int, total: int) -> None:
            if total > 0:
                _set("downloading", min(99, block * block_size * 100 // total), tmp_path)

        _set("downloading", 0, tmp_path)
        urllib.request.urlretrieve(url, tmp_path, reporthook=reporthook)
        _set("done", 100, tmp_path)

    except Exception:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
        _set("error", 0)


def start_download(url: str) -> None:
    _set("downloading", 0)
    threading.Thread(target=_download_thread, args=(url,), daemon=True).start()


def apply_update() -> bool:
    """Creates a helper .bat that replaces the exe after the app closes, then launches it."""
    if not getattr(sys, "frozen", False):
        return False

    with _lock:
        tmp_path = _state.get("tmp_path", "")

    if not tmp_path or not os.path.exists(tmp_path):
        return False

    current_exe = sys.executable
    bat = (
        "@echo off\n"
        "ping 127.0.0.1 -n 3 > nul\n"
        f'copy /Y "{tmp_path}" "{current_exe}"\n'
        f'if errorlevel 1 ( ping 127.0.0.1 -n 2 > nul & copy /Y "{tmp_path}" "{current_exe}" )\n'
        f'del "{tmp_path}"\n'
        f'start "" "{current_exe}"\n'
        "del \"%~f0\"\n"
    )
    bat_path = os.path.join(tempfile.gettempdir(), "showdown_update.bat")
    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(bat)

    subprocess.Popen(
        ["cmd", "/c", bat_path],
        creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS,
    )
    return True
