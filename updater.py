from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import urllib.request

APP_VERSION = "1.3.1"
# ─── GitHub repo the auto-updater pulls releases from ────────────────────────
GITHUB_OWNER = "WcgStark"
GITHUB_REPO = "Showdown"
# ─────────────────────────────────────────────────────────────────────────────

_API_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"

_state: dict = {"status": "idle", "value": 0, "tmp_path": ""}
_lock = threading.Lock()

# Diagnostic log for the (notoriously fiddly) self-replace step. On by default
# because update failures only happen on end-user machines; set the env var to
# "0" to silence it.
UPDATE_DEBUG = os.environ.get("SHOWDOWN_UPDATE_DEBUG", "1") != "0"
_LOG_PATH = os.path.join(tempfile.gettempdir(), "showdown_update.log")


def _ulog(msg: str, *, reset: bool = False) -> None:
    if not UPDATE_DEBUG:
        return
    try:
        with open(_LOG_PATH, "w" if reset else "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


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
_CREATE_BREAKAWAY_FROM_JOB = 0x01000000  # escape Windows Job Object so PS survives parent exit


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
    log_path = _LOG_PATH
    ps_path  = os.path.join(tempfile.gettempdir(), "showdown_update.ps1")

    # Write Python-level diagnostic before touching PowerShell
    _ulog(f"[py] frozen={getattr(sys, 'frozen', False)}", reset=True)
    _ulog(f"[py] pid={pid}")
    _ulog(f"[py] tmp_path={tmp_path}")
    _ulog(f"[py] tmp_exists={os.path.exists(tmp_path)}")
    _ulog(f"[py] current_exe={current_exe}")
    _ulog(f"[py] ps_path={ps_path}")
    _ulog(f"[py] powershell_exists={os.path.exists(_POWERSHELL)}")

    ps = (
        f'$appPid = {pid}\n'
        f'$src = "{tmp_path}"\n'
        f'$dst = "{current_exe}"\n'
        f'$log = "{log_path}"\n'
        '"[ps] script started" | Out-File $log -Encoding utf8 -Append\n'
        'while (Get-Process -Id $appPid -ErrorAction SilentlyContinue) { Start-Sleep -Milliseconds 300 }\n'
        '"[ps] process exited" | Out-File $log -Append\n'
        'Start-Sleep -Milliseconds 2000\n'
        # Copy new exe (retry up to 5x in case file is briefly locked)
        '$ok = $false\n'
        'for ($i = 0; $i -lt 5; $i++) {\n'
        '  try { Copy-Item -Path $src -Destination $dst -Force -ErrorAction Stop; $ok = $true; break }\n'
        '  catch { "[ps] copy attempt $i failed: $_" | Out-File $log -Append; Start-Sleep -Milliseconds 600 }\n'
        '}\n'
        'if ($ok) { "[ps] copy succeeded" | Out-File $log -Append } else { "[ps] copy FAILED" | Out-File $log -Append; exit 1 }\n'
        'Remove-Item $src -Force -ErrorAction SilentlyContinue\n'
        # Let the freshly-written exe settle: Defender real-time scan can briefly lock
        # the file, which makes the onefile bootloader fail to extract python3xx.dll.
        'Start-Sleep -Milliseconds 4000\n'
        '"[ps] settle done, launching" | Out-File $log -Append\n'
        # Launch via explorer.exe so the new exe runs in a clean shell context (exactly
        # like a double-click) instead of as a child of this hidden PowerShell. Launching
        # it as a PowerShell child was making the onefile bootloader fail to load
        # python3xx.dll, while a manual relaunch always worked.
        'try { Start-Process -FilePath "explorer.exe" -ArgumentList $dst; "[ps] launch succeeded" | Out-File $log -Append }\n'
        'catch { "[ps] launch failed: $_" | Out-File $log -Append }\n'
        # Keep PowerShell alive while the new exe finishes extracting its _MEI bundle.
        'Start-Sleep -Milliseconds 3000\n'
        'Remove-Item $PSCommandPath -Force -ErrorAction SilentlyContinue\n'
    )

    with open(ps_path, "w", encoding="utf-8") as f:
        f.write(ps)

    # ShellExecuteW launches via the Windows Shell — the spawned process is NOT
    # placed in the calling process's Job Object, bypassing PyInstaller's job limit.
    import ctypes
    ps_args = f'-ExecutionPolicy Bypass -WindowStyle Hidden -File "{ps_path}"'
    try:
        _ulog("[py] launching via ShellExecuteW")
        ret = ctypes.windll.shell32.ShellExecuteW(None, "open", _POWERSHELL, ps_args, None, 0)
        _ulog(f"[py] ShellExecuteW returned {ret}")
        if ret <= 32:
            raise RuntimeError(f"ShellExecuteW error code {ret}")
    except Exception as e:
        _ulog(f"[py] ShellExecuteW FAILED ({e}), falling back to Popen")
        try:
            subprocess.Popen(
                [_POWERSHELL, "-ExecutionPolicy", "Bypass", "-WindowStyle", "Hidden", "-File", ps_path],
                creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | _CREATE_BREAKAWAY_FROM_JOB,
                close_fds=True,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception as e2:
            _ulog(f"[py] Popen fallback FAILED: {e2}")
            return False

    return True
