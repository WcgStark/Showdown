from __future__ import annotations
import subprocess
import time
import signal
import os
import webview
from api.bridge import GameAPI

frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
npm_proc = subprocess.Popen(
    ["cmd", "/c", "npm run dev"],
    cwd=frontend_dir,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
)

time.sleep(3)

api = GameAPI()
window = webview.create_window(
    "Showdown Draft [DEV]",
    url="http://localhost:5173",
    js_api=api,
    width=1920,
    height=1080,
    fullscreen=True,
    resizable=True,
    min_size=(1280, 720),
)
webview.start()

npm_proc.send_signal(signal.CTRL_BREAK_EVENT)
npm_proc.terminate()
