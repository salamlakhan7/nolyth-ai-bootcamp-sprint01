# tasks/router.py
# Task routes - all protected, all scoped to the logged-in user

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional

from tasks.schemas import NewTask, TaskOut
from tasks.service import create_task, get_tasks_for_user, get_single_task_for_user
from auth.dependencies import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def add_task(payload: NewTask, current_user: dict = Depends(get_current_user)):
    """Create a new task for the logged-in user."""
    return create_task(payload, owner=current_user["username"])


@router.get("", response_model=list[TaskOut])
def list_my_tasks(
    is_done: Optional[bool] = None,
    priority: Optional[int] = None,
    current_user: dict = Depends(get_current_user),
):
    """List only the logged-in user's tasks, with optional filters."""
    return get_tasks_for_user(current_user["username"], is_done, priority)


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, current_user: dict = Depends(get_current_user)):
    """Get a single task - only if it belongs to the logged-in user."""
    task = get_single_task_for_user(task_id, current_user["username"])
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task