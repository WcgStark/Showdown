import re, sys

version = sys.argv[1]
with open("updater.py", "r", encoding="utf-8") as f:
    content = f.read()
content = re.sub(r'APP_VERSION = "[^"]+"', f'APP_VERSION = "{version}"', content)
with open("updater.py", "w", encoding="utf-8") as f:
    f.write(content)
print(f"[OK] APP_VERSION = {version}")
