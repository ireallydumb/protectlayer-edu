# Installation Guide

Complete step-by-step installation instructions for all operating systems.

**ProtectLayer is FREE and OPEN SOURCE - No accounts, no sign-ups required!**

---

## Quick Navigation

- **[🪟 Windows Installation](#-windows-installation)**
- **[🍎 macOS Installation](#-macos-installation)**
- **[🐧 Linux Installation](#-linux-installation)**
- **[❓ Troubleshooting](#-troubleshooting)**
- **[✅ Verify Installation](#-verify-installation)**

---

# 🪟 Windows Installation

### System Requirements
- **OS:** Windows 10 or later (Home, Pro, or Enterprise)
- **RAM:** 2 GB minimum (4 GB recommended)
- **Disk Space:** 500 MB minimum
- **Admin Rights:** Not required, but helps for some installs

---

## Step 1: Install Python 3.12+

### Option A: Using Microsoft Store (Recommended)
1. Open **Microsoft Store** (search from Start menu)
2. Search for **"Python 3.12"**
3. Click on official **Python 3.12** from Python Software Foundation
4. Click **"Get"** or **"Install"**
5. Wait for installation to complete

### Option B: Direct Download
1. Visit https://www.python.org/downloads/
2. Click **"Download Python 3.12.x"** (or latest 3.x version)
3. Run the installer (`.exe` file)
4. **IMPORTANT:** Check "Add Python to PATH" before clicking Install
5. Click "Install Now"
6. Wait for completion

### Verify Python Installation
Open **Command Prompt** (Win + R, type `cmd`, press Enter):
```cmd
python --version
```

Should show: `Python 3.12.x` or higher ✅

---

## Step 2: Clone the Repository

In **Command Prompt**, run:
```cmd
# Navigate to where you want the project (e.g., Documents)
cd Documents

# Clone the repository
git clone https://github.com/ireallydumb/protectlayer-edu.git

# Enter the project directory
cd protectlayer-edu
```

If you don't have Git installed, download from: https://git-scm.com/download/win

---

## Step 3: Run Setup

In **Command Prompt** (in the `protectlayer-edu` folder):
```cmd
setup.bat
```

This will:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies
- ✅ Set up your student profile
- ✅ Initialize the database
- ✅ Ask if you want to launch the dashboard

**Takes 2-5 minutes.**

**Answer the questions:**
- Legal disclaimer: Type `yes` and press Enter
- Optional name: Enter your name or press Enter to skip

---

## Step 4: Launch ProtectLayer

After setup completes, use either command:

**Option A (Recommended):**
```cmd
launch.bat
```

**Option B:**
```cmd
python launch.py
```

You should see an interactive menu with layer options!

---

## Step 5: Start Learning

From the menu, select:
- `1` - Layer 1: Detection
- `2` - Run tutorial
- Follow the interactive challenges

---

## Updating to Latest Version

To get new features and fixes:

```cmd
cd protectlayer-edu
git pull origin main
pip install -r requirements.txt --upgrade
```

---

---

# 🍎 macOS Installation

### System Requirements
- **OS:** macOS 10.14 or later (Intel or Apple Silicon)
- **RAM:** 2 GB minimum (4 GB recommended)
- **Disk Space:** 500 MB minimum
- **Terminal Access:** Basic command-line knowledge helpful

---

## Step 1: Install Python 3.12+

### Option A: Using Homebrew (Recommended)

First, install Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python:
```bash
brew install python@3.12
```

### Option B: Direct Download
1. Visit https://www.python.org/downloads/macos/
2. Download the **"macOS 64-bit universal2 installer"** (works on all Macs)
3. Run the installer
4. Follow the installation wizard
5. Python will be installed to `/Library/Frameworks/Python.framework`

### Verify Installation
Open **Terminal** (Cmd + Space, type `terminal`, press Enter):
```bash
python3 --version
```

Should show: `Python 3.12.x` or higher ✅

---

## Step 2: Clone the Repository

In **Terminal**:
```bash
# Navigate to where you want the project
cd ~/Documents

# Clone the repository
git clone https://github.com/ireallydumb/protectlayer-edu.git

# Enter the project directory
cd protectlayer-edu
```

If you don't have Git, macOS will prompt to install command-line tools. Follow the prompts.

---

## Step 3: Run Setup

Still in **Terminal** in the `protectlayer-edu` folder:

```bash
# Make setup script executable
chmod +x setup.sh

# Run setup
./setup.sh
```

This will:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies
- ✅ Set up your student profile
- ✅ Initialize the database
- ✅ Ask if you want to launch the dashboard

**Takes 2-5 minutes.**

**Answer the questions:**
- Legal disclaimer: Type `yes` and press Enter
- Optional name: Enter your name or press Enter to skip

---

## Step 4: Launch ProtectLayer

After setup completes, use either command:

**Option A (Recommended):**
```bash
./launch.sh
```

**Option B:**
```bash
python3 launch.py
```

You should see an interactive menu with layer options!

---

## Step 5: Start Learning

From the menu, select:
- `1` - Layer 1: Detection
- `2` - Run tutorial
- Follow the interactive challenges

---

## Updating to Latest Version

To get new features and fixes:

```bash
cd protectlayer-edu
git pull origin main
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

---

---

# 🐧 Linux Installation

### System Requirements
- **OS:** Ubuntu 20.04+, Debian 10+, Fedora 32+, or similar
- **RAM:** 2 GB minimum (4 GB recommended)
- **Disk Space:** 500 MB minimum
- **Terminal Access:** Required (you're using it anyway!)

---

## Installation Instructions for Major Distributions

### Ubuntu / Debian-Based

#### Step 1: Install Python 3.12+

```bash
# Update package manager
sudo apt update

# Install Python 3.12 and development tools
sudo apt install -y python3.12 python3.12-venv python3.12-dev git curl

# Verify installation
python3.12 --version
```

Should show: `Python 3.12.x` ✅

#### Step 2: Clone Repository

```bash
# Go to your home directory or preferred location
cd ~/Downloads  # or ~/Documents, etc.

# Clone the repository
git clone https://github.com/ireallydumb/protectlayer-edu.git

# Enter the project
cd protectlayer-edu
```

#### Step 3: Run Setup

```bash
# Make setup executable
chmod +x setup.sh

# Run setup
./setup.sh
```

**Answer the questions:**
- Legal disclaimer: Type `yes` and press Enter
- Optional name: Enter your name or press Enter to skip

---

### Fedora / RHEL-Based

#### Step 1: Install Python 3.12+

```bash
# Install Python 3.12 and development tools
sudo dnf install -y python3.12 python3.12-devel git curl

# Verify installation
python3.12 --version
```

#### Step 2: Clone Repository

```bash
cd ~/Downloads
git clone https://github.com/ireallydumb/protectlayer-edu.git
cd protectlayer-edu
```

#### Step 3: Run Setup

```bash
chmod +x setup.sh
./setup.sh
```

---

### Arch Linux / Manjaro

#### Step 1: Install Python 3.12+

```bash
# Install Python 3.12
sudo pacman -S python python-pip base-devel git

# Verify
python --version
```

#### Step 2: Clone Repository

```bash
cd ~/Downloads
git clone https://github.com/ireallydumb/protectlayer-edu.git
cd protectlayer-edu
```

#### Step 3: Run Setup

```bash
chmod +x setup.sh
./setup.sh
```

---

## Step 4: Launch ProtectLayer

After setup completes:

```bash
./launch.sh
```

Or:

```bash
python3 launch.py
```

You should see an interactive menu!

---

## Step 5: Start Learning

From the menu:
- Select `1` for Layer 1
- Select `2` to run tutorial
- Follow the challenges

---

## Updating to Latest Version

```bash
cd protectlayer-edu
git pull origin main
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

---

---

# ✅ Verify Installation

After setup completes successfully, verify everything works:

## Windows (Command Prompt)
```cmd
# Activate virtual environment
venv\Scripts\activate

# Test imports
python -c "import cv2; print('✅ OpenCV works')"
python -c "import numpy; print('✅ NumPy works')"

# Launch app
launch.bat
```

## macOS / Linux (Terminal)
```bash
# Activate virtual environment
source venv/bin/activate

# Test imports
python3 -c "import cv2; print('✅ OpenCV works')"
python3 -c "import numpy; print('✅ NumPy works')"

# Launch app
./launch.sh
```

---

---

# ❓ Troubleshooting

## "Python not found" / "python: command not found"

**Windows:**
- Check "Add Python to PATH" during installation
- Restart Command Prompt after installing Python
- Try: `python3` instead of `python`

**macOS/Linux:**
- Try: `python3.12` instead of `python3`
- Check: `which python3` (should show Python path)

**Fix:**
```bash
# Find Python location
which python3        # macOS/Linux
where python         # Windows
```

---

## "Virtual environment already exists, skipping..."

This is normal! It means setup ran before. Continue - it will install dependencies.

---

## "ModuleNotFoundError: No module named 'cv2'"

Virtual environment not activated:

**Windows:**
```cmd
venv\Scripts\activate
python -m pip install opencv-python
```

**macOS/Linux:**
```bash
source venv/bin/activate
pip install opencv-python
```

---

## "Permission denied: ./setup.sh"

Make it executable:

```bash
chmod +x setup.sh
chmod +x launch.sh
./setup.sh
```

---

## "git: command not found"

Install Git:

**Ubuntu/Debian:**
```bash
sudo apt install -y git
```

**Fedora/RHEL:**
```bash
sudo dnf install -y git
```

**macOS:**
```bash
brew install git
```

**Windows:**
Download from https://git-scm.com/download/win

---

## "Cannot find venv/Scripts/activate.bat"

Setup didn't complete. Run setup again:

**Windows:**
```cmd
setup.bat
```

**macOS/Linux:**
```bash
./setup.sh
```

---

## "Port 5000 already in use"

Another application is using port 5000. Either:

1. Close the other application using port 5000
2. Wait for it to timeout (5-10 minutes)
3. Or use a different port:

```bash
python3 launch.py --port 5001
```

---

## "Connection refused" / "Cannot connect to database"

Delete the database and let setup recreate it:

```bash
# macOS/Linux
rm -rf ~/.protectlayer/data/progress.db

# Windows (Command Prompt)
del %USERPROFILE%\.protectlayer\data\progress.db
```

Then run setup again.

---

## Still Having Issues?

1. **Check Python version:**
   - Should be 3.8 or higher
   - `python --version`

2. **Check disk space:**
   - Need at least 500 MB free
   - `df -h` (macOS/Linux)

3. **Check internet connection:**
   - Setup needs to download dependencies
   - Try running setup again if interrupted

4. **Report issues:**
   - https://github.com/ireallydumb/protectlayer-edu/issues
   - Include your OS and the error message

---

---

# 🎯 Next Steps

Once installation is complete:

1. **Read QUICK_START.md:** `cat QUICK_START.md`
2. **Launch the app:** `./launch.sh` (macOS/Linux) or `launch.bat` (Windows)
3. **Start Layer 1:** Select option `1` from the menu
4. **Begin tutorial:** Select option `2` to run the tutorial
5. **Track progress:** Check progress anytime from menu option `P`

---

# 📝 System Requirements Summary

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.12+ |
| RAM | 2 GB | 4 GB+ |
| Disk | 500 MB | 1 GB |
| OS | Windows 10+ / macOS 10.14+ / Ubuntu 20.04+ | Latest versions |

---

# ✅ Installation Checklist

After installation, verify:

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Setup completed without errors
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Launcher works (`./launch.sh` or `launch.bat`)
- [ ] Menu appears when launched
- [ ] Can select layers

**All checked? You're ready to learn! 🎓**

---

## Need Help?

- **Installation issues?** Check the Troubleshooting section above
- **Feature requests?** Open an issue on GitHub
- **Have questions?** Check FAQ.md
- **Legal questions?** See DISCLAIMER.md

**Happy learning! 🚀**
