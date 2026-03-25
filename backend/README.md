
# Pollaris Backend

This README is intended for developers who want to run the Pollaris backend locally.

## Prerequisites
- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended dependency manager)

## 1. Create a virtual environment (venv)

From the `backend/` folder, run:

```bash
python -m venv .venv
```

Activate the virtual environment:
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source .venv/bin/activate
  ```

## 2. Install dependencies

With [uv](https://github.com/astral-sh/uv) (recommended):

```bash
uv pip install -e .
```

Or with pip (if you don't use uv):

```bash
pip install -e .
```

## 3. Run the server

From the `backend/` folder, run:

```bash
uvicorn app.main:app --reload
```

The backend will be available at: [http://localhost:8000](http://localhost:8000)

## 4. Main folder structure

```
backend/
│   pyproject.toml
│   README.md
│
├───alembic/           # Database migrations (optional)
├───app/
│   ├───api/           # Routers and endpoints
│   ├───core/          # Configuration and utilities
│   ├───db/            # Database connection and utilities
│   ├───models/        # ORM models
│   ├───routers/       # Additional routers
│   ├───schemas/       # Pydantic schemas
│   ├───services/      # Business logic
│   └───main.py        # FastAPI entry point
└───tests/             # Automated tests
```

> **Note:** This README covers only the basic steps to run the backend. For advanced tasks (migrations, testing, etc.), check the internal documentation or ask the team.
