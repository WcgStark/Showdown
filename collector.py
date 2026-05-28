"""
Image collector.

Downloads a portrait for every character of every universe from its Fandom
wiki (via the MediaWiki API in config/universes.py) and saves it into the
universe's asset folder. Characters that already have an image are skipped, so
it is safe to re-run — it only fills in what is missing.

Usage:
    python collector.py              # all universes
    python collector.py jojo         # only the "jojo" universe
    python collector.py jojo naruto  # only these universes

Uses the Python standard library only (no pip install needed).
"""

from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

from config.universes import ALL_UNIVERSES

BASE_DIR = pathlib.Path(__file__).parent

# Frontend looks for "<Name>.jpeg" for static portraits (only .gif is special),
# so everything we download is saved with a .jpeg filename. A renamed PNG still
# renders fine in the WebView. Existing files in any of these formats count as
# "already collected" and are left untouched.
KNOWN_EXTS = (".jpeg", ".jpg", ".png", ".gif", ".webp")
SAVE_EXT = ".jpeg"

THUMB_SIZE = 500           # px — width of the portrait we request
REQUEST_PAUSE = 0.25       # seconds between API hits (be polite to Fandom)
USER_AGENT = "ShowdownDraft-Collector/1.0 (asset fetcher; contact: showdown app)"


def _api_get(api_url: str, params: dict) -> dict:
    """Call a MediaWiki API endpoint and return the parsed JSON."""
    params = {**params, "format": "json", "formatversion": "2"}
    url = f"{api_url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _page_image(api_url: str, title: str) -> str | None:
    """Return the thumbnail URL for a page title, following redirects."""
    try:
        data = _api_get(api_url, {
            "action": "query",
            "prop": "pageimages",
            "piprop": "thumbnail",
            "pithumbsize": str(THUMB_SIZE),
            "titles": title,
            "redirects": "1",
        })
    except Exception:
        return None
    for page in data.get("query", {}).get("pages", []):
        if page.get("missing"):
            continue
        thumb = page.get("thumbnail", {}).get("source")
        if thumb:
            return thumb
    return None


def _search_title(api_url: str, query: str) -> str | None:
    """Find the best-matching page title for a name (handles short names)."""
    try:
        data = _api_get(api_url, {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": "1",
        })
    except Exception:
        return None
    results = data.get("query", {}).get("search", [])
    return results[0]["title"] if results else None


def _resolve_image(api_url: str, name: str) -> str | None:
    """Try the exact title first, then a wiki search fallback."""
    url = _page_image(api_url, name)
    if url:
        return url
    time.sleep(REQUEST_PAUSE)
    found = _search_title(api_url, name)
    if found and found.lower() != name.lower():
        time.sleep(REQUEST_PAUSE)
        return _page_image(api_url, found)
    return None


def _download(url: str, dest: pathlib.Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    dest.write_bytes(data)


def _already_has_image(folder: pathlib.Path, name: str) -> bool:
    return any((folder / f"{name}{ext}").exists() for ext in KNOWN_EXTS)


def collect_universe(key: str) -> None:
    universe = ALL_UNIVERSES[key]
    folder = BASE_DIR / universe.asset_folder
    folder.mkdir(parents=True, exist_ok=True)

    print(f"\n=== {universe.name}  ({len(universe.characters)} personagens) ===")
    print(f"    pasta: {folder}")
    print(f"    wiki:  {universe.api_url}")

    downloaded = skipped = missing = 0
    not_found: list[str] = []

    for name in universe.characters:
        if _already_has_image(folder, name):
            skipped += 1
            continue
        url = _resolve_image(universe.api_url, name)
        time.sleep(REQUEST_PAUSE)
        if not url:
            missing += 1
            not_found.append(name)
            print(f"    [ x ] {name}  (sem imagem)")
            continue
        try:
            _download(url, folder / f"{name}{SAVE_EXT}")
            downloaded += 1
            print(f"    [ ok] {name}")
        except Exception as exc:
            missing += 1
            not_found.append(name)
            print(f"    [ x ] {name}  (erro: {exc})")

    print(f"\n    Baixadas: {downloaded} | Já existiam: {skipped} | Faltando: {missing}")

    # TXT report of what could not be downloaded (one per universe folder).
    report = folder / "_imagens_faltando.txt"
    if not_found:
        lines = [
            f"# {universe.name} — imagens que NAO foram baixadas",
            f"# Adicione manualmente em {universe.asset_folder}/ (como {SAVE_EXT} ou .gif)",
            "",
            *[f"{n}{SAVE_EXT}" for n in not_found],
        ]
        report.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"    Lista do que faltou salva em: {report}")
    elif report.exists():
        report.unlink()  # nothing missing now — drop the stale report


def main() -> None:
    args = [a.lower() for a in sys.argv[1:]]
    if args:
        unknown = [a for a in args if a not in ALL_UNIVERSES]
        if unknown:
            print(f"Universo(s) desconhecido(s): {', '.join(unknown)}")
            print(f"Disponíveis: {', '.join(ALL_UNIVERSES)}")
            sys.exit(1)
        targets = args
    else:
        targets = list(ALL_UNIVERSES)

    print("=== COLLECTOR DE IMAGENS — Showdown Draft ===")
    print(f"Universos: {', '.join(targets)}")
    for key in targets:
        collect_universe(key)
    print("\n=== CONCLUÍDO ===")


if __name__ == "__main__":
    main()
