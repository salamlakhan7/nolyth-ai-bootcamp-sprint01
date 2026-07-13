from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session

from tasks.schemas import NewTask, TaskOut
from tasks.service import create_task, get_tasks_for_user, get_single_task_for_user
from auth.dependencies import get_current_user
from database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def add_task(payload: NewTask, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return create_task(db, payload, owner=current_user.username)


@router.get("", response_model=list[TaskOut])
def list_my_tasks(
    is_done: Optional[bool] = None,
    priority: Optional[int] = None,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_tasks_for_user(db, current_user.username, is_done, priority)


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    task = get_single_task_for_user(db, task_id, current_user.username)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    """Delete a task - only if it belongs to the logged-in user."""
    task = get_single_task_for_user(db, task_id, current_user.username)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    db.delete(task)
    db.commit()


@router.patch("/{task_id}", response_model=TaskOut)
def mark_task_done(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    """Toggle a task's is_done status - only if it belongs to the logged-in user."""
    task = get_single_task_for_user(db, task_id, current_user.username)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    task.is_done = not task.is_done
    db.commit()
    db.refresh(task)
    return task