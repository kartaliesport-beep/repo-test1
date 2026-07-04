# Blog API

A simple FastAPI-based Blog API with comprehensive test coverage.

## Features

- ✅ Create, Read, Update, Delete (CRUD) blog posts
- ✅ Filter blogs by author
- ✅ Timestamp tracking (created_at, updated_at)
- ✅ Comprehensive test suite (Unit, Integration, E2E)
- ✅ Automated CI/CD with GitHub Actions
- ✅ API documentation with Swagger UI

## Project Structure

```
.
├── app.py                 # Main FastAPI application
├── conftest.py            # Pytest configuration and fixtures
├── pytest.ini             # Pytest settings
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore patterns
├── README.md              # This file
└── tests/
    ├── __init__.py
    ├── test_unit.py       # Unit tests for models
    ├── test_integration.py # Integration tests for API endpoints
    └── test_e2e.py        # End-to-end tests
```

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/kartaliesport-beep/repo-test1.git
cd repo-test1
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Access API Documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Blog Posts

- `GET /` - Welcome message
- `POST /blogs` - Create a new blog post
- `GET /blogs` - Get all blog posts
- `GET /blogs/{blog_id}` - Get a specific blog post
- `PUT /blogs/{blog_id}` - Update a blog post
- `DELETE /blogs/{blog_id}` - Delete a blog post
- `GET /blogs/author/{author}` - Get blogs by author

### Request/Response Examples

**Create Blog Post:**
```bash
curl -X POST "http://127.0.0.1:8000/blogs" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"My First Blog\",
    \"content\": \"This is my first blog post\",
    \"author\": \"John Doe\"
  }"
```

**Get All Blogs:**
```bash
curl -X GET "http://127.0.0.1:8000/blogs"
```

**Update Blog:**
```bash
curl -X PUT "http://127.0.0.1:8000/blogs/1" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Updated Title\"
  }"
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test types:
```bash
# Unit tests only
pytest tests/test_unit.py -v

# Integration tests only
pytest tests/test_integration.py -v

# E2E tests only
pytest tests/test_e2e.py -v
```

### Run with coverage:
```bash
pytest --cov=app --cov-report=html
```

Coverage report will be generated in `htmlcov/index.html`

## Test Coverage

The project includes comprehensive tests:

- **Unit Tests** (`test_unit.py`): Test data models and validation
- **Integration Tests** (`test_integration.py`): Test API endpoints and database operations
- **E2E Tests** (`test_e2e.py`): Test full application flow with browser automation

## CI/CD Pipeline

GitHub Actions automatically runs tests on:
- Push to `main` and `develop` branches
- Pull requests to `main` and `develop` branches

Tests run on Python 3.9, 3.10, and 3.11

## Dependencies

See `requirements.txt` for all dependencies:
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Pytest-cov
- Playwright
- Requests

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

MIT License - feel free to use this project for your own purposes.

## Author

Kartal İES PORT - [GitHub](https://github.com/kartaliesport-beep)
