#!/usr/bin/env python3
"""
Layer 1: Detection - INTERACTIVE TUTORIAL
Learn to detect watermarks and protected content

This tutorial provides hands-on exercises to understand how to:
1. Identify visible watermarks
2. Detect hidden watermarks
3. Analyze protection mechanisms
4. Verify authenticity
"""

import os
import sys
from pathlib import Path

class InteractiveTutorial:
    """Interactive Detection Tutorial"""
    
    def __init__(self):
        self.completed = []
        self.current_exercise = 0
    
    def intro(self):
        """Start the tutorial"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║           LAYER 1: DETECTION - Interactive Tutorial            ║
║                                                                ║
║  Learn to identify and detect watermarks and DRM protections  ║
╚════════════════════════════════════════════════════════════════╝

Welcome! In this layer, you'll learn the DETECTION phase of DRM:
how to identify when content is protected.

This is the first line of defense - recognizing protection exists
is the first step toward understanding it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU'LL LEARN:
  ✅ Visible watermark detection
  ✅ Hidden data detection  
  ✅ Protection mechanism identification
  ✅ Authenticity verification
  ✅ Threat analysis

TIME: ~30 minutes
DIFFICULTY: Beginner → Intermediate

Let's start!
        """)
    
    def exercise_1_visible_watermarks(self):
        """Exercise 1: Detect visible watermarks"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║         EXERCISE 1: Detecting Visible Watermarks               ║
╚════════════════════════════════════════════════════════════════╝

SCENARIO:
You have an image that may contain visible watermarks (like text
overlays, logos, or stamps). How would you detect them?

DETECTION METHODS:
1. Visual inspection - Look for text/logos on images
2. Color analysis - Watermarks often use different colors
3. Edge detection - Watermarks have distinct edges
4. Histogram analysis - Different pixel distribution

HANDS-ON EXERCISE:
Let's create a simple visible watermark detection function:
        """)
        
        self.show_code_example_1()
        
        print("""
KEY CONCEPTS:
  • Watermarks modify pixel colors
  • Text watermarks have distinct font patterns
  • Edges in images show where watermarks are
  • Color histograms reveal modifications

WHAT YOU LEARNED:
  ✅ How to detect visible watermarks programmatically
  ✅ Why color space analysis works
  ✅ How edge detection helps find watermarks

NEXT: Let's move to hidden watermarks...
        """)
        
        self.current_exercise += 1
        self.completed.append("Exercise 1: Visible Watermarks")
    
    def show_code_example_1(self):
        """Show detection code example"""
        print("""
DETECTION CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image
import numpy as np

def detect_visible_watermark(image_path):
    '''Detect visible watermarks in image'''
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Method 1: Color Anomaly Detection
    # Watermarks often use bright colors (white, red, etc.)
    
    red_channel = pixels[:,:,0]    # Red pixels
    white_pixels = (pixels[:,:,0] > 200) & \\
                   (pixels[:,:,1] > 200) & \\
                   (pixels[:,:,2] > 200)
    
    watermark_coverage = white_pixels.sum() / white_pixels.size
    
    # Method 2: Edge Detection
    # Watermarks have distinct edges (text boundaries)
    
    from scipy.ndimage import sobel
    edges = sobel(pixels.mean(axis=2))
    edge_density = (edges > np.mean(edges)).sum() / edges.size
    
    # Method 3: Histogram Analysis
    # Compare color distribution
    original_histogram = np.histogram(pixels.flatten(), bins=256)[0]
    
    results = {
        'has_watermark': watermark_coverage > 0.05,
        'watermark_coverage': watermark_coverage * 100,
        'edge_density': edge_density * 100,
        'likely_modified': edge_density > 0.3
    }
    
    return results

# Try it:
# result = detect_visible_watermark('image.jpg')
# print(f"Watermark detected: {result['has_watermark']}")
# print(f"Coverage: {result['watermark_coverage']:.2f}%")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Save this code as detect_watermark.py
2. Run it on an image with a watermark
3. Observe the results
4. Try adjusting the thresholds (0.05, 0.3)
5. See how detection changes
        """)
    
    input("Press Enter to continue...")
    
    def exercise_2_hidden_watermarks(self):
        """Exercise 2: Detect hidden data"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║      EXERCISE 2: Detecting Hidden Data (Steganography)         ║
╚════════════════════════════════════════════════════════════════╝

SCENARIO:
Someone hid data in the Least Significant Bits (LSBs) of an image.
You can't see it, but it's there. How would you know?

DETECTION METHODS:
1. Statistical analysis - Random data has different statistics
2. Entropy analysis - LSB data increases entropy
3. Steganalysis - Specialized techniques to detect hidden data
4. Noise patterns - Hidden data creates patterns

KEY INSIGHT:
When data is hidden in LSBs, it changes the statistical properties
of the image. We can detect this mathematically.
        """)
        
        self.show_code_example_2()
        
        print("""
WHAT YOU LEARNED:
  ✅ How LSB steganography works
  ✅ Why hidden data changes statistics
  ✅ How to detect hidden data without seeing it
  ✅ Statistical methods for steganography detection

IMPORTANT:
  • Not all steganography is detectable
  • Better hiding uses sophisticated techniques
  • But statistical analysis can reveal patterns

NEXT: Protection mechanism identification...
        """)
        
        self.current_exercise += 1
        self.completed.append("Exercise 2: Hidden Watermarks")
    
    def show_code_example_2(self):
        """Show hidden data detection code"""
        print("""
HIDDEN DATA DETECTION CODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image
import numpy as np
from scipy import stats

def detect_hidden_data(image_path):
    '''Detect hidden data in LSBs'''
    
    img = Image.open(image_path)
    pixels = np.array(img).flatten()
    
    # Method 1: LSB Distribution
    # Extract LSBs (rightmost bits)
    lsbs = pixels & 0x01  # Get last bit of each pixel
    
    # Normal image LSBs are roughly 50/50 (0s and 1s)
    # If data is hidden, distribution changes
    lsb_ones = lsbs.sum()
    lsb_zeros = len(lsbs) - lsb_ones
    
    chi_square = ((lsb_ones - len(lsbs)/2)**2 + 
                  (lsb_zeros - len(lsbs)/2)**2) / (len(lsbs)/2)
    
    # Method 2: Entropy Analysis
    # Higher entropy = more random = likely hidden data
    unique, counts = np.unique(pixels, return_counts=True)
    probabilities = counts / len(pixels)
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
    
    # Normal: ~7.5 bits entropy
    # With hidden data: higher entropy
    
    results = {
        'lsb_distribution': {
            'ones': lsb_ones,
            'zeros': lsb_zeros,
            'chi_square': chi_square
        },
        'entropy': entropy,
        'likely_steganography': chi_square > 100 or entropy > 7.8,
        'confidence': min(100, (chi_square - 50) * 0.5)
    }
    
    return results

# Try it:
# result = detect_hidden_data('image.png')
# if result['likely_steganography']:
#     print("⚠️  Hidden data detected!")
#     print(f"Confidence: {result['confidence']:.0f}%")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Create an image with hidden data (use Layer 3 code)
2. Run this detection on it
3. Try on images WITHOUT hidden data
4. See the difference in chi-square scores
5. Adjust thresholds to tune detection
        """)
        
        input("Press Enter to continue...")
    
    def exercise_3_protection_analysis(self):
        """Exercise 3: Analyze protection mechanisms"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    EXERCISE 3: Analyzing Protection Mechanisms                 ║
╚════════════════════════════════════════════════════════════════╝

SCENARIO:
You encounter protected content. How do you identify WHAT
protection was used?

TYPES OF PROTECTION:
1. Visible Watermarks - You can see them
2. Invisible Watermarks - LSB, frequency domain, etc.
3. Fingerprinting - Device ID embedded
4. Cryptographic Signing - Digital signature for verification
5. Encryption - Content is scrambled

ANALYSIS STRATEGY:
1. Check for visible marks
2. Analyze statistical properties
3. Examine file metadata
4. Try to extract watermark info
5. Identify the protection layer

HANDS-ON:
Let's build a protection analyzer:
        """)
        
        self.show_code_example_3()
        
        print("""
WHAT YOU LEARNED:
  ✅ How to analyze protection types
  ✅ Multi-layer detection approach
  ✅ File metadata examination
  ✅ Statistical fingerprinting

REAL-WORLD APPLICATION:
When you encounter protected content:
1. Look for visible marks
2. Check metadata
3. Analyze statistics
4. Run appropriate detection
5. Document findings

NEXT: Practical verification...
        """)
        
        self.current_exercise += 1
        self.completed.append("Exercise 3: Protection Analysis")
    
    def show_code_example_3(self):
        """Show protection analysis code"""
        print("""
PROTECTION ANALYZER CODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image
import numpy as np
import os
from datetime import datetime

def analyze_protection(image_path):
    '''Comprehensive protection analysis'''
    
    img = Image.open(image_path)
    pixels = np.array(img).flatten()
    
    # Analysis 1: Metadata
    metadata = {
        'file_size': os.path.getsize(image_path),
        'format': Image.open(image_path).format,
        'size': Image.open(image_path).size,
        'modified': datetime.fromtimestamp(
            os.path.getmtime(image_path)
        )
    }
    
    # Analysis 2: Visible Watermarks
    img_array = np.array(img)
    white_pixels = (img_array[:,:,0] > 200) & \\
                   (img_array[:,:,1] > 200) & \\
                   (img_array[:,:,2] > 200)
    visible_coverage = white_pixels.sum() / white_pixels.size
    
    # Analysis 3: Statistical Anomalies
    lsbs = pixels & 0x01
    lsb_ones = lsbs.sum()
    chi_square = ((lsb_ones - len(lsbs)/2)**2) / (len(lsbs)/2)
    
    # Analysis 4: Entropy
    unique, counts = np.unique(pixels, return_counts=True)
    probabilities = counts / len(pixels)
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
    
    # Conclusions
    protections_detected = []
    
    if visible_coverage > 0.05:
        protections_detected.append(
            "Visible Watermark (confidence: HIGH)"
        )
    
    if chi_square > 100:
        protections_detected.append(
            "Hidden Data/Steganography (confidence: MEDIUM)"
        )
    
    if entropy > 7.8:
        protections_detected.append(
            "Possible Encryption (confidence: LOW)"
        )
    
    if len(protections_detected) == 0:
        protections_detected.append("No obvious protection detected")
    
    return {
        'metadata': metadata,
        'visible_watermark': visible_coverage > 0.05,
        'watermark_coverage': visible_coverage * 100,
        'entropy': entropy,
        'lsb_anomaly': chi_square > 100,
        'protections_detected': protections_detected,
        'protection_layers': len(protections_detected)
    }

# Try it:
# analysis = analyze_protection('protected_image.jpg')
# print(f"Protections found: {analysis['protection_layers']}")
# for protection in analysis['protections_detected']:
#     print(f"  • {protection}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Collect different protected images
2. Run analyzer on each
3. Document what's detected
4. Try to identify protection layers
5. Build your detection skills
        """)
        
        input("Press Enter to continue...")
    
    def exercise_4_practical_verification(self):
        """Exercise 4: Verify protection authenticity"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║         EXERCISE 4: Verifying Protection Authenticity          ║
╚════════════════════════════════════════════════════════════════╝

SCENARIO:
You detect protection on content. How do you VERIFY it's real
and not just someone's failed attempt at protection?

VERIFICATION METHODS:
1. Check for known protection signatures
2. Verify watermark robustness
3. Test for proper implementation
4. Authenticate the source
5. Validate cryptographic signatures

EXAMPLE:
A watermark should survive:
  • Small image crops
  • Compression
  • Color adjustments
  • Rotation (small angles)
  • Brightness/contrast changes

If it doesn't, the protection is weak or fake.
        """)
        
        self.show_code_example_4()
        
        print("""
WHAT YOU LEARNED:
  ✅ How to verify watermark robustness
  ✅ Testing protection implementations
  ✅ Evaluating protection strength
  ✅ Identifying weak protections

KEY INSIGHT:
Not all watermarks are created equal.
Some are strong and survive attacks.
Others are fragile and disappear easily.

THIS COMPLETES LAYER 1:
You now understand how to:
  ✅ Detect visible watermarks
  ✅ Find hidden data
  ✅ Analyze protection mechanisms
  ✅ Verify protection authenticity

NEXT STEPS:
Move to Layer 2 to learn how to CREATE watermarks.

Ready? Run: python3 ../layer2_visible/tutorial.py
        """)
        
        self.current_exercise += 1
        self.completed.append("Exercise 4: Verification")
    
    def show_code_example_4(self):
        """Show verification code"""
        print("""
WATERMARK VERIFICATION CODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from PIL import Image
import numpy as np

def verify_watermark_robustness(original_path, modified_path):
    '''Test if watermark survives modifications'''
    
    original = np.array(Image.open(original_path))
    modified = np.array(Image.open(modified_path))
    
    # Test 1: Compression Resistance
    # Save as JPEG with quality loss
    img = Image.open(original_path)
    img.save('/tmp/test_compressed.jpg', quality=85)
    compressed = np.array(Image.open('/tmp/test_compressed.jpg'))
    
    # Compare: does watermark survive compression?
    pixel_change = np.abs(
        compressed.astype(float) - original.astype(float)
    ).mean()
    
    # Test 2: Crop Resistance  
    # Crop 10% from edges
    h, w = original.shape[:2]
    crop = original[int(h*0.1):int(h*0.9), 
                    int(w*0.1):int(w*0.9)]
    
    # Is watermark still visible/detectable?
    
    # Test 3: Rotation Resistance
    rotated = np.rot90(original)
    
    results = {
        'compression_resistance': pixel_change < 5,
        'pixel_change_on_compression': pixel_change,
        'likely_robust': pixel_change < 10,
        'protection_strength': 'WEAK' if pixel_change > 20 
                               else 'MEDIUM' if pixel_change > 10 
                               else 'STRONG'
    }
    
    return results

# Try it:
# result = verify_watermark_robustness('original.jpg', 'modified.jpg')
# print(f"Protection strength: {result['protection_strength']}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Take a watermarked image
2. Create compressed version (JPEG 85%)
3. Compare them with this code
4. Test robustness
5. Judge protection quality
        """)
        
        input("Press Enter to continue...")
    
    def summary(self):
        """Show summary of completed exercises"""
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║           LAYER 1 TUTORIAL - SUMMARY                           ║
╚════════════════════════════════════════════════════════════════╝

CONGRATULATIONS! You've completed Layer 1: Detection

EXERCISES COMPLETED:
        """)
        
        for i, exercise in enumerate(self.completed, 1):
            print(f"  {i}. ✅ {exercise}")
        
        print(f"""
KEY SKILLS LEARNED:
  ✅ Visible watermark detection
  ✅ Hidden data detection (steganography)
  ✅ Protection mechanism analysis
  ✅ Robustness verification
  ✅ Statistical analysis for protection

YOU CAN NOW:
  • Identify protected content
  • Detect different protection types
  • Analyze protection strength
  • Understand detection techniques
  • Evaluate protection implementations

NEXT: Layer 2 - Creating visible watermarks
  
Ready to learn how to ADD watermarks?
Run: python3 ../layer2_visible/tutorial.py
        """)
    
    def run(self):
        """Run the complete tutorial"""
        self.intro()
        
        input("\nPress Enter to begin Exercise 1...")
        self.exercise_1_visible_watermarks()
        
        input("\nPress Enter to begin Exercise 2...")
        self.exercise_2_hidden_watermarks()
        
        input("\nPress Enter to begin Exercise 3...")
        self.exercise_3_protection_analysis()
        
        input("\nPress Enter to begin Exercise 4...")
        self.exercise_4_practical_verification()
        
        input("\nPress Enter to see summary...")
        self.summary()

if __name__ == "__main__":
    tutorial = InteractiveTutorial()
    tutorial.run()
