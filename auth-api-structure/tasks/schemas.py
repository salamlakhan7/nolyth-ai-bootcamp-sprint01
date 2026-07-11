# tasks/schemas.py
# Pydantic schemas for tasks (same as fastapi-basics, now owner-aware)

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class NewTask(BaseModel):
    title: str = Field(..., min_length=3, max_length=80)
    notes: Optional[str] = Field(default=None, max_length=300)
    priority: int = Field(default=2, ge=1, le=3)
    due_date: Optional[date] = None
    is_done: bool = False


class TaskOut(BaseModel):
    task_id: int
    title: str
    notes: Optional[str]
    priority: int
    due_date: Optional[date]
    is_done: bool
    owner: str   # new - tracks which user created this task