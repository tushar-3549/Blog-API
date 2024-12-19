from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Union

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

class Post(PostBase):
    id: int 
    created_at: datetime
    author_id: int 
    author: UserOut
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Union[str, int]

class Vote(BaseModel):
    post_id: int
    ratings: float = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post  
    # votes: float 
    rating: float = Field(0.0, description="Rating for the post") 

    class Config:
        from_attributes = True