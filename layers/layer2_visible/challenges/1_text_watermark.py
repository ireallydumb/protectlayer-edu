#!/usr/bin/env python3
"""
Challenge 1.1: Add Text Watermark to Image

TASK:
  Modify the add_watermark() function to accept custom parameters:
  - Position (corners: TL, TR, BL, BR)
  - Opacity (0.0-1.0)
  - Color (RGB tuple)
  - Font size

TEST:
  Run: python3 1_text_watermark.py

Your implementation should:
  ✓ Accept position parameter
  ✓ Support different opacities
  ✓ Allow custom colors
  ✓ Scale font size appropriately
"""

from PIL import Image, ImageDraw
import sys

def add_watermark_custom(image_path, output_path, text, position='BR', 
                        opacity=0.5, color=(255, 255, 255), font_size=40):
    """
    TODO: Implement this function
    
    Parameters:
      image_path: Path to input image
      output_path: Path to save result
      text: Watermark text
      position: 'TL' (top-left), 'TR', 'BL', 'BR' (bottom-right)
      opacity: 0.0 (transparent) to 1.0 (opaque)
      color: RGB tuple (255, 255, 255)
      font_size: Size in pixels
    """
    pass

# Test cases
if __name__ == "__main__":
    # TODO: Test with sample image
    print("Challenge 1.1: Add Text Watermark")
    print("TODO: Implement add_watermark_custom()")
