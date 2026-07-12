from fastapi import FastAPI

from auth.router import router as auth_router
from tasks.router import router as tasks_router
from database import Base, engine
import auth.models
import tasks.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Task Tracker - Auth Edition",
    description="Sprint 01 Days 11-12 - Nolyth AI Bootcamp - Abdul Salam",
    version="0.3.0",
)

app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Personal Task Tracker - Auth Edition"}
