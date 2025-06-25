from pydantic import BaseModel
from datetime import date


class TaskBase(BaseModel):
    date: date
    task: str
    is_finished: bool = False


class TaskCreate(TaskBase):
    user_id: str


class TaskUpdate(TaskBase):
    pass  # ou você pode permitir edição parcial usando `BaseModel` com `Optional[...]`


class TaskOut(TaskBase):
    id: str
    user_id: str
