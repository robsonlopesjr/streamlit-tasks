from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    task = Column(String, nullable=False)
    is_finished = Column(Boolean, default=False)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")
