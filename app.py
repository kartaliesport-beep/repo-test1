from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Blog API", version="1.0.0")

# Models
class BlogPost(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

# In-memory database
blogs_db: List[BlogPost] = []
blog_counter = 0

# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to Blog API", "version": "1.0.0"}

@app.post("/blogs", response_model=BlogPost)
def create_blog(blog: BlogPost):
    global blog_counter
    blog_counter += 1
    blog.id = blog_counter
    blog.created_at = datetime.now()
    blog.updated_at = datetime.now()
    blogs_db.append(blog)
    return blog

@app.get("/blogs", response_model=List[BlogPost])
def get_all_blogs():
    return blogs_db

@app.get("/blogs/{blog_id}", response_model=BlogPost)
def get_blog(blog_id: int):
    for blog in blogs_db:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.put("/blogs/{blog_id}", response_model=BlogPost)
def update_blog(blog_id: int, blog_update: BlogPostUpdate):
    for blog in blogs_db:
        if blog.id == blog_id:
            if blog_update.title:
                blog.title = blog_update.title
            if blog_update.content:
                blog.content = blog_update.content
            if blog_update.author:
                blog.author = blog_update.author
            blog.updated_at = datetime.now()
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):
    global blogs_db
    for i, blog in enumerate(blogs_db):
        if blog.id == blog_id:
            blogs_db.pop(i)
            return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

@app.get("/blogs/author/{author}", response_model=List[BlogPost])
def get_blogs_by_author(author: str):
    return [blog for blog in blogs_db if blog.author.lower() == author.lower()]
