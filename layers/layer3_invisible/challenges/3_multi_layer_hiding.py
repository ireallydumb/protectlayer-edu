#!/usr/bin/env python3
"""
Challenge 3: Multi-Layer Steganography

Hide messages in MULTIPLE color channels (R, G, B)
to increase capacity and robustness.

TASK:
Implement hiding in RGB channels separately
to triple the message capacity.
"""

from PIL import Image
import numpy as np
import sys

class MultiLayerSteganography:
    """Multi-channel message hiding"""
    
    @staticmethod
    def hide_in_channels(image_path, message, output_path):
        """
        Distribute message across RGB channels
        R: First third of message
        G: Second third
        B: Third part
        """
        
        try:
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            pixels = np.array(img)
            
            # Split message into three parts
            part_size = len(message) // 3
            part1 = message[:part_size]
            part2 = message[part_size:2*part_size]
            part3 = message[2*part_size:]
            
            # Convert to binary
            binary1 = ''.join(format(ord(c), '08b') for c in part1)
            binary2 = ''.join(format(ord(c), '08b') for c in part2)
            binary3 = ''.join(format(ord(c), '08b') for c in part3)
            
            # Hide in each channel
            for i, bit in enumerate(binary1):
                pixels[i//img.size[0], i%img.size[0], 0] = \
                    (pixels[i//img.size[0], i%img.size[0], 0] & 0xFE) | int(bit)
            
            for i, bit in enumerate(binary2):
                pixels[i//img.size[0], i%img.size[0], 1] = \
                    (pixels[i//img.size[0], i%img.size[0], 1] & 0xFE) | int(bit)
            
            for i, bit in enumerate(binary3):
                pixels[i//img.size[0], i%img.size[0], 2] = \
                    (pixels[i//img.size[0], i%img.size[0], 2] & 0xFE) | int(bit)
            
            result_img = Image.fromarray(pixels)
            result_img.save(output_path)
            
            print(f"✅ Message hidden in 3 channels")
            print(f"   Capacity: 3x the normal LSB hiding!")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

if __name__ == "__main__":
    print("Challenge 3: Multi-Layer Steganography")
    print("")
    
    if len(sys.argv) < 4:
        print("Usage: python3 3_multi_layer_hiding.py <image> <message> <output>")
        sys.exit(1)
    
    image = sys.argv[1]
    message = sys.argv[2]
    output = sys.argv[3]
    
    MultiLayerSteganography.hide_in_channels(image, message, output)
    print(f"Result: {output}")
