#!/usr/bin/env python3
"""
Layer 5, Example 1: Cryptographic Signing & Verification

Use digital signatures to ensure authenticity.
"""

from hashlib import sha256
import hmac

def sign_content(content, secret_key):
    """Sign content with HMAC"""
    return hmac.new(
        secret_key.encode(),
        content.encode(),
        sha256
    ).hexdigest()

def verify_signature(content, signature, secret_key):
    """Verify content signature"""
    expected = sign_content(content, secret_key)
    return hmac.compare_digest(signature, expected)

if __name__ == "__main__":
    secret = "my_secret_key"
    message = "Protected content"
    
    sig = sign_content(message, secret)
    print(f"Signature: {sig}")
    
    verified = verify_signature(message, sig, secret)
    print(f"Verified: {verified}")
