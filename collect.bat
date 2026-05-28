@echo off
cd /d "%~dp0"
echo === COLLECTOR DE IMAGENS ===
echo.
echo Sem argumentos: baixa imagens que faltam de TODOS os universos.
echo Para um so universo:  collect.bat jojo
echo.
python collector.py %*
echo.
pause
