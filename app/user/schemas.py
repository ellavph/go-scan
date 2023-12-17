from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4


class BaseUser(BaseModel):
    username: Optional[str] = Field(None, example='josue.silva')


class UserLogin(BaseUser):
    password: str = Field(None, example='#$%P@ssworD')


class UserCreate(BaseModel):
    username: Optional[str] = Field(None, example='josue.silva')
    password: str = Field(None, example='#$%P@ssworD')
    document: Optional[str] = Field(None, example='224.234.840-03')
    email: str = Field(None, example='exemplo@exemplo.com')

    first_name: Optional[str] = Field(None, example='Josué')
    last_name: Optional[str] = Field(None, example='Silva')


class LoginResponse(BaseModel):
    access_token: str = Field(None, example=str(uuid4()))
    refresh_token: str = Field(None, example=str(uuid4()))
    type: str = Field('Bearer')


class UserDetailsResponse(BaseUser):
    picture: str = Field(None, example='user/default.png')
    name: str = Field(None, example='Josué')
    id: str = Field(None, example='10')
    balance: float = Field(None, example='150.00')


class UserResponseModel(BaseUser):
    id: str = Field(None, example='10')
    email: str = Field(None, example='exemplo@exemplo.com')
    dat_insercao: datetime = Field(None, example=datetime.utcnow())
    status: bool = Field(None, example=True)
    first_name: str = Field(None, example='Josué')
    last_name: str = Field(None, example='Silva')
    profile: str = Field(None, example='user')


class HistoryResponse(BaseModel):
    id: int = Field(None, example='10')
    balance_id: int = Field(None, example='50')
    previous_value: float = Field(None, example='100.00')
    current_value: float = Field(None, example='150.00')
    transaction_value: float = Field(None, example='50.00')
    month_and_year: str = Field(None, example='12-2023')
    type: str = Field(None, example='deposit')
