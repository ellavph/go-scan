from pydantic import BaseModel


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

