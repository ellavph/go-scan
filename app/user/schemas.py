from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    document: str
    username: str
    password: str
    email: str


class LoginResponse(BaseModel):
    token: str


class CreateResponse(BaseModel):
    username: str
