from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.db.session import SessionLocal
from app.services.page_service import get_or_create_page, search_pages

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/pages/search")
def search_pages_api(
    name: Optional[str] = None,
    industry: Optional[str] = None,
    followers_min: Optional[int] = None,
    followers_max: Optional[int] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    pages = search_pages(
        db=db,
        name=name,
        industry=industry,
        followers_min=followers_min,
        followers_max=followers_max,
        page=page,
        limit=limit
    )

    return [
        {
            "page_id": p.page_id,
            "name": p.name,
            "industry": p.industry,
            "followers": p.followers
        }
        for p in pages
    ]

@router.get("/pages/{page_id}")
def get_page(page_id: str, db: Session = Depends(get_db)):
    page = get_or_create_page(db, page_id)

    return {
        "page_id": page.page_id,
        "name": page.name,
        "url": page.url,
        "industry": page.industry,
        "followers": page.followers,
        "description": page.description
    }
