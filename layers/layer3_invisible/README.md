# Layer 3: Invisible Protection - Steganography & Fingerprinting

Learn to hide ownership data and fingerprints imperceptibly within content.

## Overview

**Difficulty:** Advanced  
**Time Estimate:** 6-8 hours  
**Prerequisites:** Complete Layers 1-2

## What You'll Learn

- ✅ LSB (Least Significant Bit) steganography
- ✅ Frequency domain embedding (DCT, FFT)
- ✅ Perceptual hashing
- ✅ Robustness against compression
- ✅ Tamper detection

## Concepts

### Steganography
Hiding data inside content without visible indicators.

Types:
- LSB embedding (image/audio)
- Frequency domain (DCT in JPEG)
- Wavelet domain (image compression)
- Temporal (video frame distribution)

### Perceptual Hashing
Creating fingerprints of content that survive minor modifications.

Uses:
- Identify copies and variants
- Detect remixes
- Track pirated content
- Verify authenticity

## Key Differences from Layer 2

| Layer 2 (Visible) | Layer 3 (Invisible) |
|---|---|
| Obvious watermark | Hidden data |
| Visual/audio markers | Data in LSBs/frequency |
| Users see/hear it | Imperceptible to users |
| Easy to implement | Requires signal processing |
| Limited robustness | High robustness possible |

## Contents

- **tutorial.py** - Interactive tutorial
- **examples/** - Code examples
- **challenges/** - Practice problems
- **projects/** - Build your own

## Success Criteria

✅ Embed invisible data in images
✅ Survive JPEG/MP4 compression
✅ Create robust fingerprints
✅ Detect tampered content
✅ Explain robustness trade-offs

---

**Estimated completion:** 6-8 hours  
**Difficulty:** Advanced  
**Next layer:** Layer 4 - Device Protection
