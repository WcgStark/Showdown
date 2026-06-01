@echo off
cd /d "%~dp0"

echo === GIT STATUS ===
git status -s
echo.

set /p MSG="Mensagem do commit: "
if "%MSG%"=="" (
    echo Mensagem vazia. Cancelando.
    pause
    exit /b 1
)

git add -A
git commit -m "%MSG%"

echo.
pause
