# app/user/routes.py
from fastapi import APIRouter, HTTPException, Depends
from app.user.services import UserService
from app.user.schemas import UserSchema
from app.user.repositories import UserRepository
from sqlalchemy.orm import Session
from app.settings.database import get_db

router = APIRouter()


@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(user_repository=UserRepository(db))
    user = user_service.get_user(user_id)
    return user


@router.post("/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_service = UserService(user_repository=UserRepository(db))
    created_user = user_service.create_user(user)
    return created_user
