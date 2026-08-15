from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from auth import authenticate
from database import get_db
from models import User
from schemas import UserResponse, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(authenticate)]
)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    users = db.query(User)\
            .order_by(User.username)\
            .all()
    

    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int,
             db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    return user

@router.post(
        "/",
        response_model = UserResponse,
        status_code = status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )


    new_user = User(
        username = user.username,
        is_active = user.is_active,
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

    existing_user = (
        db.query(User)
        .filter(func.lower(User.username) == user_data.username.lower(),
        User.id != user_id)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Another user with this name already exists."
        )

    user.username = user_data.username
    user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)

    return user
