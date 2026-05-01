#!/usr/bin/env python3
"""
Layer 3, Example 2: LSB (Least Significant Bit) Steganography

Hide data in the least significant bits of image pixels.

This is imperceptible to human vision but can survive some compression.
"""

from PIL import Image
import numpy as np

def hide_data_in_image(image_path, secret_message, output_path):
    """
    Hide text in image LSBs
    
    Args:
        image_path: Source image
        secret_message: Text to hide (max ~300 chars in 512x512 image)
        output_path: Output image with hidden data
    """
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Convert message to binary
    message_binary = ''.join(format(ord(c), '08b') for c in secret_message)
    
    # Hide in LSBs
    flat = pixels.flatten()
    for i, bit in enumerate(message_binary):
        flat[i] = (flat[i] & 0xFE) | int(bit)
    
    result = flat.reshape(pixels.shape)
    Image.fromarray(result.astype('uint8')).save(output_path)
    print(f"✅ Data hidden in image (message size: {len(secret_message)} chars)")

def extract_data_from_image(image_path):
    """Extract hidden text from image"""
    img = Image.open(image_path)
    pixels = np.array(img).flatten()
    
    # Extract LSBs
    binary = ''.join(str(p & 1) for p in pixels[:2400])  # 300*8
    message = ''.join(chr(int(binary[i:i+8], 2)) 
                     for i in range(0, len(binary), 8))
    return message.split('\x00')[0]  # Stop at null terminator

if __name__ == "__main__":
    print("LSB steganography example")
    print("Used for: Hidden ownership marks, undetectable fingerprints")
