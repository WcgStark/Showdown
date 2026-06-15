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

:: Valida o formato X.Y.Z — evita publicar uma versao invalida tipo "bat"
echo %VERSION%| findstr /r "^[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$" >nul
if errorlevel 1 (
    echo.
    echo  ERRO: versao invalida "%VERSION%". Use o formato X.Y.Z
    echo  Exemplo: release.bat 1.3.2
    echo.
    pause
    exit /b 1
)

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
:: Remove o .exe da build anterior de dentro de dist\ — senao o PyInstaller
:: empacota o exe antigo dentro do novo, inflando o tamanho a cada release.
if exist "dist\ShowdownDraft.exe" del /q "dist\ShowdownDraft.exe"
pyinstaller --noconfirm showdown.spec
if errorlevel 1 ( echo ERRO ao gerar .exe! & pause & exit /b 1 )

:: [4/4] Publica no GitHub
echo.
echo [4/4] Publicando no GitHub...
%GIT% add -u
%GIT% add frontend\src api assets *.py *.bat *.spec
%GIT% commit -m "release v%VERSION%"
%GIT% push
if errorlevel 1 (
    echo.
    echo  ERRO no push! O remoto provavelmente tem commits novos.
    echo  Rode:  git pull --rebase   e depois execute o release.bat de novo.
    echo  (Release NAO publicado, para nao gerar versao quebrada.)
    echo.
    pause
    exit /b 1
)
gh release create v%VERSION% "dist\ShowdownDraft.exe" --repo WcgStark/ShowdownDraft --title "Versao %VERSION%" --notes ""
if errorlevel 1 ( echo ERRO ao publicar no GitHub! & pause & exit /b 1 )

echo.
echo ================================
echo  PRONTO! Release v%VERSION% publicado.
echo  Os jogadores ja podem atualizar.
echo ================================
echo.
pause
