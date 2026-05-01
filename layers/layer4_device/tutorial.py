#!/usr/bin/env python3
"""
Layer 4: Device Protection - Fingerprinting & Behavioral Analysis

In this layer, you'll learn about device-level protection mechanisms that
identify, verify, and track devices accessing content.

What You'll Learn:
  • Hardware fingerprinting
  • Device identification
  • Behavioral analysis
  • Geo-restrictions
  • Device attestation
  • Risk scoring

Prerequisites:
  • Complete Layers 1-3
  • Understanding of system architecture
  • Network concepts (IP, DNS, etc.)

Time Estimate: 8-10 hours
Difficulty: Advanced
Status: Tutorial Available
"""

import sys

def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║        Layer 4: Device Protection - Hardware Fingerprinting              ║
║                                                                          ║
║     Identify & verify devices accessing your protected content           ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

Welcome to Layer 4: Device Protection!

WHAT IS DEVICE PROTECTION?
─────────────────────────────────────────────────────────────────────────

Device protection identifies, verifies, and tracks WHICH DEVICES are
accessing your content.

This adds a new dimension: not just protecting the CONTENT, but protecting
it on SPECIFIC, TRUSTED DEVICES.

LAYERS SO FAR
─────────────────────────────────────────────────────────────────────────

Layer 1: Content Detection
  ✓ Identify WHAT is being protected
  ✓ Tag ownership and metadata

Layer 2: Visible Protection
  ✓ Make protection OBVIOUS (watermarks)
  ✓ Deter casual pirates

Layer 3: Invisible Protection
  ✓ Hide protection DATA within content
  ✓ Track sources & verify authenticity

Layer 4: Device Protection
  ✓ Verify WHO is accessing content
  ✓ Ensure AUTHORIZED devices only
  ✓ Prevent unauthorized sharing

DEVICE FINGERPRINTING
─────────────────────────────────────────────────────────────────────────

Hardware fingerprint = unique identifier for a device

Based on:
  • CPU serial number
  • GPU model & memory
  • HDD/SSD serial
  • MAC address (network card)
  • BIOS/UEFI info
  • Device name/UUID
  • OS info
  • Installed software

Used by:
  ✓ Netflix (prevents account sharing)
  ✓ Adobe CC (enforces licensing)
  ✓ Video games (piracy protection)
  ✓ Corporate software (usage tracking)

BEHAVIORAL ANALYSIS
─────────────────────────────────────────────────────────────────────────

Beyond hardware, analyze HOW devices use content:

  • Access patterns (when, where, how often)
  • Simultaneous logins (same account, different devices)
  • Geographic anomalies (logged in from different countries)
  • Unusual activity (downloading all content at once)
  • File operations (attempting to extract/save)

GEO-RESTRICTIONS
─────────────────────────────────────────────────────────────────────────

Restrict content by geographic location:

  • IP geolocation (where is this request from?)
  • License agreements (movie available only in USA)
  • Regional distribution rights
  • Time-based availability

LAYER 4 TOPICS
─────────────────────────────────────────────────────────────────────────

1. Hardware Fingerprinting
   - Collect device information
   - Create unique device ID
   - Store in secure database
   - Verify on each access

2. Device Attestation
   - Verify device hasn't been tampered
   - Check for jailbreak/root
   - Verify security patches
   - Ensure trusted environment

3. Geo-IP Detection
   - Get user location from IP
   - Check against restrictions
   - Detect VPN/proxy attempts
   - Block unauthorized regions

4. Behavioral Analysis
   - Track access patterns
   - Detect anomalies
   - Calculate risk scores
   - Block suspicious activity

5. Multi-Device Management
   - Allow 1-4 simultaneous devices
   - Track which devices
   - Revoke access if needed
   - Prevent account sharing

═══════════════════════════════════════════════════════════════════════════

Getting Started with Layer 4:

1. Read the Layer 4 README
2. Study code examples
3. Try the challenges
4. Build your own system

Use the launcher for best experience:
  ./launch.sh (macOS/Linux) or launch.bat (Windows)

═══════════════════════════════════════════════════════════════════════════
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
