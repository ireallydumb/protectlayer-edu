#!/usr/bin/env python3
"""
Layer 3: Invisible Protection - INTERACTIVE TUTORIAL
Learn steganography: hide data invisibly in images

This tutorial covers:
1. LSB (Least Significant Bit) embedding
2. Message capacity calculation
3. Data extraction
4. Robustness testing
5. Multi-layer hiding
"""

import sys
from pathlib import Path

class Layer3Tutorial:
    """Interactive Invisible Protection Tutorial"""
    
    def __init__(self):
        self.completed = []
    
    def intro(self):
        """Introduction to Layer 3"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    LAYER 3: Invisible Protection - Interactive Tutorial        ║
║                                                                ║
║    Learn to hide data invisibly in images (Steganography)     ║
╚════════════════════════════════════════════════════════════════╝

Welcome to Layer 3!

Layer 2 taught you VISIBLE watermarks.
Layer 3 teaches you INVISIBLE watermarks.

Key difference:
  • Layer 2: Everyone can see the watermark
  • Layer 3: Only those who know where to look can find it

Invisible watermarks use STEGANOGRAPHY:
  Hiding data inside other data so it's imperceptible.

ADVANTAGES:
  ✅ Not visible to casual observers
  ✅ Can hide more information
  ✅ Harder to remove
  ⚠️  More complex to implement

DISADVANTAGES:
  ❌ Not obvious (doesn't deter casual copying)
  ❌ More computational overhead
  ❌ Can be destroyed by format conversion

REAL-WORLD USES:
  • Digital watermarking (copyright info embedded)
  • Covert communication
  • Data integrity verification
  • Secret message transmission
  • Forensic marking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU'LL LEARN:
  ✅ LSB steganography basics
  ✅ Binary data encoding
  ✅ Message capacity calculation
  ✅ Data extraction
  ✅ Robustness & compression
  ✅ Multi-layer hiding

TIME: ~45 minutes
DIFFICULTY: Intermediate

Let's start!
        """)
    
    def exercise_1_lsb_basics(self):
        """Exercise 1: LSB embedding basics"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    EXERCISE 1: LSB Basics - Hiding Data in the Least Bit       ║
╚════════════════════════════════════════════════════════════════╝

THE CONCEPT:
Every pixel in a digital image is represented by numbers (0-255).
The Least Significant Bit (LSB) is the rightmost bit.

Changing the LSB:
  • Changes the pixel value by 1 (254 → 255 or 100 → 101)
  • Nearly invisible to human eyes
  • Perfect for hiding data

EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pixel value: 100 (binary: 01100100)
  LSB = 0 (the rightmost digit)

To hide bit '1':
  100 → 101 (change LSB from 0 to 1)
  Change: only +1 in value
  Visual difference: INVISIBLE

To hide bit '0':
  100 → 100 (already 0, no change needed)

HUMAN PERCEPTION:
  100 vs 101 = Almost indistinguishable
  Our eyes can't see a 1-pixel difference!

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def hide_bit_in_pixel(pixel_value, bit_to_hide):
    '''Hide a single bit in a pixel'''
    
    # Remove the LSB and set it to our bit
    cleaned = pixel_value & 0xFE  # Clear the LSB
    result = cleaned | int(bit_to_hide)  # Set LSB to our bit
    
    return result

def extract_bit_from_pixel(pixel_value):
    '''Extract the hidden bit from a pixel'''
    
    return pixel_value & 0x01  # Get just the LSB

# EXAMPLES:
# Hide bit 1 in pixel 100:
hidden = hide_bit_in_pixel(100, 1)  # Returns 101

# Extract it back:
extracted = extract_bit_from_pixel(101)  # Returns 1

# Hide bit 0 in pixel 50:
hidden = hide_bit_in_pixel(50, 0)  # Returns 50

print(f"Original: 100, Hidden: {hidden}, Extracted: {extracted}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Create lsb_basics.py with the code above
2. Run it
3. Try hiding different bits
4. Verify you can extract them correctly
5. Notice: data is perfectly recoverable!

KEY INSIGHT:
  • We can hide 1 bit per pixel
  • Changes are minimal (±1 in value)
  • 100% recoverable
  • 300x600 image = 180,000 bits = 22.5 KB of hidden data

✅ WHAT YOU LEARNED:
  • How LSB steganography works
  • Bit manipulation in Python
  • Why it's invisible to humans
  • Basic hide/extract operations
        """)
        
        input("\nPress Enter when you've tried Exercise 1...")
        self.completed.append("Exercise 1: LSB Basics")
    
    def exercise_2_message_encoding(self):
        """Exercise 2: Encode messages in binary"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 2: Message Encoding - Convert Text to Binary        ║
╚════════════════════════════════════════════════════════════════╝

THE CHALLENGE:
We can hide 1 bit per pixel.
But we want to hide TEXT (letters, numbers, symbols).
How do we convert text to bits?

ANSWER: ASCII/Unicode encoding

HOW IT WORKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each character is represented by a number:
  'A' = 65 = 01000001 (8 bits)
  'B' = 66 = 01000010 (8 bits)
  'H' = 72 = 01001000 (8 bits)
  'i' = 105 = 01101001 (8 bits)

To hide "Hi":
  'H' = 72 = 01001000 (need 8 pixels)
  'i' = 105 = 01101001 (need 8 pixels)
  Total: 16 pixels for 2 characters

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def text_to_binary(text):
    '''Convert text to binary string'''
    
    binary = ''
    for char in text:
        # Convert character to ASCII number
        ascii_val = ord(char)
        # Convert number to 8-bit binary
        binary_char = format(ascii_val, '08b')
        binary += binary_char
    
    return binary

def binary_to_text(binary):
    '''Convert binary string back to text'''
    
    text = ''
    for i in range(0, len(binary), 8):
        # Take 8 bits at a time
        byte = binary[i:i+8]
        if len(byte) == 8:  # Make sure we have a full byte
            ascii_val = int(byte, 2)  # Convert binary to decimal
            text += chr(ascii_val)  # Convert ASCII to character
    
    return text

# EXAMPLES:
msg = "SECRET"
binary = text_to_binary(msg)
print(f"'{msg}' in binary: {binary}")
print(f"Length: {len(binary)} bits")
print(f"Needs: {len(binary)} pixels")

# Extract back:
recovered = binary_to_text(binary)
print(f"Recovered: '{recovered}'")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Create message_encoding.py with code above
2. Encode different messages
3. Count how many bits needed
4. Calculate pixels required
5. Test encoding/decoding

CAPACITY CALCULATION:
  Message "Hello" = 5 chars × 8 bits = 40 bits
  Need: 40 pixels minimum
  In 300x600 image: Can hide ~180,000 bits = 22.5 KB text!

✅ WHAT YOU LEARNED:
  • Text to binary conversion
  • Character encoding (ASCII)
  • Message capacity calculation
  • Lossless compression (100% recovery)
        """)
        
        input("\nPress Enter when you've tried Exercise 2...")
        self.completed.append("Exercise 2: Message Encoding")
    
    def exercise_3_full_embedding(self):
        """Exercise 3: Full hide and extract"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║  EXERCISE 3: Full Implementation - Hide and Extract Messages   ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Combine everything: LSB + encoding to hide complete messages.

COMPLETE CODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image
import numpy as np

def hide_message(image_path, message, output_path):
    '''Hide message in image LSBs'''
    
    img = Image.open(image_path)
    pixels = np.array(img)
    flat = pixels.flatten()
    
    # Encode message to binary
    binary = ''.join(format(ord(c), '08b') for c in message)
    
    # Add length header (first 16 bits = message length)
    length_binary = format(len(message), '016b')
    full_binary = length_binary + binary
    
    # Check capacity
    if len(full_binary) > len(flat):
        print("❌ Message too long!")
        return False
    
    # Hide bits
    for i, bit in enumerate(full_binary):
        flat[i] = (flat[i] & 0xFE) | int(bit)
    
    # Save
    result = flat.reshape(pixels.shape)
    result_img = Image.fromarray(result.astype('uint8'))
    result_img.save(output_path)
    
    print(f"✅ Hidden: {len(message)} chars = {len(binary)} bits")
    return True

def extract_message(image_path):
    '''Extract message from image LSBs'''
    
    img = Image.open(image_path)
    pixels = np.array(img)
    flat = pixels.flatten()
    
    # Extract all LSBs
    binary = ''.join(str(p & 0x01) for p in flat)
    
    # Extract length (first 16 bits)
    length = int(binary[:16], 2)
    
    # Extract message (next bits)
    msg_binary = binary[16:16+(length*8)]
    
    # Decode
    message = ''
    for i in range(0, len(msg_binary), 8):
        byte = msg_binary[i:i+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))
    
    return message

# USE IT:
# hide_message('image.jpg', 'Hello World!', 'hidden.jpg')
# extracted = extract_message('hidden.jpg')
# print(f"Extracted: '{extracted}'")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Create full_embedding.py with code above
2. Create a test image (or use existing one)
3. Hide a message in it
4. Extract it back
5. Verify it matches perfectly!

WHAT TO TRY:
  • Short message: "HI"
  • Medium: "Hello, World!"
  • Longer: Full sentences
  • Special characters: "Test!@#$%"

RESULT:
You now have a working steganography system!

✅ WHAT YOU LEARNED:
  • Complete hide/extract pipeline
  • Length-header encoding
  • Capacity management
  • File I/O with PIL
  • Practical steganography
        """)
        
        input("\nPress Enter when you've tried Exercise 3...")
        self.completed.append("Exercise 3: Full Embedding")
    
    def exercise_4_robustness(self):
        """Exercise 4: Test compression robustness"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║   EXERCISE 4: Robustness Testing - Surviving Compression       ║
╚════════════════════════════════════════════════════════════════╝

THE PROBLEM:
LSB steganography is fragile!

When images are compressed (JPEG), LSBs are destroyed.
Your hidden message might not survive.

COMPRESSION EFFECTS:
  Original: PNG (lossless) = message preserved ✅
  Compressed: JPEG quality 95 = might survive ⚠️
  Compressed: JPEG quality 85 = often destroyed ❌

TEST CODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image

def test_robustness(stego_image_path, message):
    '''Test if hidden message survives compression'''
    
    img = Image.open(stego_image_path)
    
    results = {}
    
    # Test 1: PNG (lossless)
    img.save('/tmp/test_png.png')
    png_img = Image.open('/tmp/test_png.png')
    # Compare - should be identical
    
    # Test 2: JPEG quality 95 (high quality)
    img.save('/tmp/test_q95.jpg', quality=95)
    
    # Test 3: JPEG quality 85 (medium)
    img.save('/tmp/test_q85.jpg', quality=85)
    
    # Test 4: JPEG quality 70 (low)
    img.save('/tmp/test_q70.jpg', quality=70)
    
    print("Robustness Test Results:")
    print("  PNG (lossless): ✅ Will preserve LSBs")
    print("  JPEG Q95: ⚠️  Might survive")
    print("  JPEG Q85: ❌ Likely destroyed")
    print("  JPEG Q70: ❌ Definitely destroyed")
    
    return results

# USE IT:
# test_robustness('hidden.png', 'Hello')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Hide a message in PNG format
2. Save it as PNG (lossless)
3. Save it as JPEG (various qualities)
4. Try to extract from each
5. See where message survives/dies

KEY INSIGHT:
For robust steganography:
  ✅ Use PNG format (lossless)
  ❌ Avoid JPEG (lossy compression)
  ⚠️  If using JPEG, use high quality (95+)

BETTER APPROACH:
Multiple layers + error correction can improve robustness.

✅ WHAT YOU LEARNED:
  • Lossy vs. lossless compression
  • LSB fragility under compression
  • Format selection for steganography
  • Robustness testing methods
        """)
        
        input("\nPress Enter when you've tried Exercise 4...")
        self.completed.append("Exercise 4: Robustness Testing")
    
    def summary(self):
        """Summary of Layer 3"""
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║    LAYER 3: INVISIBLE PROTECTION - SUMMARY                     ║
╚════════════════════════════════════════════════════════════════╝

CONGRATULATIONS! You've completed Layer 3

EXERCISES COMPLETED:
        """)
        
        for i, exercise in enumerate(self.completed, 1):
            print(f"  {i}. ✅ {exercise}")
        
        print(f"""
KEY SKILLS MASTERED:
  ✅ LSB steganography
  ✅ Binary encoding
  ✅ Message hiding & extraction
  ✅ Capacity calculation
  ✅ Robustness testing
  ✅ Compression effects

YOU CAN NOW:
  • Hide messages in images invisibly
  • Calculate capacity requirements
  • Extract hidden data perfectly
  • Test steganography robustness
  • Understand format limitations

STEGANOGRAPHY vs. CRYPTOGRAPHY:
  Steganography: Hide that data exists
  Cryptography: Make data unreadable if found

Layer 3 = Steganography (hiding)
Layer 5 = Cryptography (encryption)

REAL-WORLD APPLICATIONS:
  • Covert communication
  • Copyright watermarking
  • Data integrity marking
  • Secret message transmission
  • Forensic evidence embedding

NEXT: Layer 4 - Device Protection (Fingerprinting)

Ready to learn hardware-level protection?
Run: python3 ../layer4_device/tutorial.py
        """)
    
    def run(self):
        """Run the complete tutorial"""
        self.intro()
        
        input("\nPress Enter to begin Exercise 1...")
        self.exercise_1_lsb_basics()
        
        input("\nPress Enter to begin Exercise 2...")
        self.exercise_2_message_encoding()
        
        input("\nPress Enter to begin Exercise 3...")
        self.exercise_3_full_embedding()
        
        input("\nPress Enter to begin Exercise 4...")
        self.exercise_4_robustness()
        
        input("\nPress Enter to see summary...")
        self.summary()

if __name__ == "__main__":
    tutorial = Layer3Tutorial()
    tutorial.run()
