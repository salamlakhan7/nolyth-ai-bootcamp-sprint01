# tasks/models.py
from sqlalchemy import Column, Integer, String, Boolean, Date

from database import Base


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    priority = Column(Integer, default=2)
    due_date = Column(Date, nullable=True)
    is_done = Column(Boolean, default=False)
    owner = Column(String, index=True, nullable=False)  # username, matches your existing schema
