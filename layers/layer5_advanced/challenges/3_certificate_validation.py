#!/usr/bin/env python3
"""
Challenge 3: Certificate Validation & Chain of Trust

Build a system that validates certificate chains:
Root CA → Intermediate → Server Certificate

TASK:
Implement certificate validation including:
- Chain verification
- Expiration checking
- Trust path validation
- Revocation checking
"""

import json
from datetime import datetime, timedelta
import hashlib

class CertificateValidator:
    """Certificate validation system"""
    
    def __init__(self):
        self.trusted_cas = {}
        self.revoked_certs = set()
    
    def add_trusted_ca(self, ca_name, ca_cert_hash):
        """Add trusted Certificate Authority"""
        
        self.trusted_cas[ca_name] = ca_cert_hash
        print(f"✅ Trusted CA added: {ca_name}")
    
    def create_certificate(self, subject, issuer, public_key, 
                          valid_days=365):
        """Create a certificate"""
        
        cert_data = {
            'subject': subject,  # Who this cert is for
            'issuer': issuer,    # Who signed it
            'public_key': public_key,
            'issued': datetime.now().isoformat(),
            'expires': (datetime.now() + 
                       timedelta(days=valid_days)).isoformat()
        }
        
        # Create certificate hash (signature in real system)
        cert_string = json.dumps(cert_data, sort_keys=True)
        cert_hash = hashlib.sha256(cert_string.encode()).hexdigest()
        
        cert_data['certificate_hash'] = cert_hash
        
        return cert_data
    
    def validate_certificate(self, certificate, trusted_cas):
        """Validate a certificate"""
        
        # Check 1: Is issuer trusted?
        issuer = certificate['issuer']
        if issuer not in trusted_cas:
            return False, f"Issuer {issuer} not trusted"
        
        # Check 2: Has it expired?
        exp_date = datetime.fromisoformat(certificate['expires'])
        if datetime.now() > exp_date:
            return False, "Certificate expired"
        
        # Check 3: Is it revoked?
        if certificate['certificate_hash'] in self.revoked_certs:
            return False, "Certificate revoked"
        
        return True, "Certificate valid"

if __name__ == "__main__":
    print("Challenge 3: Certificate Validation")
    print("")
    print("How HTTPS works:")
    print("  1. Browser trusts Certificate Authorities")
    print("  2. Website has certificate signed by CA")
    print("  3. Browser verifies signature")
    print("  4. Browser trusts the website")
    print("")
    
    validator = CertificateValidator()
    
    # Add trusted CA
    validator.add_trusted_ca("Verisign", "verisign-hash-12345")
    
    # Create certificate
    cert = validator.create_certificate(
        subject="google.com",
        issuer="Verisign",
        public_key="google-public-key-xyz"
    )
    
    print("\nCertificate created for google.com")
    
    # Validate
    is_valid, message = validator.validate_certificate(
        cert, 
        validator.trusted_cas
    )
    
    print(f"Valid: {is_valid}")
    print(f"Message: {message}")
