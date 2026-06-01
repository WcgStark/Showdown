# Showdown Draft

App de desktop (Windows) para draft de personagens entre dois jogadores, por universo
(One Piece, Naruto, Bleach, Invincible, JoJo). Frontend em React + Vite, empacotado
num executável standalone com pywebview + PyInstaller.

## Arquitetura

```
api/            # Bridge entre o frontend (JS) e o backend (Python) via pywebview
application/    # Casos de uso: GameService (regras de draft) + SessionManager (estado)
domain/         # Entidades puras: Match, Player, e regras de matchmaking
config/         # Universos, arenas e settings (fonte única de dados)
frontend/       # App React (telas, componentes, i18n, sons, keybinds)
updater.py      # Auto-update via releases do GitHub
main.py         # Entry point — cria a janela pywebview
```

## Modo dev (testar sem buildar)

```
dev.bat
```

Sobe o servidor Vite (frontend) e abre o app apontando para `localhost:5173`.
Mudanças no frontend aparecem automaticamente, sem reiniciar. Para parar, feche a janela.

**Requisitos (instalar uma vez):**

```
pip install pywebview pyinstaller
cd frontend && npm install
```

## Build (gerar o .exe)

```
build.bat
```

1. Builda o frontend (`npm run build`) → gera `dist/`
2. Empacota tudo com PyInstaller → gera `dist/ShowdownDraft.exe`

O `.exe` é standalone — não precisa de Python instalado.

## Lançar uma release

```
release.bat 1.2.9
```

Faz **tudo localmente** e publica no GitHub (não há GitHub Actions; o build do `.exe`
roda na sua máquina):

1. Atualiza a versão em `updater.py` (`_set_version.py`)
2. Builda frontend + `.exe`
3. Commita, faz push e cria a release com `gh release create`

Os jogadores que abrirem o app veem o banner de atualização automaticamente e
instalam com um clique.

## Testes

```
python -m pytest
```

Cobre a lógica de draft do `GameService` (draw / assign / skip / switch / undo).

## Fluxo do dia a dia

- Mexeu no código? → `commit.bat` (ou `git add . && git commit -m "..." && git push`)
- Quer que os jogadores recebam a versão nova? → `release.bat 1.X.X`
