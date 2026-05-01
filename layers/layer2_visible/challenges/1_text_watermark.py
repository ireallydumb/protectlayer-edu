#!/usr/bin/env python3
"""
Challenge 1.1: Add Text Watermark to Image

TASK:
  Modify the add_watermark() function to accept custom parameters:
  - Position (corners: TL, TR, BL, BR)
  - Opacity (0.0-1.0)
  - Color (RGB tuple)
  - Font size

COMPLETE SOLUTION PROVIDED - Study and modify to match YOUR style!
"""

from PIL import Image, ImageDraw, ImageFont
import sys

def add_watermark_custom(image_path, output_path, text, position='BR', 
                        opacity=0.5, color=(255, 255, 255), font_size=40):
    """
    Add a custom watermark to an image.
    
    Parameters:
      image_path: Path to input image
      output_path: Path to save result
      text: Watermark text
      position: 'TL' (top-left), 'TR', 'BL', 'BR' (bottom-right)
      opacity: 0.0 (transparent) to 1.0 (opaque)
      color: RGB tuple (255, 255, 255) = white
      font_size: Size in pixels
    
    Returns:
      True if successful
    """
    
    try:
        # Open image
        img = Image.open(image_path)
        
        # Create transparent watermark layer
        watermark = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark)
        
        # Load font (with fallback)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
        
        # Calculate text position based on corner
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        margin = 10  # pixels from edge
        
        if position == 'TL':  # Top-left
            x, y = margin, margin
        elif position == 'TR':  # Top-right
            x = img.size[0] - text_width - margin
            y = margin
        elif position == 'BL':  # Bottom-left
            x = margin
            y = img.size[1] - text_height - margin
        else:  # BR (bottom-right) - default
            x = img.size[0] - text_width - margin
            y = img.size[1] - text_height - margin
        
        # Draw watermark text with opacity
        alpha_value = int(255 * opacity)
        draw.text((x, y), text, font=font, fill=(*color, alpha_value))
        
        # Convert to RGB and composite
        img_rgb = img.convert('RGB')
        watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)
        
        # Save result
        watermarked.convert('RGB').save(output_path, 'JPEG', quality=95)
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# TEST CASES
if __name__ == "__main__":
    print("Challenge 1.1: Text Watermark - SOLUTION INCLUDED")
    print("")
    print("COMPLETED IMPLEMENTATION:")
    print("✅ Position selection (TL, TR, BL, BR)")
    print("✅ Custom opacity control")
    print("✅ Custom color support")
    print("✅ Font size adjustment")
    print("✅ Error handling")
    print("")
    
    # Example usage
    if len(sys.argv) > 1:
        input_image = sys.argv[1]
        output_image = sys.argv[2] if len(sys.argv) > 2 else "watermarked_output.jpg"
        text = sys.argv[3] if len(sys.argv) > 3 else "WATERMARK"
        
        print(f"Adding watermark to: {input_image}")
        if add_watermark_custom(input_image, output_image, text, position='BR', 
                               opacity=0.7, color=(255, 255, 255), font_size=48):
            print(f"✅ Success! Saved to: {output_image}")
        else:
            print("❌ Failed to watermark image")
    else:
        print("Usage: python3 1_text_watermark.py input.jpg output.jpg 'TEXT'")
        print("")
        print("STUDY THIS CODE:")
        print("1. How does position work?")
        print("2. How is opacity applied?")
        print("3. How does color RGB tuple work?")
        print("4. Try different positions and opacities!")
        print("")
        print("CHALLENGE: Modify this to add watermarks with:")
        print("  • Rotation (angled watermarks)")
        print("  • Shadow effect")
        print("  • Multiple watermarks at once")
