# Layer 1: Detection & Metadata

## Objective
Understand how systems **identify and tag content ownership**. Learn why metadata matters for protection.

---

## What You'll Learn

✅ How content identification works
✅ Metadata structure and purpose
✅ Logging and tracking systems
✅ Why metadata can be spoofed (and why that matters)
✅ Designing tamper-resistant tagging

---

## The Concept

Before you can protect content, you need to **know whose content it is**.

```
Step 1: Is this content OWNED by me?  → YES = Allow recording
                                    → NO = Restrict recording
```

Layer 1 answers that question.

### Simple Example
```python
content_database = {
    "owned": [
        "my_video.mp4",      # ✅ I can record this
        "my_presentation.mp4"
    ],
    "restricted": [
        "netflix_sample.mp4" # ❌ Don't record this
    ]
}

def can_record(filename):
    if filename in content_database["owned"]:
        return True  # Allow recording
    return False     # Block or watermark
```

---

## How It Works

### 1. **Content Identification**
When content enters OBS, it needs a status tag:
- **OWNED** - Content I created or have permission to record
- **RESTRICTED** - Protected content I don't own
- **UNKNOWN** - Uncertain status (default to restricted)

### 2. **Metadata Tagging**
Attach metadata to content:
```json
{
    "filename": "my_video.mp4",
    "owner": "John Doe",
    "created_at": "2026-04-29",
    "status": "OWNED",
    "license": "personal-use"
}
```

### 3. **Logging**
Record every recording attempt:
```json
{
    "timestamp": "2026-04-29 14:30:00",
    "content": "netflix_sample.mp4",
    "status": "RESTRICTED",
    "action": "BLOCKED"
}
```

---

## Why This Matters

**Problem:** How do you know if content is owned or restricted?
**Solution:** Metadata that identifies ownership

**But then:** What if someone lies about ownership?
**That's where Layer 2, 3, 4, 5 come in...**

---

## Challenges in This Layer

### Challenge 1.1: Metadata Fields
Add more information to content identification.

### Challenge 1.2: Logging System
Create a system that records all recording attempts.

### Challenge 1.3: Spoof Detection
Design a system that detects when metadata is faked.

---

## Files

- **tutorial.py** - Interactive walkthrough (start here!)
- **examples/** - Code examples
- **challenges/** - Hands-on exercises
- **projects/** - Mini-projects

---

## Getting Started

### For Beginners
1. Read this README
2. Run `python3 tutorial.py`
3. Answer conceptual questions
4. Understand the concept

### For Intermediate
1. Read this README
2. Study `examples/basic_detection.py`
3. Complete challenges with starter code
4. Build your own metadata system

### For Advanced
1. Study `solution.py` thoroughly
2. Design improvements
3. Implement from scratch
4. Create novel identification method

---

## Key Concepts

### Metadata
Information about data. Example:
```python
metadata = {
    "content": "filename",
    "owner": "who created it",
    "created": "when",
    "status": "owned or restricted"
}
```

### Logging
Record of events:
```python
log = {
    "timestamp": "when",
    "event": "what happened",
    "details": "info about the event"
}
```

### Database
Centralized storage:
```python
database = {
    "owned_content": [...],
    "restricted_content": [...],
    "access_logs": [...]
}
```

---

## Common Mistakes

❌ **Storing metadata in plain text files** - easy to modify
❌ **Not logging attempts** - can't track violations
❌ **Trusting user input** - metadata can be spoofed
❌ **No backup system** - what if metadata is deleted?

✅ **Use checksums or signatures**
✅ **Log everything to a database**
✅ **Verify metadata integrity**
✅ **Keep centralized records**

---

## Next Steps

1. **Start Tutorial:** `python3 tutorial.py`
2. **Read Examples:** `cat examples/basic_detection.py`
3. **Try Challenges:** `cd challenges/1.1_metadata_fields`
4. **Build Project:** Design your own system

---

## Questions?

- Read FAQ.md
- Check examples/
- Look at solution.py (after trying yourself)
- Ask in Discussions

---

**Ready? Run:** `python3 tutorial.py` 🚀
