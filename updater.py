from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import urllib.request

APP_VERSION = "1.0.8"
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


_POWERSHELL = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"


def apply_update() -> bool:
    """Launches a PowerShell helper that waits for this process to exit, then replaces the exe."""
    if not getattr(sys, "frozen", False):
        return False

    with _lock:
        tmp_path = _state.get("tmp_path", "")

    if not tmp_path or not os.path.exists(tmp_path):
        return False

    current_exe = sys.executable
    pid = os.getpid()
    mei_path = getattr(sys, "_MEIPASS", "")
    log_path = os.path.join(tempfile.gettempdir(), "showdown_update.log")
    ps_path  = os.path.join(tempfile.gettempdir(), "showdown_update.ps1")

    # Write Python-level diagnostic before touching PowerShell
    try:
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"[py] frozen={getattr(sys, 'frozen', False)}\n")
            f.write(f"[py] pid={pid}\n")
            f.write(f"[py] tmp_path={tmp_path}\n")
            f.write(f"[py] tmp_exists={os.path.exists(tmp_path)}\n")
            f.write(f"[py] current_exe={current_exe}\n")
            f.write(f"[py] ps_path={ps_path}\n")
            f.write(f"[py] powershell_exists={os.path.exists(_POWERSHELL)}\n")
    except Exception:
        pass

    ps = (
        f'$appPid = {pid}\n'
        f'$src = "{tmp_path}"\n'
        f'$dst = "{current_exe}"\n'
        f'$mei = "{mei_path}"\n'
        f'$log = "{log_path}"\n'
        '"[ps] script started" | Out-File $log -Encoding utf8 -Append\n'
        # Wait until this process is fully gone ($PID is reserved — use $appPid)
        'while (Get-Process -Id $appPid -ErrorAction SilentlyContinue) { Start-Sleep -Milliseconds 300 }\n'
        '"[ps] process exited" | Out-File $log -Append\n'
        'Start-Sleep -Milliseconds 2000\n'
        # Clean up old MEI temp dir so the new exe starts fresh
        'if ($mei -and (Test-Path $mei)) { Remove-Item $mei -Recurse -Force -ErrorAction SilentlyContinue }\n'
        '"[ps] MEI cleaned" | Out-File $log -Append\n'
        # Copy new exe (retry up to 5x in case file is briefly locked)
        '$ok = $false\n'
        'for ($i = 0; $i -lt 5; $i++) {\n'
        '  try { Copy-Item -Path $src -Destination $dst -Force -ErrorAction Stop; $ok = $true; break }\n'
        '  catch { "[ps] copy attempt $i failed: $_" | Out-File $log -Append; Start-Sleep -Milliseconds 600 }\n'
        '}\n'
        'if ($ok) { "[ps] copy succeeded" | Out-File $log -Append } else { "[ps] copy FAILED" | Out-File $log -Append; exit 1 }\n'
        'Remove-Item $src -Force -ErrorAction SilentlyContinue\n'
        # Launch updated exe
        'try { Start-Process -FilePath $dst; "[ps] launch succeeded" | Out-File $log -Append }\n'
        'catch { "[ps] launch failed: $_" | Out-File $log -Append }\n'
        'Remove-Item $PSCommandPath -Force -ErrorAction SilentlyContinue\n'
    )

    with open(ps_path, "w", encoding="utf-8") as f:
        f.write(ps)

    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[py] ps1 written, launching powershell\n")
        subprocess.Popen(
            [_POWERSHELL, "-ExecutionPolicy", "Bypass", "-WindowStyle", "Hidden", "-File", ps_path],
            creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP,
            close_fds=True,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[py] Popen returned OK\n")
    except Exception as e:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[py] Popen FAILED: {e}\n")
        return False

    return True
