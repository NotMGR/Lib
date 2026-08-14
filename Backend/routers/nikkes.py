from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func


from database import get_db
from models import Nikke, TeamCharacter, Team
from schemas import NikkeResponse, NikkeCreate

router = APIRouter(
    prefix="/nikkes",
    tags=["Nikkes"]
)
for r in router.routes:
    print(r)

@router.get("/", response_model=list[NikkeResponse])
def get_nikkes(
    db: Session = Depends(get_db)
):
    nikke_list = db.query(Nikke).all()

    return nikke_list

@router.get("/{nikke_id}", response_model=NikkeResponse)
def get_nikke(
    nikke_id: int,
    db: Session = Depends(get_db)
):
    nikke_response = db.get(Nikke, nikke_id)

    if nikke_response is None:
        raise HTTPException(
            status_code=404,
            detail="Nikke not found"
        )


    return nikke_response

@router.post("/", response_model=NikkeResponse)
def create_nikke(
    nikke: NikkeCreate,
    db: Session = Depends(get_db)
):
    existing_nikke = (
    db.query(Nikke)
    .filter(func.lower(Nikke.name) == nikke.name.lower())
    .first()
)
    if existing_nikke:
        raise HTTPException(
            status_code=409,
            detail="Nikke with same name already exists"
        )
        
    new_nikke = Nikke(
        name = nikke.name,
        burst= nikke.burst,
        element = nikke.element,
        manufacturer = nikke.manufacturer,
        role = nikke.role,
        image_path = f"nikke/{nikke.image_path}",
    )

    db.add(new_nikke)
    db.commit()
    db.refresh(new_nikke)

    return new_nikke

@router.delete("/{nikke_id}")
def delete_nikke(
    nikke_id: int,
    db: Session = Depends(get_db)
):
    nikke = db.get(Nikke, nikke_id)

    if nikke is None:
        raise HTTPException(
            status_code=404,
            detail="Nikke not found."
        )

    used = (
    db.query(TeamCharacter)
    .filter(TeamCharacter.character_id == nikke_id)
    .first()
)

    if used:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete Nikke because it is used in existing teams.")
        
    db.delete(nikke)
    db.commit()
    return {
        "message": "Nikke deleted successfully."
    }

@router.put("/{nikke_id}", response_model=NikkeResponse)
def update_nikke(
    nikke_id: int,
    nikke_data: NikkeCreate,
    db: Session =  Depends(get_db)
):

    nikke = db.get(Nikke, nikke_id)

    if nikke is None:
        raise HTTPException(
            status_code=404,
            detail="Nikke not found."
        )

    existing = (
        db.query(Nikke)
        .filter(
            func.lower(Nikke.name) == nikke_data.name.lower(),
            Nikke.id != nikke_id
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Another Nikke with this name already exists."
        )

    nikke.name = nikke_data.name
    nikke.burst = nikke_data.burst
    nikke.element = nikke_data.element
    nikke.manufacturer = nikke_data.manufacturer
    nikke.role = nikke_data.role
    nikke.image_path = f"nikke/{nikke_data.image_path}"

    db.commit()
    db.refresh(nikke)

    return nikke
