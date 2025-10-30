# Contributing to A/B Testing Framework for Nykaa

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker
- Clearly describe the issue with steps to reproduce
- Include relevant code snippets and error messages
- Specify your environment (Python version, OS, etc.)

### Suggesting Enhancements

- Open an issue with the tag "enhancement"
- Clearly describe the proposed feature
- Explain why it would be useful
- Provide examples if possible

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/Vinoth11111/A-B-Testing-Nykaa.git
   cd A-B-Testing-Nykaa
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Run tests**
   ```bash
   cd tests
   python test_ab_testing.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines

### Python Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Include usage examples
- Update QUICKSTART.md if adding major features

### Testing

- Add unit tests for new features
- Ensure all existing tests pass
- Aim for good test coverage
- Test edge cases

## Development Setup

```bash
# Install in development mode
pip install -r requirements.txt

# Run tests
python tests/test_ab_testing.py

# Run example
python example.py
```

## Areas for Contribution

### High Priority
- Additional statistical tests (e.g., Mann-Whitney U, Fisher's exact test)
- Multi-armed bandit algorithms
- Sequential testing capabilities
- More visualization options
- Performance optimizations

### Medium Priority
- Support for continuous metrics (not just conversion rates)
- Time-series analysis
- Integration with analytics platforms
- Dashboard creation
- Export to different formats (PDF, Excel)

### Documentation
- More usage examples
- Video tutorials
- Case studies
- Best practices guide

## Pull Request Process

1. Update documentation with details of changes
2. Add tests that prove your fix/feature works
3. Ensure all tests pass
4. Update the CHANGELOG if applicable
5. The PR will be merged once reviewed and approved

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## Questions?

Feel free to open an issue with your questions or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
