from pydantic import BaseModel
from datetime import datetime
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        orm_mode = True
