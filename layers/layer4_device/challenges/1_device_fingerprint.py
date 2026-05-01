#!/usr/bin/env python3
"""
Challenge 1.1: Create Unique Device Fingerprint

COMPLETE WORKING SOLUTION - STUDY & EXTEND IT!

Task: Create a unique, stable device ID that identifies this specific machine
"""

import hashlib
import platform
import socket
import uuid
import json
from pathlib import Path

def generate_device_fingerprint():
    """
    Generate a unique, stable device fingerprint.
    
    Combines:
    - Hostname
    - Platform (OS)
    - Processor
    - Machine type
    - MAC address (unique to network card)
    - CPU count
    
    Returns a stable hash that identifies THIS specific device.
    """
    
    fingerprint_data = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'release': platform.release(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'cpu_count': __import__('os').cpu_count(),
        'uuid': str(uuid.getnode()),  # MAC address based UUID
    }
    
    # Create deterministic string
    fingerprint_string = '|'.join(
        f"{k}={v}" for k, v in sorted(fingerprint_data.items())
    )
    
    # Create SHA256 hash
    device_hash = hashlib.sha256(fingerprint_string.encode()).hexdigest()
    
    return {
        'data': fingerprint_data,
        'hash': device_hash[:16],  # Use first 16 chars
        'full_hash': device_hash
    }

def save_fingerprint(filepath):
    """Save fingerprint to file for future reference"""
    fp = generate_device_fingerprint()
    
    with open(filepath, 'w') as f:
        json.dump(fp, f, indent=2)
    
    return fp

def load_fingerprint(filepath):
    """Load previously saved fingerprint"""
    with open(filepath) as f:
        return json.load(f)

def verify_device_match(fp1, fp2):
    """
    Verify if two fingerprints match (same device)
    
    Returns: (match: bool, similarity: float)
    """
    
    if fp1['full_hash'] == fp2['full_hash']:
        return True, 1.0
    
    # If exact match fails, compare key fields
    match_count = 0
    key_fields = ['hostname', 'machine', 'processor', 'uuid']
    
    for field in key_fields:
        if fp1['data'].get(field) == fp2['data'].get(field):
            match_count += 1
    
    similarity = match_count / len(key_fields)
    return similarity > 0.75, similarity  # 75%+ match = same device

# DEMO & TESTING
if __name__ == "__main__":
    print("Challenge 1.1: Device Fingerprinting - COMPLETE SOLUTION")
    print("")
    
    fp = generate_device_fingerprint()
    
    print("📱 DEVICE FINGERPRINT:")
    print(f"  Short ID: {fp['hash']}")
    print(f"  Full ID:  {fp['full_hash']}")
    print("")
    print("📊 DEVICE INFO:")
    for key, value in fp['data'].items():
        print(f"  {key}: {value}")
    print("")
    
    # Save and reload
    fp_file = Path.home() / ".protectlayer" / "device_fingerprint.json"
    fp_file.parent.mkdir(parents=True, exist_ok=True)
    
    saved_fp = save_fingerprint(fp_file)
    loaded_fp = load_fingerprint(fp_file)
    
    match, similarity = verify_device_match(saved_fp, loaded_fp)
    print(f"✅ Saved and loaded fingerprint match: {match} (similarity: {similarity*100:.0f}%)")
    print("")
    
    print("WHAT YOU LEARNED:")
    print("✅ How device fingerprinting works")
    print("✅ What makes a device unique")
    print("✅ How to verify device identity")
    print("✅ Stability vs. spoofing resistance")
    print("")
    
    print("CHALLENGE EXTENSIONS:")
    print("1. Add geolocation data")
    print("2. Implement fingerprint update logic")
    print("3. Detect device tampering")
    print("4. Create fingerprint database")
    print("5. Implement device trust scoring")
