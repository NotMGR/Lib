from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import select, func


from database import get_db
from models import Raid, Boss, AttemptFrameTable, User
from schemas import RaidResponse, RaidInfoResponse, AttemptResponse, RaidUpdate, RaidCreate

router = APIRouter(
    prefix="/raids",
    tags=["Raids"]
)

@router.get("/", response_model=list[RaidResponse])
def get_raids(db: Session = Depends(get_db)):

    raids = db.query(Raid)\
            .order_by(Raid.name)\
            .all()

    return raids

@router.get("/{raid_id}", response_model=RaidInfoResponse)
def get_raid_info(
    raid_id: int,
    db: Session = Depends(get_db)
):
    raid_response = (db.query(Raid)
                .filter(Raid.id == raid_id)
                .options(
                    joinedload(Raid.bosses)
                )
                .first()
)   
    if raid_response is None:
        raise HTTPException(
            status_code=404,
            detail="Raid not found"
        )
    
    return raid_response

@router.put("/{raid_id}", response_model=RaidResponse)
def update_raid_info(
    raid_id: int,
    raid_data: RaidUpdate,
    db: Session = Depends(get_db)
):
    raid = db.get(Raid, raid_id)

    if raid is None:
        raise HTTPException(
            status_code=404,
            detail="Raid not found."
        )

    existing = (
            db.query(Raid)
            .filter(
                func.lower(Raid.name) == raid_data.name.lower(),
                Raid.id != raid.id
            )
            .first()
        )

    if existing:
        raise HTTPException(
            status_code=409,
            detail = "Another raid with this name already exists."
        )

    raid.name = raid_data.name
    for boss_data in raid_data.bosses:
        boss = db.get(Boss, boss_data.id)

        if boss is None:
            raise HTTPException(
                status_code=404,
                detail = f"Boss {boss_data.id} not found."
            )
        boss.name = boss_data.name
        boss.weakness = boss_data.weakness

    db.commit()
    db.refresh(raid)

    return raid

@router.post("/", response_model=RaidResponse)
def create_raid(
    raid_data: RaidCreate,
    db: Session = Depends(get_db)
):
    existing_name = db.query(Raid).filter(func.lower(Raid.name) == raid_data.name.lower()).first()
    if existing_name:
        raise HTTPException(
            status_code=409,
            detail="Another raid with this name already exists."
        )
    
    raid = Raid(
        name=raid_data.name,
        bosses=[
            Boss(
                name=b.name,
                weakness=b.weakness,
                hp=100_000_000_000
            )
            for b in raid_data.bosses
        ]
    )

    db.add(raid)
    db.flush()
    create_attempt_frames(db, raid)

    db.commit()
    db.refresh(raid)


    return raid

@router.delete("/{raid_id}")
def delete_raid(
    raid_id: int,
    db: Session = Depends(get_db)
):
    raid = db.get(Raid, raid_id)

    if not raid:
        raise HTTPException(
            status_code=404,
            detail="Raid not found."
        )

    db.delete(raid)
    db.commit()
    return{
        "message": "Raid deleted successfully."
    }
    



def create_attempt_frames(db, raid):
        users = (
             db.query(User)
             .filter(User.is_active == True)
             .all()
        )

        for user in users:
            raid.raid_attempt.append(                 
                AttemptFrameTable(
                    user_id = user.id,
                    btn_1=0,
                    btn_2=0,
                    btn_3=0,
                    btn_4=0,
                    btn_5=0,
                    attempts_remaining=3
                )
            )
