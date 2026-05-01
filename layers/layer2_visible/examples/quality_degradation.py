#!/usr/bin/env python3
"""
Layer 2, Example 2: Quality Degradation

Reduce video/image quality to deter unauthorized sharing.

This example shows how streaming services protect content by:
  • Reducing bitrate for screen recording detection
  • Lowering resolution for preview content
  • Adding compression artifacts
"""

from PIL import Image
import cv2

def degrade_image_quality(image_path, output_path, quality=50):
    """
    Reduce image quality (simulate JPEG compression)
    
    Args:
        image_path: Input image path
        output_path: Output image path
        quality: JPEG quality (1-100, lower = worse)
    """
    img = Image.open(image_path)
    img.save(output_path, 'JPEG', quality=quality)
    print(f"✅ Degraded image saved (quality={quality})")

def degrade_video_bitrate(video_path, output_path, bitrate="500k"):
    """
    Reduce video bitrate (requires ffmpeg)
    
    Args:
        video_path: Input video path
        output_path: Output video path
        bitrate: Target bitrate (e.g., "500k", "1000k")
    """
    import subprocess
    cmd = [
        'ffmpeg', '-i', video_path,
        '-b:v', bitrate,
        '-c:a', 'aac', '-b:a', '128k',
        output_path
    ]
    subprocess.run(cmd)
    print(f"✅ Degraded video saved (bitrate={bitrate})")

if __name__ == "__main__":
    print("Quality degradation example")
    print("Used for: Preview content, deterring unauthorized use")
