from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import time

from ..database import Base

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    is_active = Column(Boolean, default=True)
    priority = Column(String(20), default="very-high")
    activity_group_id = Column(Integer, ForeignKey("activity.id"))
    createdAt = Column(Integer, default=time.time()) # unix time format
    updateAt = Column(Integer, default=time.time()) # unix time format

    activity = relationship("Activity", back_populates="todos")