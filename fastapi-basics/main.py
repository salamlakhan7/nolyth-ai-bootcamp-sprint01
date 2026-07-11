# Nolyth AI Bootcamp - Sprint 01 (Days 5-7)
# Personal Task Tracker API - basic routes, validation, and in-memory storage
# (Persistent DB layer arrives in Days 11-12 with SQLAlchemy)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

app = FastAPI(
    title="Personal Task Tracker",
    description="Backend API built for Nolyth Sprint 01 - Abdul Salam",
    version="0.1.0"
)

# ----- Temporary in-memory "database" -----
# will be replaced by SQLAlchemy models once Days 11-12 arrive
task_store = {}
task_counter = 0


# ----- Pydantic Schemas -----

class NewTask(BaseModel):
    title: str = Field(..., min_length=3, max_length=80)
    notes: Optional[str] = Field(default=None, max_length=300)
    priority: int = Field(default=2, ge=1, le=3)  # 1=high, 2=medium, 3=low
    due_date: Optional[date] = None
    is_done: bool = False


class TaskOut(BaseModel):
    task_id: int
    title: str
    notes: Optional[str]
    priority: int
    due_date: Optional[date]
    is_done: bool


# ----- Routes -----

@app.get("/", tags=["Health"])
def health_check():
    """Quick check that the API is alive."""
    return {"status": "ok", "service": "Personal Task Tracker"}


@app.post("/tasks", response_model=TaskOut, status_code=201, tags=["Tasks"])
def add_task(payload: NewTask):
    """Create a new task and store it."""
    global task_counter
    task_counter += 1

    stored_task = {
        "task_id": task_counter,
        "title": payload.title,
        "notes": payload.notes,
        "priority": payload.priority,
        "due_date": payload.due_date,
        "is_done": payload.is_done,
    }
    task_store[task_counter] = stored_task
    return stored_task


@app.get("/tasks", response_model=list[TaskOut], tags=["Tasks"])
def get_all_tasks(is_done: Optional[bool] = None, priority: Optional[int] = None):
    """
    Return all tasks, with optional filters.
    Query params: is_done=true/false, priority=1/2/3
    """
    results = list(task_store.values())

    if is_done is not None:
        results = [t for t in results if t["is_done"] == is_done]

    if priority is not None:
        results = [t for t in results if t["priority"] == priority]

    return results


@app.get("/tasks/{task_id}", response_model=TaskOut, tags=["Tasks"])
def get_single_task(task_id: int):
    """Fetch one task using its ID (path parameter)."""
    task = task_store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} does not exist.")
    return task