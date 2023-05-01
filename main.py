from typing import Union
from app.database import engine
from app.models.activity import Base as ActivityBase
from app.models.todolist import ToDo as ToDoBase
from app.api import activity, todolist


from fastapi import FastAPI

app = FastAPI()

app.include_router(activity.router)
app.include_router(todolist.router)


ActivityBase.metadata.create_all(bind=engine)
ToDoBase.metadata.create_all(bind=engine)

