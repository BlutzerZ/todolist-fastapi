from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.todolist import ToDo as toDoModel
from ..schemas.todolist import toDoCreate, toDoUpdate
import time

router = APIRouter(prefix="/todo-items", tags=["todo-items"])

# Get ALl
@router.get("/")
async def get_all_todo(activity_group_id: int, db: Session = Depends(get_db)):
    db_item = db.query(toDoModel).filter(toDoModel.activity_group_id == activity_group_id).all()
    return {"status": "Success",
            "message": "Success",
            "data": db_item
            }

# Get One
@router.get("/{activity_id}")
async def get_one_todo(activity_id: int, db: Session = Depends(get_db)):
    db_item = db.query(toDoModel).filter(toDoModel.id == activity_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_item

# create
@router.post("/")
async def create_todo(todo: toDoCreate, db: Session = Depends(get_db)):
    db_item = toDoModel(
            title=todo.title, 
            activity_group_id=todo.activity_group_id,
            is_active=todo.is_active
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"status": "Success",
            "message": "Success",
            "data": db_item
            }

# update
@router.patch("/{todo_id}")
async def update_todo(todo_id: int, todo: toDoUpdate,db: Session = Depends(get_db)):
    db_item = db.query(toDoModel).filter(toDoModel.id == todo_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = todo.title
    db_item.priority = todo.priority
    db_item.is_active = todo.is_active
    db_item.updateAt = time.time()
    db.commit()
    db.refresh(db_item)
    return {"status": "Success",
            "message": "Success",
            "data": db_item
            }

# Delete
@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_item = db.query(toDoModel).filter(toDoModel.id == todo_id).first()
    if db_item is None:
        return JSONResponse(
            status_code=404,
            content={"status": "Not Found",
                    "message": f"Todo with ID {todo_id} Not Found"
                    },
            )
    db.delete(db_item)
    db.commit()
    return {
        "status": "Success",
        "message": "Success",
        "data": {}
    }