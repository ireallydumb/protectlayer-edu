#!/usr/bin/env python3
"""
Challenge 2: Capacity Calculator

Calculate the MAXIMUM message size that can be hidden
in an image without degradation.

TASK:
Build a tool to analyze images and determine exactly
how many bytes/bits can be hidden.
"""

from PIL import Image
import numpy as np
import sys

class CapacityCalculator:
    """Calculate steganography capacity"""
    
    @staticmethod
    def calculate_capacity(image_path):
        """Calculate bits available for hiding"""
        
        try:
            img = Image.open(image_path)
            pixels = np.array(img)
            
            # Total pixels
            total_pixels = pixels.size
            
            # 1 bit per pixel (LSB method)
            total_bits = total_pixels
            
            # 16 bits reserved for length header
            usable_bits = total_bits - 16
            
            # Convert to bytes
            usable_bytes = usable_bits // 8
            
            # Estimate with different methods
            results = {
                'image_file': image_path,
                'dimensions': img.size,
                'total_pixels': total_pixels,
                'total_bits': total_bits,
                'usable_bits': usable_bits,
                'usable_bytes': usable_bytes,
                'usable_kb': usable_bytes / 1024,
                'max_text_chars': usable_bytes,  # 1 char = 1 byte
            }
            
            return results
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    @staticmethod
    def estimate_compression(usable_bytes):
        """Estimate compression with different algorithms"""
        
        compression_estimates = {
            'no_compression': usable_bytes,
            'basic_compression': usable_bytes * 0.7,
            'advanced_compression': usable_bytes * 0.5,
            'max_compression': usable_bytes * 0.3,
        }
        
        return compression_estimates

if __name__ == "__main__":
    print("Challenge 2: Capacity Calculator")
    print("")
    
    if len(sys.argv) < 2:
        print("Usage: python3 2_capacity_calculator.py <image>")
        sys.exit(1)
    
    image_file = sys.argv[1]
    capacity = CapacityCalculator.calculate_capacity(image_file)
    
    if capacity:
        print(f"Image: {capacity['image_file']}")
        print(f"Dimensions: {capacity['dimensions']}")
        print(f"Total capacity: {capacity['usable_bytes']} bytes")
        print(f"              ({capacity['usable_kb']:.2f} KB)")
        print(f"Max characters: {capacity['max_text_chars']}")
        print("")
        print("You could hide:")
        print(f"  • A 5-page document ({capacity['usable_kb']:.0f} KB)")
        print(f"  • A small image")
        print(f"  • Metadata + watermark info")
