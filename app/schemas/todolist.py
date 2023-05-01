from typing import Optional
from pydantic import BaseModel

class toDoCreate(BaseModel):
    title: str
    activity_group_id: str
    is_active: Optional[bool]

class toDoUpdate(BaseModel):
    title: str
    priority: Optional[str]
    is_active: Optional[bool]
    status: Optional[str]