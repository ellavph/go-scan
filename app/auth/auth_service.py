from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

secret_key = 'nXe4-ZQEiFYBR3iJfuT0Tm9m6LlL9e6khhF2ZcvahdA'
ACCESS_TOKEN_EXPIRE_MINUTES = 0.30
REFRESH_TOKEN_EXPIRES = 2


class AuthService:

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return payload
        except JWTError:
            raise credentials_exception
