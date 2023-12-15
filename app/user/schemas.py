from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4


class BaseUser(BaseModel):
    username: str = Field(default='josue')


class UserLogin(BaseUser):
    password: str = Field(default='123456')


class UserCreate(UserLogin):
    document: str
    email: str = Field(default='exemplo@exemplo.com')
    first_name: str = Field(default='Josué')
    last_name: str = Field(default='Silva')


class LoginResponse(BaseModel):
    access_token: str = Field(default=uuid4().hex)
    refresh_token: str = Field(default=uuid4().hex)
    type: str = Field('Bearer')


class UserDetailsResponse(BaseUser):
    picture: str = Field(default='user/default.png')
    name: str = Field(default='Josué')
    id: str = Field(default='10')
    balance: float = Field(default='150.00')


class UserResponseModel(BaseUser):
    id: str = Field(default='10')
    email: str = Field(default='exemplo@exemplo.com')
    dat_insercao: datetime = Field(default=datetime.utcnow())
    status: bool = Field(default=True)
    first_name: str = Field(default='Josué')
    last_name: str = Field(default='Silva')
    profile: str = Field(default='user')


class HistoryResponse(BaseModel):
    id: int = Field(default='10')
    balance_id: int = Field(default='50')
    previous_value: float = Field(default='100.00')
    current_value: float = Field(default='150.00')
    transaction_value: float = Field(default='50.00')
    month_and_year: str = Field(default='12-2023')
    type: str = Field(default='deposit')

