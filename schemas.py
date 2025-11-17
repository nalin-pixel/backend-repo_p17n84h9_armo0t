"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
- ContactMessage -> "contactmessage" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: Optional[str] = Field(None, description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

class BlogPost(BaseModel):
    title: str = Field(..., description="Post title")
    slug: str = Field(..., description="URL slug")
    excerpt: Optional[str] = Field(None, description="Short summary")
    content: str = Field(..., description="Markdown or rich text content")
    tags: List[str] = Field(default_factory=list, description="Tags for filtering")
    cover_image: Optional[str] = Field(None, description="Optional cover image URL")
    published: bool = Field(True, description="Whether the post is published")

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=5000)
