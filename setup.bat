@echo off
REM ============================================================================
REM ProtectLayer Educational DRM System - Windows Setup Script
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                   ProtectLayer Educational System v1.0                     ║
echo ║                         Setup ^& Installation                               ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% found

REM Create virtual environment
if not exist "venv" (
    echo.
    echo Creating Python virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
pip install -q --upgrade pip setuptools wheel
pip install -q -r requirements.txt
echo ✅ Dependencies installed

REM Create directories
echo.
echo Setting up student workspace...
if not exist "%USERPROFILE%\.protectlayer\students" mkdir "%USERPROFILE%\.protectlayer\students"
if not exist "%USERPROFILE%\.protectlayer\submissions" mkdir "%USERPROFILE%\.protectlayer\submissions"
if not exist "%USERPROFILE%\.protectlayer\data" mkdir "%USERPROFILE%\.protectlayer\data"
echo ✅ Workspace directories created

REM Display disclaimer
cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                         ⚠️  LEGAL DISCLAIMER ⚠️                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo This is an EDUCATIONAL TOOL ONLY for learning about content protection.
echo.
echo IMPORTANT:
echo.
echo ● Circumventing copy protection on content you don't own may be ILLEGAL
echo ● You are responsible for your use of this software
echo ● The creators assume NO LIABILITY for misuse
echo ● You must comply with all applicable laws in your jurisdiction
echo ● See docs/DISCLAIMER.md for complete legal terms
echo.
set /p "agree=Do you agree to these terms? (yes/no): "
if /i not "%agree%"=="yes" (
    echo ❌ Setup cancelled. You must agree to the terms to continue.
    pause
    exit /b 1
)

echo ✅ Terms accepted

REM Initialize database
echo.
echo Initializing database...
python -c "from pathlib import Path; import sqlite3; db=Path.home()/'.protectlayer'/'data'/'progress.db'; db.parent.mkdir(parents=True,exist_ok=True); sqlite3.connect(str(db)).execute('CREATE TABLE IF NOT EXISTS student_info (id TEXT PRIMARY KEY, display_name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, last_activity TIMESTAMP)'); print('Database initialized')"
echo ✅ Database initialized

REM Setup complete
cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                        ✅  SETUP COMPLETE  ✅                             ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo ProtectLayer is ready to use!
echo.
echo Next steps:
echo   1. Read the documentation:  cat docs\LEARNING_PATHS.md
echo   2. Start with Layer 1:      cd layers\layer1_detection
echo   3. Run the tutorial:        python tutorial.py
echo   4. View your progress:      python dashboard\app.py
echo.
echo Documentation:
echo   - Learning Paths:  docs\LEARNING_PATHS.md
echo   - FAQ:             docs\FAQ.md
echo   - Legal:           docs\DISCLAIMER.md
echo.

set /p "launch=Launch dashboard now? (yes/no): "
if /i "%launch%"=="yes" (
    echo.
    echo Opening http://localhost:5000...
    python dashboard\app.py
) else (
    echo.
    echo To launch later, run: python dashboard\app.py
    pause
)
