import pytest
from app import app, blogs_db
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def clear_database():
    """Clear the in-memory database before each test"""
    blogs_db.clear()
    yield
    blogs_db.clear()


@pytest.fixture
def client():
    """Provide test client for API tests"""
    return TestClient(app)
