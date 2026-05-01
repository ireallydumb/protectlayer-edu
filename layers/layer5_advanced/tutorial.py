#!/usr/bin/env python3
"""
Layer 5: Advanced Protection - INTERACTIVE TUTORIAL
Learn cryptographic signing and verification

This tutorial covers:
1. Cryptographic hashing
2. HMAC authentication
3. Digital signatures
4. Tamper detection
5. Trust chains
"""

import sys

class Layer5Tutorial:
    """Interactive Advanced Protection Tutorial"""
    
    def __init__(self):
        self.completed = []
    
    def intro(self):
        """Introduction to Layer 5"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    LAYER 5: Advanced Protection - Interactive Tutorial         ║
║                                                                ║
║  Learn cryptographic signing and content verification        ║
╚════════════════════════════════════════════════════════════════╝

Welcome to Layer 5!

THE PREVIOUS LAYERS:
  Layer 1: Detect protection (identifying marked content)
  Layer 2: Visible watermarks (obvious markings)
  Layer 3: Invisible watermarks (steganography)
  Layer 4: Device protection (hardware binding)

LAYER 5: CRYPTOGRAPHIC PROTECTION
Using mathematics to ensure authenticity and prevent tampering.

THE QUESTION:
"Is this content AUTHENTIC and UNMODIFIED?"

CRYPTOGRAPHIC SIGNING:
Creating a 'proof' that content came from a specific source
and hasn't been tampered with.

WHY IT MATTERS:
  ✅ Verify software came from trusted vendor
  ✅ Detect if data was modified
  ✅ Prove non-repudiation (you can't deny signing it)
  ✅ Build trust chains
  ✅ Implement strong DRM

KEY CONCEPTS:
  • Hash = Unique fingerprint of data
  • Signature = Proof of authenticity
  • Keys = Secrets that sign/verify

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU'LL LEARN:
  ✅ Cryptographic hashing
  ✅ HMAC authentication
  ✅ Digital signatures
  ✅ Tamper detection
  ✅ Content verification
  ✅ Trust chains

TIME: ~45 minutes
DIFFICULTY: Advanced

Let's start!
        """)
    
    def exercise_1_hashing(self):
        """Exercise 1: Cryptographic hashing"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║  EXERCISE 1: Cryptographic Hashing - Unique Data Fingerprints  ║
╚════════════════════════════════════════════════════════════════╝

WHAT IS HASHING?
Converting any data into a fixed-length unique string.

PROPERTIES OF GOOD HASHES:
1. Deterministic
   Same input → Same output always
   
2. Fixed output
   Any size input → Fixed size output (SHA256 = 64 chars)
   
3. One-way
   Can't reverse: hash → original data
   
4. Avalanche effect
   Tiny change in input → Completely different hash
   
5. Collision-resistant
   Nearly impossible to find two inputs with same hash

EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Input: "Hello"
SHA256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

Change one letter:
Input: "Hallo"
SHA256: c1802e6b9c98ce64f11c085eaca197998b2acffa9e18e7b87e43341b5e41027f

COMPLETELY DIFFERENT!

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import hashlib

def hash_data(data):
    '''Create cryptographic hash of data'''
    
    if isinstance(data, str):
        data = data.encode()
    
    return hashlib.sha256(data).hexdigest()

def hash_file(filepath):
    '''Create hash of file contents'''
    
    sha256 = hashlib.sha256()
    
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    
    return sha256.hexdigest()

# TRY IT:
# h1 = hash_data("Test document")
# print(f"Hash: {h1}")
#
# # Change one character
# h2 = hash_data("Test documant")  # 'e' → 'a'
# print(f"Hash: {h2}")
# print(f"Same? {h1 == h2}")  # Will be False!

YOUR TURN:
1. Create hashing.py with code above
2. Try hashing different strings
3. Change one character and see hash change
4. Notice: avalanche effect
5. Try large vs. small changes (both produce different hashes)

USE CASE:
You can detect file tampering!
  • Original file hash: a1b2c3d4...
  • Someone modifies file
  • New hash: z9y8x7w6... (completely different!)
  • Detection: Hashes don't match = file modified!

✅ WHAT YOU LEARNED:
  • How cryptographic hashing works
  • Hash properties
  • Avalanche effect
  • Tamper detection
  • File integrity verification
        """)
        
        input("\nPress Enter when you've tried Exercise 1...")
        self.completed.append("Exercise 1: Hashing")
    
    def exercise_2_hmac(self):
        """Exercise 2: HMAC authentication"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 2: HMAC - Authenticated Hashing with Secrets        ║
╚════════════════════════════════════════════════════════════════╝

THE PROBLEM WITH PLAIN HASHING:
Anyone can compute hashes.
How do you prove YOU computed it?

SOLUTION: HMAC
Hash-based Message Authentication Code

It's like hashing, but with a SECRET key:
  • Only you know the key
  • You compute hash using secret key
  • Others can verify (if they know the key)
  • But can't create fake hashes (without the key)

REAL-WORLD ANALOGY:
  Plain hash = Fingerprint (everyone can see)
  HMAC = Signed fingerprint (only you can sign)

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import hmac
import hashlib

def create_hmac(data, secret_key):
    '''Create HMAC signature'''
    
    if isinstance(data, str):
        data = data.encode()
    
    if isinstance(secret_key, str):
        secret_key = secret_key.encode()
    
    signature = hmac.new(
        secret_key,
        data,
        hashlib.sha256
    ).hexdigest()
    
    return signature

def verify_hmac(data, signature, secret_key):
    '''Verify HMAC signature'''
    
    expected = create_hmac(data, secret_key)
    
    # Use constant-time comparison (prevent timing attacks)
    return hmac.compare_digest(signature, expected)

# TRY IT:
# secret = "my-secret-key-12345"
# msg = "Important message"
#
# sig = create_hmac(msg, secret)
# print(f"Signature: {sig}")
#
# # Verify
# is_valid = verify_hmac(msg, sig, secret)
# print(f"Valid: {is_valid}")
#
# # Try with wrong key
# is_valid = verify_hmac(msg, sig, "wrong-key")
# print(f"Valid with wrong key: {is_valid}")  # False!

YOUR TURN:
1. Create hmac_demo.py with code above
2. Create message + signature
3. Verify with correct key (should pass)
4. Try wrong key (should fail)
5. Try tampering with message (should fail)

KEY PROPERTY:
Without the secret key, attacker cannot create valid signatures.
This is the foundation of digital signatures!

✅ WHAT YOU LEARNED:
  • HMAC concept
  • Secret key authentication
  • Signature creation and verification
  • Constant-time comparison
  • Foundation for digital signatures
        """)
        
        input("\nPress Enter when you've tried Exercise 2...")
        self.completed.append("Exercise 2: HMAC")
    
    def exercise_3_digital_signatures(self):
        """Exercise 3: Complete digital signatures"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 3: Digital Signatures - Proving Content Authenticity ║
╚════════════════════════════════════════════════════════════════╝

COMPLETE SIGNATURE SYSTEM:
1. Create data to sign (message, file, software)
2. Sign with secret key (create signature)
3. Distribute data + signature
4. Others verify using public key
5. Only original signer could create valid signature

ANALOGY:
You sign a document with a pen. Others can verify your signature.
But they can't forge it (requires your exact pen).

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import hmac
import hashlib

class DigitalSignature:
    """Digital signature system"""
    
    def __init__(self, signing_key):
        self.signing_key = signing_key.encode() 
            if isinstance(signing_key, str) else signing_key
    
    def sign_content(self, content):
        '''Sign content'''
        if isinstance(content, str):
            content = content.encode()
        
        signature = hmac.new(
            self.signing_key,
            content,
            hashlib.sha256
        ).hexdigest()
        
        return signature
    
    def verify_signature(self, content, signature):
        '''Verify signature'''
        expected = self.sign_content(content)
        return hmac.compare_digest(signature, expected)

# USAGE:
# signer = DigitalSignature("secret-key-12345")
#
# # Sign a file
# with open('document.txt') as f:
#     content = f.read()
#
# signature = signer.sign_content(content)
# print(f"Signature: {signature}")
#
# # Later, verify
# is_valid = signer.verify_signature(content, signature)
# print(f"Document valid: {is_valid}")
#
# # If someone changes the document
# modified = content + "HACKED"
# is_valid = signer.verify_signature(modified, signature)
# print(f"Modified valid: {is_valid}")  # False!

YOUR TURN:
1. Create digital_sig.py with code above
2. Sign some content
3. Verify the signature
4. Tamper with the content slightly
5. Verification should fail

REAL-WORLD:
This is how software is signed!
  • Apple signs iOS apps
  • Microsoft signs Windows updates
  • GitHub verifies commit signatures
  • Package managers verify installations

✅ WHAT YOU LEARNED:
  • Digital signature creation
  • Signature verification
  • Tamper detection
  • Content authenticity proof
  • Practical DRM application
        """)
        
        input("\nPress Enter when you've tried Exercise 3...")
        self.completed.append("Exercise 3: Digital Signatures")
    
    def exercise_4_trust_chains(self):
        """Exercise 4: Trust chains"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 4: Trust Chains - Proving who you trust            ║
╚════════════════════════════════════════════════════════════════╝

THE PROBLEM:
How do you know a signature is from someone trustworthy?

SOLUTION: Trust Chains
  • You trust Company A
  • Company A signs Company B's certificate
  • Now you trust Company B (transitively)
  • Each link verified with a signature

REAL-WORLD EXAMPLE - HTTPS:
1. Your browser trusts Certificate Authorities (CAs)
2. CA signs server certificate
3. Server sends certificate
4. Browser verifies: "Is this signed by a CA I trust?"
5. If yes → Trust the server → Use HTTPS

CHAIN OF TRUST:
┌─────────────┐
│ Root CA     │ (you trust this)
│ (Verisign)  │
└──────┬──────┘
       │ signs
       ↓
┌─────────────┐
│ Server Cert │ (signed by CA, so you trust it)
│ (google.com)│
└─────────────┘

CONCEPT:
Signatures create chains of trust.
Each signature links back to someone you trust.

CODE CONCEPT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Simplified trust chain
def verify_trust_chain(cert, trusted_signers):
    '''Verify certificate is signed by someone we trust'''
    
    issuer = cert['issued_by']
    signature = cert['signature']
    
    for trusted_key in trusted_signers:
        if verify_signature(cert, signature, trusted_key):
            # Certificate was signed by trusted source
            return True, f"Verified by {issuer}"
    
    # Not signed by anyone we trust
    return False, "Certificate not trusted"

YOUR TURN:
Think about trust chains:
1. Do you trust Microsoft?
2. Do you trust Apple?
3. They both sign software
4. You download from them
5. Should you trust it?

This is how modern security works!

✅ WHAT YOU LEARNED:
  • Trust chain concepts
  • Certificate validation
  • Chain of custody
  • Transitive trust
  • Real-world security infrastructure
        """)
        
        input("\nPress Enter when you've tried Exercise 4...")
        self.completed.append("Exercise 4: Trust Chains")
    
    def summary(self):
        """Summary of Layer 5"""
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 5: ADVANCED PROTECTION - SUMMARY                    ║
╚════════════════════════════════════════════════════════════════╝

CONGRATULATIONS! You've completed Layer 5 - All 5 Layers!

EXERCISES COMPLETED:
        """)
        
        for i, exercise in enumerate(self.completed, 1):
            print(f"  {i}. ✅ {exercise}")
        
        print(f"""
KEY SKILLS MASTERED:
  ✅ Cryptographic hashing
  ✅ HMAC authentication
  ✅ Digital signatures
  ✅ Tamper detection
  ✅ Trust chains
  ✅ Content verification

YOU CAN NOW:
  • Sign digital content
  • Verify content authenticity
  • Detect tampering
  • Build trust chains
  • Implement strong DRM

ALL 5 LAYERS COMPLETED:
  Layer 1: Detection ✅ (identify protection)
  Layer 2: Visible ✅ (add watermarks)
  Layer 3: Invisible ✅ (steganography)
  Layer 4: Device ✅ (fingerprinting)
  Layer 5: Cryptography ✅ (signatures)

COMPLETE DRM SYSTEM:
You now understand how to:
  1. Detect when content is protected
  2. Add visible protection (watermarks)
  3. Add invisible protection (hidden data)
  4. Bind to specific devices
  5. Verify authenticity (signatures)

THIS IS ENTERPRISE-LEVEL DRM!

NEXT STEPS:
  • Study the projects in each layer
  • Implement complete systems
  • Combine layers for stronger protection
  • Build your own DRM platform

Ready to build complete projects?
Check: python3 ../layer2_visible/projects/image_watermarker.py
Or: python3 ../layer3_invisible/projects/steganography_toolkit.py
        """)
    
    def run(self):
        """Run the complete tutorial"""
        self.intro()
        
        input("\nPress Enter to begin Exercise 1...")
        self.exercise_1_hashing()
        
        input("\nPress Enter to begin Exercise 2...")
        self.exercise_2_hmac()
        
        input("\nPress Enter to begin Exercise 3...")
        self.exercise_3_digital_signatures()
        
        input("\nPress Enter to begin Exercise 4...")
        self.exercise_4_trust_chains()
        
        input("\nPress Enter to see summary...")
        self.summary()

if __name__ == "__main__":
    tutorial = Layer5Tutorial()
    tutorial.run()
