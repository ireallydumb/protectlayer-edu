#!/usr/bin/env python3
"""
Layer 2 Project: Build a Batch Image Watermarking System

Create a system that:
  1. Takes a directory of images
  2. Adds watermarks to all of them
  3. Saves results to output directory
  4. Generates a report

Requirements:
  • Support multiple image formats (JPG, PNG, etc.)
  • Add customizable watermarks (text, logo, pattern)
  • Preserve image quality
  • Handle errors gracefully
  • Log all operations

Bonus:
  • Add configuration file support
  • Implement dry-run mode
  • Create progress bar
  • Generate HTML report
"""

import os
from pathlib import Path

class ImageWatermarker:
    """Batch image watermarking system"""
    
    def __init__(self, input_dir, output_dir, watermark_text):
        """Initialize watermarker"""
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.watermark_text = watermark_text
        
    def watermark_batch(self):
        """Watermark all images in input directory"""
        # TODO: Implement
        pass
    
    def add_watermark_to_image(self, image_path):
        """Add watermark to single image"""
        # TODO: Implement
        pass
    
    def generate_report(self):
        """Generate processing report"""
        # TODO: Implement
        pass

# Main
if __name__ == "__main__":
    watermarker = ImageWatermarker(
        input_dir="./input_images",
        output_dir="./output_images",
        watermark_text="PROTECTED"
    )
    
    watermarker.watermark_batch()
    watermarker.generate_report()
