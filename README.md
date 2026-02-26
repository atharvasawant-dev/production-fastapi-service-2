# Production FastAPI Service

A production-grade FastAPI service designed to demonstrate backend engineering fundamentals recruiters look for: modular architecture, request validation, structured logging, error handling, and tests.

## Architecture

- `src/main.py`: application entry point
- `src/routes/`: API route modules
- `src/services/`: business logic
- `src/models/`: Pydantic domain models

## Features

- Health and readiness endpoints
- CRUD-style API for work items
- Structured logging
- Input validation and consistent error responses
- Pytest test suite

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn src.main:app --reload
# GET http://127.0.0.1:8000/health
```

## Project Structure

```
production-fastapi-service-2/
  src/
    main.py
    routes/
    services/
    models/
  tests/
  .github/workflows/ci.yml
  README.md
  requirements.txt
  .gitignore
```
