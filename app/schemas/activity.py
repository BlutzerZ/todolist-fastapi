from typing import Optional
from pydantic import BaseModel

class ActivityCreate(BaseModel):
    title: Optional[str]
    email: str

class ActivityUpdate(BaseModel):
    title: str