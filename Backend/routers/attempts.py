from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

from database import get_db
from models import AttemptFrameTable, User, Raid
from schemas import AttemptResponse, AttemptUpdate

router = APIRouter(
    prefix="/attempts",
    tags=["Attempts"]
)

@router.get("/{raid_id}", response_model=list[AttemptResponse])
def get_attempts_for_raid(
    raid_id: int,
    db: Session = Depends(get_db)
):
    raid = db.get(Raid, raid_id)

    if raid is None:
        raise HTTPException(
            status_code=404,
            detail="Raid not found."
        )

    attempts = get_attempts_for_raid(db, raid_id)

    return [
        AttemptResponse(
            id=row.id,
            user_id=row.user_id,
            raid_id=row.raid_id,
            username=row.user.username,
            attempts=[
                row.btn_1,
                row.btn_2,
                row.btn_3,
                row.btn_4,
                row.btn_5,
            ],
            attempts_remaining=row.attempts_remaining,
        )
        for row in attempts
    ]

@router.put("/{attempt_id}")
def update_attempt(
    attempt_id: int,
    attempt_data: AttemptUpdate,
    db: Session = Depends(get_db)
):
    attempt = db.get(AttemptFrameTable, attempt_id)

    if attempt is None:
        raise HTTPException(
            status_code=404,
            detail="Attempt not found."
        )

    for i in range (1, 6):
        setattr(
            attempt,
            f"btn_{i}",
            1 if i in attempt_data.active_buttons else 0
        )

    attempt.attempts_remaining = 3 - len(attempt_data.active_buttons)

    db.commit()
    db.refresh(attempt)

    return {
        "message": "Attempt updated sucessfully."
    }



def get_attempts_for_raid(db: Session, raid_id: int):
    return (
        db.execute(
            select(AttemptFrameTable)
            .join(User, AttemptFrameTable.user_id == User.id)
            .options(joinedload(AttemptFrameTable.user))
            .where(AttemptFrameTable.raid_id == raid_id)
            .order_by(User.username)
        )
        .scalars()
        .all()
    )