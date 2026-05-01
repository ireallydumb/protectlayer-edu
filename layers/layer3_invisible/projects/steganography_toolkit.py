#!/usr/bin/env python3
"""
Layer 3 Project: Complete Steganography Toolkit

PRODUCTION-QUALITY STEGANOGRAPHY SYSTEM

Features:
  • Hide/extract messages from images
  • Capacity calculation
  • Multiple image format support
  • Compression testing
  • Batch operations
  • Integrity verification
  • Progress tracking
"""

from PIL import Image
import numpy as np
from pathlib import Path
import json
from datetime import datetime
import sys

class SteganographyToolkit:
    """Complete steganography implementation"""
    
    def __init__(self):
        self.operations = []
        self.capacity_cache = {}
    
    # ─────────────────────────────────────────────────────────────
    # BASIC OPERATIONS
    # ─────────────────────────────────────────────────────────────
    
    def calculate_capacity(self, image_path):
        """Calculate maximum message capacity in bytes"""
        try:
            img = Image.open(image_path)
            pixels = np.array(img).size
            # 1 bit per pixel = 8 bits per byte
            capacity_bits = pixels
            capacity_bytes = capacity_bits // 8
            
            # Reserve 16 bits for length header
            capacity_bytes -= 2
            
            return capacity_bytes
        except Exception as e:
            print(f"Error calculating capacity: {e}")
            return 0
    
    def hide_message(self, image_path, message, output_path):
        """Hide message in image LSBs"""
        try:
            # Validate
            capacity = self.calculate_capacity(image_path)
            if len(message) > capacity:
                print(f"❌ Message too large!")
                print(f"   Message: {len(message)} bytes")
                print(f"   Capacity: {capacity} bytes")
                return False
            
            # Load image
            img = Image.open(image_path)
            pixels = np.array(img).astype(np.uint32)
            flat = pixels.flatten()
            
            # Encode message
            binary = ''.join(format(ord(c), '08b') for c in message)
            length_binary = format(len(message), '016b')
            full_binary = length_binary + binary
            
            # Hide bits
            for i, bit in enumerate(full_binary):
                flat[i] = (flat[i] & 0xFFFFFFFE) | int(bit)
            
            # Save
            result_pixels = flat.reshape(pixels.shape)
            result_img = Image.fromarray(result_pixels.astype(np.uint8))
            
            if output_path.endswith('.png'):
                result_img.save(output_path, 'PNG')
            else:
                result_img.save(output_path, 'JPEG', quality=95)
            
            self.operations.append({
                'operation': 'hide',
                'message_length': len(message),
                'bits_used': len(full_binary),
                'image_path': output_path,
                'timestamp': datetime.now().isoformat()
            })
            
            print(f"✅ Hidden: {len(message)} characters")
            print(f"   Output: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error hiding message: {e}")
            return False
    
    def extract_message(self, image_path):
        """Extract message from image LSBs"""
        try:
            img = Image.open(image_path)
            pixels = np.array(img)
            flat = pixels.flatten()
            
            # Extract LSBs
            binary = ''.join(str(p & 0x01) for p in flat)
            
            # Extract length
            length = int(binary[:16], 2)
            
            # Extract message
            msg_binary = binary[16:16+(length*8)]
            
            # Decode
            message = ''.join(
                chr(int(msg_binary[i:i+8], 2))
                for i in range(0, len(msg_binary), 8)
                if i+8 <= len(msg_binary)
            )
            
            self.operations.append({
                'operation': 'extract',
                'message_length': len(message),
                'image_path': image_path,
                'timestamp': datetime.now().isoformat()
            })
            
            return message
            
        except Exception as e:
            print(f"❌ Error extracting message: {e}")
            return None
    
    # ─────────────────────────────────────────────────────────────
    # ROBUSTNESS TESTING
    # ─────────────────────────────────────────────────────────────
    
    def test_compression_robustness(self, stego_path, message):
        """Test if hidden message survives different compression levels"""
        results = {}
        
        try:
            img = Image.open(stego_path)
            
            # Test PNG (lossless)
            png_path = '/tmp/test_png.png'
            img.save(png_path, 'PNG')
            extracted = self.extract_message(png_path)
            results['PNG'] = {
                'success': extracted == message,
                'format': 'lossless',
                'confidence': 'HIGH' if extracted == message else 'FAILED'
            }
            
            # Test JPEG at different qualities
            for quality in [95, 85, 75]:
                jpeg_path = f'/tmp/test_q{quality}.jpg'
                img.save(jpeg_path, 'JPEG', quality=quality)
                extracted = self.extract_message(jpeg_path)
                
                results[f'JPEG_{quality}'] = {
                    'success': extracted == message,
                    'quality': quality,
                    'format': 'lossy',
                    'confidence': 'HIGH' if extracted == message 
                               else 'MEDIUM' if extracted else 'FAILED'
                }
            
            return results
            
        except Exception as e:
            print(f"❌ Robustness test error: {e}")
            return None
    
    # ─────────────────────────────────────────────────────────────
    # BATCH OPERATIONS
    # ─────────────────────────────────────────────────────────────
    
    def batch_hide_messages(self, input_dir, output_dir, messages_file):
        """Hide multiple messages in multiple images"""
        
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Load message mappings
        with open(messages_file) as f:
            mappings = json.load(f)
        
        results = {'successful': 0, 'failed': 0, 'details': []}
        
        for image_file in input_path.glob('*.jpg'):
            filename = image_file.name
            
            if filename not in mappings:
                continue
            
            message = mappings[filename]['message']
            output_file = output_path / filename
            
            print(f"Processing: {filename}...", end=' ')
            
            if self.hide_message(str(image_file), message, str(output_file)):
                results['successful'] += 1
                results['details'].append({
                    'file': filename,
                    'status': 'success',
                    'message_length': len(message)
                })
                print("✅")
            else:
                results['failed'] += 1
                results['details'].append({
                    'file': filename,
                    'status': 'failed'
                })
                print("❌")
        
        return results
    
    # ─────────────────────────────────────────────────────────────
    # ANALYSIS & REPORTING
    # ─────────────────────────────────────────────────────────────
    
    def analyze_image(self, image_path):
        """Analyze image for hidden data"""
        try:
            img = Image.open(image_path)
            pixels = np.array(img)
            flat = pixels.flatten()
            
            # LSB distribution
            lsbs = flat & 0x01
            ones = lsbs.sum()
            zeros = len(lsbs) - ones
            
            # Chi-square test
            expected = len(lsbs) / 2
            chi_square = ((ones - expected)**2 + (zeros - expected)**2) / expected
            
            # Entropy
            unique, counts = np.unique(flat, return_counts=True)
            probs = counts / len(flat)
            entropy = -np.sum(probs * np.log2(probs + 1e-10))
            
            return {
                'file': image_path,
                'dimensions': img.size,
                'pixels': len(flat),
                'lsb_ones_percent': (ones / len(lsbs)) * 100,
                'chi_square': chi_square,
                'entropy': entropy,
                'likely_steganography': chi_square > 100,
                'capacity_bytes': (len(flat) // 8) - 2
            }
            
        except Exception as e:
            print(f"❌ Analysis error: {e}")
            return None
    
    def generate_report(self):
        """Generate summary report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_operations': len(self.operations),
            'operations': self.operations,
            'summary': {
                'hide_operations': sum(1 for o in self.operations 
                                     if o['operation'] == 'hide'),
                'extract_operations': sum(1 for o in self.operations 
                                        if o['operation'] == 'extract'),
            }
        }
        
        return report

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMMAND-LINE INTERFACE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    toolkit = SteganographyToolkit()
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 3: STEGANOGRAPHY TOOLKIT - PROJECT                  ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  python3 steganography_toolkit.py <command> [options]

COMMANDS:
  capacity <image>
    Calculate message capacity for image
    
  hide <image> <message> <output>
    Hide message in image
    
  extract <image>
    Extract hidden message from image
    
  analyze <image>
    Analyze image for hidden data
    
  test-robustness <image> <message>
    Test if message survives compression

EXAMPLES:
  python3 steganography_toolkit.py capacity photo.jpg
  python3 steganography_toolkit.py hide photo.jpg "Secret message" hidden.jpg
  python3 steganography_toolkit.py extract hidden.jpg
  python3 steganography_toolkit.py analyze hidden.jpg
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "capacity":
        image = sys.argv[2]
        capacity = toolkit.calculate_capacity(image)
        print(f"Capacity: {capacity} bytes ({capacity * 8} bits)")
    
    elif command == "hide":
        image = sys.argv[2]
        message = sys.argv[3]
        output = sys.argv[4]
        toolkit.hide_message(image, message, output)
    
    elif command == "extract":
        image = sys.argv[2]
        message = toolkit.extract_message(image)
        if message:
            print(f"Extracted: '{message}'")
    
    elif command == "analyze":
        image = sys.argv[2]
        analysis = toolkit.analyze_image(image)
        if analysis:
            print(json.dumps(analysis, indent=2))
    
    elif command == "test-robustness":
        image = sys.argv[2]
        message = sys.argv[3]
        results = toolkit.test_compression_robustness(image, message)
        print(json.dumps(results, indent=2))
    
    else:
        print(f"Unknown command: {command}")
