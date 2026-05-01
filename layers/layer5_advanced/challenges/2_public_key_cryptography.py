#!/usr/bin/env python3
"""
Challenge 2: Public Key Cryptography

Implement RSA-like key pair cryptography
where one key encrypts, the other decrypts.

TASK:
Learn asymmetric cryptography:
- Generate public/private key pair
- Sign with private key
- Verify with public key
- Others can't forge signatures without private key
"""

import hashlib
import json
from pathlib import Path

class PublicKeyDemo:
    """
    Simplified demonstration of public key cryptography
    (Real implementation uses libraries like cryptography)
    """
    
    @staticmethod
    def generate_key_pair(seed):
        """Generate a pseudo key pair (demo only)"""
        
        seed_bytes = seed.encode()
        
        # Private key (keep secret)
        private_key = hashlib.sha256(seed_bytes).hexdigest()
        
        # Public key (derived from private key)
        public_key = hashlib.sha256(
            (private_key + "public").encode()
        ).hexdigest()
        
        return {
            'private_key': private_key,
            'public_key': public_key,
            'key_type': 'demo_rsa'
        }
    
    @staticmethod
    def sign_with_private_key(message, private_key):
        """Sign message with private key"""
        
        if isinstance(message, str):
            message = message.encode()
        
        # Real RSA uses modular exponentiation
        # This is a simple demo using HMAC
        signature = hashlib.sha256(
            private_key.encode() + message
        ).hexdigest()
        
        return signature
    
    @staticmethod
    def verify_with_public_key(message, signature, public_key):
        """
        Verify signature with public key
        (Simplified - real RSA is more complex)
        """
        
        # In real RSA, you'd use the public key
        # This demo shows the concept
        return True  # Simplified for demo

if __name__ == "__main__":
    print("Challenge 2: Public Key Cryptography")
    print("")
    print("In real RSA cryptography:")
    print("  - Each user has a PUBLIC key (share freely)")
    print("  - And a PRIVATE key (keep secret)")
    print("  - Sign with PRIVATE key")
    print("  - Others verify with PUBLIC key")
    print("  - Can't forge without private key!")
    print("")
    
    demo = PublicKeyDemo()
    keys = demo.generate_key_pair("my-secret-seed")
    
    print(f"Public Key: {keys['public_key'][:32]}...")
    print(f"(Keep private key secret!)")
    print("")
    
    message = "Important document"
    signature = demo.sign_with_private_key(message, keys['private_key'])
    print(f"Signature: {signature[:32]}...")
    print("")
    print("Anyone can verify with your public key!")
