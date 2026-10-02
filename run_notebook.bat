@echo off
title 90-Day Transformation Jupyter Notebook
cd /d "%~dp0"
echo ========================================================
echo   OPENING 90-DAY TRANSFORMATION JUPYTER NOTEBOOK
echo ========================================================
echo.
echo Activating Virtual Environment...
call "..\venv\Scripts\activate.bat"

echo Starting Jupyter Notebook Server...
jupyter notebook 90_Day_Transformation_Mastery.ipynb
pause
