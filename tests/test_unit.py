import pytest
from datetime import datetime
from pydantic import ValidationError
from app import BlogPost, BlogPostUpdate


class TestBlogPostModel:
    """Unit tests for BlogPost model"""
    
    def test_blog_post_creation(self):
        """Test creating a BlogPost instance"""
        blog = BlogPost(
            title="Test Blog",
            content="This is a test blog",
            author="John Doe"
        )
        assert blog.title == "Test Blog"
        assert blog.content == "This is a test blog"
        assert blog.author == "John Doe"
        assert blog.id is None
    
    def test_blog_post_with_all_fields(self):
        """Test creating BlogPost with all fields"""
        now = datetime.now()
        blog = BlogPost(
            id=1,
            title="Complete Blog",
            content="Full content",
            author="Jane Doe",
            created_at=now,
            updated_at=now
        )
        assert blog.id == 1
        assert blog.created_at == now
        assert blog.updated_at == now
    
    def test_blog_post_missing_required_fields(self):
        """Test that missing required fields raises validation error"""
        with pytest.raises(ValidationError):
            BlogPost(title="Only Title")
    
    def test_blog_post_update_model(self):
        """Test BlogPostUpdate model"""
        update = BlogPostUpdate(title="Updated Title")
        assert update.title == "Updated Title"
        assert update.content is None
        assert update.author is None


class TestBlogPostValidation:
    """Unit tests for data validation"""
    
    def test_blog_title_is_string(self):
        """Test that title must be string"""
        blog = BlogPost(
            title="String Title",
            content="Content",
            author="Author"
        )
        assert isinstance(blog.title, str)
    
    def test_blog_with_empty_strings(self):
        """Test BlogPost accepts empty strings"""
        blog = BlogPost(
            title="",
            content="",
            author=""
        )
        assert blog.title == ""
    
    def test_blog_post_with_special_characters(self):
        """Test BlogPost with special characters"""
        blog = BlogPost(
            title="Test @#$%^&*()",
            content="Content with newlines and tabs",
            author="Author-123"
        )
        assert "@#$%" in blog.title
