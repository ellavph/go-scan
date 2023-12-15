from cgi import parse_qs

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.user.services import UserService
from app.user.schemas import UserCreate, BaseUser, UserLogin, LoginResponse, UserDetailsResponse, UserResponseModel, HistoryResponse
from app.auth.dependencies import get_current_user

from typing import List

router = APIRouter()


@router.post('/login', response_model=LoginResponse)
def login(user_login: str | UserLogin, db: Session = Depends(get_db)):
    if isinstance(user_login, str):
        user_login = parse_qs(user_login)
        user_login = {key: value[0] for key, value in user_login.items()}
        user_login = UserLogin(**user_login)

    user_service = UserService(db)
    authenticated, token_info = user_service.authenticate_user(username=user_login.username, password=user_login.password)

    if authenticated:
        return LoginResponse(access_token=token_info.get('access_token'), refresh_token=token_info.get('refresh_token'), type='Bearer')

    raise HTTPException(status_code=401, detail='Invalid credentials')


@router.post('/create', response_model=BaseUser)
def create(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    existing_user, field = user_service.get_user(user_data)
    if existing_user:
        raise HTTPException(status_code=409, detail='{} already registered'.format(field).capitalize())

    user = user_service.create_user(user_data)
    if not user:
        raise HTTPException(status_code=500, detail='Internal Server Error.')

    return BaseUser(username=user.username)


@router.get('/details', response_model=UserDetailsResponse)
def home(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    details = user_service.get_details(current_user)

    if details is None:
        raise HTTPException(status_code=500, detail='Details not found')
    return details


@router.get('/transaction/history', response_model=List[HistoryResponse])
def transaction_history(user_id: str, month_and_year: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    historic, description, status_code = user_service.transaction_history(user_id, month_and_year, current_user)
    if not historic:
        raise HTTPException(status_code=status_code, detail=description)
    return historic


@router.get('/all', response_model=List[UserResponseModel])
def get_all_users(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user_service = UserService(db)
    all_users = user_service.get_all_users(current_user)
    return all_users
