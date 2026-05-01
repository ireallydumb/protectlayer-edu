#!/usr/bin/env python3
"""
Layer 3, Example 1: Perceptual Hash (Fingerprinting)

Create fingerprints that identify content even after modification.
"""

from PIL import Image
import numpy as np

def perceptual_hash_image(image_path, size=8):
    """
    Create a perceptual hash of an image
    
    A perceptual hash is similar for visually similar images,
    even after editing, compression, or format conversion.
    """
    img = Image.open(image_path).convert('L').resize((size, size))
    pixels = np.array(img).flatten()
    avg = np.mean(pixels)
    hash_bits = ''.join('1' if p > avg else '0' for p in pixels)
    return hash_bits

def hamming_distance(hash1, hash2):
    """Calculate hamming distance between two hashes"""
    return sum(c1 != c2 for c1, c2 in zip(hash1, hash2))

if __name__ == "__main__":
    print("Perceptual hashing example")
    print("Used for: Identifying copies, detecting variants")
