@echo off
cd /d "%~dp0"
echo === BUILD SHOWDOWN ===

echo.
echo [1/2] Buildando frontend...
cd /d "%~dp0frontend"
call npm run build
if errorlevel 1 (
    echo ERRO no build do frontend!
    pause
    exit /b 1
)

echo.
echo [2/2] Gerando .exe...
cd /d "%~dp0"
pyinstaller --noconfirm showdown.spec
if errorlevel 1 (
    echo ERRO ao gerar o .exe!
    pause
    exit /b 1
)

echo.
echo === PRONTO! ===
echo O .exe esta em: dist\ShowdownDraft.exe
pause
