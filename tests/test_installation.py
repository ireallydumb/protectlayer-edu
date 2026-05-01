#!/usr/bin/env python3
"""
Installation Test Suite

Verifies all critical components are installed and working.

Run with: python3 -m pytest tests/
Or: python3 tests/test_installation.py
"""

import sys
from pathlib import Path

def test_python_version():
    """Test Python 3.8+"""
    assert sys.version_info >= (3, 8), f"Python 3.8+ required, got {sys.version_info}"
    print("✅ Python version check passed")

def test_imports():
    """Test critical packages"""
    packages = ['numpy', 'cv2', 'PIL', 'sqlite3']
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"✅ {pkg} import successful")
        except ImportError:
            raise AssertionError(f"Missing package: {pkg}")

def test_directory_structure():
    """Test required directories exist"""
    required_dirs = [
        'layers/layer1_detection',
        'layers/layer2_visible',
        'layers/layer3_invisible',
        'layers/layer4_device',
        'layers/layer5_advanced',
        'docs',
    ]
    for d in required_dirs:
        assert Path(d).exists(), f"Missing directory: {d}"
        print(f"✅ Directory exists: {d}")

def test_layer_files():
    """Test all layer files exist"""
    for i in range(1, 6):
        layer_paths = list(Path('layers').glob(f'layer{i}_*'))
        assert len(layer_paths) > 0, f"Layer {i} not found"
        print(f"✅ Layer {i} exists")

def test_documentation():
    """Test documentation files"""
    docs = [
        'README.md',
        'QUICK_START.md',
        'docs/INSTALLATION.md',
        'docs/FAQ.md',
    ]
    for doc in docs:
        assert Path(doc).exists(), f"Missing: {doc}"
        print(f"✅ {doc} exists")

if __name__ == "__main__":
    try:
        test_python_version()
        test_imports()
        test_directory_structure()
        test_layer_files()
        test_documentation()
        print("\n✅ ALL TESTS PASSED!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
