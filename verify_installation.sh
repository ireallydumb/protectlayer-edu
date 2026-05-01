#!/bin/bash
# verify_installation.sh - ProtectLayer Installation Verification Script

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                        ║"
echo "║          ProtectLayer Installation Verification Script                ║"
echo "║                                                                        ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

PASS=0
FAIL=0
WARNINGS=0

check_command() {
    if command -v "$1" &> /dev/null; then
        echo "✅ $2"
        ((PASS++))
        return 0
    else
        echo "❌ $2 ($1 not found)"
        ((FAIL++))
        return 1
    fi
}

check_python_module() {
    if python3 -c "import $1" 2>/dev/null; then
        echo "✅ $2"
        ((PASS++))
        return 0
    else
        echo "❌ $2 (module $1 not found)"
        ((FAIL++))
        return 1
    fi
}

check_file() {
    if [ -f "$1" ]; then
        echo "✅ $2"
        ((PASS++))
        return 0
    else
        echo "❌ $2 (file not found: $1)"
        ((FAIL++))
        return 1
    fi
}

check_directory() {
    if [ -d "$1" ]; then
        echo "✅ $2"
        ((PASS++))
        return 0
    else
        echo "❌ $2 (directory not found: $1)"
        ((FAIL++))
        return 1
    fi
}

echo "SYSTEM CHECKS"
echo "─────────────────────────────────────────────────────────────────────────"
check_command "python3" "Python 3 installed"
check_command "git" "Git installed"
check_command "bash" "Bash shell available"

echo ""
echo "PYTHON ENVIRONMENT"
echo "─────────────────────────────────────────────────────────────────────────"
check_directory "venv" "Virtual environment exists"

if [ -d "venv" ]; then
    # Try to activate and check
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        check_python_module "numpy" "NumPy package"
        check_python_module "cv2" "OpenCV (cv2) package"
        check_python_module "PIL" "Pillow (PIL) package"
        deactivate 2>/dev/null || true
    fi
fi

echo ""
echo "PROJECT FILES"
echo "─────────────────────────────────────────────────────────────────────────"
check_file "README.md" "README.md exists"
check_file "QUICK_START.md" "QUICK_START.md exists"
check_file "requirements.txt" "requirements.txt exists"
check_file "launch.py" "launch.py exists"
check_file "setup.sh" "setup.sh exists"

echo ""
echo "LAYER STRUCTURE"
echo "─────────────────────────────────────────────────────────────────────────"
check_directory "layers/layer1_detection" "Layer 1 directory"
check_file "layers/layer1_detection/tutorial.py" "Layer 1 tutorial"
check_directory "layers/layer2_visible" "Layer 2 directory"
check_file "layers/layer2_visible/tutorial.py" "Layer 2 tutorial"
check_directory "layers/layer3_invisible" "Layer 3 directory"
check_file "layers/layer3_invisible/tutorial.py" "Layer 3 tutorial"
check_directory "layers/layer4_device" "Layer 4 directory"
check_file "layers/layer4_device/tutorial.py" "Layer 4 tutorial"
check_directory "layers/layer5_advanced" "Layer 5 directory"
check_file "layers/layer5_advanced/tutorial.py" "Layer 5 tutorial"

echo ""
echo "DOCUMENTATION"
echo "─────────────────────────────────────────────────────────────────────────"
check_file "docs/INSTALLATION.md" "Installation guide"
check_file "docs/FAQ.md" "FAQ document"
check_file "docs/ETHICS.md" "Ethics document"
check_file "docs/DISCLAIMER.md" "Disclaimer"

echo ""
echo "STUDENT DATABASE"
echo "─────────────────────────────────────────────────────────────────────────"
if [ -d "$HOME/.protectlayer" ]; then
    echo "✅ Student directory exists"
    ((PASS++))
else
    echo "⚠️  Student directory not created (will be created on first run)"
    ((WARNINGS++))
fi

echo ""
echo "═════════════════════════════════════════════════════════════════════════"
echo ""
echo "RESULTS"
echo "─────────────────────────────────────────────────────────────────────────"
echo "✅ Passed:   $PASS"
echo "❌ Failed:   $FAIL"
echo "⚠️  Warnings: $WARNINGS"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "═════════════════════════════════════════════════════════════════════════"
    echo ""
    echo "✅ INSTALLATION VERIFIED!"
    echo ""
    echo "Your ProtectLayer installation is complete and ready to use."
    echo ""
    echo "Next steps:"
    echo "  1. Launch the application:"
    echo "     ./launch.sh        (macOS/Linux)"
    echo "     launch.bat         (Windows)"
    echo "     python3 launch.py  (Any platform)"
    echo ""
    echo "  2. Start learning:"
    echo "     Select Layer 1 from the menu"
    echo ""
    echo "═════════════════════════════════════════════════════════════════════════"
    exit 0
else
    echo "═════════════════════════════════════════════════════════════════════════"
    echo ""
    echo "❌ INSTALLATION INCOMPLETE"
    echo ""
    echo "Some files or dependencies are missing."
    echo ""
    echo "To fix:"
    echo "  1. Run: ./setup.sh"
    echo "  2. Run this verification again"
    echo ""
    echo "═════════════════════════════════════════════════════════════════════════"
    exit 1
fi
