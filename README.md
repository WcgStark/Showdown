# Showdown Draft

Desktop app (Windows) for drafting characters between two players, organized by universe
(One Piece, Naruto, Bleach, Invincible, JoJo, JJK). Frontend built with React + Vite, packaged
into a standalone executable using pywebview + PyInstaller.

## Architecture

```
api/            # Bridge between frontend (JS) and backend (Python) via pywebview
application/    # Use cases: GameService (draft rules) + SessionManager (state)
domain/         # Pure entities: Match, Player, and matchmaking rules
config/         # Universes, arenas, and settings (single source of truth)
frontend/       # React app (screens, components, i18n, sounds, keybinds)
updater.py      # Auto-update via GitHub releases
main.py         # Entry point — creates the pywebview window
```

## Usage

The app runs by simply executing `ShowdownDraft.exe` — no installation or Python required.
> 📦 **[Download the latest release](https://github.com/WcgStark/ShowdownDraft/releases)** — grab the `.exe` directly without building anything.

If you want to modify the code, read the sections below.

---
## Dev mode (run without building)

```
dev.bat
```

Starts the Vite server (frontend) and opens the app pointing to `localhost:5173`.
Frontend changes are applied automatically, without restarting. To stop, close the window.

**Requirements (install once):**

```
pip install pywebview pyinstaller
cd frontend && npm install
```

## Build (generate the .exe)

```
build.bat
```

1. Builds the frontend (`npm run build`) → generates `dist/`
2. Packages everything with PyInstaller → generates `dist/ShowdownDraft.exe`

The `.exe` is standalone — no Python installation required.

## Release deployment

```
release.bat 1.2.9
```

Runs **everything locally** and publishes to GitHub (there are no GitHub Actions; the `.exe`
build runs on your machine):

1. Updates the version in `updater.py` (`_set_version.py`)
2. Builds frontend + `.exe`
3. Commits, pushes, and creates the release with `gh release create`

Players who open the app automatically see the update banner and can install it with one click.

## Tests

```
python -m pytest
```

Covers the draft logic in `GameService` (draw / assign / skip / switch / undo).

## Daily workflow

- Changed code? → `commit.bat` (or `git add . && git commit -m "..." && git push`)
- Want players to receive the new version? → `release.bat 1.X.X`
