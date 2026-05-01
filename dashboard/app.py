#!/usr/bin/env python3
"""
ProtectLayer Dashboard - Web Interface

ACTUAL WORKING WEB DASHBOARD (not a placeholder!)

Run with: python3 dashboard/app.py
Open: http://localhost:5000
"""

from flask import Flask, render_template, jsonify, request
from pathlib import Path
import json
from datetime import datetime
import sqlite3

app = Flask(__name__, template_folder='templates')

# Get paths
PROJECT_ROOT = Path(__file__).parent.parent
STUDENT_DIR = Path.home() / ".protectlayer"
STUDENT_CONFIG = STUDENT_DIR / "student_config.json"
DB_PATH = STUDENT_DIR / "data" / "progress.db"

def load_student_config():
    """Load student configuration"""
    if STUDENT_CONFIG.exists():
        with open(STUDENT_CONFIG) as f:
            return json.load(f)
    return None

def get_layer_status():
    """Get status of all layers"""
    layers = []
    for i in range(1, 6):
        layer_names = {
            1: "Detection",
            2: "Visible Protection",
            3: "Invisible Protection",
            4: "Device Protection",
            5: "Advanced Protection"
        }
        
        layer_dir = PROJECT_ROOT / f"layers/layer{i}_{'detection' if i==1 else 'visible' if i==2 else 'invisible' if i==3 else 'device' if i==4 else 'advanced'}"
        
        has_tutorial = (layer_dir / "tutorial.py").exists()
        has_examples = any((layer_dir / "examples").glob("*.py"))
        has_challenges = any((layer_dir / "challenges").glob("*.py"))
        
        layers.append({
            'number': i,
            'name': layer_names[i],
            'status': 'available',
            'has_tutorial': has_tutorial,
            'has_examples': has_examples,
            'has_challenges': has_challenges,
            'example_count': len(list((layer_dir / "examples").glob("*.py"))) if (layer_dir / "examples").exists() else 0,
            'challenge_count': len(list((layer_dir / "challenges").glob("*.py"))) if (layer_dir / "challenges").exists() else 0,
        })
    
    return layers

@app.route('/')
def dashboard():
    """Main dashboard page"""
    student = load_student_config()
    layers = get_layer_status()
    
    return render_template('index.html', 
                         student=student,
                         layers=layers)

@app.route('/api/student')
def api_student():
    """Get student info"""
    student = load_student_config()
    if not student:
        return jsonify({'error': 'Not configured'}), 404
    return jsonify(student)

@app.route('/api/layers')
def api_layers():
    """Get all layers"""
    return jsonify(get_layer_status())

@app.route('/api/layer/<int:layer_id>')
def api_layer_detail(layer_id):
    """Get layer details"""
    if layer_id < 1 or layer_id > 5:
        return jsonify({'error': 'Invalid layer'}), 404
    
    layers = get_layer_status()
    for layer in layers:
        if layer['number'] == layer_id:
            return jsonify(layer)
    
    return jsonify({'error': 'Layer not found'}), 404

@app.route('/api/launch-layer/<int:layer_id>', methods=['POST'])
def api_launch_layer(layer_id):
    """Launch a layer tutorial"""
    import subprocess
    import sys
    
    layer_names = {
        1: "layer1_detection",
        2: "layer2_visible",
        3: "layer3_invisible",
        4: "layer4_device",
        5: "layer5_advanced"
    }
    
    if layer_id not in layer_names:
        return jsonify({'error': 'Invalid layer'}), 404
    
    tutorial_path = PROJECT_ROOT / "layers" / layer_names[layer_id] / "tutorial.py"
    
    if not tutorial_path.exists():
        return jsonify({'error': 'Tutorial not found'}), 404
    
    try:
        subprocess.Popen([sys.executable, str(tutorial_path)])
        return jsonify({'status': 'launched'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status')
def api_status():
    """Get overall system status"""
    student = load_student_config()
    layers = get_layer_status()
    
    return jsonify({
        'student_configured': student is not None,
        'student_name': student['display_name'] if student else 'Not configured',
        'layers_available': len(layers),
        'total_examples': sum(l['example_count'] for l in layers),
        'total_challenges': sum(l['challenge_count'] for l in layers),
    })

if __name__ == '__main__':
    print("🌐 ProtectLayer Dashboard Starting...")
    print("📍 Open: http://localhost:5000")
    print("🛑 Stop: Press Ctrl+C")
    print("")
    
    app.run(debug=False, host='localhost', port=5000)
