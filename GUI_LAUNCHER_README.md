# ProtectLayer GUI Launcher

**Easy, click-to-launch interface - No command line needed!**

## Quick Start (All Platforms)

### Easiest Way: Run GUI Launcher
```bash
python3 gui_launcher.py
```

Then just **click buttons** to:
- Choose which layer to learn
- View documentation
- Verify installation
- Get help

## Platform-Specific Instructions

### 🪟 Windows - Create Desktop Shortcut

1. Open Command Prompt in the protectlayer-edu folder
2. Run:
   ```cmd
   create_shortcut_windows.bat
   ```
3. Look for **ProtectLayer.lnk** on your Desktop
4. **Double-click** to launch

### 🍎 macOS - Create App

1. Open Terminal in the protectlayer-edu folder
2. Run:
   ```bash
   chmod +x create_app_macos.sh
   ./create_app_macos.sh
   ```
3. Look for **ProtectLayer.app** in ~/Applications
4. **Double-click** to launch

### 🐧 Linux

1. In the project directory, run:
   ```bash
   python3 gui_launcher.py
   ```
   OR create a desktop shortcut pointing to `gui_launcher.py`

## What the GUI Does

### 🎯 Main Menu
- **5 Layer Buttons** - Click to start any layer
- **📖 Documentation** - View README, FAQ, Installation guides
- **✅ Verify Installation** - Check if everything is installed correctly
- **❓ Help** - Get quick help and information

### 🎓 Choose a Layer
Each layer has:
- ✅ Interactive tutorial
- 📚 Example code
- 💪 Challenges to practice
- 🎯 Projects to build

### 📖 View Docs
Access without leaving the app:
- README.md
- QUICK_START.md
- Installation guide
- FAQ
- Ethics document

### ✅ Verify Installation
Checks:
- Python version
- All 5 layers present
- Required packages (NumPy, OpenCV)
- Documentation files

## Features

### ✨ User-Friendly
- No command line needed
- Click buttons to navigate
- Clean, dark theme interface
- Helpful status messages

### 🎯 Integrated
- Launch tutorials directly
- Read docs in app
- Verify installation
- Get help without leaving

### 🔧 Smart
- Checks installation on startup
- Verifies files exist
- Shows helpful error messages
- Guides users to solutions

## System Requirements

**Same as ProtectLayer:**
- Python 3.8+
- tkinter (included with Python on most systems)
- 2 GB RAM
- 500 MB disk space

## Troubleshooting

### GUI Won't Launch
```bash
# Make sure Python is installed
python3 --version

# Try running from command line
python3 gui_launcher.py

# Check for Python path issues
which python3
```

### Missing tkinter
On some Linux systems, tkinter needs to be installed separately:

```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS (should be included with Python)
# If missing: brew install python-tk
```

### Shortcut Not Working (Windows)
- Make sure Python is in your PATH
- Try running `python gui_launcher.py` from command line first
- Check that project directory hasn't moved

## Usage Workflow

1. **Launch GUI**
   ```bash
   python3 gui_launcher.py
   ```

2. **Check Installation**
   - Click "✅ Verify Installation"
   - Make sure everything is green

3. **Choose a Layer**
   - Start with "🔍 Layer 1: Content Detection"
   - Click to launch tutorial

4. **Learn & Practice**
   - Follow tutorial
   - Try examples
   - Complete challenges
   - Build projects

5. **Progress**
   - Move to next layer
   - Repeat until you reach Layer 5

6. **Capstone**
   - Complete final project
   - Build enterprise system
   - Graduate! 🎓

## Advanced

### Launch Specific Layer Programmatically
```python
import subprocess
import sys

subprocess.Popen([sys.executable, "layers/layer2_visible/tutorial.py"])
```

### Customize GUI
Edit `gui_launcher.py` to:
- Change colors (look for `#1e1e1e`, `#00ff00`, etc.)
- Add new buttons
- Change layout
- Add more features

### Create Custom Launcher
You can extend `gui_launcher.py` to:
- Add progress tracking
- Store user preferences
- Create student profiles
- Generate certificates

## Features Coming Soon

💭 Potential enhancements:
- Progress bar showing completion
- Student name registration
- Challenge auto-grading
- Certificate generation
- Dark/Light theme toggle
- Video tutorial links
- Community features

## What Makes This Easy

### No CLI Knowledge Needed
- Just click buttons
- No typing commands
- No memorizing syntax
- Intuitive interface

### Self-Contained
- No external dependencies (except Python)
- Uses tkinter (built-in)
- Works offline
- No internet required

### User-Friendly
- Clear error messages
- Helpful status updates
- Quick links to docs
- Easy troubleshooting

## Alternatives

If you prefer command line:
```bash
# Terminal launcher
./launch.sh          # macOS/Linux
launch.bat           # Windows
python3 launch.py    # Any platform
```

## Support

Having trouble?
- Read: `docs/FAQ.md`
- Check: `docs/INSTALLATION.md`
- Help: `❓ Help` button in GUI
- Issues: GitHub issues page

---

**ProtectLayer GUI Launcher - Learn DRM Protection the Easy Way!** 🚀
