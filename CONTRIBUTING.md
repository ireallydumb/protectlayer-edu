# Contributing to ProtectLayer

Thank you for your interest in contributing to ProtectLayer! This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on educational value
- No help with illegal circumvention of protections
- Maintain the educational mission

## How to Contribute

### Reporting Issues
- **Bugs:** Use GitHub Issues with a clear description
- **Suggestions:** Use GitHub Discussions
- **Security issues:** Do not use Issues - see Security section below

### Contributing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/protectlayer-edu.git
   cd protectlayer-edu
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature
   # or
   git checkout -b fix/your-fix
   ```

3. **Make your changes**
   - Follow the code style (see below)
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   pytest layers/ -v
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "Clear description of changes"
   git push origin feature/your-feature
   ```

6. **Create a Pull Request**
   - Reference any related issues
   - Explain your changes
   - Ensure tests pass

## Code Style

- Python: Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### Example
```python
def identify_content(filename: str) -> str:
    """
    Identify if content is owned or restricted.
    
    Args:
        filename: Path to content file
    
    Returns:
        Status: 'OWNED', 'RESTRICTED', or 'UNKNOWN'
    """
    # Implementation
    return status
```

## Adding Challenges

New challenges are welcome! Follow this structure:

```
layers/layer{N}/{challenge_id}/
├── README.md           # Challenge description
├── starter_code.py     # Starter skeleton
├── tests.py           # Automated tests
└── solution.py        # Reference solution (optional)
```

### Challenge README Template
```markdown
# Challenge {N}.{M}: Title

## Objective
What will students learn?

## What You'll Learn
- Point 1
- Point 2

## Tasks
1. Task 1
2. Task 2

## Success Looks Like
[Example of correct solution]

## Hints
[Optional hints]
```

## Testing

All contributions must pass tests:

```bash
pytest layers/ -v --cov=layers
```

## Documentation

Update documentation for:
- New features
- Changes to existing functionality
- New challenges or layers
- Bug fixes that affect users

## Security

For security issues:
1. Do NOT open a public issue
2. Email with details (check DISCLAIMER.md for contact)
3. Allow time for response before disclosing

## Educational Focus

Remember that ProtectLayer is for education. Contributions should:
- ✅ Teach important concepts
- ✅ Be legally compliant
- ✅ Respect intellectual property
- ✅ Support ethical learning

## Pull Request Process

1. Update README if needed
2. Add tests for new functionality
3. Ensure CI/CD passes
4. Respond to review feedback
5. Maintainer merges when ready

## Styles and Conventions

### File Naming
- Layers: `layerN_description/`
- Challenges: `N.M_description/`
- Files: `snake_case.py`

### Git Commits
- Clear, concise messages
- Reference issues: `Fixes #123`
- One feature per commit when possible

### Documentation
- Use Markdown
- Include code examples
- Link to related docs

## Questions?

- Check [FAQ.md](docs/FAQ.md)
- Open a [Discussion](https://github.com/ireallydumb/protectlayer-edu/discussions)
- Review existing Issues

---

**Thank you for making ProtectLayer better for everyone!** 🎓
