from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.settings.database import get_db
from app.user.services import UserService
from app.user.schemas import UserCreate, UserLogin, LoginResponse

router = APIRouter()



@router.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs", status_code=302)


@router.post("/login", response_model=LoginResponse)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user_service = UserService(db)
    authenticated, token = user_service.authenticate_user(user_login.username, user_login.password)

    if authenticated:
        authenticated, token = user_service.authenticate_user(user_login.username, user_login.password)
        return LoginResponse(token=token)

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/create")
def create(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    existing_user = user_service.get_user_by_username(user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    user = user_service.create_user(user_data)
    return user
