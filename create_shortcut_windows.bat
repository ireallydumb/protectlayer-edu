@echo off
REM Create desktop shortcut for ProtectLayer GUI Launcher

setlocal enabledelayedexpansion

echo Creating ProtectLayer desktop shortcut...

REM Get the full path to the project directory
for %%A in (.) do set "current_path=%%~dpA"
set "project_path=%current_path:~0,-1%"

REM Create shortcut using PowerShell
powershell -NoProfile -Command ^
"$WshShell = New-Object -ComObject WScript.Shell; ^
$Shortcut = $WshShell.CreateShortcut([System.Environment]::GetFolderPath('Desktop') + '\ProtectLayer.lnk'); ^
$Shortcut.TargetPath = 'python.exe'; ^
$Shortcut.Arguments = '%project_path%\gui_launcher.py'; ^
$Shortcut.WorkingDirectory = '%project_path%'; ^
$Shortcut.IconLocation = '%project_path%\assets\icon.ico'; ^
$Shortcut.Save()"

if errorlevel 1 (
    echo ❌ Failed to create shortcut
    pause
    exit /b 1
) else (
    echo ✅ Shortcut created on Desktop!
    echo.
    echo You can now launch ProtectLayer by double-clicking "ProtectLayer.lnk"
    pause
)
