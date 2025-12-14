from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True)
    page_id = Column(String, unique=True, index=True)
    name = Column(String)
    url = Column(String)
    industry = Column(String)
    followers = Column(Integer)
    description = Column(String)
