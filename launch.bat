@echo off
REM ProtectLayer - Easy Launcher (Windows)
REM Just run: launch.bat

setlocal enabledelayedexpansion

REM Check if venv exists
if not exist "venv\" (
    echo ❌ Virtual environment not found!
    echo Please run 'setup.bat' first
    pause
    exit /b 1
)

REM Activate venv
call venv\Scripts\activate.bat

REM Run launcher
python launch.py

pause
