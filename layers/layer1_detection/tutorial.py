#!/usr/bin/env python3
"""
Layer 1: Detection & Metadata - Interactive Tutorial

Learn how to identify and tag content ownership.
"""

import json
from datetime import datetime
from pathlib import Path

class ContentProtector:
    """Simple content protection system"""
    
    def __init__(self):
        self.owned = ["my_video.mp4", "my_presentation.mp4"]
        self.restricted = ["netflix_sample.mp4", "hbo_sample.mp4"]
        self.logs = []
    
    def identify_content(self, filename):
        """Identify if content is owned or restricted"""
        if filename in self.owned:
            return "OWNED"
        elif filename in self.restricted:
            return "RESTRICTED"
        return "UNKNOWN"
    
    def can_record(self, filename):
        """Should we allow recording?"""
        status = self.identify_content(filename)
        return status == "OWNED"
    
    def log_attempt(self, filename):
        """Log the recording attempt"""
        status = self.identify_content(filename)
        action = "ALLOWED" if status == "OWNED" else "BLOCKED"
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "filename": filename,
            "status": status,
            "action": action
        }
        
        self.logs.append(log_entry)
        return log_entry
    
    def get_logs(self):
        """Return all logs"""
        return self.logs

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def main():
    print_header("🎓 Layer 1: Detection & Metadata Tutorial")
    print("Let's learn how to identify content ownership!\n")
    
    # Create our system
    protector = ContentProtector()
    
    # === PART 1: Basic Identification ===
    print_header("Part 1: Content Identification")
    
    print("Our system knows about these files:")
    print(f"  OWNED: {protector.owned}")
    print(f"  RESTRICTED: {protector.restricted}\n")
    
    # Test owned content
    test_file = "my_video.mp4"
    status = protector.identify_content(test_file)
    print(f"Q: Is '{test_file}' owned or restricted?")
    print(f"A: {status} ✅\n")
    
    # Test restricted content
    test_file = "netflix_sample.mp4"
    status = protector.identify_content(test_file)
    print(f"Q: Is '{test_file}' owned or restricted?")
    print(f"A: {status} ❌\n")
    
    # === PART 2: Recording Decisions ===
    print_header("Part 2: Recording Decisions")
    
    print("Based on content identification, should we allow recording?\n")
    
    files_to_test = [
        "my_video.mp4",
        "my_presentation.mp4",
        "netflix_sample.mp4",
        "hbo_sample.mp4",
        "unknown_file.mp4"
    ]
    
    for file in files_to_test:
        allowed = protector.can_record(file)
        symbol = "✅ ALLOW" if allowed else "❌ BLOCK"
        print(f"  {file:25} {symbol}")
    
    # === PART 3: Logging ===
    print_header("Part 3: Logging Attempts")
    
    print("Let's record what happens when someone tries to record:\n")
    
    # Simulate recording attempts
    attempts = [
        "my_video.mp4",      # Should succeed
        "netflix_sample.mp4", # Should be blocked
        "my_presentation.mp4" # Should succeed
    ]
    
    for filename in attempts:
        log = protector.log_attempt(filename)
        print(f"Attempt: {filename}")
        print(f"  Status: {log['status']}")
        print(f"  Action: {log['action']}")
        print(f"  Time:   {log['timestamp']}\n")
    
    # === PART 4: View All Logs ===
    print_header("Part 4: Complete Log History")
    
    logs = protector.get_logs()
    print(f"Total attempts recorded: {len(logs)}\n")
    print("Log Summary:")
    print(f"{'Time':<27} {'File':<25} {'Status':<12} {'Action':<10}")
    print("-" * 74)
    
    for log in logs:
        timestamp = log['timestamp'].split('T')[1][:8]  # Just time part
        print(f"{timestamp:<27} {log['filename']:<25} {log['status']:<12} {log['action']:<10}")
    
    # === PART 5: Understanding the Weakness ===
    print_header("Part 5: The Weakness (Spoofing)")
    
    print("Here's the problem with Layer 1:\n")
    print("Anyone could claim their file is in the 'owned' list!")
    print("The metadata isn't signed or verified.\n")
    print("For example:")
    print('  Attacker: "I claim netflix_sample.mp4 is actually owned!"')
    print('  System:   "OK, I believe you!" ✗\n')
    print("This is where Layers 2-5 come in:")
    print("  Layer 2: Add visible watermarks")
    print("  Layer 3: Add invisible fingerprints")
    print("  Layer 4: Track device fingerprints")
    print("  Layer 5: Cryptographic verification\n")
    
    # === SUMMARY ===
    print_header("Summary")
    
    print("What we learned:")
    print("✅ How to identify content ownership")
    print("✅ How to make recording decisions")
    print("✅ How to log attempts")
    print("✅ Why spoofing is a problem\n")
    
    print("What's next:")
    print("→ Challenge 1.1: Add more metadata fields")
    print("→ Challenge 1.2: Design a better logging system")
    print("→ Challenge 1.3: Prevent metadata spoofing\n")
    
    print("Ready for challenges?")
    print("  cd challenges/1.1_metadata_fields")
    print("  cat README.md\n")

if __name__ == "__main__":
    main()
