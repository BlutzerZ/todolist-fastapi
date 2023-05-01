from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.activity import Activity as activityModel
from ..schemas.activity import ActivityCreate, ActivityUpdate
import time

router = APIRouter(prefix="/activity-groups", tags=["activity-group"])

# Get ALl
@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    db_item = db.query(activityModel).all()
    return db_item

# Get One
@router.get("/{activity_id}")
async def get_one(activity_id: int, db: Session = Depends(get_db)):
    db_item = db.query(activityModel).filter(activityModel.id == activity_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_item

# Create
@router.post("/")
async def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    db_item = activityModel(
            title=activity.title, 
            email=activity.email
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Update
@router.patch("/{activity_id}")
async def update_activity(activity_id: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    db_item = db.query(activityModel).filter(activityModel.id == activity_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = activity.title
    db_item.updateAt = time.time()
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete
@router.delete("/{activity_id}")
async def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    db_item = db.query(activityModel).filter(activityModel.id == activity_id).first()
    if db_item is None:
        return JSONResponse(
            status_code=404,
            content={"status": "Not Found",
                    "message": f"Activity with ID {activity_id} Not Found"
                    },
            )
    db.delete(db_item)
    db.commit()
    return {
        "status": "Success",
        "message": "Success",
        "data": {}
    }