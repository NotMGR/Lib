from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import User, Union
from schemas import UserResponse, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserResponse])
def get_users(
    union_id: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(User)

    if union_id is not None:
        query = query.filter(User.union_id == union_id)

    return query.order_by(User.username).all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    username = user.username.strip()

    existing_user = (
        db.query(User)
        .filter(func.lower(User.username) == username.lower())
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Username already exists."
        )

    # Make sure the selected union actually exists
    union = db.get(Union, user.union_id)

    if union is None:
        raise HTTPException(
            status_code=404,
            detail="Union not found."
        )

    new_user = User(
        username=username,
        is_active=user.is_active,
        union_id=user.union_id,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    username = user_data.username.strip()

    existing_user = (
        db.query(User)
        .filter(
            func.lower(User.username) == username.lower(),
            User.id != user_id
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Another user with this name already exists."
        )

    # Make sure the new union exists
    union = db.get(Union, user_data.union_id)

    if union is None:
        raise HTTPException(
            status_code=404,
            detail="Union not found."
        )

    user.username = username
    user.is_active = user_data.is_active
    user.union_id = user_data.union_id

    db.commit()
    db.refresh(user)

    return user