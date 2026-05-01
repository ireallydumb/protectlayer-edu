#!/usr/bin/env python3
"""
Layer 4, Example 1: Device Fingerprinting

Create unique identifiers for devices.
"""

import hashlib
import platform
import socket
import uuid

def get_device_fingerprint():
    """Create a device fingerprint"""
    
    fingerprint_data = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'processor': platform.processor(),
        'machine': platform.machine(),
        'uuid': str(uuid.getnode()),
    }
    
    fingerprint_string = '|'.join(str(v) for v in fingerprint_data.values())
    device_hash = hashlib.sha256(fingerprint_string.encode()).hexdigest()
    
    return {
        'data': fingerprint_data,
        'hash': device_hash[:16]  # First 16 chars
    }

if __name__ == "__main__":
    fp = get_device_fingerprint()
    print(f"Device Fingerprint: {fp['hash']}")
    print(f"Data: {fp['data']}")
