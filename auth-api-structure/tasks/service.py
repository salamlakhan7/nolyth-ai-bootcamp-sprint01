# tasks/service.py
# Task business logic - now scoped per user (owner field)

from tasks.schemas import NewTask

task_store: dict[int, dict] = {}
task_counter = 0


def create_task(payload: NewTask, owner: str) -> dict:
    """Create a task tied to the logged-in user."""
    global task_counter
    task_counter += 1

    task = {
        "task_id": task_counter,
        "title": payload.title,
        "notes": payload.notes,
        "priority": payload.priority,
        "due_date": payload.due_date,
        "is_done": payload.is_done,
        "owner": owner,
    }
    task_store[task_counter] = task
    return task


def get_tasks_for_user(owner: str, is_done: bool | None = None, priority: int | None = None) -> list[dict]:
    """Return only the current user's tasks, with optional filters."""
    results = [t for t in task_store.values() if t["owner"] == owner]

    if is_done is not None:
        results = [t for t in results if t["is_done"] == is_done]
    if priority is not None:
        results = [t for t in results if t["priority"] == priority]

    return results


def get_single_task_for_user(task_id: int, owner: str) -> dict | None:
    """Return one task only if it belongs to the current user."""
    task = task_store.get(task_id)
    if task and task["owner"] == owner:
        return task
    return None