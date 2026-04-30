# Frequently Asked Questions (FAQ)

Got questions? You probably aren't alone. Check here first!

---

## 🎯 Getting Started

### Q: Do I need OBS Studio installed?
**A:** **No!** OBS is completely optional.

- **Beginner Path** (2-3 hours) - ✅ Zero external tools
- **Intermediate Path** (1-2 weeks) - ✅ Zero external tools
- **Advanced Path** (4-8 weeks) - ⚠️ OBS plugin part only (optional)

You can complete 90% of ProtectLayer without OBS. Start with Beginner or Intermediate!

---

### Q: Do I need to pay for anything?
**A:** **No!** ProtectLayer is 100% free and open source (MIT License).

- ✅ Free to download
- ✅ Free to use
- ✅ Free to modify
- ✅ No accounts required
- ✅ No sign-ups
- ✅ No hidden costs

---

### Q: What operating systems are supported?
**A:** All major OSes:

- ✅ Windows 10 and later
- ✅ macOS 10.14 and later
- ✅ Linux (Ubuntu, Debian, Fedora, Arch, etc.)

See [docs/INSTALLATION.md](INSTALLATION.md) for OS-specific setup.

---

### Q: How long does installation take?
**A:** About **2-5 minutes** total:

1. Download Python (if needed) - 2-3 min
2. Clone repo - 1 min
3. Run setup - 1-2 min
4. Done!

Most of the time is downloading dependencies over the network.

---

### Q: Do I need administrator/sudo access?
**A:** Usually **no**, but it helps.

- Windows: Not required
- macOS: Needed for Homebrew (to install Python)
- Linux: Needed for apt/dnf/pacman (to install Python)

You can install Python to your home directory to avoid admin access.

---

## 💻 System Requirements

### Q: What are the minimum system requirements?
**A:** Very modest:

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 / macOS 10.14 / Ubuntu 20.04 | Latest versions |
| **Python** | 3.8 | 3.12+ |
| **RAM** | 2 GB | 4+ GB |
| **Disk** | 500 MB | 1 GB |
| **CPU** | Any modern processor | Intel i5+/AMD Ryzen 5+ |

Most laptops from the last 10 years work fine.

---

### Q: Can I run this on a Raspberry Pi?
**A:** **Probably not well.** 

- Raspberry Pi OS is ARM-based
- Installing OpenCV on ARM is tricky
- Performance would be very slow

Better to use a laptop or desktop. If you really want to try: https://github.com/opencv-python-headless

---

### Q: How much disk space does it use?
**A:** About **500 MB - 1 GB**:

- Repository: ~50 MB
- Virtual environment: ~400 MB (Python packages)
- Your progress data: <1 MB
- Test content: ~50 MB (optional)

You can delete the `venv/` folder anytime to free up space (just run setup again).

---

### Q: Can I run this on a work/school computer?
**A:** **Probably yes**, but check:

- ✅ Do you have Python installation permissions?
- ✅ Does your network allow downloading from GitHub?
- ⚠️ Some corporate firewalls block installations

If restricted, ask your IT department or use your personal computer instead.

---

## 🎓 Learning & Paths

### Q: Which learning path should I choose?
**A:** Depends on your experience:

- **🟢 Beginner** - New to security, 2-3 hours, no coding required
- **🟡 Intermediate** - Python developer, 1-2 weeks, hands-on building
- **🔴 Advanced** - Expert programmer, 4-8 weeks, production systems

**If unsure, start with Beginner!** You can always do more.

---

### Q: Can I skip layers?
**A:** Not recommended. Each layer builds on the previous.

- Layer 1 teaches core concepts (detection)
- Layer 2 uses Layer 1 (visible protection)
- Layer 3 uses Layers 1-2 (invisible protection)
- Layer 4 uses 1-3 (device protection)
- Layer 5 uses everything (advanced)

**Better to go in order, but you can review Layer 1 concepts later if needed.**

---

### Q: How much time does each layer take?
**A:** Intermediate path estimates:

| Layer | Theory | Code | Testing | Total |
|-------|--------|------|---------|-------|
| 1 | 30 min | 1.5h | 30 min | **2.5h** |
| 2 | 45 min | 2h | 45 min | **3.5h** |
| 3 | 1h | 2.5h | 1h | **4.5h** |
| 4 | 1h | 3h | 1.5h | **5.5h** |
| 5 | 1.5h | 4h | 2h | **7.5h** |

**Total: ~23 hours** for intermediate path

---

### Q: Can I do layers at my own pace?
**A:** **Absolutely!** ProtectLayer is 100% self-paced.

- Work whenever you want (evenings, weekends, etc.)
- Take breaks anytime
- Resume later without losing progress
- Your progress is saved automatically

---

### Q: Can I switch learning paths?
**A:** **Yes!** You can:

- Start with Beginner, switch to Intermediate later ✅
- Start with Intermediate, skip Beginner ✅
- Do different paths for different layers ✅
- Review earlier layers anytime ✅

---

### Q: What if I get stuck on a challenge?
**A:** Several options:

1. **Read the README** - Explains concepts
2. **Check examples/** - Working reference code
3. **Read the comments** - Code explains itself
4. **Move on** - Come back later with fresh eyes
5. **Ask for help** - GitHub Issues/Discussions

---

## 🔧 Technical Questions

### Q: Is there a web dashboard?
**A:** The current version has an **interactive terminal menu** (`launch.sh` / `launch.bat`).

A web dashboard is planned for a future version. For now, the terminal launcher is clean and works everywhere.

---

### Q: Can I run this in Docker?
**A:** **Not yet**, but it's a great idea! 

You can Docker-ize it yourself. Dockerfile would be:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "launch.py"]
```

Contributions welcome! Open an issue on GitHub.

---

### Q: Can I use this in a classroom/university?
**A:** **Yes!** ProtectLayer is designed for education.

- ✅ Teach security concepts
- ✅ Hands-on learning
- ✅ Individual progress tracking
- ✅ Open source (modify as needed)
- ✅ No licensing issues

Suggest to your instructor/professor!

---

### Q: Can I contribute code?
**A:** **Yes!** See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

Welcome contributions:
- Bug fixes
- New challenges
- Documentation improvements
- New layers/features
- Translation to other languages

---

## 🔐 Privacy & Security

### Q: Where is my progress data stored?
**A:** **Only on your computer**, locally.

- Windows: `C:\Users\[Your Name]\.protectlayer\`
- macOS/Linux: `~/.protectlayer/`

Nothing is sent to servers or external services.

---

### Q: Is my data safe?
**A:** **Yes**, it's just SQLite on your computer.

- No internet connection needed
- No cloud sync
- No accounts
- No tracking
- You own your data

---

### Q: Will you ever require an account?
**A:** **No.** ProtectLayer is offline-first by design.

Accounts would require servers, which requires privacy policies, which requires trust. We prefer local-only.

---

### Q: Can I delete my data?
**A:** **Anytime.** Just delete the `.protectlayer` folder:

```bash
# macOS/Linux
rm -rf ~/.protectlayer

# Windows (Command Prompt)
rmdir /S %USERPROFILE%\.protectlayer
```

Then run setup again to start fresh.

---

## ⚖️ Legal & Ethics

### Q: Is this legal to use?
**A:** **For education: yes.** See [DISCLAIMER.md](DISCLAIMER.md).

The law depends on your country:
- **USA**: Check DMCA rules
- **EU**: Check local laws
- **Canada/UK**: Similar to USA
- **Other countries**: Research your laws

ProtectLayer is designed for learning, not circumvention. Use responsibly.

---

### Q: Can I use this on content I don't own?
**A:** **No.** Only test on content you own or have permission for.

Legal rule: Don't circumvent protection on content you don't own.

---

### Q: Is this about piracy?
**A:** **No.** It's about understanding security.

Like studying locks doesn't make you a burglar. Learning security makes you understand it better.

---

### Q: Should I feel guilty learning this?
**A:** **No!** It's valid education.

Security professionals need to understand how systems work. That's how we build better protection.

---

## 🐛 Troubleshooting

### Q: I get "Python not found"
**A:** See [docs/INSTALLATION.md](INSTALLATION.md#python-not-found--python-command-not-found) troubleshooting section.

Quick fix:
```bash
# Check if Python is installed
python3 --version  # or 'python --version'

# If not, install from https://www.python.org/
```

---

### Q: "ModuleNotFoundError: No module named 'cv2'"
**A:** Virtual environment not activated or setup incomplete.

```bash
# macOS/Linux
source venv/bin/activate
pip install opencv-python

# Windows
venv\Scripts\activate
pip install opencv-python
```

---

### Q: Setup gets stuck
**A:** Usually network issues downloading dependencies.

Try again - it should resume. If it keeps failing:

```bash
# Delete venv and try again
rm -rf venv  # macOS/Linux
rmdir venv   # Windows
./setup.sh   # or setup.bat
```

---

### Q: Terminal menu doesn't work
**A:** Try running Python directly:

```bash
python3 launch.py
```

If that doesn't work, there's a dependency issue. Run setup again.

---

## 🚀 Advanced Questions

### Q: Can I modify the code?
**A:** **Absolutely!** It's MIT licensed.

- ✅ Modify for your needs
- ✅ Build on top of it
- ✅ Use in your project
- ✅ Share your changes

Just keep the MIT license header.

---

### Q: Can I use this commercially?
**A:** **Yes**, under MIT license.

Just include the license with your derivative work.

---

### Q: Can I hire someone to extend this?
**A:** **Yes!** That's what open source enables.

You can:
- Hire a developer to add features
- Publish your extensions
- Build a product on top of it
- All with MIT's blessing

---

### Q: What about Python 2.7?
**A:** **No.** Python 2 is dead.

We support Python 3.8+. If you have Python 2.7, upgrade! It's free.

---

## 📞 Still Have Questions?

1. **Check this FAQ** (you're reading it!)
2. **Read [docs/INSTALLATION.md](INSTALLATION.md)** - Setup issues
3. **Read [CONTRIBUTING.md](../CONTRIBUTING.md)** - Contributing
4. **Read [DISCLAIMER.md](DISCLAIMER.md)** - Legal questions
5. **Check [ETHICS.md](ETHICS.md)** - Ethical considerations
6. **Open an issue** - https://github.com/ireallydumb/protectlayer-edu/issues
7. **Start a discussion** - https://github.com/ireallydumb/protectlayer-edu/discussions

---

## 🎓 Ready to Start?

1. Install: Follow [docs/INSTALLATION.md](INSTALLATION.md)
2. Launch: `./launch.sh` or `launch.bat`
3. Learn: Pick Layer 1
4. Enjoy! 🎉

**Questions? Ask on GitHub!**
