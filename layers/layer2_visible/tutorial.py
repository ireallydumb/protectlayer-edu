#!/usr/bin/env python3
"""
Layer 2: Visible Protection - INTERACTIVE TUTORIAL
Learn to add and manage visible watermarks

This tutorial provides hands-on exercises to:
1. Create text watermarks
2. Position watermarks strategically
3. Control watermark opacity
4. Batch process images
5. Verify watermark effectiveness
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import tempfile
import os

class Layer2Tutorial:
    """Interactive Visible Protection Tutorial"""
    
    def __init__(self):
        self.completed = []
        self.temp_dir = tempfile.mkdtemp()
    
    def intro(self):
        """Introduction to Layer 2"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 2: Visible Protection - Interactive Tutorial        ║
║                                                                ║
║    Learn to add visible watermarks and protect content        ║
╚════════════════════════════════════════════════════════════════╝

Welcome to Layer 2!

In Layer 1, you learned to DETECT protection.
Now you'll learn to CREATE visible protection.

Visible watermarks are:
  ✅ Obvious to humans (deter casual copying)
  ✅ Easy to verify (just look at the image)
  ✅ Simple to implement
  ⚠️  Easy to remove with image editing

USE CASES:
  • Copyright marking on photos
  • Photography portfolio watermarks
  • Draft document indicators
  • Branding on social media
  • Version control (draft/final)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU'LL LEARN:
  ✅ Text watermark placement
  ✅ Opacity control
  ✅ Color selection
  ✅ Font management
  ✅ Batch watermarking
  ✅ Quality verification

TIME: ~40 minutes
DIFFICULTY: Beginner → Intermediate

Let's start!
        """)
    
    def exercise_1_basic_watermark(self):
        """Exercise 1: Create basic text watermark"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║       EXERCISE 1: Creating Your First Text Watermark           ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Add a simple text watermark to an image.

STEPS:
1. Load an image (or create a test one)
2. Create a text label
3. Place it on the image
4. Save the result

Let's code this step by step:
        """)
        
        print("""
STEP 1: CREATE OR LOAD AN IMAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# If you don't have an image, create a test one:
from PIL import Image, ImageDraw, ImageFont

# Create a simple test image
test_image = Image.new('RGB', (800, 600), color='white')
test_draw = ImageDraw.Draw(test_image)

# Add some content so we can see the watermark
test_draw.rectangle([50, 50, 750, 550], outline='black', width=2)
test_draw.text((100, 100), "Sample Image for Watermarking", fill='black')

test_image.save('/tmp/test_image.jpg')

# Or load your own image:
img = Image.open('your_image.jpg')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: ADD TEXT WATERMARK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Open the image
img = Image.open('test_image.jpg')

# Create a transparent layer for the watermark
watermark = Image.new('RGBA', img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(watermark)

# Load a font (or use default)
try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 
        size=50
    )
except:
    font = ImageFont.load_default()

# Draw the watermark text
text = "© 2024 PROTECTED"
text_color = (255, 255, 255, 180)  # White, semi-transparent

# Bottom-right corner
x = img.size[0] - 250
y = img.size[1] - 100

draw.text((x, y), text, font=font, fill=text_color)

# Composite the watermark onto the image
img_rgb = img.convert('RGB')
watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)

# Save the result
watermarked.convert('RGB').save('watermarked.jpg', quality=95)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Copy the code above
2. Create test_watermark.py with this code
3. Run it: python3 test_watermark.py
4. Open watermarked.jpg in an image viewer
5. You should see "© 2024 PROTECTED" on the image!

✅ WHAT YOU LEARNED:
  • How to create transparent watermark layers
  • Font loading and text rendering
  • Image compositing (layering)
  • Opacity control (alpha values)
  • Image saving with quality control
        """)
        
        input("\nPress Enter when you've tried Exercise 1...")
        self.completed.append("Exercise 1: Basic Watermark")
    
    def exercise_2_position_control(self):
        """Exercise 2: Control watermark position"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    EXERCISE 2: Positioning Watermarks (Smart Placement)        ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Learn to place watermarks in different positions strategically.

COMMON POSITIONS:
  • Top-left: Visible but non-intrusive
  • Top-right: Copyright indicator style
  • Bottom-left: Professional placement
  • Bottom-right: Most common (expected by viewers)
  • Center: Maximum visibility
  • Diagonal: Difficulty for removal

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def add_watermark_positioned(image_path, text, position='BR'):
    '''Add watermark at specific position'''
    
    img = Image.open(image_path)
    watermark = Image.new('RGBA', img.size, (255,255,255,0))
    draw = ImageDraw.Draw(watermark)
    
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40
        )
    except:
        font = ImageFont.load_default()
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    margin = 20
    
    # Calculate position
    positions = {
        'TL': (margin, margin),                    # Top-left
        'TR': (img.size[0] - text_width - margin, margin),  # Top-right
        'BL': (margin, img.size[1] - text_height - margin),  # Bottom-left
        'BR': (img.size[0] - text_width - margin,           # Bottom-right
               img.size[1] - text_height - margin),
        'CENTER': ((img.size[0] - text_width) // 2,  # Center
                   (img.size[1] - text_height) // 2)
    }
    
    x, y = positions.get(position, positions['BR'])
    
    # Draw watermark
    draw.text((x, y), text, font=font, fill=(255,255,255,200))
    
    # Composite
    img_rgb = img.convert('RGB')
    watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)
    
    return watermarked

# TRY DIFFERENT POSITIONS:
# for pos in ['TL', 'TR', 'BL', 'BR', 'CENTER']:
#     result = add_watermark_positioned('image.jpg', 'PROTECTED', pos)
#     result.convert('RGB').save(f'watermark_{pos}.jpg')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Save code above as position_watermark.py
2. Run it on your test image
3. Generate watermarks at all 5 positions
4. Compare: TL, TR, BL, BR, CENTER
5. Which is most noticeable? Most professional?

STRATEGY TIPS:
  • Bottom-right = Most professional
  • Center = Maximum visibility
  • Top-left = Unobtrusive
  • Diagonal = Hard to remove

✅ WHAT YOU LEARNED:
  • Dynamic position calculation
  • Text dimension measurement
  • Strategic placement for different goals
  • User preference vs. protection strength
        """)
        
        input("\nPress Enter when you've tried Exercise 2...")
        self.completed.append("Exercise 2: Position Control")
    
    def exercise_3_opacity_control(self):
        """Exercise 3: Control watermark opacity"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║    EXERCISE 3: Opacity Control (Visibility vs. Usability)      ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Balance watermark visibility with image usability.

THE CHALLENGE:
  • Too opaque: Watermark covers the content
  • Too transparent: Watermark disappears
  • Just right: Visible but content readable

OPACITY RANGE:
  0 = Completely transparent (invisible)
  128 = 50% transparent (gray)
  255 = Fully opaque (solid)

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def add_watermark_opacity(image_path, text, opacity=0.7):
    '''Add watermark with adjustable opacity'''
    
    img = Image.open(image_path)
    watermark = Image.new('RGBA', img.size, (255,255,255,0))
    draw = ImageDraw.Draw(watermark)
    
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40
        )
    except:
        font = ImageFont.load_default()
    
    # Convert opacity (0.0-1.0) to alpha (0-255)
    alpha = int(255 * opacity)
    text_color = (255, 255, 255, alpha)
    
    # Position (bottom-right)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = img.size[0] - text_width - 20
    y = img.size[1] - text_height - 20
    
    # Draw at specified opacity
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Composite
    img_rgb = img.convert('RGB')
    watermarked = Image.alpha_composite(img_rgb.convert('RGBA'), watermark)
    
    return watermarked

# TEST DIFFERENT OPACITIES:
# for opacity in [0.3, 0.5, 0.7, 0.9]:
#     result = add_watermark_opacity('image.jpg', 'PROTECTED', opacity)
#     result.convert('RGB').save(f'watermark_opacity_{int(opacity*100)}.jpg')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Save code as opacity_watermark.py
2. Create watermarks at: 0.3, 0.5, 0.7, 0.9 opacity
3. Compare all versions side-by-side
4. Which is best? Why?
5. Consider: purpose matters!
   - Social media: Higher opacity (more visible)
   - Professional documents: Lower opacity (less intrusive)
   - Photography portfolio: Medium (balance)

OPACITY GUIDELINES:
  • 0.3-0.4: Barely visible (subtle branding)
  • 0.5-0.6: Light watermark (readable content)
  • 0.7-0.8: Clear watermark (protection-focused)
  • 0.9-1.0: Strong watermark (maximum protection)

✅ WHAT YOU LEARNED:
  • Opacity control in PIL
  • Alpha channel manipulation
  • Balance between protection and usability
  • Context-aware watermarking
        """)
        
        input("\nPress Enter when you've tried Exercise 3...")
        self.completed.append("Exercise 3: Opacity Control")
    
    def exercise_4_batch_watermarking(self):
        """Exercise 4: Batch process multiple images"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║     EXERCISE 4: Batch Processing (Watermark Many Images)       ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Apply the same watermark to many images efficiently.

REAL-WORLD SCENARIO:
You have 500 photos to protect. Add watermark to all of them.

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def batch_watermark(input_dir, output_dir, text, opacity=0.7):
    '''Watermark all images in a directory'''
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    
    successful = 0
    failed = 0
    
    # Process each image
    for image_file in input_path.iterdir():
        if image_file.suffix.lower() not in image_extensions:
            continue
        
        try:
            print(f"Processing: {image_file.name}...", end=' ')
            
            # Load and watermark
            img = Image.open(image_file)
            watermark = Image.new('RGBA', img.size, (255,255,255,0))
            draw = ImageDraw.Draw(watermark)
            
            # Font
            try:
                font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40
                )
            except:
                font = ImageFont.load_default()
            
            # Calculate position
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = img.size[0] - text_width - 20
            y = img.size[1] - text_height - 20
            
            # Draw
            alpha = int(255 * opacity)
            draw.text((x, y), text, font=font, 
                     fill=(255, 255, 255, alpha))
            
            # Composite
            img_rgb = img.convert('RGB')
            watermarked = Image.alpha_composite(
                img_rgb.convert('RGBA'), watermark
            )
            
            # Save
            output_file = output_path / image_file.name
            watermarked.convert('RGB').save(output_file, quality=95)
            
            print("✅")
            successful += 1
            
        except Exception as e:
            print(f"❌ ({e})")
            failed += 1
    
    print(f"\n✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")

# USE IT:
# batch_watermark('./input_images', './watermarked_output', 'PROTECTED')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Save as batch_watermark.py
2. Create a test directory with 3-5 images
3. Run the script
4. Check the output directory
5. Verify all images are watermarked

REAL-WORLD TIPS:
  • Use this for photography collections
  • Automate protection workflows
  • Process photos before uploading
  • Batch in background while you work

✅ WHAT YOU LEARNED:
  • Directory iteration in Python
  • File handling and validation
  • Error handling in batch processes
  • Progress reporting
  • Practical automation
        """)
        
        input("\nPress Enter when you've tried Exercise 4...")
        self.completed.append("Exercise 4: Batch Processing")
    
    def exercise_5_quality_verification(self):
        """Exercise 5: Verify watermark quality"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║     EXERCISE 5: Quality Verification (Did it work?)            ║
╚════════════════════════════════════════════════════════════════╝

GOAL:
Verify that watermarks were properly applied.

QUALITY CHECKS:
1. Visual inspection (does it look good?)
2. File size check (is it reasonable?)
3. Watermark detection (can we detect it?)
4. Metadata verification (info preserved?)

CODE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def verify_watermark(original_path, watermarked_path):
    '''Verify watermark was properly applied'''
    
    import os
    
    original_img = Image.open(original_path)
    watermarked_img = Image.open(watermarked_path)
    
    # Check 1: Size comparison
    orig_size = os.path.getsize(original_path)
    wmrk_size = os.path.getsize(watermarked_path)
    size_increase = ((wmrk_size - orig_size) / orig_size) * 100
    
    # Check 2: Dimensions preserved
    dims_match = (original_img.size == watermarked_img.size)
    
    # Check 3: Pixel difference
    orig_pixels = np.array(original_img)
    wmrk_pixels = np.array(watermarked_img)
    
    # If watermarked, pixels should be different
    pixel_diff = np.mean(
        np.abs(wmrk_pixels.astype(float) - orig_pixels.astype(float))
    )
    
    # Has watermark if pixel difference > 5
    has_watermark = pixel_diff > 5
    
    results = {
        'file_size_original': f"{orig_size / 1024:.1f} KB",
        'file_size_watermarked': f"{wmrk_size / 1024:.1f} KB",
        'size_increase_percent': f"{size_increase:.1f}%",
        'dimensions_match': dims_match,
        'average_pixel_change': f"{pixel_diff:.2f}",
        'watermark_detected': has_watermark,
        'quality': 'PASS' if dims_match and has_watermark else 'FAIL'
    }
    
    return results

# VERIFY:
# result = verify_watermark('original.jpg', 'watermarked.jpg')
# print(f"Watermark applied: {result['watermark_detected']}")
# print(f"Quality check: {result['quality']}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR TURN:
1. Create verify_watermark.py with code above
2. Run on your watermarked images
3. Check that watermarks were detected
4. Verify file sizes are reasonable
5. Generate a verification report

WHAT GOOD RESULTS LOOK LIKE:
  ✅ Watermark detected: True
  ✅ Dimensions preserved: True
  ✅ File size change: 5-20%
  ✅ Pixel difference: 10-50
  ✅ Quality: PASS

✅ WHAT YOU LEARNED:
  • Image comparison techniques
  • File quality metrics
  • Verification automation
  • Quality assurance in watermarking
        """)
        
        input("\nPress Enter when you've tried Exercise 5...")
        self.completed.append("Exercise 5: Quality Verification")
    
    def summary(self):
        """Summary of Layer 2"""
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║      LAYER 2: VISIBLE PROTECTION - SUMMARY                     ║
╚════════════════════════════════════════════════════════════════╝

CONGRATULATIONS! You've completed Layer 2

EXERCISES COMPLETED:
        """)
        
        for i, exercise in enumerate(self.completed, 1):
            print(f"  {i}. ✅ {exercise}")
        
        print(f"""
KEY SKILLS MASTERED:
  ✅ Text watermark creation
  ✅ Strategic positioning
  ✅ Opacity control
  ✅ Batch processing
  ✅ Quality verification

YOU CAN NOW:
  • Create professional watermarks
  • Protect image collections
  • Batch process images efficiently
  • Verify watermark quality
  • Apply different opacity levels

REAL-WORLD APPLICATIONS:
  • Photography protection
  • Document watermarking
  • Social media branding
  • Copyright enforcement
  • Portfolio protection

WATERMARKING STRATEGY:
  Layer 1 alone = Easily removed with image editing
  Layer 2 + Layer 3 = Multiple protection layers
  Harder to completely remove

NEXT: Layer 3 - Invisible Protection (Steganography)

Ready to learn invisible watermarking?
Run: python3 ../layer3_invisible/tutorial.py
        """)
    
    def run(self):
        """Run the complete tutorial"""
        self.intro()
        
        input("\nPress Enter to begin Exercise 1...")
        self.exercise_1_basic_watermark()
        
        input("\nPress Enter to begin Exercise 2...")
        self.exercise_2_position_control()
        
        input("\nPress Enter to begin Exercise 3...")
        self.exercise_3_opacity_control()
        
        input("\nPress Enter to begin Exercise 4...")
        self.exercise_4_batch_watermarking()
        
        input("\nPress Enter to begin Exercise 5...")
        self.exercise_5_quality_verification()
        
        input("\nPress Enter to see summary...")
        self.summary()

if __name__ == "__main__":
    tutorial = Layer2Tutorial()
    tutorial.run()
