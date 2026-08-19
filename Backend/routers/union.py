from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import Union
from schemas import UnionCreate, UnionResponse

router = APIRouter(
    prefix="/unions",
    tags=["Unions"]
)

@router.get("/", response_model=list[UnionResponse])
def get_unions(db: Session = Depends(get_db)):

    unions = db.query(Union)\
             .order_by(Union.name)\
             .all()

    return unions

@router.get("/{union_id}", response_model=UnionResponse)
def get_union(
    union_id: int,
    db: Session = Depends(get_db)
):
    union = db.get(Union, union_id)

    if union is None:
        raise HTTPException(
            status_code=404,
            detail="Union not found"
        )

    return union


@router.post("/", response_model = UnionResponse, status_code=status.HTTP_201_CREATED)
def create_union(
    union: UnionCreate,
    db: Session = Depends(get_db)
):
    name = union.name.strip()
    existing_union = db.query(Union).filter(Union.name == name).first()

    if existing_union:
        raise HTTPException(
            status_code=409,
            detail="Union name already taken."
        )

    new_union = Union(
        name = name
    )

    db.add(new_union)
    db.commit()
    db.refresh(new_union)

    return new_union

@router.put("/{union_id}", response_model=UnionResponse)
def update_union(
    union_id: int,
    union_data: UnionCreate,
    db: Session = Depends(get_db)
):
    union = db.get(Union, union_id)

    if union is None:
        raise HTTPException(
            status_code=404,
            detail="Union not found."
        )

    name = union_data.name.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Union name cannot be empty."
        )

    existing_union = (
        db.query(Union)
        .filter(
            func.lower(Union.name) == name.lower(),
            Union.id != union.id
        )
        .first()
    )

    if existing_union:
        raise HTTPException(
            status_code=409,
            detail="Another union with this name already exists."
        )

    union.name = name

    db.commit()
    db.refresh(union)

    return union