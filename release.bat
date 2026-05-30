@echo off
setlocal

if "%1"=="" (
    echo.
    echo  Uso: release.bat VERSAO
    echo  Exemplo: release.bat 1.0.3
    echo.
    pause
    exit /b 1
)

set VERSION=%1
set GIT="C:\Program Files\Git\bin\git.exe"

echo.
echo === RELEASE v%VERSION% ===
echo.

:: [1/4] Atualiza versao no codigo
echo [1/4] Atualizando versao...
python _set_version.py %VERSION%
if errorlevel 1 ( echo ERRO ao atualizar versao! & pause & exit /b 1 )

:: [2/4] Build do frontend
echo.
echo [2/4] Buildando frontend...
cd /d "%~dp0frontend"
call npm run build
if errorlevel 1 ( echo ERRO no build do frontend! & pause & exit /b 1 )
cd /d "%~dp0"

:: [3/4] Build do .exe
echo.
echo [3/4] Gerando .exe...
pyinstaller --noconfirm showdown.spec
if errorlevel 1 ( echo ERRO ao gerar .exe! & pause & exit /b 1 )

:: [4/4] Publica no GitHub
echo.
echo [4/4] Publicando no GitHub...
%GIT% add -u
%GIT% add frontend\src api assets *.py *.bat *.spec
%GIT% commit -m "release v%VERSION%"
%GIT% push
gh release create v%VERSION% "dist\ShowdownDraft.exe" --title "Versao %VERSION%" --notes ""
if errorlevel 1 ( echo ERRO ao publicar no GitHub! & pause & exit /b 1 )

echo.
echo ================================
echo  PRONTO! Release v%VERSION% publicado.
echo  Os jogadores ja podem atualizar.
echo ================================
echo.
pause
