from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.user.services import UserService
from app.user.schemas import UserCreate, UserLogin, LoginResponse
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user_service = UserService(db)
    authenticated, info_token = user_service.authenticate_user(user_login.username, user_login.password)

    if authenticated:
        return LoginResponse(access_token=info_token.get('access_token'), refresh_token=info_token.get('refresh_token'), type='Bearer')

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/create")
def create(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    existing_user, field = user_service.get_user(user_data)
    if existing_user:
        raise HTTPException(status_code=409, detail="{} already registered".format(field).capitalize())

    user = user_service.create_user(user_data)
    return user


@router.get('/home')
def home(current_user:  dict = Depends(get_current_user)):
    return True