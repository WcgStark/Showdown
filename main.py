from __future__ import annotations

import pathlib
import sys

import webview

from api.bridge import GameAPI


def _get_base() -> pathlib.Path:
    if getattr(sys, "frozen", False):
        return pathlib.Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return pathlib.Path(__file__).parent


if __name__ == "__main__":
    base = _get_base()
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
    webview.start()
