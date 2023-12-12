from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth_service = AuthService()

    try:
        payload = auth_service.decode_access_token(token)
        return payload
    except:
        raise credentials_exception
