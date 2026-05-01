#!/usr/bin/env python3
"""
Layer 4 Project: Device Verification System

PRODUCTION-QUALITY DEVICE FINGERPRINTING & VERIFICATION

Features:
  • Generate unique device fingerprints
  • Multi-device fingerprint database
  • Device matching and verification
  • Spoofing detection
  • Trust scoring (0-100%)
  • Certificate generation
  • Anomaly detection
  • Audit logging
"""

import hashlib
import platform
import socket
import uuid
import json
import os
from pathlib import Path
from datetime import datetime
import sys

class DeviceVerificationSystem:
    """Complete device verification implementation"""
    
    def __init__(self, db_file=None):
        if db_file is None:
            db_file = Path.home() / ".protectlayer" / "device_database.json"
        
        self.db_file = Path(db_file)
        self.db_file.parent.mkdir(parents=True, exist_ok=True)
        self.devices = self._load_database()
        self.audit_log = []
    
    # ─────────────────────────────────────────────────────────────
    # FINGERPRINT GENERATION
    # ─────────────────────────────────────────────────────────────
    
    def generate_fingerprint(self):
        """Generate unique device fingerprint"""
        
        data = {
            'hostname': socket.gethostname(),
            'platform': platform.system(),
            'release': platform.release(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'cpu_count': os.cpu_count(),
            'uuid': str(uuid.getnode()),
            'python_version': platform.python_version(),
        }
        
        # Create deterministic string
        fingerprint_string = '|'.join(
            f"{k}={v}" for k, v in sorted(data.items())
        )
        
        # Create hashes
        full_hash = hashlib.sha256(fingerprint_string.encode()).hexdigest()
        short_id = full_hash[:16]
        
        return {
            'data': data,
            'fingerprint_string': fingerprint_string,
            'full_hash': full_hash,
            'short_id': short_id,
            'timestamp': datetime.now().isoformat()
        }
    
    # ─────────────────────────────────────────────────────────────
    # DEVICE MANAGEMENT
    # ─────────────────────────────────────────────────────────────
    
    def register_device(self, device_name, fingerprint_dict=None):
        """Register a new device"""
        
        if fingerprint_dict is None:
            fingerprint_dict = self.generate_fingerprint()
        
        device_id = fingerprint_dict['short_id']
        
        device_record = {
            'device_id': device_id,
            'device_name': device_name,
            'fingerprint': fingerprint_dict,
            'registration_date': datetime.now().isoformat(),
            'last_seen': datetime.now().isoformat(),
            'verification_count': 0,
            'trust_score': 100,
            'status': 'active',
            'suspicious_activity': []
        }
        
        self.devices[device_id] = device_record
        self._save_database()
        
        self._log_audit('register', device_id, 'success')
        
        print(f"✅ Device registered: {device_name}")
        print(f"   ID: {device_id}")
        
        return device_id
    
    def list_devices(self):
        """List all registered devices"""
        
        print("\n" + "=" * 70)
        print("REGISTERED DEVICES")
        print("=" * 70)
        
        if not self.devices:
            print("No devices registered")
            return
        
        for device_id, device in self.devices.items():
            print(f"\nDevice: {device['device_name']}")
            print(f"  ID: {device_id}")
            print(f"  Status: {device['status']}")
            print(f"  Trust Score: {device['trust_score']}/100")
            print(f"  Verifications: {device['verification_count']}")
            print(f"  Registered: {device['registration_date'][:10]}")
            print(f"  Last Seen: {device['last_seen'][:10]}")
    
    def get_device(self, device_id):
        """Get device by ID"""
        return self.devices.get(device_id)
    
    # ─────────────────────────────────────────────────────────────
    # VERIFICATION
    # ─────────────────────────────────────────────────────────────
    
    def verify_device(self, current_fingerprint):
        """Verify current device against registered devices"""
        
        current_hash = current_fingerprint['full_hash']
        
        # Exact match
        if current_hash in [d['fingerprint']['full_hash'] 
                           for d in self.devices.values()]:
            for device_id, device in self.devices.items():
                if device['fingerprint']['full_hash'] == current_hash:
                    device['last_seen'] = datetime.now().isoformat()
                    device['verification_count'] += 1
                    self._save_database()
                    self._log_audit('verify', device_id, 'success')
                    return True, device_id, "Exact match"
        
        # Partial match (some fields changed)
        best_match = None
        best_score = 0
        
        for device_id, device in self.devices.items():
            match_score = self._compare_fingerprints(
                current_fingerprint,
                device['fingerprint']
            )
            
            if match_score > best_score:
                best_score = match_score
                best_match = (device_id, device, match_score)
        
        if best_score >= 0.75:  # 75% match
            device_id, device, score = best_match
            device['last_seen'] = datetime.now().isoformat()
            
            if score < 0.9:
                device['suspicious_activity'].append({
                    'timestamp': datetime.now().isoformat(),
                    'type': 'minor_change',
                    'match_score': score
                })
                device['trust_score'] -= 5
            
            self._save_database()
            self._log_audit('verify', device_id, 'partial_match', score)
            
            return True, device_id, f"Partial match ({score*100:.0f}%)"
        
        # No match
        self._log_audit('verify', 'unknown', 'failed')
        return False, None, "No matching device found"
    
    def _compare_fingerprints(self, fp1, fp2):
        """Compare two fingerprints, return similarity (0-1)"""
        
        data1 = fp1['data']
        data2 = fp2['data']
        
        matching = 0
        total = len(data1)
        
        for field in data1:
            if data1.get(field) == data2.get(field):
                matching += 1
        
        return matching / total
    
    # ─────────────────────────────────────────────────────────────
    # SPOOFING DETECTION
    # ─────────────────────────────────────────────────────────────
    
    def detect_spoofing(self, device_id, new_fingerprint):
        """Detect if device was spoofed/tampered"""
        
        device = self.devices.get(device_id)
        if not device:
            return False, "Device not found"
        
        old_fp = device['fingerprint']
        new_fp = new_fingerprint
        
        old_data = old_fp['data']
        new_data = new_fp['data']
        
        critical_fields = ['uuid', 'machine']  # Can't change
        major_changes = []
        minor_changes = []
        
        for field in critical_fields:
            if old_data.get(field) != new_data.get(field):
                major_changes.append(field)
        
        for field in old_data:
            if field not in critical_fields:
                if old_data.get(field) != new_data.get(field):
                    minor_changes.append(field)
        
        if major_changes:
            self._log_audit('spoofing_detected', device_id, 'critical', major_changes)
            device['status'] = 'suspicious'
            device['trust_score'] = 0
            return True, f"CRITICAL: {major_changes} changed!"
        
        if len(minor_changes) > 3:
            self._log_audit('spoofing_detected', device_id, 'warning', minor_changes)
            device['trust_score'] = max(0, device['trust_score'] - 20)
            return True, f"WARNING: Multiple changes detected"
        
        return False, "No spoofing detected"
    
    # ─────────────────────────────────────────────────────────────
    # TRUST SCORING
    # ─────────────────────────────────────────────────────────────
    
    def calculate_trust_score(self, device_id):
        """Calculate trust score (0-100)"""
        
        device = self.devices.get(device_id)
        if not device:
            return 0
        
        score = 100
        
        # Recent activity decreases trust slowly
        if device['verification_count'] < 5:
            score -= (5 - device['verification_count']) * 5
        
        # Suspicious activity
        suspicious_count = len(device['suspicious_activity'])
        score -= suspicious_count * 10
        
        # Status
        if device['status'] != 'active':
            score -= 50
        
        return max(0, min(100, score))
    
    # ─────────────────────────────────────────────────────────────
    # CERTIFICATE GENERATION
    # ─────────────────────────────────────────────────────────────
    
    def generate_certificate(self, device_id):
        """Generate device certificate"""
        
        device = self.devices.get(device_id)
        if not device:
            return None
        
        certificate = {
            'device_id': device_id,
            'device_name': device['device_name'],
            'fingerprint_hash': device['fingerprint']['full_hash'],
            'certificate_date': datetime.now().isoformat(),
            'expiration': (datetime.now() + 
                         __import__('datetime').timedelta(days=365)).isoformat(),
            'trust_score': device['trust_score'],
            'status': device['status']
        }
        
        # Sign certificate
        cert_string = json.dumps(certificate, sort_keys=True)
        signature = hashlib.sha256(cert_string.encode()).hexdigest()
        
        certificate['signature'] = signature
        
        self._log_audit('certificate_generated', device_id, 'success')
        
        return certificate
    
    # ─────────────────────────────────────────────────────────────
    # DATABASE MANAGEMENT
    # ─────────────────────────────────────────────────────────────
    
    def _load_database(self):
        """Load device database from file"""
        
        if self.db_file.exists():
            with open(self.db_file) as f:
                return json.load(f)
        return {}
    
    def _save_database(self):
        """Save device database to file"""
        
        with open(self.db_file, 'w') as f:
            json.dump(self.devices, f, indent=2)
    
    # ─────────────────────────────────────────────────────────────
    # AUDIT LOGGING
    # ─────────────────────────────────────────────────────────────
    
    def _log_audit(self, operation, device_id, status, details=None):
        """Log operation for audit trail"""
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'device_id': device_id,
            'status': status,
            'details': details
        }
        
        self.audit_log.append(log_entry)
        
        # Also save to file
        log_file = self.db_file.parent / "audit_log.json"
        
        logs = []
        if log_file.exists():
            with open(log_file) as f:
                logs = json.load(f)
        
        logs.append(log_entry)
        
        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)
    
    def get_audit_log(self):
        """Get full audit log"""
        return self.audit_log

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMMAND-LINE INTERFACE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    system = DeviceVerificationSystem()
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║  LAYER 4: DEVICE VERIFICATION SYSTEM - PROJECT                 ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  python3 device_verification_system.py <command> [options]

COMMANDS:
  fingerprint
    Generate fingerprint for this device
    
  register <name>
    Register this device with a name
    
  list
    List all registered devices
    
  verify
    Verify this device
    
  detect-spoofing <device_id>
    Check if device was spoofed
    
  certificate <device_id>
    Generate certificate for device

EXAMPLES:
  python3 device_verification_system.py fingerprint
  python3 device_verification_system.py register "My Laptop"
  python3 device_verification_system.py list
  python3 device_verification_system.py verify
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "fingerprint":
        fp = system.generate_fingerprint()
        print(json.dumps(fp, indent=2))
    
    elif command == "register":
        name = sys.argv[2] if len(sys.argv) > 2 else "Device"
        device_id = system.register_device(name)
    
    elif command == "list":
        system.list_devices()
    
    elif command == "verify":
        fp = system.generate_fingerprint()
        is_valid, device_id, message = system.verify_device(fp)
        print(f"Valid: {is_valid}")
        print(f"Device ID: {device_id}")
        print(f"Message: {message}")
    
    elif command == "certificate":
        device_id = sys.argv[2]
        cert = system.generate_certificate(device_id)
        if cert:
            print(json.dumps(cert, indent=2))
    
    else:
        print(f"Unknown command: {command}")
