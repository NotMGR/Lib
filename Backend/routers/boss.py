from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import authenticate
from database import get_db
from models import Boss
from schemas import BossResponse

router = APIRouter(
    prefix="/boss",
    tags=["Boss"],
    dependencies=[Depends(authenticate)]
)

@router.get("/", response_model=list[BossResponse])
def get_bosses(raid_id: int, db: Session = Depends(get_db)):

    bosses = db.query(Boss).filter(Boss.raid_id == raid_id).all()

    return bosses