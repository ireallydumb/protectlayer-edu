#!/usr/bin/env python3
"""
Layer 4: Device Protection - INTERACTIVE TUTORIAL
Learn device fingerprinting and hardware binding

This tutorial covers:
1. Unique device identification
2. Fingerprint generation
3. Device binding
4. Spoofing detection
5. Trust scoring
"""

import sys

class Layer4Tutorial:
    """Interactive Device Protection Tutorial"""
    
    def __init__(self):
        self.completed = []
    
    def intro(self):
        """Introduction to Layer 4"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 4: Device Protection - Interactive Tutorial         ║
║                                                                ║
║   Learn to identify and authenticate devices (Fingerprinting) ║
╚════════════════════════════════════════════════════════════════╝

Welcome to Layer 4!

Layers 1-3 protected CONTENT (images, watermarks, hidden data).
Layer 4 protects DEVICES (hardware, computers, phones).

THE QUESTION:
"Is this the SAME device as before?"

DEVICE FINGERPRINTING:
Creating a unique ID for a specific computer/phone.

WHY IT MATTERS:
  ✅ License management (software tied to device)
  ✅ Security (verify device hasn't been tampered)
  ✅ Anti-piracy (prevent unauthorized use)
  ✅ Fraud detection (identify stolen credentials)
  ✅ Hardware binding (DRM that works on one device)

THE CHALLENGE:
Devices change! Updates, new hardware, etc.
Need fingerprints that are:
  ✅ Stable (survive updates)
  ✅ Unique (identify each device)
  ❌ Not too specific (survive minor changes)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU'LL LEARN:
  ✅ Device identification methods
  ✅ Fingerprint generation
  ✅ Fingerprint comparison
  ✅ Device matching algorithms
  ✅ Spoofing detection
  ✅ Trust scoring

TIME: ~40 minutes
DIFFICULTY: Intermediate → Advanced

Let's start!
        """)
    
    def exercise_1_device_properties(self):
        """Exercise 1: Extract device properties"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 1: Device Properties - What Makes a Device Unique?  ║
╚════════════════════════════════════════════════════════════════╝

UNIQUE DEVICE PROPERTIES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hostname: Device name on network
  Stable: Usually doesn't change ✅
  Unique: Different per device ✅
  Example: "MacBook-Pro-2024"

MAC Address: Network card identifier
  Stable: Hardcoded into hardware ✅
  Unique: Globally unique ✅
  Example: "A1:B2:C3:D4:E5:F6"

Platform: OS and version
  Stable: Survives updates ⚠️
  Unique: Shared with many devices ❌
  Example: "Darwin 23.0" (macOS)

CPU Model: Processor type
  Stable: Never changes ✅
  Unique: Shared with similar devices ⚠️
  Example: "Intel Core i7-1234U"

Disk Serial: Hard drive identifier
  Stable: Hardcoded ✅
  Unique: Per physical drive ✅
  Example: "QWERTYUIOPASDFGH"

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import platform
import socket
import uuid
import os

def get_device_info():
    '''Extract device properties'''
    
    info = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'release': platform.release(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'cpu_count': os.cpu_count(),
        'uuid': str(uuid.getnode()),  # MAC-based UUID
        'python_version': platform.python_version(),
    }
    
    return info

# USE IT:
# info = get_device_info()
# for key, value in info.items():
#     print(f"{key}: {value}")

YOUR TURN:
1. Create device_info.py with code above
2. Run it
3. Look at YOUR device properties
4. Try on another computer/VM
5. See what changes and what stays same

✅ WHAT YOU LEARNED:
  • Device property extraction
  • Stability assessment (stable vs. changing)
  • Uniqueness evaluation
  • Sources of fingerprint data
        """)
        
        input("\nPress Enter when you've tried Exercise 1...")
        self.completed.append("Exercise 1: Device Properties")
    
    def exercise_2_fingerprint_generation(self):
        """Exercise 2: Generate device fingerprints"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 2: Fingerprint Generation - Create Device ID        ║
╚════════════════════════════════════════════════════════════════╝

THE PROCESS:
1. Collect device properties
2. Combine them into a string
3. Hash them (create a fixed-length fingerprint)
4. Result: Unique device ID

WHY HASHING?
  • Fingerprints are deterministic (same input = same output)
  • Fixed length (SHA256 = 64 characters always)
  • One-way (can't reverse-engineer device info)
  • Collision-resistant (virtually no duplicates)

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import hashlib
import platform
import socket
import uuid
import json

def generate_fingerprint():
    '''Generate device fingerprint'''
    
    # Collect properties
    data = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'uuid': str(uuid.getnode()),
    }
    
    # Create deterministic string
    string = '|'.join(
        f"{k}={v}" for k, v in sorted(data.items())
    )
    
    # Hash it
    fingerprint = hashlib.sha256(
        string.encode()
    ).hexdigest()
    
    return {
        'data': data,
        'string': string,
        'fingerprint': fingerprint,
        'short_id': fingerprint[:16]  # First 16 chars
    }

# USE IT:
# fp = generate_fingerprint()
# print(f"Device ID: {fp['short_id']}")
# print(f"Full fingerprint: {fp['fingerprint']}")

YOUR TURN:
1. Create fingerprint_gen.py with code above
2. Run it multiple times
3. Fingerprint should be IDENTICAL each time
4. Run on different device
5. Should be DIFFERENT (unless identical computer)

KEY PROPERTY:
  Deterministic = Same input always gives same output
  This is crucial for device identification!

✅ WHAT YOU LEARNED:
  • Deterministic hashing
  • Fingerprint generation
  • Stability vs. uniqueness tradeoff
  • Creating device IDs
        """)
        
        input("\nPress Enter when you've tried Exercise 2...")
        self.completed.append("Exercise 2: Fingerprint Generation")
    
    def exercise_3_device_binding(self):
        """Exercise 3: Bind content to device"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║  EXERCISE 3: Device Binding - Lock Content to a Device         ║
╚════════════════════════════════════════════════════════════════╝

THE GOAL:
Make software/content only work on SPECIFIC devices.

HOW IT WORKS:
1. Generate device fingerprint
2. Embed fingerprint in software/license
3. When running, check: "Is this the registered device?"
4. If no: Refuse to run (license tied to device)

USE CASE:
Company A sells software license.
License includes device fingerprint of buyer's computer.
If copied to another computer = License check fails!

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import hashlib

def create_device_license(hardware_fingerprint, 
                         software_id, 
                         expiration_date):
    '''Create a device-bound license'''
    
    license_data = {
        'hardware_fingerprint': hardware_fingerprint,
        'software_id': software_id,
        'expiration': expiration_date,
        'created': str(__import__('datetime').datetime.now())
    }
    
    # Sign the license (prevent tampering)
    license_string = '|'.join(
        f"{k}={v}" for k, v in license_data.items()
    )
    
    signature = hashlib.sha256(
        license_string.encode()
    ).hexdigest()
    
    return {
        'license_data': license_data,
        'signature': signature
    }

def verify_license(license_obj, current_fingerprint):
    '''Verify license is valid for this device'''
    
    # Check device match
    if license_obj['license_data']['hardware_fingerprint'] != current_fingerprint:
        return False, "Device mismatch"
    
    # Check expiration
    import datetime
    exp_date = datetime.datetime.fromisoformat(
        license_obj['license_data']['expiration']
    )
    
    if datetime.datetime.now() > exp_date:
        return False, "License expired"
    
    # Verify signature hasn't been tampered
    # ... signature verification code ...
    
    return True, "License valid"

YOUR TURN:
1. Create device_binding.py with code above
2. Generate a fingerprint
3. Create a license for it
4. Verify on same device (should pass)
5. Modify fingerprint slightly (should fail)

RESULT:
You now understand license binding!

✅ WHAT YOU LEARNED:
  • Device binding concept
  • License generation
  • License verification
  • Expiration management
  • Tamper detection
        """)
        
        input("\nPress Enter when you've tried Exercise 3...")
        self.completed.append("Exercise 3: Device Binding")
    
    def exercise_4_spoofing_detection(self):
        """Exercise 4: Detect spoofed fingerprints"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║  EXERCISE 4: Spoofing Detection - Is This Really That Device?  ║
╚════════════════════════════════════════════════════════════════╝

THE THREAT:
Attacker tries to FAKE a device fingerprint.

TECHNIQUES:
  • Change hostname (easy)
  • Spoof MAC address (medium)
  • Fake CPU info (medium)
  • VM detection evasion (hard)
  • Hardware emulation (very hard)

DETECTION STRATEGY:
Compare fingerprints across sessions:
  • Same device = fingerprint unchanged
  • Spoofed device = fingerprints don't match

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def detect_spoofing(previous_fp, current_fp):
    '''Detect if device was spoofed/faked'''
    
    # Exact match = legitimate
    if previous_fp == current_fp:
        return False, "Device fingerprint matches", 100
    
    # Field-by-field comparison
    prev_data = previous_fp['data']
    curr_data = current_fp['data']
    
    matching_fields = 0
    total_fields = len(prev_data)
    
    suspicious_changes = []
    
    for field in prev_data:
        if prev_data[field] == curr_data.get(field):
            matching_fields += 1
        else:
            suspicious_changes.append(
                f"{field}: {prev_data[field]} → {curr_data[field]}"
            )
    
    match_percent = (matching_fields / total_fields) * 100
    
    if match_percent >= 75:
        # Minor changes (updates, etc.)
        return False, "Device likely legitimate", match_percent
    else:
        # Major changes (suspicious!)
        return True, f"Spoofing detected! {suspicious_changes}", match_percent

YOUR TURN:
1. Create spoofing_detection.py
2. Generate a fingerprint
3. "Spoof" it by changing a field
4. Run detection
5. See if spoofing is detected

SPOOFING ATTEMPTS:
  Try changing:
  • hostname (easy, usually detected)
  • platform (hard, breaks things)
  • UUID (easy, easy to detect)

✅ WHAT YOU LEARNED:
  • Fingerprint stability analysis
  • Change detection
  • Anomaly identification
  • Trust scoring
        """)
        
        input("\nPress Enter when you've tried Exercise 4...")
        self.completed.append("Exercise 4: Spoofing Detection")
    
    def summary(self):
        """Summary of Layer 4"""
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 4: DEVICE PROTECTION - SUMMARY                      ║
╚════════════════════════════════════════════════════════════════╝

CONGRATULATIONS! You've completed Layer 4

EXERCISES COMPLETED:
        """)
        
        for i, exercise in enumerate(self.completed, 1):
            print(f"  {i}. ✅ {exercise}")
        
        print(f"""
KEY SKILLS MASTERED:
  ✅ Device property extraction
  ✅ Fingerprint generation
  ✅ Device binding
  ✅ Spoofing detection
  ✅ Trust scoring

YOU CAN NOW:
  • Create unique device identifiers
  • Bind software to specific devices
  • Detect tampering/spoofing
  • Implement device-based licensing
  • Prevent unauthorized access

REAL-WORLD APPLICATIONS:
  • Software licensing (one device only)
  • Mobile device management
  • Security compliance (tied to device)
  • Fraud prevention
  • Digital rights management

LIMITATIONS:
  • Fingerprints can be spoofed with effort
  • Legitimate changes break verification
  • Privacy concerns (device tracking)
  • Not 100% reliable alone

NEXT: Layer 5 - Cryptographic Signing & Verification

Ready to learn cryptography and digital signatures?
Run: python3 ../layer5_advanced/tutorial.py
        """)
    
    def run(self):
        """Run the complete tutorial"""
        self.intro()
        
        input("\nPress Enter to begin Exercise 1...")
        self.exercise_1_device_properties()
        
        input("\nPress Enter to begin Exercise 2...")
        self.exercise_2_fingerprint_generation()
        
        input("\nPress Enter to begin Exercise 3...")
        self.exercise_3_device_binding()
        
        input("\nPress Enter to begin Exercise 4...")
        self.exercise_4_spoofing_detection()
        
        input("\nPress Enter to see summary...")
        self.summary()

if __name__ == "__main__":
    tutorial = Layer4Tutorial()
    tutorial.run()
