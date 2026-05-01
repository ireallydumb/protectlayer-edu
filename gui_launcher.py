#!/usr/bin/env python3
"""
ProtectLayer GUI Launcher - Click to Learn!

A simple graphical interface for launching ProtectLayer without using
the command line. Just run this file and click to start learning.

Usage:
  Double-click this file (on Windows/macOS)
  Or: python3 gui_launcher.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
from pathlib import Path
import json
import webbrowser

class ProtectLayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ProtectLayer - Educational DRM System")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'), background="#1e1e1e", foreground="#00ff00")
        self.style.configure('Subtitle.TLabel', font=('Arial', 12), background="#1e1e1e", foreground="#cccccc")
        self.style.configure('Normal.TLabel', font=('Arial', 10), background="#1e1e1e", foreground="#ffffff")
        self.style.configure('Layer.TButton', font=('Arial', 11, 'bold'), padding=10)
        self.style.configure('Action.TButton', font=('Arial', 10), padding=8)
        
        self.setup_ui()
        self.check_installation()
        
    def setup_ui(self):
        """Create the user interface"""
        
        # Main frame with scrollbar
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = ttk.Label(main_frame, text="🎓 ProtectLayer", style='Title.TLabel')
        title.pack(pady=10)
        
        subtitle = ttk.Label(main_frame, text="Learn DRM Protection Mechanisms", style='Subtitle.TLabel')
        subtitle.pack(pady=5)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Loading...", style='Normal.TLabel')
        self.status_label.pack(pady=10)
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Layers section
        layers_label = ttk.Label(main_frame, text="Choose Your Learning Layer:", style='Subtitle.TLabel')
        layers_label.pack(pady=10)
        
        # Layer buttons
        layers_frame = ttk.Frame(main_frame)
        layers_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.layers = [
            ("Layer 1: Content Detection", "layer1_detection", "🔍"),
            ("Layer 2: Visible Protection", "layer2_visible", "🎨"),
            ("Layer 3: Invisible Protection", "layer3_invisible", "👻"),
            ("Layer 4: Device Protection", "layer4_device", "📱"),
            ("Layer 5: Advanced Protection", "layer5_advanced", "🔐"),
        ]
        
        for label, folder, emoji in self.layers:
            btn = ttk.Button(
                layers_frame,
                text=f"{emoji} {label}",
                command=lambda f=folder: self.launch_layer(f),
                style='Layer.TButton'
            )
            btn.pack(fill=tk.X, pady=8)
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Action buttons
        actions_frame = ttk.Frame(main_frame)
        actions_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            actions_frame,
            text="📖 Read Documentation",
            command=self.open_documentation,
            style='Action.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            actions_frame,
            text="✅ Verify Installation",
            command=self.verify_installation,
            style='Action.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            actions_frame,
            text="❓ Help",
            command=self.show_help,
            style='Action.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Footer
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill=tk.X, pady=20)
        
        footer = ttk.Label(
            footer_frame,
            text="ProtectLayer - Educational DRM System | Version 1.0",
            style='Normal.TLabel',
            justify=tk.CENTER
        )
        footer.pack()
    
    def check_installation(self):
        """Check if installation is complete"""
        required_layers = ['layer1_detection', 'layer2_visible', 'layer3_invisible', 'layer4_device', 'layer5_advanced']
        missing = []
        
        for layer in required_layers:
            layer_path = Path(f"layers/{layer}")
            if not layer_path.exists():
                missing.append(layer)
        
        if missing:
            self.status_label.config(text="⚠️  Some layers missing - Run setup.sh first")
            self.root.after(3000, lambda: messagebox.showwarning(
                "Installation Incomplete",
                "ProtectLayer setup not complete.\n\nPlease run setup.sh or setup.bat first."
            ))
        else:
            self.status_label.config(text="✅ Installation complete - Ready to learn!")
    
    def launch_layer(self, layer_folder):
        """Launch a specific layer"""
        tutorial_path = Path(f"layers/{layer_folder}/tutorial.py")
        
        if not tutorial_path.exists():
            messagebox.showerror("Not Found", f"Tutorial not found for {layer_folder}")
            return
        
        try:
            # Launch tutorial in new window
            subprocess.Popen([sys.executable, str(tutorial_path)])
            messagebox.showinfo("Launched", "Tutorial started!\n\nCheck the new window.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch tutorial:\n{e}")
    
    def open_documentation(self):
        """Open documentation files"""
        doc_window = tk.Toplevel(self.root)
        doc_window.title("Documentation")
        doc_window.geometry("600x400")
        
        # Center on parent
        doc_window.transient(self.root)
        doc_window.grab_set()
        
        docs = [
            ("README", "README.md"),
            ("Quick Start", "QUICK_START.md"),
            ("Installation", "docs/INSTALLATION.md"),
            ("FAQ", "docs/FAQ.md"),
            ("Ethics", "docs/ETHICS.md"),
        ]
        
        frame = ttk.Frame(doc_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Documentation", font=('Arial', 16, 'bold')).pack(pady=10)
        
        for label, path in docs:
            def open_file(p=path):
                try:
                    with open(p) as f:
                        content = f.read()
                    
                    text_window = tk.Toplevel(self.root)
                    text_window.title(label)
                    text_window.geometry("700x500")
                    
                    text = tk.Text(text_window, wrap=tk.WORD, bg="#1e1e1e", fg="#ffffff")
                    text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                    text.insert('1.0', content)
                    text.config(state=tk.DISABLED)
                    
                    # Scrollbar
                    scrollbar = ttk.Scrollbar(text_window, command=text.yview)
                    text['yscrollcommand'] = scrollbar.set
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                except FileNotFoundError:
                    messagebox.showerror("Not Found", f"File not found: {p}")
            
            ttk.Button(
                frame,
                text=f"📄 {label}",
                command=open_file
            ).pack(fill=tk.X, pady=5)
    
    def verify_installation(self):
        """Verify installation"""
        checks = {
            "Python version": sys.version_info >= (3, 8),
            "Layer 1": Path("layers/layer1_detection").exists(),
            "Layer 2": Path("layers/layer2_visible").exists(),
            "Layer 3": Path("layers/layer3_invisible").exists(),
            "Layer 4": Path("layers/layer4_device").exists(),
            "Layer 5": Path("layers/layer5_advanced").exists(),
            "README": Path("README.md").exists(),
            "Documentation": Path("docs/INSTALLATION.md").exists(),
        }
        
        # Try imports
        try:
            import cv2
            checks["OpenCV"] = True
        except:
            checks["OpenCV"] = False
        
        try:
            import numpy
            checks["NumPy"] = True
        except:
            checks["NumPy"] = False
        
        result_text = "Installation Verification Results:\n\n"
        all_passed = True
        
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            result_text += f"{status} {check}\n"
            if not passed:
                all_passed = False
        
        if all_passed:
            messagebox.showinfo("Verification Passed", result_text + "\n✅ Installation is complete!")
        else:
            messagebox.showwarning("Verification Failed", result_text + "\n⚠️  Some components missing.\nRun setup.sh to complete installation.")
    
    def show_help(self):
        """Show help information"""
        help_text = """
ProtectLayer - Educational DRM System

GETTING STARTED:
1. Choose a layer above to start learning
2. Complete tutorials and challenges
3. Build projects to practice skills
4. Progress through all 5 layers

LAYERS:
🔍 Layer 1: Content Detection
   Learn how to identify and tag content

🎨 Layer 2: Visible Protection  
   Add watermarks and quality degradation

👻 Layer 3: Invisible Protection
   Hide data with steganography

📱 Layer 4: Device Protection
   Fingerprint and verify devices

🔐 Layer 5: Advanced Protection
   Enterprise-grade cryptography

FEATURES:
• Interactive tutorials for each layer
• Working code examples
• Practice challenges
• Capstone projects
• Complete documentation

REQUIREMENTS:
• Python 3.8+
• OpenCV (cv2)
• NumPy
• PIL (Pillow)

For more help:
• Read documentation (📖 button above)
• Check FAQ.md
• See INSTALLATION.md for troubleshooting

Enjoy learning! 🚀
        """
        messagebox.showinfo("Help", help_text)

def main():
    """Main entry point"""
    root = tk.Tk()
    
    # Set dark theme colors
    root.configure(bg="#1e1e1e")
    
    app = ProtectLayerGUI(root)
    
    # Run GUI
    root.mainloop()

if __name__ == "__main__":
    main()
