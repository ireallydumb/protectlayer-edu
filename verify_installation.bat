@echo off
REM verify_installation.bat - ProtectLayer Installation Verification (Windows)

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                                                                        ║
echo ║          ProtectLayer Installation Verification Script                ║
echo ║                                                                        ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.

set PASS=0
set FAIL=0
set WARNINGS=0

REM Python Check
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3 installed
    set /a FAIL+=1
) else (
    echo ✅ Python 3 installed
    set /a PASS+=1
)

REM Virtual Environment Check
if exist "venv\" (
    echo ✅ Virtual environment exists
    set /a PASS+=1
) else (
    echo ❌ Virtual environment exists
    set /a FAIL+=1
)

REM Project Files Check
if exist "README.md" (
    echo ✅ README.md exists
    set /a PASS+=1
) else (
    echo ❌ README.md exists
    set /a FAIL+=1
)

if exist "launch.py" (
    echo ✅ launch.py exists
    set /a PASS+=1
) else (
    echo ❌ launch.py exists
    set /a FAIL+=1
)

if exist "setup.bat" (
    echo ✅ setup.bat exists
    set /a PASS+=1
) else (
    echo ❌ setup.bat exists
    set /a FAIL+=1
)

REM Layer Checks
if exist "layers\layer1_detection\tutorial.py" (
    echo ✅ Layer 1 tutorial exists
    set /a PASS+=1
) else (
    echo ❌ Layer 1 tutorial exists
    set /a FAIL+=1
)

if exist "layers\layer2_visible\tutorial.py" (
    echo ✅ Layer 2 tutorial exists
    set /a PASS+=1
) else (
    echo ❌ Layer 2 tutorial exists
    set /a FAIL+=1
)

if exist "layers\layer3_invisible\tutorial.py" (
    echo ✅ Layer 3 tutorial exists
    set /a PASS+=1
) else (
    echo ❌ Layer 3 tutorial exists
    set /a FAIL+=1
)

if exist "layers\layer4_device\tutorial.py" (
    echo ✅ Layer 4 tutorial exists
    set /a PASS+=1
) else (
    echo ❌ Layer 4 tutorial exists
    set /a FAIL+=1
)

if exist "layers\layer5_advanced\tutorial.py" (
    echo ✅ Layer 5 tutorial exists
    set /a PASS+=1
) else (
    echo ❌ Layer 5 tutorial exists
    set /a FAIL+=1
)

REM Documentation Check
if exist "docs\INSTALLATION.md" (
    echo ✅ Installation guide exists
    set /a PASS+=1
) else (
    echo ❌ Installation guide exists
    set /a FAIL+=1
)

REM Results
echo.
echo ═════════════════════════════════════════════════════════════════════════
echo.
echo RESULTS
echo ───────────────────────────────────────────────────────────────────────
echo ✅ Passed:   !PASS!
echo ❌ Failed:   !FAIL!
echo.

if !FAIL! equ 0 (
    echo ═════════════════════════════════════════════════════════════════════════
    echo.
    echo ✅ INSTALLATION VERIFIED!
    echo.
    echo Your ProtectLayer installation is complete and ready to use.
    echo.
    echo Next steps:
    echo   1. Launch the application:
    echo      launch.bat         (Windows)
    echo      python3 launch.py  (Any platform)
    echo.
    echo   2. Start learning:
    echo      Select Layer 1 from the menu
    echo.
    echo ═════════════════════════════════════════════════════════════════════════
    pause
    exit /b 0
) else (
    echo ═════════════════════════════════════════════════════════════════════════
    echo.
    echo ❌ INSTALLATION INCOMPLETE
    echo.
    echo Some files or dependencies are missing.
    echo.
    echo To fix:
    echo   1. Run: setup.bat
    echo   2. Run this verification again
    echo.
    echo ═════════════════════════════════════════════════════════════════════════
    pause
    exit /b 1
)
