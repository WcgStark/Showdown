@echo off
setlocal

if "%1"=="" (
    echo.
    echo  Uso: release.bat VERSAO
    echo  Exemplo: release.bat 1.0.2
    echo.
    pause
    exit /b 1
)

set VERSION=%1

echo.
echo === RELEASE v%VERSION% ===
echo.

:: Atualiza APP_VERSION no updater.py
python _set_version.py %VERSION%
if errorlevel 1 ( echo ERRO ao atualizar versao! & pause & exit /b 1 )

:: Commit + tag + push
"C:\Program Files\Git\bin\git.exe" add updater.py .gitignore .github
"C:\Program Files\Git\bin\git.exe" commit -m "release v%VERSION%"
"C:\Program Files\Git\bin\git.exe" tag v%VERSION%
"C:\Program Files\Git\bin\git.exe" push
"C:\Program Files\Git\bin\git.exe" push --tags

echo.
echo === PRONTO! ===
echo GitHub Actions vai buildar e publicar o .exe automaticamente.
echo Acompanhe em: https://github.com/WcgStark/Showdown/actions
echo.
pause
