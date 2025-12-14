from sqlalchemy.orm import Session
from app.models.page import Page
from app.scraper.linkedin_scraper import scrape_linkedin_page


def get_or_create_page(db: Session, page_id: str):
    page = db.query(Page).filter(Page.page_id == page_id).first()

    if page:
        return page

    data = scrape_linkedin_page(page_id)

    page = Page(
        page_id=data["page_id"],
        name=data["name"],
        url=data["url"],
        industry=data["industry"],
        followers=data["followers"],
        description=data["description"]
    )

    db.add(page)
    db.commit()
    db.refresh(page)

    return page


# 🔍 NEW: Search pages with filters + pagination
def search_pages(
    db: Session,
    name: str = None,
    industry: str = None,
    followers_min: int = None,
    followers_max: int = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(Page)

    if name:
        query = query.filter(Page.name.ilike(f"%{name}%"))

    if industry:
        query = query.filter(Page.industry.ilike(f"%{industry}%"))

    if followers_min is not None:
        query = query.filter(Page.followers >= followers_min)

    if followers_max is not None:
        query = query.filter(Page.followers <= followers_max)

    offset = (page - 1) * limit

    return query.offset(offset).limit(limit).all()
