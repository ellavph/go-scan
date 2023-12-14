from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.user.services import UserService
from app.user.schemas import UserCreate, BaseUser, UserLogin, LoginResponse, UserDetailsResponse
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post('/login', response_model=LoginResponse)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user_service = UserService(db)
    authenticated, token_info = user_service.authenticate_user(user_login.username, user_login.password)

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
        raise HTTPException(status_code=500, detail='Internal Server Error.')
    return details
