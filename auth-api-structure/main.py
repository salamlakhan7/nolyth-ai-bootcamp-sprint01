# main.py
# Nolyth AI Bootcamp - Sprint 01 (Days 8-10)
# Auth + organized API structure - routers, services, schemas, protected routes

from fastapi import FastAPI

from auth.router import router as auth_router
from tasks.router import router as tasks_router

app = FastAPI(
    title="Personal Task Tracker - Auth Edition",
    description="Sprint 01 Days 8-10 - Nolyth AI Bootcamp - Abdul Salam",
    version="0.2.0",
)

app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "Personal Task Tracker - Auth Edition"}