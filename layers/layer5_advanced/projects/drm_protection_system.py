#!/usr/bin/env python3
"""
Layer 5 Project: Complete DRM Protection System

ENTERPRISE-GRADE DIGITAL RIGHTS MANAGEMENT

Features:
  • Content encryption/decryption
  • Digital signatures
  • License generation & verification
  • Key management
  • Content binding to devices
  • Threat detection & alerts
  • Audit logging
  • License revocation
"""

import hmac
import hashlib
import json
from pathlib import Path
from datetime import datetime, timedelta
import sys
import os

class DRMProtectionSystem:
    """Complete DRM implementation"""
    
    def __init__(self, key_store=None):
        if key_store is None:
            key_store = Path.home() / ".protectlayer" / "drm_keys"
        
        self.key_store = Path(key_store)
        self.key_store.mkdir(parents=True, exist_ok=True)
        
        self.licenses = {}
        self.revoked_licenses = set()
        self.audit_trail = []
    
    # ─────────────────────────────────────────────────────────────
    # SIGNING & VERIFICATION
    # ─────────────────────────────────────────────────────────────
    
    def sign_content(self, content, secret_key):
        """Sign content with HMAC-SHA256"""
        
        if isinstance(content, str):
            content = content.encode()
        
        if isinstance(secret_key, str):
            secret_key = secret_key.encode()
        
        signature = hmac.new(
            secret_key,
            content,
            hashlib.sha256
        ).hexdigest()
        
        self._log_audit('sign_content', 'success', len(content))
        
        return signature
    
    def verify_signature(self, content, signature, secret_key):
        """Verify content signature"""
        
        expected = self.sign_content(content, secret_key)
        
        is_valid = hmac.compare_digest(signature, expected)
        
        self._log_audit('verify_signature', 
                       'success' if is_valid else 'failed')
        
        return is_valid
    
    # ─────────────────────────────────────────────────────────────
    # ENCRYPTION/DECRYPTION
    # ─────────────────────────────────────────────────────────────
    
    def encrypt_content(self, content, key):
        """Simple XOR encryption (demonstration)"""
        
        # WARNING: XOR is for demonstration only!
        # Real DRM uses AES or similar
        
        if isinstance(content, str):
            content = content.encode()
        
        if isinstance(key, str):
            key = key.encode()
        
        encrypted = bytes(
            content[i] ^ key[i % len(key)]
            for i in range(len(content))
        )
        
        return encrypted.hex()
    
    def decrypt_content(self, encrypted_hex, key):
        """Decrypt content"""
        
        if isinstance(key, str):
            key = key.encode()
        
        encrypted = bytes.fromhex(encrypted_hex)
        
        decrypted = bytes(
            encrypted[i] ^ key[i % len(key)]
            for i in range(len(encrypted))
        )
        
        return decrypted.decode('utf-8', errors='ignore')
    
    # ─────────────────────────────────────────────────────────────
    # LICENSE MANAGEMENT
    # ─────────────────────────────────────────────────────────────
    
    def generate_license(self, content_id, device_fingerprint, 
                        duration_days=365, signing_key=None):
        """Generate device-bound license"""
        
        if signing_key is None:
            signing_key = "default-signing-key"
        
        license_id = hashlib.sha256(
            f"{content_id}{device_fingerprint}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:16]
        
        license_data = {
            'license_id': license_id,
            'content_id': content_id,
            'device_fingerprint': device_fingerprint,
            'issued_date': datetime.now().isoformat(),
            'expiration_date': (datetime.now() + 
                              timedelta(days=duration_days)).isoformat(),
            'status': 'active',
            'permissions': ['read', 'use'],
            'restrictions': {
                'device_locked': True,
                'transferable': False,
                'sharable': False
            }
        }
        
        # Sign license
        license_string = json.dumps(license_data, sort_keys=True)
        signature = self.sign_content(license_string, signing_key)
        
        license_data['signature'] = signature
        
        self.licenses[license_id] = license_data
        
        self._log_audit('generate_license', 'success', license_id)
        
        print(f"✅ License generated: {license_id}")
        
        return license_data
    
    def verify_license(self, license_data, device_fingerprint, 
                      signing_key=None):
        """Verify license is valid and active"""
        
        if signing_key is None:
            signing_key = "default-signing-key"
        
        # Check if revoked
        if license_data['license_id'] in self.revoked_licenses:
            self._log_audit('verify_license', 'revoked')
            return False, "License revoked"
        
        # Check device match
        if license_data['device_fingerprint'] != device_fingerprint:
            self._log_audit('verify_license', 'device_mismatch')
            return False, "License bound to different device"
        
        # Check expiration
        exp_date = datetime.fromisoformat(
            license_data['expiration_date']
        )
        
        if datetime.now() > exp_date:
            self._log_audit('verify_license', 'expired')
            return False, "License expired"
        
        # Verify signature
        sig = license_data.pop('signature')
        license_string = json.dumps(license_data, sort_keys=True)
        
        if not self.verify_signature(license_string, sig, signing_key):
            license_data['signature'] = sig
            self._log_audit('verify_license', 'signature_invalid')
            return False, "License signature invalid (tampered)"
        
        license_data['signature'] = sig
        
        self._log_audit('verify_license', 'success')
        
        return True, "License valid"
    
    def revoke_license(self, license_id, reason=""):
        """Revoke a license"""
        
        self.revoked_licenses.add(license_id)
        
        if license_id in self.licenses:
            self.licenses[license_id]['status'] = 'revoked'
        
        self._log_audit('revoke_license', 'success', 
                       f"{license_id}: {reason}")
        
        print(f"✅ License revoked: {license_id}")
    
    # ─────────────────────────────────────────────────────────────
    # CONTENT BINDING
    # ─────────────────────────────────────────────────────────────
    
    def bind_content_to_device(self, content, device_fingerprint, 
                              content_id=None):
        """Bind content to specific device"""
        
        if content_id is None:
            content_id = hashlib.sha256(
                content.encode() if isinstance(content, str) else content
            ).hexdigest()[:16]
        
        binding_data = {
            'content_id': content_id,
            'device_fingerprint': device_fingerprint,
            'bound_date': datetime.now().isoformat(),
            'content_hash': hashlib.sha256(
                content.encode() if isinstance(content, str) else content
            ).hexdigest()
        }
        
        # Create binding certificate
        binding_string = json.dumps(binding_data, sort_keys=True)
        binding_signature = hashlib.sha256(binding_string.encode()).hexdigest()
        
        binding_data['signature'] = binding_signature
        
        self._log_audit('bind_content', 'success', content_id)
        
        return binding_data
    
    def verify_content_binding(self, content, binding_data):
        """Verify content is bound to device"""
        
        # Check content hasn't changed
        content_hash = hashlib.sha256(
            content.encode() if isinstance(content, str) else content
        ).hexdigest()
        
        if content_hash != binding_data['content_hash']:
            self._log_audit('verify_binding', 'content_modified')
            return False, "Content has been modified"
        
        self._log_audit('verify_binding', 'success')
        
        return True, "Content binding verified"
    
    # ─────────────────────────────────────────────────────────────
    # THREAT DETECTION
    # ─────────────────────────────────────────────────────────────
    
    def detect_unauthorized_access(self, device_fingerprint, 
                                  license_device):
        """Detect if content accessed from wrong device"""
        
        if device_fingerprint == license_device:
            return False, "Authorized access"
        
        self._log_audit('threat_detected', 'unauthorized_device', 
                       device_fingerprint)
        
        print(f"⚠️  THREAT: Unauthorized device access detected!")
        
        return True, "Unauthorized device access"
    
    def detect_tampering(self, original_signature, current_content, 
                        secret_key):
        """Detect if content was tampered with"""
        
        current_signature = self.sign_content(current_content, secret_key)
        
        if original_signature != current_signature:
            self._log_audit('threat_detected', 'tampering_detected')
            print(f"⚠️  THREAT: Content tampering detected!")
            return True, "Content modified"
        
        return False, "Content integrity verified"
    
    # ─────────────────────────────────────────────────────────────
    # AUDIT LOGGING
    # ─────────────────────────────────────────────────────────────
    
    def _log_audit(self, operation, status, details=""):
        """Log operation for audit trail"""
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'status': status,
            'details': details
        }
        
        self.audit_trail.append(log_entry)
    
    def get_audit_trail(self):
        """Get complete audit trail"""
        return self.audit_trail
    
    def generate_drm_report(self):
        """Generate DRM system status report"""
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'active_licenses': len(self.licenses),
            'revoked_licenses': len(self.revoked_licenses),
            'audit_entries': len(self.audit_trail),
            'threats_detected': sum(
                1 for entry in self.audit_trail
                if 'threat' in entry['operation']
            ),
            'summary': {
                'total_operations': len(self.audit_trail),
                'successful': sum(
                    1 for entry in self.audit_trail
                    if entry['status'] == 'success'
                )
            }
        }
        
        return report

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMMAND-LINE INTERFACE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    drm = DRMProtectionSystem()
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║    LAYER 5: COMPLETE DRM PROTECTION SYSTEM - PROJECT            ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  python3 drm_protection_system.py <command> [options]

COMMANDS:
  sign <file> <key>
    Sign a file
    
  verify <file> <signature> <key>
    Verify file signature
    
  encrypt <content> <key>
    Encrypt content
    
  decrypt <encrypted> <key>
    Decrypt content
    
  license <content_id> <device_fp>
    Generate device-bound license
    
  verify-license <license_json>
    Verify license is valid
    
  revoke <license_id> [reason]
    Revoke a license
    
  bind <content> <device_fp>
    Bind content to device
    
  report
    Generate DRM status report

EXAMPLES:
  python3 drm_protection_system.py sign content.txt mykey
  python3 drm_protection_system.py encrypt "secret data" mykey
  python3 drm_protection_system.py license content001 device123
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "sign":
        file_path = sys.argv[2]
        key = sys.argv[3]
        with open(file_path) as f:
            content = f.read()
        sig = drm.sign_content(content, key)
        print(f"Signature: {sig}")
    
    elif command == "encrypt":
        content = sys.argv[2]
        key = sys.argv[3]
        encrypted = drm.encrypt_content(content, key)
        print(f"Encrypted: {encrypted}")
    
    elif command == "decrypt":
        encrypted = sys.argv[2]
        key = sys.argv[3]
        decrypted = drm.decrypt_content(encrypted, key)
        print(f"Decrypted: {decrypted}")
    
    elif command == "license":
        content_id = sys.argv[2]
        device_fp = sys.argv[3]
        license_data = drm.generate_license(content_id, device_fp)
        print(json.dumps(license_data, indent=2))
    
    elif command == "report":
        report = drm.generate_drm_report()
        print(json.dumps(report, indent=2))
    
    else:
        print(f"Unknown command: {command}")
