# tasks/service.py
from sqlalchemy.orm import Session

from tasks.schemas import NewTask
from tasks.models import Task


def create_task(db: Session, payload: NewTask, owner: str) -> Task:
    task = Task(
        title=payload.title,
        notes=payload.notes,
        priority=payload.priority,
        due_date=payload.due_date,
        is_done=payload.is_done,
        owner=owner,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks_for_user(db: Session, owner: str, is_done: bool | None = None, priority: int | None = None):
    query = db.query(Task).filter(Task.owner == owner)
    if is_done is not None:
        query = query.filter(Task.is_done == is_done)
    if priority is not None:
        query = query.filter(Task.priority == priority)
    return query.all()


def get_single_task_for_user(db: Session, task_id: int, owner: str) -> Task | None:
    return db.query(Task).filter(Task.task_id == task_id, Task.owner == owner).first()
