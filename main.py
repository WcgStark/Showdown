from __future__ import annotations

import os
import pathlib
import shutil
import sys

import webview

from api.bridge import GameAPI


def _get_base() -> pathlib.Path:
    if getattr(sys, "frozen", False):
        return pathlib.Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return pathlib.Path(__file__).parent


def _clear_webview_cache(storage_path: str) -> None:
    # The bundled frontend is loaded from a fixed file:// path, so WebView2's
    # HTTP/code cache survives app updates and keeps serving the OLD UI — this
    # caused the "Dragon Ball without banner / wrong lobby grid" bug after
    # updating, even though the new build was correct. Drop those caches on
    # every launch; the frontend is local so re-reading it is instant. User
    # settings live in "Local Storage" and are deliberately left untouched.
    default = pathlib.Path(storage_path) / "EBWebView" / "Default"
    for sub in ("Cache", "Code Cache", "GPUCache", "DawnCache", "DawnGraphiteCache"):
        shutil.rmtree(default / sub, ignore_errors=True)


def _user_storage() -> str:
    # Persists localStorage (volumes, keybinds, language, …) outside the
    # install dir so updates that overwrite dist/ don't wipe user settings.
    if sys.platform == "win32":
        root = pathlib.Path(os.environ.get("LOCALAPPDATA", pathlib.Path.home()))
    elif sys.platform == "darwin":
        root = pathlib.Path.home() / "Library" / "Application Support"
    else:
        root = pathlib.Path(os.environ.get("XDG_DATA_HOME") or (pathlib.Path.home() / ".local" / "share"))
    path = root / "ShowdownDraft" / "webview"
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


if __name__ == "__main__":
    base = _get_base()
    storage = _user_storage()
    _clear_webview_cache(storage)
    api = GameAPI()
    window = webview.create_window(
        "Showdown Draft",
        url=str(base / "dist" / "index.html"),
        js_api=api,
        width=1920,
        height=1080,
        fullscreen=True,
        resizable=True,
        min_size=(1280, 720),
    )
    webview.start(private_mode=False, storage_path=storage)
