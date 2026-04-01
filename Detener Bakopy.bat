@echo off
title Detener Bakopy
echo =========================================
echo   Deteniendo Bakopy...
echo =========================================
taskkill /f /im python.exe /fi "WINDOWTITLE eq Bakopy*" >nul 2>&1
taskkill /f /im python.exe >nul 2>&1
echo Bakopy detenido correctamente.
echo Podes cerrar esta ventana.
echo =========================================
pause
