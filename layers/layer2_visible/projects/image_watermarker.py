#!/usr/bin/env python3
"""
Layer 2 Project: Batch Image Watermarking System

COMPLETE WORKING IMPLEMENTATION

Build a system that:
1. Takes a directory of images
2. Adds watermarks to all
3. Saves to output directory
4. Generates a report
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
from datetime import datetime

class BatchWatermarker:
    """Complete batch watermarking system"""
    
    def __init__(self, input_dir, output_dir, watermark_text="PROTECTED"):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.watermark_text = watermark_text
        self.processed = []
        self.failed = []
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def watermark_image(self, image_path):
        """Watermark a single image"""
        try:
            img = Image.open(image_path)
            
            # Create watermark layer
            watermark = Image.new('RGBA', img.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(watermark)
            
            # Try to load font
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            except:
                try:
                    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
                except:
                    font = ImageFont.load_default()
            
            # Calculate position (bottom right)
            text_bbox = draw.textbbox((0, 0), self.watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            x = img.size[0] - text_width - 10
            y = img.size[1] - text_height - 10
            
            # Draw watermark
            draw.text((x, y), self.watermark_text, font=font, 
                     fill=(255, 255, 255, int(255 * 0.7)))
            
            # Composite
            img_rgb = img.convert('RGB')
            watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)
            
            # Save
            output_path = self.output_dir / image_path.name
            watermarked.convert('RGB').save(output_path, 'JPEG', quality=95)
            
            return True, str(output_path)
        
        except Exception as e:
            return False, str(e)
    
    def process_batch(self):
        """Process all images in directory"""
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        
        images = [f for f in self.input_dir.iterdir() 
                 if f.is_file() and f.suffix.lower() in image_extensions]
        
        print(f"Processing {len(images)} images...")
        
        for image_path in images:
            success, result = self.watermark_image(image_path)
            
            if success:
                self.processed.append({
                    'input': str(image_path),
                    'output': result,
                    'status': 'success'
                })
                print(f"  ✅ {image_path.name}")
            else:
                self.failed.append({
                    'input': str(image_path),
                    'error': result,
                    'status': 'failed'
                })
                print(f"  ❌ {image_path.name}: {result}")
    
    def generate_report(self):
        """Generate processing report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'watermark_text': self.watermark_text,
            'total_processed': len(self.processed),
            'total_failed': len(self.failed),
            'success_rate': (len(self.processed) / (len(self.processed) + len(self.failed)) * 100) if (len(self.processed) + len(self.failed)) > 0 else 0,
            'processed_files': self.processed,
            'failed_files': self.failed
        }
        
        report_path = self.output_dir / "watermarking_report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report

# MAIN USAGE
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("LAYER 2 PROJECT: Batch Image Watermarking System")
        print("")
        print("Usage: python3 image_watermarker.py <input_dir> [output_dir] [watermark_text]")
        print("")
        print("Examples:")
        print("  python3 image_watermarker.py ./input_images")
        print("  python3 image_watermarker.py ./images ./watermarked 'CONFIDENTIAL'")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./watermarked_output"
    watermark_text = sys.argv[3] if len(sys.argv) > 3 else "PROTECTED"
    
    watermarker = BatchWatermarker(input_dir, output_dir, watermark_text)
    watermarker.process_batch()
    report = watermarker.generate_report()
    
    print("")
    print("✅ REPORT:")
    print(f"  Processed: {report['total_processed']}")
    print(f"  Failed: {report['total_failed']}")
    print(f"  Success Rate: {report['success_rate']:.1f}%")
    print(f"  Report: {output_dir}/watermarking_report.json")
