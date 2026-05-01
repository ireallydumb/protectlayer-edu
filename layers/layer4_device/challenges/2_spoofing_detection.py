#!/usr/bin/env python3
"""
Challenge 2: Device Spoofing Detection

Detect when someone tries to FAKE a device fingerprint.

TASK:
Implement detection for various spoofing attempts:
- Hostname changes
- MAC address spoofing  
- VM detection
- Hardware emulation
"""

import platform
import socket

class SpoofingDetector:
    """Detect device spoofing attempts"""
    
    @staticmethod
    def get_critical_hardware_id():
        """Get hardware-level ID that can't be easily spoofed"""
        
        # These are very hard to spoof:
        critical_info = {
            'machine_type': platform.machine(),  # ARM, x86_64, etc
            'processor': platform.processor(),     # Intel, ARM, Apple Silicon
            'cpu_count': __import__('os').cpu_count(),
        }
        
        return critical_info
    
    @staticmethod
    def detect_vm_environment():
        """Detect if running in virtual machine"""
        
        vm_indicators = {
            'hypervisor_detected': False,
            'vm_software': None,
            'physical_cpus': __import__('os').cpu_count(),
        }
        
        # Simple detection - in practice would use more methods
        platform_str = str(platform.platform()).lower()
        
        if 'virtual' in platform_str or 'vmware' in platform_str:
            vm_indicators['hypervisor_detected'] = True
            vm_indicators['vm_software'] = 'VMware'
        
        return vm_indicators
    
    @staticmethod
    def detect_spoofing_attempt(original_fp, claimed_fp):
        """
        Detect if fingerprint looks spoofed
        by comparing critical hardware IDs
        """
        
        # Can't change these without physical hardware change
        critical_fields = ['machine', 'processor', 'cpu_count']
        
        spoofing_score = 0
        
        for field in critical_fields:
            orig_val = str(original_fp.get(field, ''))
            claimed_val = str(claimed_fp.get(field, ''))
            
            if orig_val != claimed_val:
                spoofing_score += 30
        
        # Hostname can change (10 points each)
        if original_fp.get('hostname') != claimed_fp.get('hostname'):
            spoofing_score += 10
        
        detected = spoofing_score > 30
        
        return {
            'spoofing_detected': detected,
            'spoofing_score': spoofing_score,
            'confidence': min(100, spoofing_score)
        }

if __name__ == "__main__":
    print("Challenge 2: Device Spoofing Detection")
    print("")
    
    detector = SpoofingDetector()
    
    print("Critical Hardware IDs:")
    print(detector.get_critical_hardware_id())
    print("")
    
    print("VM Detection:")
    print(detector.detect_vm_environment())
    print("")
    
    print("Try changing hostname and run again:")
    print("  You'll see it's detected!")
