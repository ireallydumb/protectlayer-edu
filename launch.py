#!/usr/bin/env python3
"""
ProtectLayer - Easy Application Launcher
Run this to start learning or continue where you left off.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

class ProtectLayerLauncher:
    def __init__(self):
        self.home = Path.home()
        self.config_dir = self.home / ".protectlayer"
        self.config_file = self.config_dir / "student_config.json"
        self.project_root = Path(__file__).parent
        
    def ensure_setup(self):
        """Check if setup has been run"""
        if not self.config_file.exists():
            print("❌ Setup not complete. Run './setup.sh' first.")
            sys.exit(1)
    
    def load_config(self):
        """Load student configuration"""
        with open(self.config_file) as f:
            return json.load(f)
    
    def show_menu(self):
        """Display main menu"""
        config = self.load_config()
        
        print("\n" + "="*60)
        print(f"  ProtectLayer - Welcome, {config['display_name']}!")
        print("="*60 + "\n")
        
        print("📚 LEARNING LAYERS:")
        print("  1️⃣  Layer 1: Detection (Content identification)")
        print("  2️⃣  Layer 2: Visible Protection (Watermarks)")
        print("  3️⃣  Layer 3: Invisible Protection (Steganography)")
        print("  4️⃣  Layer 4: Device Protection (Fingerprinting)")
        print("  5️⃣  Layer 5: Advanced Protection (Enterprise)")
        print("\n🔧 TOOLS:")
        print("  D   View Documentation")
        print("  P   View Progress")
        print("  S   Show Student Profile")
        print("  Q   Quit")
        print("\n" + "-"*60)
    
    def open_layer(self, layer_num):
        """Open a specific layer"""
        layer_dir = self.project_root / f"layers" / f"layer{layer_num}_detection" if layer_num == 1 else f"layer{layer_num}_{'visible' if layer_num == 2 else 'invisible' if layer_num == 3 else 'device' if layer_num == 4 else 'advanced'}"
        
        # Correct mapping
        layer_names = {
            1: "layer1_detection",
            2: "layer2_visible", 
            3: "layer3_invisible",
            4: "layer4_device",
            5: "layer5_advanced"
        }
        
        layer_dir = self.project_root / "layers" / layer_names[layer_num]
        
        if not layer_dir.exists():
            print(f"❌ Layer {layer_num} directory not found: {layer_dir}")
            return
        
        tutorial = layer_dir / "tutorial.py"
        readme = layer_dir / "README.md"
        
        print(f"\n📂 Layer {layer_num} Contents:")
        
        if readme.exists():
            print(f"   ✅ README.md - Start here for overview")
        if tutorial.exists():
            print(f"   ✅ tutorial.py - Interactive tutorial")
        
        print(f"\n   📁 Full path: {layer_dir}\n")
        
        choice = input("What would you like to do?\n  1. View README\n  2. Run tutorial\n  3. Open folder\n  4. Back\nChoice: ").strip()
        
        if choice == "1" and readme.exists():
            self.show_file(readme)
        elif choice == "2" and tutorial.exists():
            print(f"\n▶️  Running tutorial.py...\n")
            subprocess.run([sys.executable, str(tutorial)], cwd=str(layer_dir))
        elif choice == "3":
            print(f"📂 Opening: {layer_dir}")
            if sys.platform == "darwin":  # macOS
                subprocess.run(["open", str(layer_dir)])
            elif sys.platform == "win32":  # Windows
                os.startfile(str(layer_dir))
            else:  # Linux
                subprocess.run(["xdg-open", str(layer_dir)])
    
    def show_file(self, filepath):
        """Display file contents"""
        try:
            with open(filepath) as f:
                content = f.read()
            
            # Simple pagination for long files
            lines = content.split('\n')
            for i, line in enumerate(lines):
                print(line)
                if (i + 1) % 30 == 0 and i < len(lines) - 1:
                    response = input("\n--- More (press Enter to continue, 'q' to quit) ---\n")
                    if response.lower() == 'q':
                        break
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    
    def show_progress(self):
        """Show learning progress"""
        config = self.load_config()
        
        print("\n" + "="*60)
        print(f"  📊 YOUR PROGRESS")
        print("="*60 + "\n")
        
        print(f"Student ID: {config['student_id']}")
        print(f"Name: {config['display_name']}")
        print(f"Member since: {config['created_at'][:10]}\n")
        
        db_path = self.config_dir / "data" / "progress.db"
        if db_path.exists():
            try:
                import sqlite3
                conn = sqlite3.connect(str(db_path))
                cursor = conn.cursor()
                
                # Get layer progress
                cursor.execute("""
                    SELECT layer, status, time_spent FROM layer_progress 
                    ORDER BY layer
                """)
                
                print("Layer Status:")
                for layer, status, time_spent in cursor.fetchall():
                    status_emoji = "✅" if status == "COMPLETED" else "🔄" if status == "IN_PROGRESS" else "⏳"
                    print(f"  {status_emoji} Layer {layer}: {status} ({time_spent//60}h {time_spent%60}m)")
                
                # Get challenge stats
                cursor.execute("SELECT COUNT(*), SUM(passed) FROM challenge_progress")
                total, passed = cursor.fetchone()
                if total:
                    print(f"\nChallenges: {passed}/{total} completed ({int(passed*100/total)}%)")
                
                conn.close()
            except Exception as e:
                print(f"(No progress data yet - complete a challenge to track progress)")
        else:
            print("(No progress data yet - start with Layer 1!)")
        
        print()
    
    def show_profile(self):
        """Show student profile"""
        config = self.load_config()
        
        print("\n" + "="*60)
        print(f"  👤 YOUR PROFILE")
        print("="*60 + "\n")
        
        print(f"Display Name: {config['display_name']}")
        print(f"Student ID:   {config['student_id']}")
        print(f"Created:      {config['created_at'][:10]}")
        print(f"Config File:  {self.config_file}")
        print(f"\nℹ️  Your data is stored locally only at: {self.config_dir}")
        print("   Nothing is sent to external servers.\n")
    
    def run(self):
        """Main launcher loop"""
        self.ensure_setup()
        
        while True:
            self.show_menu()
            choice = input("Select option: ").strip().upper()
            
            if choice in ["1", "2", "3", "4", "5"]:
                self.open_layer(int(choice))
            elif choice == "D":
                readme = self.project_root / "README.md"
                if readme.exists():
                    self.show_file(readme)
            elif choice == "P":
                self.show_progress()
            elif choice == "S":
                self.show_profile()
            elif choice == "Q":
                print("\n👋 Thanks for learning with ProtectLayer! Keep coding!\n")
                break
            else:
                print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    launcher = ProtectLayerLauncher()
    launcher.run()
