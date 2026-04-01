@echo off
title Bakopy
cd /d "%~dp0"

echo =========================================
echo   Bakopy - Iniciando...
echo =========================================

if not exist venv (
    echo Configurando Bakopy por primera vez...
    python -m venv venv
    if errorlevel 1 (
        echo.
        echo ERROR: Python no esta instalado.
        echo Descargalo desde https://www.python.org/downloads/
        echo Asegurate de marcar "Add Python to PATH" al instalar.
        pause
        exit /b 1
    )
    call venv\Scripts\activate.bat
    pip install flask --quiet
    echo Listo.
) else (
    call venv\Scripts\activate.bat
)

echo Abriendo Bakopy en tu navegador...
echo Para cerrar Bakopy usa el archivo "Detener Bakopy.bat"
echo O simplemente cerra esta ventana.
echo =========================================

start "" http://localhost:5099
python bakopy.py
