# 🏥 Personal Health Intelligence Platform

**Mission:** Unify fragmented health data (medical, nutritional, activity, biometric) into a single queryable system that prevents over-supplementation, optimizes wellness decisions, and empowers individuals with the complete picture their doctors, nutritionists, and trainers each see only partially.

---

## 🎯 The Problem

Healthcare is fragmented:
- **Doctors** prescribe medications without nutrition context
- **Nutritionists** suggest supplements without checking medication interactions  
- **Trainers** plan workouts without considering recovery data
- **You** spend money on duplicate supplements and make decisions with incomplete information

## 💡 The Solution

Three interconnected data kingdoms:

### 🗂️ Kingdom 1: File Commander
A queryable file management system with metadata extraction, organization, and automated cleanup.

**Tech Stack:** Python, SQLite, Streamlit, Docker, Airflow

### 🏃 Kingdom 2: Health Tracker  
Unified health data aggregator pulling from multiple sources (Oura Ring, Apple Health, Sleep Number, etc.)

**Tech Stack:** Python, PostgreSQL, Streamlit, Docker, Airflow, REST APIs

### 🍎 Kingdom 3: Mood Food Clarity
ML-powered nutritional intelligence that predicts mood, detects supplement overlaps, and prevents over-supplementation.

**Tech Stack:** Python, PostgreSQL, Streamlit, scikit-learn, Docker, Airflow

---

## 🏗️ Architecture

```
Development (Local)  →  GitHub (Version Control)  →  AWS (Production)
     Docker                  CI/CD                   Terraform
```

---

## 🚀 Quick Start

**Prerequisites:**
- Python 3.11+
- Docker Desktop
- Git

**Setup:**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/personal-health-intelligence.git
cd personal-health-intelligence

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Start Kingdom 1 (File Commander)
cd kingdoms/file_commander
python src/cli.py scan ~/Documents
```

---

## 📚 Documentation

- [Master Plan](docs/MASTER_PLAN.md) - Complete project specification
- [Architecture](docs/ARCHITECTURE.md) - System design and data flow
- [Learning Path](docs/LEARNING_PATH.md) - Phase-by-phase development guide
- [AWS Integration](docs/AWS_GUIDE.md) - Cloud deployment strategy

---

## 🧪 Testing

We follow the testing pyramid:
- **Unit Tests (70%):** Test individual functions
- **Integration Tests (20%):** Test components together  
- **E2E Tests (10%):** Test complete workflows

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific kingdom tests
pytest kingdoms/file_commander/tests/
```

---

## 🛠️ Development Workflow

1. **Plan** - Define feature requirements
2. **Design** - Sketch data flow and APIs
3. **Test** - Write failing tests (TDD)
4. **Implement** - Write code to pass tests
5. **Refactor** - Clean up while keeping tests green
6. **Document** - Add docstrings and examples
7. **Commit** - Save to Git with clear message

---

## 📊 Project Status

**Current Phase:** Phase 0 - Foundation Setup ✅

- [x] Project structure created
- [x] Git repository initialized
- [ ] Kingdom 1 MVP (File Scanner)
- [ ] Kingdom 1 Full (UI + Airflow)
- [ ] Kingdom 2 (Health Tracker)
- [ ] Kingdom 3 (Mood Food Clarity)
- [ ] AWS Deployment

---

## 🤝 Contributing

This is a personal learning project, but contributions are welcome! 

**How to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`pytest`)
5. Commit your changes (`git commit -m 'feat: add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

Built as a learning journey to master:
- Data Engineering pipelines
- Machine Learning applications
- AWS Solutions Architecture
- Full-stack development

**Learning Resources:**
- AWS Solutions Architect Certification (Neal Davis course)
- Python for Data Analysis (Wes McKinney)
- Designing Data-Intensive Applications (Martin Kleppmann)

---

## 📧 Contact

Have questions or want to collaborate?
- GitHub Issues: [Report a bug or request a feature](https://github.com/YOUR_USERNAME/personal-health-intelligence/issues)
- Email: your.email@example.com

---

**Remember:** This isn't just about code - it's about building tools that genuinely improve lives, starting with your own.
