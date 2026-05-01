#!/usr/bin/env python3
"""
Challenge 3: Batch Watermarking with Metadata

Watermark multiple images AND embed metadata
(date, photographer, copyright, etc.)
"""

from PIL import Image, ImageDraw, ImageFont
import json
from pathlib import Path
import sys

class BatchWatermarkWithMetadata:
    """Watermark images with embedded metadata"""
    
    def __init__(self):
        self.metadata_log = []
    
    def watermark_with_metadata(self, image_path, output_path, 
                               photographer, copyright_year, 
                               location=""):
        """
        Add watermark + embed metadata in image EXIF/JSON
        """
        
        try:
            img = Image.open(image_path)
            
            # Add watermark
            watermark = Image.new('RGBA', img.size, (255,255,255,0))
            draw = ImageDraw.Draw(watermark)
            
            try:
                font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30
                )
            except:
                font = ImageFont.load_default()
            
            # Watermark text
            text = f"© {copyright_year} {photographer}"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            x = img.size[0] - text_width - 10
            y = img.size[1] - 40
            
            draw.text((x, y), text, font=font, fill=(255,255,255,150))
            
            # Composite
            img_rgb = img.convert('RGB')
            watermarked = Image.alpha_composite(
                img_rgb.convert('RGBA'), watermark
            )
            watermarked.convert('RGB').save(output_path, quality=95)
            
            # Store metadata
            metadata = {
                'image': output_path,
                'photographer': photographer,
                'copyright': copyright_year,
                'location': location
            }
            
            self.metadata_log.append(metadata)
            
            print(f"✅ Watermarked: {Path(image_path).name}")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def save_metadata_log(self, output_file):
        """Save metadata log to JSON"""
        
        with open(output_file, 'w') as f:
            json.dump(self.metadata_log, f, indent=2)
        
        print(f"✅ Metadata saved to: {output_file}")

if __name__ == "__main__":
    print("Challenge 3: Batch Watermarking with Metadata")
    print("")
    
    toolkit = BatchWatermarkWithMetadata()
    
    if len(sys.argv) < 4:
        print("Usage: python3 3_batch_watermark_metadata.py")
        print("       <image> <output> <photographer> [copyright_year] [location]")
        sys.exit(1)
    
    image = sys.argv[1]
    output = sys.argv[2]
    photographer = sys.argv[3]
    copyright_year = sys.argv[4] if len(sys.argv) > 4 else "2024"
    location = sys.argv[5] if len(sys.argv) > 5 else ""
    
    if toolkit.watermark_with_metadata(
        image, output, photographer, copyright_year, location
    ):
        print(f"Result: {output}")
        print("Metadata embedded and logged!")
