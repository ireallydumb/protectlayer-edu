#!/usr/bin/env python3
"""
Layer 2, Example 1: Basic Text Watermark

Learn how to add a simple text watermark to an image.

This example demonstrates:
  • PIL Image operations
  • ImageDraw for text rendering
  • Alpha blending for transparency
  • Watermark positioning

Usage:
  python3 basic_watermark.py input.jpg output.jpg "WATERMARK TEXT"
"""

from PIL import Image, ImageDraw, ImageFont
import sys

def add_text_watermark(image_path, output_path, watermark_text, opacity=0.5):
    """
    Add a text watermark to an image
    
    Args:
        image_path: Path to input image
        output_path: Path to save watermarked image
        watermark_text: Text to add as watermark
        opacity: Watermark opacity (0.0-1.0)
    """
    
    # Open image
    img = Image.open(image_path)
    
    # Create transparent watermark layer
    watermark = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)
    
    # Try to use a nice font, fall back to default
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position (bottom right)
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = img.size[0] - text_width - 10  # 10px from right
    y = img.size[1] - text_height - 10  # 10px from bottom
    
    # Draw watermark text
    # White text with opacity
    draw.text((x, y), watermark_text, font=font, 
              fill=(255, 255, 255, int(255 * opacity)))
    
    # Convert to RGB and composite
    img_rgb = img.convert('RGB')
    watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)
    
    # Save result
    watermarked.convert('RGB').save(output_path, 'JPEG', quality=95)
    print(f"✅ Watermarked image saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 basic_watermark.py input.jpg output.jpg 'WATERMARK TEXT'")
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    watermark = sys.argv[3]
    
    add_text_watermark(input_image, output_image, watermark)
