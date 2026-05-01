#!/usr/bin/env python3
"""
Layer 3: Invisible Protection - Steganography & Fingerprinting

In this layer, you'll learn about INVISIBLE protection mechanisms that
embed information imperceptibly within content itself.

What You'll Learn:
  • Steganographic embedding (hiding data in media)
  • Perceptual hashing (fingerprinting)
  • LSB (Least Significant Bit) techniques
  • Frequency domain embedding
  • Robustness testing
  • Tamper detection

Prerequisites:
  • Complete Layers 1-2
  • Understanding of digital signal processing basics
  • Python data structures

Time Estimate: 6-8 hours
Difficulty: Advanced
Status: Tutorial Available
"""

import sys

def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║         Layer 3: Invisible Protection - Steganography                    ║
║                                                                          ║
║      Hide ownership data inside content - nobody can see it!             ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

Welcome to Layer 3: Invisible Protection!

WHAT IS INVISIBLE PROTECTION?
─────────────────────────────────────────────────────────────────────────

Invisible protection embeds identifying or protective information INSIDE
the content itself, imperceptibly.

Unlike Layer 2 (visible watermarks), users don't see it. The protection
is embedded in the data itself.

STEGANOGRAPHY vs WATERMARKING
─────────────────────────────────────────────────────────────────────────

Visible (Layer 2):        Invisible (Layer 3):
  • Text overlays          • Data in LSBs
  • Image watermarks       • Frequency domain
  • Easy to see            • Imperceptible
  • Obvious protection     • Hidden protection

REAL-WORLD EXAMPLES
─────────────────────────────────────────────────────────────────────────

✓ Movie studio marks (imperceptible, but trackable)
✓ Broadcast fingerprints (hidden in signal)
✓ Digital rights tracking (inside video stream)
✓ Piracy source tracking (identifies leaker)
✓ Authenticity verification (in image metadata)

LAYER 3 TOPICS
─────────────────────────────────────────────────────────────────────────

1. LSB Steganography (Least Significant Bits)
   - Hide data in image/video LSBs
   - Trade off: capacity vs robustness
   - Vulnerable to compression

2. Frequency Domain Embedding
   - DCT (Discrete Cosine Transform)
   - Wavelet transform
   - More robust than LSB

3. Perceptual Hashing
   - Create fingerprints of content
   - Similar content = similar hash
   - Identify copies and variants

4. Robustness Testing
   - Can watermark survive editing?
   - Video codec compression?
   - Format conversion?
   - Intentional attacks?

5. Tamper Detection
   - Fragile watermarks
   - Detect content modification
   - Prove authenticity

═══════════════════════════════════════════════════════════════════════════

Getting Started with Layer 3:

1. Read the Layer 3 README
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
