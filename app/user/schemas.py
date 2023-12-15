from pydantic import BaseModel
from datetime import datetime


class BaseUser(BaseModel):
    username: str


class UserLogin(BaseUser):
    password: str


class UserCreate(UserLogin):
    document: str
    email: str
    first_name: str
    last_name: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    type: str


class UserDetailsResponse(BaseUser):
    picture: str
    name: str
    id: str
    balance: float


class UserResponseModel(BaseUser):
    id: str
    email: str
    dat_insercao: datetime  # Ajuste o tipo de dado conforme necessário
    status: bool
    first_name: str
    last_name: str
    profile: str


class HistoryResponse(BaseModel):
    id: int
    balance_id: int
    previous_value: float
    current_value: float
    transaction_value: float
    month_and_year: str
    type: str
