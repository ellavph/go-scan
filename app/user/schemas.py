from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class UserLogin(BaseUser):
    password: str


class UserCreate(UserLogin):
    document: str
    email: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    type: str
