.PHONY: help install test lint format clean docker-build docker-up docker-down

# Default target when you just run 'make'
help:
	@echo "🏥 Personal Health Intelligence Platform - Development Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install          Install all Python dependencies"
	@echo "  make install-dev      Install dev dependencies (testing, linting)"
	@echo ""
	@echo "Code Quality:"
	@echo "  make test             Run all tests with coverage"
	@echo "  make test-fast        Run tests without coverage (faster)"
	@echo "  make lint             Check code quality with flake8"
	@echo "  make format           Auto-format code with black"
	@echo "  make type-check       Run type checking with mypy"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build     Build all Docker images"
	@echo "  make docker-up        Start all services (app + database + airflow)"
	@echo "  make docker-down      Stop all services"
	@echo "  make docker-logs      View logs from all containers"
	@echo ""
	@echo "Cleaning:"
	@echo "  make clean            Remove cache files and build artifacts"
	@echo "  make clean-db         Remove local database files"
	@echo ""
	@echo "Kingdom Specific:"
	@echo "  make k1-test          Test Kingdom 1 (File Commander)"
	@echo "  make k2-test          Test Kingdom 2 (Health Tracker)"
	@echo "  make k3-test          Test Kingdom 3 (Mood Food Clarity)"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

# Testing
test:
	pytest --cov --cov-report=html --cov-report=term

test-fast:
	pytest -v

test-watch:
	pytest-watch

k1-test:
	pytest kingdoms/file_commander/tests/ -v

k2-test:
	pytest kingdoms/health_tracker/tests/ -v

k3-test:
	pytest kingdoms/mood_food_clarity/tests/ -v

# Code Quality
lint:
	flake8 kingdoms/ shared/ --max-line-length=100

format:
	black kingdoms/ shared/ --line-length=100

type-check:
	mypy kingdoms/ shared/

quality: format lint type-check
	@echo "✅ Code quality checks complete!"

# Docker
docker-build:
	docker-compose build

docker-up:
	docker-compose up -d
	@echo "🚀 Services started! Access them at:"
	@echo "  - Streamlit: http://localhost:8501"
	@echo "  - Airflow: http://localhost:8080"

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-restart: docker-down docker-up

# Cleaning
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	@echo "🧹 Cleaned up cache files!"

clean-db:
	rm -f *.db *.sqlite *.sqlite3
	@echo "🗑️  Removed database files!"

# Development
run-k1:
	cd kingdoms/file_commander && streamlit run src/app.py

run-k2:
	cd kingdoms/health_tracker && streamlit run src/app.py

run-k3:
	cd kingdoms/mood_food_clarity && streamlit run src/app.py

# Git helpers
git-setup:
	git config --global user.name "Your Name"
	git config --global user.email "your.email@example.com"
	@echo "✅ Git configured! Update with your actual name and email."

# Database migrations
db-migrate:
	alembic upgrade head

db-rollback:
	alembic downgrade -1

db-create-migration:
	@read -p "Enter migration message: " msg; \
	alembic revision --autogenerate -m "$$msg"
