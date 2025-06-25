from sqlalchemy.orm import Session
from tasks.models.task_model import Task
from tasks.schemas.task_schema import TaskCreate, TaskUpdate
import uuid


def get_all(db: Session):
    return db.query(Task).order_by(Task.date.desc()).all()


def get_by_id(db: Session, task_id: str):
    return db.query(Task).filter(Task.id == task_id).first()


def get_by_user(db: Session, user_id: str):
    return db.query(Task).filter(Task.user_id == user_id).order_by(Task.date.desc()).all()


def create(db: Session, data: TaskCreate):
    task = Task(
        id=str(uuid.uuid4()),
        date=data.date,
        task=data.task,
        is_finished=data.is_finished,
        user_id=data.user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update(db: Session, task_id: str, data: TaskUpdate):
    task = get_by_id(db, task_id)
    if not task:
        return None
    task.date = data.date
    task.task = data.task
    task.is_finished = data.is_finished
    db.commit()
    db.refresh(task)
    return task


def delete(db: Session, task_id: str):
    task = get_by_id(db, task_id)
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
