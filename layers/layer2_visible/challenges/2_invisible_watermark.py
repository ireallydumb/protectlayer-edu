#!/usr/bin/env python3
"""
Challenge 2: Invisible Watermark (Quality-Degraded)

Add a watermark that's imperceptible to human eyes but 
recoverable through analysis.

TASK:
Create a watermark by slightly degrading image quality
that only those who know to look for it can detect.
"""

from PIL import Image
import numpy as np

def add_invisible_watermark(image_path, output_path, intensity=0.01):
    """
    Add invisible watermark by subtle quality degradation.
    Reduces brightness/contrast slightly to embed mark.
    """
    
    try:
        img = Image.open(image_path)
        pixels = np.array(img).astype(float)
        
        # Apply subtle quality reduction
        # Reduce by small percentage (imperceptible)
        watermarked = pixels * (1 - intensity)
        
        # Keep values in valid range
        watermarked = np.clip(watermarked, 0, 255)
        
        # Convert back to image
        result = Image.fromarray(watermarked.astype('uint8'))
        result.save(output_path)
        
        print(f"✅ Invisible watermark added (intensity: {intensity*100:.2f}%)")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def detect_invisible_watermark(original_path, marked_path):
    """
    Detect invisible watermark by comparing pixel values.
    """
    
    try:
        original = np.array(Image.open(original_path)).astype(float)
        marked = np.array(Image.open(marked_path)).astype(float)
        
        # Calculate average difference
        diff = np.mean(np.abs(original - marked))
        
        watermark_detected = diff > 0.5
        
        print(f"Average pixel difference: {diff:.2f}")
        print(f"Watermark detected: {watermark_detected}")
        
        return watermark_detected
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("Challenge 2: Invisible Watermarking")
    print("")
    print("The goal: Add watermark imperceptible to human eyes")
    print("The method: Subtle quality degradation")
    print("")
    
    import sys
    if len(sys.argv) > 1:
        image = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else "invisible_watermarked.jpg"
        
        add_invisible_watermark(image, output, intensity=0.01)
        print("")
        print("Now you try:")
        print(f"1. Original image: {image}")
        print(f"2. Watermarked: {output}")
        print("3. To humans: They look identical!")
        print("4. To algorithms: Detectable difference")
    else:
        print("Usage: python3 2_invisible_watermark.py image.jpg [output.jpg]")
