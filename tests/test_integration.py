import pytest
import requests
import time
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestBlogAPIIntegration:
    """Integration tests for Blog API endpoints"""
    
    def test_root_endpoint(self):
        """Test GET / endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert "Welcome to Blog API" in response.json()["message"]
    
    def test_create_blog(self):
        """Test creating a new blog post"""
        blog_data = {
            "title": "My First Blog",
            "content": "This is my first blog post",
            "author": "John Doe"
        }
        response = client.post("/blogs", json=blog_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == blog_data["title"]
        assert data["content"] == blog_data["content"]
        assert data["author"] == blog_data["author"]
        assert data["id"] is not None
        assert data["created_at"] is not None
    
    def test_create_multiple_blogs(self):
        """Test creating multiple blog posts"""
        blogs = [
            {"title": "Blog 1", "content": "Content 1", "author": "Author 1"},
            {"title": "Blog 2", "content": "Content 2", "author": "Author 2"},
        ]
        responses = []
        for blog in blogs:
            response = client.post("/blogs", json=blog)
            assert response.status_code == 200
            responses.append(response.json())
        
        assert len(responses) == 2
        assert responses[0]["id"] != responses[1]["id"]
    
    def test_get_all_blogs(self):
        """Test getting all blogs"""
        blog_data = {
            "title": "Test Blog for List",
            "content": "Content",
            "author": "Test Author"
        }
        client.post("/blogs", json=blog_data)
        
        response = client.get("/blogs")
        assert response.status_code == 200
        blogs = response.json()
        assert isinstance(blogs, list)
        assert len(blogs) > 0
    
    def test_get_blog_by_id(self):
        """Test getting a specific blog by ID"""
        blog_data = {
            "title": "Blog to Retrieve",
            "content": "Content",
            "author": "Author"
        }
        create_response = client.post("/blogs", json=blog_data)
        blog_id = create_response.json()["id"]
        
        response = client.get(f"/blogs/{blog_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == blog_id
        assert data["title"] == blog_data["title"]
    
    def test_get_nonexistent_blog(self):
        """Test getting a blog that doesn't exist"""
        response = client.get("/blogs/99999")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()
    
    def test_update_blog(self):
        """Test updating a blog post"""
        blog_data = {
            "title": "Original Title",
            "content": "Original Content",
            "author": "Original Author"
        }
        create_response = client.post("/blogs", json=blog_data)
        blog_id = create_response.json()["id"]
        
        update_data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }
        response = client.put(f"/blogs/{blog_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["content"] == "Updated Content"
        assert data["author"] == "Original Author"
    
    def test_delete_blog(self):
        """Test deleting a blog post"""
        blog_data = {
            "title": "Blog to Delete",
            "content": "Content",
            "author": "Author"
        }
        create_response = client.post("/blogs", json=blog_data)
        blog_id = create_response.json()["id"]
        
        response = client.delete(f"/blogs/{blog_id}")
        assert response.status_code == 200
        assert "deleted successfully" in response.json()["message"]
        
        get_response = client.get(f"/blogs/{blog_id}")
        assert get_response.status_code == 404
    
    def test_get_blogs_by_author(self):
        """Test getting blogs filtered by author"""
        author1_blogs = [
            {"title": "Blog 1", "content": "Content 1", "author": "Alice"},
            {"title": "Blog 2", "content": "Content 2", "author": "Alice"},
        ]
        author2_blogs = [
            {"title": "Blog 3", "content": "Content 3", "author": "Bob"},
        ]
        
        for blog in author1_blogs + author2_blogs:
            client.post("/blogs", json=blog)
        
        response = client.get("/blogs/author/alice")
        assert response.status_code == 200
        blogs = response.json()
        assert len(blogs) >= 2
        for blog in blogs:
            assert blog["author"].lower() == "alice"
