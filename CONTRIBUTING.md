# 🤝 Contributing to Personal Health Intelligence Platform

Thank you for considering contributing to this project! This is primarily a learning project, but contributions are welcome.

---

## 📋 Getting Started

### Prerequisites
- Python 3.11+
- Docker Desktop
- Git
- Basic understanding of data pipelines

### Setup Development Environment

1. **Fork and Clone**
```bash
git clone https://github.com/YOUR_USERNAME/personal-health-intelligence.git
cd personal-health-intelligence
```

2. **Install Dependencies**
```bash
make install
make install-dev
```

3. **Run Tests**
```bash
make test
```

4. **Start Services**
```bash
make docker-up
```

---

## 🔄 Development Workflow

We follow a structured 7-step development cycle:

1. **PLAN** - Define what you're building
2. **DESIGN** - Sketch data flow and function signatures
3. **TEST** - Write failing tests (TDD)
4. **IMPLEMENT** - Write minimum code to pass tests
5. **REFACTOR** - Clean up code (keep tests passing)
6. **DOCUMENT** - Add docstrings and comments
7. **COMMIT** - Save to Git with descriptive message

---

## 🧪 Testing Requirements

**All contributions must include tests.**

We follow the testing pyramid:
- **70% Unit Tests** - Test individual functions
- **20% Integration Tests** - Test components together
- **10% E2E Tests** - Test complete workflows

```bash
# Run tests before committing
make test

# Check test coverage (aim for >80%)
pytest --cov --cov-report=html
```

---

## 📝 Commit Message Format

We use conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `test`: Adding tests
- `refactor`: Code change that neither fixes bug nor adds feature
- `style`: Formatting changes
- `chore`: Maintenance tasks

**Example:**
```
feat(file-commander): add file type filtering

Implemented filter_by_type() function that allows users to
scan only specific file types (e.g., only PDFs).

- Added new parameter file_types: List[str]
- Updated tests with filtering scenarios
- Performance: 40% faster when filtering is used

Closes #23
```

---

## 🎨 Code Style

We use these tools to maintain code quality:

```bash
# Auto-format code
make format

# Check linting
make lint

# Type checking
make type-check

# Run all quality checks
make quality
```

**Standards:**
- Line length: 100 characters
- Python version: 3.11+
- Type hints: Required for public functions
- Docstrings: Required for all functions/classes

---

## 🌿 Branching Strategy

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - Individual features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes

**Workflow:**
```bash
# Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Make changes, commit
git add .
git commit -m "feat: your feature"

# Push and create pull request
git push origin feature/your-feature-name
```

---

## 🐛 Reporting Bugs

Use GitHub Issues with the bug report template:

**Include:**
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment (OS, Python version, etc.)

---

## 💡 Suggesting Features

Use GitHub Issues with the feature request template:

**Include:**
- Clear description of the feature
- Use case / motivation
- Proposed implementation (if you have ideas)
- Alternatives considered

---

## ✅ Pull Request Process

1. **Ensure tests pass**
   ```bash
   make test
   ```

2. **Update documentation**
   - Update README if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md

3. **Create PR with clear description**
   - What does this PR do?
   - Why is this change needed?
   - How was it tested?
   - Screenshots (for UI changes)

4. **Respond to feedback**
   - Address review comments
   - Make requested changes
   - Keep discussion constructive

5. **Squash commits** (optional)
   - Clean up commit history before merge

---

## 🎯 Good First Issues

Look for issues tagged with:
- `good-first-issue` - Great for newcomers
- `help-wanted` - We'd appreciate help
- `documentation` - Docs improvements needed

---

## 💬 Communication

- **GitHub Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions
- **Discussions** - Questions and ideas

---

## 📜 Code of Conduct

**Be Respectful:**
- Be kind and courteous
- Welcome newcomers
- Respect differing viewpoints
- Accept constructive criticism
- Focus on what's best for the community

**Not Tolerated:**
- Harassment or discrimination
- Trolling or insulting comments
- Personal attacks
- Spam or self-promotion

---

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Acknowledged in project documentation

Thank you for helping make this project better! 🚀
