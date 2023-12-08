# app/user/routes.py
from fastapi import APIRouter, HTTPException
from app.user.services import UserService
from app.user.models import User
from app.user.repositories import UserRepository

router = APIRouter()
user_service = UserService(user_repository=UserRepository())  # Use uma injeção de dependência adequada aqui

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    user = user_service.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)