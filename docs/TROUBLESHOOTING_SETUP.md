# Setup Troubleshooting Guide

Common issues during `./setup.sh` or `setup.bat` and how to fix them.

---

## 🔴 "can't open file 'dashboard/app.py': No such file or directory"

**Error Message:**
```
Python3: can't open file '/path/to/protectlayer-edu/dashboard/app.py': 
{Errno 2} No such file in the directory
```

**What it means:**
- The setup script tried to launch a dashboard that doesn't exist
- This is a leftover reference from the old setup flow

**Solution:**

Don't worry - you don't need the dashboard! Use the **launcher instead**:

```bash
# macOS/Linux
./launch.sh

# Windows
launch.bat

# Or from anywhere
python3 launch.py
```

The launcher is much better:
- ✅ Interactive menu system
- ✅ Choose your layer
- ✅ View progress
- ✅ Track student profile
- ✅ Built-in documentation browser

**This is the recommended way to use ProtectLayer!**

---

## 🔴 "EOFError: EOF when reading a line"

**Error Message:**
```
File "<stdin>", line 21 in <module>
EOFError: EOF when reading a line
```

**What it means:**
- The setup script tried to get input from you, but stdin (keyboard input) wasn't available
- This typically happens when:
  - Running setup in a non-interactive environment
  - SSH connection without proper terminal forwarding
  - Running in a CI/CD pipeline or container
  - Terminal disconnected during setup

**Version Note:**
This issue was fixed in commit `9957ce4`. If you're using an older version, update:
```bash
git pull origin main
```

**Solution:**

### Option A: Run setup interactively (Best)
Make sure you're running setup directly in a terminal:

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows Command Prompt (Not PowerShell):**
```cmd
setup.bat
```

**Don't use:**
- `bash setup.sh < /dev/null` (disables stdin)
- Piping input with `|`
- Running in non-TTY environments

### Option B: Use non-interactive mode (Already Fixed!)
We've updated setup.sh to handle non-interactive environments gracefully. If you're still getting the error, make sure you have the **latest version** from GitHub:

```bash
git pull origin main
```

The new version will:
- Skip name prompt if stdin is not available
- Accept terms by default in non-interactive mode
- Skip dashboard launch in non-interactive mode
- Still set up everything correctly

### Option C: Provide input via echo (Workaround)
```bash
# Skip the disclaimer prompt
echo "yes" | ./setup.sh
```

---

## ⚠️ "ModuleNotFoundError: No module named 'cv2'"

**Error Message:**
```
ModuleNotFoundError: No module named 'cv2'
Hint: you might need to run 'pip install opencv-python'
```

**What it means:**
- OpenCV (computer vision library) isn't installed in your virtual environment
- Usually happens because setup failed partway

**Solution:**

### Option A: Reinstall dependencies
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Option B: Start over
```bash
# Delete virtual environment
rm -rf venv  # macOS/Linux
rmdir /S venv  # Windows

# Run setup again
./setup.sh  # or setup.bat
```

---

## 🔴 "Virtual environment not found"

**Error Message:**
```
❌ Virtual environment not found!
Please run './setup.sh' first
```

**What it means:**
- The `venv/` folder doesn't exist
- Either setup hasn't run, or failed

**Solution:**

```bash
# Make sure you're in the project directory
cd protectlayer-edu

# Run setup
./setup.sh  # macOS/Linux
setup.bat   # Windows
```

---

## ❌ "Permission denied: ./setup.sh"

**Error Message:**
```
bash: ./setup.sh: Permission denied
```

**What it means:**
- The file doesn't have execute permissions

**Solution:**
```bash
chmod +x setup.sh launch.sh
./setup.sh
```

---

## 🔴 "Python 3 not found"

**Error Message:**
```
❌ Python 3 not found
Please install Python 3.8 or higher from https://www.python.org/
```

**What it means:**
- Python isn't installed or not in your PATH

**Solution:**

### On Windows:
1. Visit https://www.python.org/downloads/
2. Download Python 3.12
3. Run installer
4. **CHECK: "Add Python to PATH"**
5. Restart Command Prompt
6. Try setup again

### On macOS:
```bash
# Option A: Homebrew
brew install python@3.12

# Option B: Direct
# Visit https://www.python.org/downloads/macos/
# Download and run installer
```

### On Linux:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.12 python3.12-venv

# Fedora
sudo dnf install python3.12

# Arch
sudo pacman -S python
```

---

## ⚠️ Setup Hangs or Freezes

**What it means:**
- Usually stuck downloading dependencies
- Network is slow or interrupted

**Solution:**

### Option A: Wait Longer
- Download can take 5-10 minutes on slow connections
- Wait at least 15 minutes before giving up

### Option B: Interrupt and Retry
```bash
# Press Ctrl+C to stop
# Then try again - it should resume from where it left off
./setup.sh
```

### Option C: Check Internet
```bash
# Test internet connection
ping google.com

# Or try to install something else
pip install requests
```

If internet is slow:
- Use a wired connection instead of WiFi
- Move closer to router
- Try again at a different time

---

## 🔴 "No space left on device"

**Error Message:**
```
OSError: [Errno 28] No space left on device
```

**What it means:**
- Your disk is full
- Virtual environment and packages need space

**Solution:**

### Check available space:
```bash
# macOS/Linux
df -h

# Windows (Command Prompt)
dir C:\
```

You need at least **1 GB free**.

### Free up space:
```bash
# Delete virtual environment (can recreate anytime)
rm -rf venv

# Delete old downloads
rm -rf ~/Downloads/*

# On macOS: Empty Trash
rm -rf ~/.Trash/*
```

Then run setup again.

---

## 🔵 "Connection refused" / "Cannot connect to database"

**Error Message:**
```
sqlite3.OperationalError: unable to open database file
```

**What it means:**
- Database file is corrupted
- Permissions issue

**Solution:**

### Delete and recreate database:
```bash
# macOS/Linux
rm -rf ~/.protectlayer/data/progress.db

# Windows
rmdir /S %USERPROFILE%\.protectlayer\data
```

Then:
```bash
./setup.sh  # or setup.bat
```

---

## ⚠️ "import cv2 failed"

**During launcher startup:**
```
ImportError: DLL load failed: The specified module could not be found
```

This is a Windows OpenCV issue.

**Solution:**

### Option A: Reinstall OpenCV
```cmd
venv\Scripts\activate.bat
pip uninstall opencv-python
pip install opencv-python
```

### Option B: Use headless version
```cmd
venv\Scripts\activate.bat
pip uninstall opencv-python
pip install opencv-python-headless
```

### Option C: Install Visual C++ Runtime
Download from: https://support.microsoft.com/en-us/help/2977003

---

## 🔴 "command not found: git"

**Error:**
```
git: command not found
```

**Solution:**

### macOS:
```bash
brew install git
# OR visit https://git-scm.com/download/mac
```

### Windows:
Visit https://git-scm.com/download/win and run installer

### Linux:
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

---

## 📊 Complete Troubleshooting Checklist

Before giving up, verify:

- [ ] Python 3.8+ installed
  ```bash
  python3 --version
  ```
  
- [ ] In project directory
  ```bash
  pwd  # Should end in protectlayer-edu
  ```
  
- [ ] Have internet connection
  ```bash
  ping google.com
  ```
  
- [ ] Have disk space (1+ GB free)
  ```bash
  df -h
  ```
  
- [ ] Using interactive terminal (not piped)
  - Don't use: `< /dev/null` or `|`
  
- [ ] Git installed (for cloning)
  ```bash
  git --version
  ```
  
- [ ] File permissions correct (macOS/Linux)
  ```bash
  chmod +x setup.sh launch.sh
  ```

---

## 🆘 Still Having Issues?

1. **Check [docs/INSTALLATION.md](INSTALLATION.md)** - Full installation guide
2. **Check [docs/FAQ.md](FAQ.md)** - Common questions
3. **Google the error message** - Might be common issue
4. **Report on GitHub:**
   - https://github.com/ireallydumb/protectlayer-edu/issues
   - Include:
     - Your OS (Windows 10/11, macOS version, Linux distro)
     - Python version (`python3 --version`)
     - Full error message
     - Steps to reproduce

---

## 🎯 Quick Recovery Steps

If setup fails partway:

```bash
# Option 1: Clean restart
rm -rf venv ~/.protectlayer
./setup.sh

# Option 2: Just reinstall dependencies
source venv/bin/activate  # or venv\Scripts\activate.bat
pip install -r requirements.txt

# Option 3: Check what went wrong
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt -v  # Verbose mode shows errors
```

---

## 🚀 Success Checklist

After setup completes, verify:

- [ ] No error messages shown
- [ ] Can run: `python3 -c "import cv2; print('OK')"`
- [ ] Can run: `./launch.sh` or `launch.bat`
- [ ] Menu appears when launcher runs
- [ ] Can select layers

If all checked: **You're ready to learn!** 🎉

---

**Still stuck? Report an issue on GitHub with your error message!**
