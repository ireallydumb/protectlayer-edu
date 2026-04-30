#!/bin/bash

set -e

# ============================================================================
# ProtectLayer Educational DRM System - Setup Script
# ============================================================================

VERSION="1.0"
REPO_URL="https://github.com/ireallydumb/protectlayer-edu.git"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ============================================================================
# FUNCTIONS
# ============================================================================

print_header() {
    clear
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                                                                            ║${NC}"
    echo -e "${BLUE}║                   ProtectLayer Educational System v${VERSION}                  ║${NC}"
    echo -e "${BLUE}║                         Setup & Installation                               ║${NC}"
    echo -e "${BLUE}║                                                                            ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_section() {
    echo -e "\n${BLUE}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

show_disclaimer() {
    echo ""
    echo -e "${RED}╔════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║                         ⚠️  LEGAL DISCLAIMER ⚠️                            ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "This is an EDUCATIONAL TOOL ONLY for learning about content protection."
    echo ""
    echo -e "${YELLOW}IMPORTANT:${NC}"
    echo ""
    echo "• Circumventing copy protection on content you don't own may be ILLEGAL"
    echo "• You are responsible for your use of this software"
    echo "• The creators assume NO LIABILITY for misuse"
    echo "• You must comply with all applicable laws in your jurisdiction"
    echo "• See docs/DISCLAIMER.md for complete legal terms"
    echo ""
    
    read -p "Do you agree to these terms and accept full responsibility? (yes/no): " response
    
    if [[ "$response" != "yes" ]]; then
        print_error "Setup cancelled. You must agree to the terms to continue."
        exit 1
    fi
    
    print_success "Terms accepted"
}

detect_os() {
    OS="$(uname -s)"
    case "$OS" in
        Linux*)     OS_TYPE="Linux";;
        Darwin*)    OS_TYPE="MacOS";;
        MINGW*)     OS_TYPE="MinGw";;
        *)          OS_TYPE="UNKNOWN";;
    esac
    echo "$OS_TYPE"
}

check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 not found"
        echo "Please install Python 3.8 or higher from https://www.python.org/"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    print_success "Python $PYTHON_VERSION found"
}

create_venv() {
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists, skipping..."
    else
        print_section "Creating Python virtual environment"
        python3 -m venv venv
        print_success "Virtual environment created"
    fi
    
    # Activate venv
    if [[ "$OS_TYPE" == "MinGw" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
}

install_dependencies() {
    print_section "Installing dependencies"
    pip install -q --upgrade pip setuptools wheel
    pip install -q -r requirements.txt
    print_success "Dependencies installed"
}

setup_directories() {
    print_section "Setting up student workspace"
    mkdir -p ~/.protectlayer/students
    mkdir -p ~/.protectlayer/submissions
    mkdir -p ~/.protectlayer/data
    print_success "Workspace directories created"
}

initialize_database() {
    print_section "Initializing database"
    python3 << 'PYTHON'
from pathlib import Path
import json
import sqlite3

db_path = Path.home() / ".protectlayer" / "data" / "progress.db"
db_path.parent.mkdir(parents=True, exist_ok=True)

# Create database
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_info (
        id TEXT PRIMARY KEY,
        display_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_activity TIMESTAMP
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS layer_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        layer INTEGER,
        started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP NULL,
        time_spent INTEGER DEFAULT 0,
        status TEXT DEFAULT 'IN_PROGRESS',
        FOREIGN KEY(student_id) REFERENCES student_info(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS challenge_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        layer INTEGER,
        challenge_id TEXT,
        attempt_number INTEGER DEFAULT 1,
        passed BOOLEAN DEFAULT 0,
        time_taken INTEGER DEFAULT 0,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES student_info(id)
    )
""")

conn.commit()
conn.close()

print("Database initialized successfully")
PYTHON
    print_success "Database initialized"
}

generate_student_id() {
    print_section "Generating student profile"
    
    python3 << 'PYTHON'
import json
import secrets
from pathlib import Path
from datetime import datetime

config_dir = Path.home() / ".protectlayer"
config_file = config_dir / "student_config.json"

config_dir.mkdir(parents=True, exist_ok=True)

if config_file.exists():
    with open(config_file, 'r') as f:
        config = json.load(f)
    print(f"✅ Student profile already exists")
    print(f"   Student ID: {config['student_id']}")
else:
    # Generate ID
    student_id = f"student_{secrets.token_hex(16)}"
    
    # Get optional name
    display_name = input("\nOptional: Enter your name (or press Enter to skip): ").strip()
    
    # Create config
    config = {
        "student_id": student_id,
        "display_name": display_name if display_name else "Anonymous Learner",
        "created_at": datetime.now().isoformat(),
        "version": "1.0"
    }
    
    # Save config
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\n✅ Your Student ID: {student_id}")
    print(f"   Name: {config['display_name']}")
    print("   This is used to track your progress locally.")
    print("   (Your data is stored only on this computer)")
PYTHON
    
    print_success "Student profile created"
}

launch_dashboard() {
    echo ""
    print_section "Setup Complete! 🎉"
    echo ""
    echo -e "${GREEN}ProtectLayer is ready to use!${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Read the documentation:  ${BLUE}cat docs/LEARNING_PATHS.md${NC}"
    echo "  2. Start with Layer 1:      ${BLUE}cd layers/layer1_detection${NC}"
    echo "  3. Run the tutorial:        ${BLUE}python3 tutorial.py${NC}"
    echo "  4. View your progress:      ${BLUE}python3 dashboard/app.py${NC}"
    echo ""
    echo "Documentation:"
    echo "  - Learning Paths:  docs/LEARNING_PATHS.md"
    echo "  - FAQ:             docs/FAQ.md"
    echo "  - Legal:           docs/DISCLAIMER.md"
    echo ""
    
    read -p "Launch dashboard now? (yes/no): " launch_choice
    
    if [[ "$launch_choice" == "yes" ]]; then
        echo ""
        print_section "Launching Dashboard"
        echo "Opening http://localhost:5000..."
        echo "(Press Ctrl+C to stop)"
        python3 dashboard/app.py
    fi
}

# ============================================================================
# MAIN SETUP FLOW
# ============================================================================

main() {
    print_header
    
    show_disclaimer
    
    OS_TYPE=$(detect_os)
    print_section "System Detection"
    print_success "OS: $OS_TYPE"
    
    check_python
    
    create_venv
    
    install_dependencies
    
    setup_directories
    
    initialize_database
    
    generate_student_id
    
    launch_dashboard
}

# Run main function
main
