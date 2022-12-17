from .database import Base
from sqlalchemy import Column, Integer, String, Boolean # DateTime

class Post(Base):
    __tablename__ : "posts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String)
    content = Column(String, nullable = False)
    published = Column(Boolean, default = True)
#    created_at = Column(DateTime)
