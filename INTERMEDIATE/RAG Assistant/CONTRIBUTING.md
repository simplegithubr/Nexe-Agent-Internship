# Contributing to RAG Assistant

Thank you for your interest in contributing to RAG Assistant! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, browser)

### Suggesting Features

Feature requests are welcome! Please include:
- Clear description of the feature
- Use case and benefits
- Possible implementation approach
- Any relevant examples

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 📋 Development Guidelines

### Code Style

**Python (Backend)**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Handle errors gracefully

**JavaScript (Frontend)**
- Use ES6+ features
- Use const/let instead of var
- Add comments for complex logic
- Keep functions pure when possible
- Handle errors with try-catch

**CSS**
- Use meaningful class names
- Keep styles organized
- Use CSS variables for colors
- Make responsive designs

### Testing

Before submitting:
- [ ] Run `python verify_setup.py`
- [ ] Run `python test_api.py`
- [ ] Test manually with sample documents
- [ ] Test on different browsers
- [ ] Check for console errors

### Documentation

Update documentation when:
- Adding new features
- Changing API endpoints
- Modifying configuration
- Fixing bugs that affect usage

## 🏗️ Project Structure

```
backend/
  - app.py           # Main Flask app
  - test_api.py      # API tests
  - verify_setup.py  # Setup verification

frontend/
  - index.html       # Complete UI

docs/
  - *.md            # All documentation
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Add more file type support (CSV, JSON, XML)
- [ ] Implement user authentication
- [ ] Add conversation history
- [ ] Improve error messages
- [ ] Add loading progress indicators

### Medium Priority
- [ ] Add document preview
- [ ] Implement batch upload
- [ ] Add export functionality
- [ ] Improve mobile UI
- [ ] Add keyboard shortcuts

### Low Priority
- [ ] Add dark mode
- [ ] Add more AI models
- [ ] Add document tagging
- [ ] Add search filters
- [ ] Add analytics dashboard

## 🐛 Bug Fixes

When fixing bugs:
1. Create an issue first (if not exists)
2. Reference the issue in your PR
3. Add tests to prevent regression
4. Update documentation if needed

## 📝 Commit Message Format

Use clear, descriptive commit messages:

```
Add: New feature description
Fix: Bug fix description
Update: Changes to existing feature
Docs: Documentation updates
Test: Test additions or changes
Refactor: Code refactoring
Style: Code style changes
```

Examples:
```
Add: Support for CSV file upload
Fix: Upload fails for large PDF files
Update: Improve error handling in query endpoint
Docs: Add deployment guide for AWS
Test: Add unit tests for document processing
```

## 🔍 Code Review Process

All contributions go through code review:
1. Automated tests must pass
2. Code must follow style guidelines
3. Documentation must be updated
4. At least one maintainer approval required

## 🚀 Release Process

1. Update CHANGELOG.md
2. Update version in package.json
3. Create release tag
4. Deploy to production

## 📞 Getting Help

- Check existing documentation
- Search existing issues
- Ask in discussions
- Contact maintainers

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to RAG Assistant! 🎉**
