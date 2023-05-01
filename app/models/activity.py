from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import time
from ..database import Base

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), index=True, unique=True)
    title = Column(String(100))
    createdAt = Column(Integer, default=time.time()) # unix time format
    updateAt = Column(Integer, default=time.time()) # unix time format

    todos = relationship("ToDo", back_populates="activity")