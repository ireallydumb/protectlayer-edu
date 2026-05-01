# Layer 2: Visible Protection - Watermarking & Quality Degradation

Learn how to make unauthorized copying obvious through visible watermarks and quality degradation.

## Overview

**Difficulty:** Intermediate  
**Time Estimate:** 4-6 hours  
**Prerequisites:** Complete Layer 1

## What You'll Learn

- ✅ Watermark embedding techniques
- ✅ Quality degradation methods
- ✅ Real-time watermarking
- ✅ Robustness testing
- ✅ User experience optimization

## Concepts

### Watermarking Types
- Text watermarks (copyright info)
- Image overlays (logos, company branding)
- Pattern watermarks (geometric patterns)
- Temporal watermarks (for video)

### Quality Degradation
- Bitrate reduction
- Resolution downscaling
- Color space reduction
- Artifact injection

### Real-World Applications
- Netflix (in screenshare recording detection)
- Streaming services (Disney+, Amazon Prime)
- Video conferences (Zoom watermarking)
- Broadcast TV (anti-piracy)
- Corporate documents

## Contents

- **tutorial.py** - Interactive tutorial (start here)
- **examples/** - Working code samples
- **challenges/** - Practice problems
- **projects/** - Build your own system

## Getting Started

```bash
# Run the tutorial
python3 tutorial.py

# Or use the launcher
./launch.sh     # macOS/Linux
launch.bat      # Windows
```

## Tutorial Flow

1. **Concepts** (30 min) - Understand theory
2. **Examples** (45 min) - Study working code
3. **Challenges** (1 hour) - Practice skills
4. **Projects** (1-2 hours) - Build system
5. **Tests** (30 min) - Verify understanding

## Key Topics

### Basic Watermarking
- Text embedding
- Opacity and blending
- Positioning strategies
- Multi-watermark systems

### Advanced Techniques
- Frequency domain (DCT, FFT)
- Wavelet transforms
- Perceptual constraints
- Adaptive watermarking

### Anti-Tampering
- Fragile watermarks
- Tamper detection
- Integrity verification
- Proof of modification

## Challenges

### Challenge 1: Text Watermark
Add "INTERNAL USE ONLY" watermark to images

### Challenge 2: Quality Degradation
Reduce video bitrate while maintaining quality

### Challenge 3: Real-Time Processing
Apply watermarks to live stream

### Challenge 4: Robustness Testing
Test watermarks survive editing and compression

## Projects

### Project 1: Image Watermarking System
Build a system to watermark batch images

### Project 2: Video Watermarking
Create watermarking for video files

### Project 3: Streaming Protection
Implement live video watermarking

## Next Steps

After completing Layer 2:
- Move to Layer 3: Invisible Protection (steganography)
- Understand limitations of visible protection
- Learn about combining with invisible techniques

## Resources

- **examples/basic_watermark.py** - Simple text watermark
- **examples/quality_degradation.py** - Bitrate reduction
- **challenges/1_text_watermark.py** - First challenge
- **projects/starter_template.py** - Project template

## Tips

- Start with text watermarks (easiest)
- Progress to image overlays
- Then tackle video watermarking
- Test robustness against editing

## Success Criteria

You'll know you've mastered Layer 2 when you can:

✅ Embed visible watermarks in images and video
✅ Apply quality degradation automatically
✅ Design watermarks that survive editing
✅ Optimize watermark visibility/usability trade-off
✅ Explain trade-offs vs invisible protection

---

**Estimated completion:** 4-6 hours  
**Difficulty:** Intermediate  
**Next layer:** Layer 3 - Invisible Protection
