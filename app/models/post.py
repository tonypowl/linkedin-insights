from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    page_id = Column(String, ForeignKey("pages.page_id"))
    content = Column(String)
