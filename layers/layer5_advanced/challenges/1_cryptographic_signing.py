#!/usr/bin/env python3
"""
Challenge 1.1: Cryptographic Signing & Verification

COMPLETE WORKING SOLUTION - STUDY & IMPROVE!

Task: Implement digital signatures to verify content authenticity
"""

import hmac
import hashlib
from pathlib import Path

class CryptoSigner:
    """Simple cryptographic signing system"""
    
    def __init__(self, secret_key=None):
        """
        Initialize signer with secret key
        
        Args:
            secret_key: Secret key for signing (string or bytes)
        """
        if secret_key is None:
            secret_key = "default_secret_key_change_me_in_production"
        
        self.secret_key = secret_key.encode() if isinstance(secret_key, str) else secret_key
    
    def sign_content(self, content):
        """
        Sign content with HMAC-SHA256
        
        Args:
            content: Text or bytes to sign
            
        Returns:
            Signature (hex string)
        """
        if isinstance(content, str):
            content = content.encode()
        
        signature = hmac.new(
            self.secret_key,
            content,
            hashlib.sha256
        ).hexdigest()
        
        return signature
    
    def verify_signature(self, content, signature):
        """
        Verify content signature
        
        Args:
            content: Original content
            signature: Signature to verify
            
        Returns:
            True if signature is valid, False otherwise
        """
        expected_signature = self.sign_content(content)
        return hmac.compare_digest(signature, expected_signature)
    
    def sign_file(self, filepath):
        """Sign a file's contents"""
        with open(filepath, 'rb') as f:
            content = f.read()
        return self.sign_content(content)
    
    def verify_file(self, filepath, signature):
        """Verify a file's signature"""
        with open(filepath, 'rb') as f:
            content = f.read()
        return self.verify_signature(content, signature)

# DEMO & TESTING
if __name__ == "__main__":
    print("Challenge 1.1: Cryptographic Signing - COMPLETE SOLUTION")
    print("")
    
    signer = CryptoSigner(secret_key="super_secret_key_12345")
    
    # Example 1: Sign a message
    message = "Protect this content!"
    signature = signer.sign_content(message)
    
    print("📋 EXAMPLE 1: Sign a Message")
    print(f"  Message: {message}")
    print(f"  Signature: {signature}")
    print("")
    
    # Verify it
    is_valid = signer.verify_signature(message, signature)
    print(f"  ✅ Verified: {is_valid}")
    print("")
    
    # Example 2: Tampering detection
    print("📋 EXAMPLE 2: Detect Tampering")
    tampered_message = "Protect this content??? (MODIFIED)"
    is_tampered_valid = signer.verify_signature(tampered_message, signature)
    print(f"  Original message: {message}")
    print(f"  Tampered message: {tampered_message}")
    print(f"  ✅ Tampered detected: {not is_tampered_valid}")
    print("")
    
    # Example 3: File signing
    print("📋 EXAMPLE 3: Sign a File")
    test_file = Path("/tmp/test_content.txt")
    test_file.write_text("Important content that must not be tampered with")
    
    file_signature = signer.sign_file(test_file)
    print(f"  File: {test_file.name}")
    print(f"  Signature: {file_signature}")
    
    # Verify file
    file_valid = signer.verify_file(test_file, file_signature)
    print(f"  ✅ File verified: {file_valid}")
    print("")
    
    # Tamper with file
    test_file.write_text("HACKED!!!")
    file_tampered = signer.verify_file(test_file, file_signature)
    print(f"  ✅ Tampering detected: {not file_tampered}")
    print("")
    
    print("WHAT YOU LEARNED:")
    print("✅ How digital signatures work")
    print("✅ HMAC authentication")
    print("✅ Content integrity verification")
    print("✅ Tamper detection")
    print("✅ Non-repudiation")
    print("")
    
    print("CHALLENGE EXTENSIONS:")
    print("1. Implement RSA public-key cryptography")
    print("2. Add timestamp to signatures")
    print("3. Create certificate system")
    print("4. Implement revocation lists")
    print("5. Build trust chain verification")
    
    # Cleanup
    test_file.unlink()
