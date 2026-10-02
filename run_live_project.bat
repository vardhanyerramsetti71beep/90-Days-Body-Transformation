@echo off
title 90-Day Body Transformation Live Suite
cd /d "%~dp0"
echo ========================================================
echo   STARTING 90-DAY TRANSFORMATION LIVE SUITE
echo ========================================================
echo.
echo Activating Virtual Environment...
call "..\venv\Scripts\activate.bat"

echo Launching Flask Web Dashboard on http://127.0.0.1:5000 ...
python app.py
pause
