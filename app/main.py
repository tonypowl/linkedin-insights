from fastapi import FastAPI
from app.api.route_pages import router
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LinkedIn Insights Service")

@app.get("/")
def root():
    return {"message": "LinkedIn Insights API is running"}

app.include_router(router)
