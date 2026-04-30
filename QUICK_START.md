# ⚡ Quick Start Guide

Get ProtectLayer up and running in 2 minutes!

> **No extra software needed!** ProtectLayer is self-contained. OBS is optional (only for Advanced 4-8 week path).

## Step 1: Setup (One Time)

**For detailed OS-specific instructions, see [docs/INSTALLATION.md](docs/INSTALLATION.md)**

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/ireallydumb/protectlayer-edu.git
cd protectlayer-edu

# Run setup (handles everything)
chmod +x setup.sh
./setup.sh
```

**Windows users:** Use `setup.bat` instead

The setup script will:
- ✅ Check your Python installation
- ✅ Create a virtual environment
- ✅ Install all dependencies
- ✅ Set up your student profile
- ✅ Initialize your progress database

**Takes ~3 minutes. Run it once, then you're done!**

---

## Step 2: Launch the App

Once setup is complete, launching is **super easy**:

### 🐧 Linux / 🍎 macOS
```bash
./launch.sh
```

### 🪟 Windows
```bash
launch.bat
```

### Any Platform
```bash
python3 launch.py
```

**That's it!** You'll see an interactive menu.

---

## What You Get

Once launched, you'll see an interactive menu:

```
============================================================
  ProtectLayer - Welcome, [Your Name]!
============================================================

📚 LEARNING LAYERS:
  1️⃣  Layer 1: Detection (Content identification)
  2️⃣  Layer 2: Visible Protection (Watermarks)
  3️⃣  Layer 3: Invisible Protection (Steganography)
  4️⃣  Layer 4: Device Protection (Fingerprinting)
  5️⃣  Layer 5: Advanced Protection (Enterprise)

🔧 TOOLS:
  D   View Documentation
  P   View Progress
  S   Show Student Profile
  Q   Quit
```

From here you can:
- 📖 **Start learning** - Pick a layer and run the tutorial
- 📊 **Track progress** - See what you've completed
- 📚 **Read docs** - View any documentation
- 👤 **View profile** - Check your student ID

## Do I Need OBS or External Software?

**NO!** ProtectLayer is fully self-contained:

| Path | Duration | External Tools | Details |
|------|----------|---|---|
| **Beginner** | 2-3 hours | ✅ **None** | Pure Python, learn concepts |
| **Intermediate** | 1-2 weeks | ✅ **None** | Python + hands-on building |
| **Advanced** | 4-8 weeks | ⚠️ OBS optional | Only if building OBS plugins |

**Start with Beginner or Intermediate - zero extra downloads!**

---

## Example: Start Learning

1. Launch: `./launch.sh`
2. Enter: `1`
3. Choose: `2` (Run tutorial)
4. **Start learning!** 🎓

The tutorial will guide you through Layer 1 concepts with hands-on challenges.

---

## Start a Specific Layer (Advanced)

Want to jump to a specific layer directly?

```bash
# Layer 1: Detection
cd layers/layer1_detection
python3 tutorial.py

# View documentation
cat README.md
```

Each layer has:
- 📖 **README.md** - Overview and concepts
- 🎓 **tutorial.py** - Interactive learning
- 💪 **challenges/** - Practical exercises
- 💡 **examples/** - Code examples
- 📁 **projects/** - Build your own

---

## Troubleshooting

For comprehensive troubleshooting:
- 📖 See **[docs/INSTALLATION.md](docs/INSTALLATION.md)** Troubleshooting section
- 🆘 Common issues:
  - "Python not found" → Install Python 3.8+
  - "Permission denied" → `chmod +x setup.sh launch.sh`
  - "Virtual env not found" → Run `./setup.sh` first
  - "Module not found" → Activate venv: `source venv/bin/activate`

---

## What's Next?

1. **Complete setup** - `./setup.sh`
2. **Launch app** - `./launch.sh` (or `launch.bat`)
3. **Choose Layer 1** - Start with detection basics
4. **Work through tutorial** - Learn by doing
5. **Track your progress** - Check stats anytime

---

## Key Features

✅ **Super Easy Launch** - Just `./launch.sh`
✅ **Interactive Menu** - No command line needed
✅ **Progress Tracking** - All data stored locally
✅ **No Accounts** - No signup required
✅ **Completely Free** - MIT Licensed

---

## Tips

- 💾 Your progress is saved automatically
- 🔒 All data is stored on your computer only
- 📱 You can launch from anywhere in the project
- 🚀 Layers build on each other - start with Layer 1
- 📖 Each layer has documentation - read the README first

---

## Installation by OS

For complete step-by-step instructions:

- **[📖 Full Installation Guide](docs/INSTALLATION.md)**
  - 🪟 Windows instructions
  - 🍎 macOS instructions  
  - 🐧 Linux instructions (Ubuntu, Fedora, Arch)
  - ❓ Troubleshooting

---

## Quick OS Commands

**Linux/macOS:**
```bash
git clone https://github.com/ireallydumb/protectlayer-edu.git
cd protectlayer-edu
chmod +x setup.sh launch.sh
./setup.sh
./launch.sh
```

**Windows (Command Prompt):**
```cmd
git clone https://github.com/ireallydumb/protectlayer-edu.git
cd protectlayer-edu
setup.bat
launch.bat
```

---

**Ready? Start with setup.sh or setup.bat! 🚀**
