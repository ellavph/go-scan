from typing import Tuple, Dict

from app.settings.database import get_db
from app.user.repositories import UserRepository
from app.user.schemas import UserCreate
from app.utils.utils import hash_password, verify_password
from datetime import timedelta
from app.auth.auth_service import AuthService, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRES


class UserService:
    def __init__(self, db=get_db()):
        self.user_repository = UserRepository(db)

    def authenticate_user(self, username: str, password: str) -> tuple[bool, dict[str, any]]:
        user = self.user_repository.get_user_by_username(username)
        if user and verify_password(password, user.password):
            # Se o usuário é autenticado com sucesso, gera o token JWT de acesso
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = AuthService.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

            # Gera o token JWT de atualização
            refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRES)  # Expira em 2 minutos, ajuste conforme necessário
            refresh_token = AuthService.create_access_token(data={"sub": user.username}, expires_delta=refresh_token_expires)

            # Retorna ambos os tokens
            return True, {"access_token": access_token, "refresh_token": refresh_token}
        return False, {}

    def create_user(self, user_data: UserCreate):
        user_data.password = hash_password(password=user_data.password)

        return self.user_repository.create_user(**user_data.dict())

    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)

    def get_user(self, user_data: UserCreate):
        fields_to_check = ["username", "email", "document"]

        for field in fields_to_check:
            user = None
            if hasattr(user_data, field):
                user = self.user_repository.get_user_by_field('id' if field == 'document' else field, getattr(user_data, field))

            if user:
                return user, field  # Retorna o usuário e o campo correspondente

        return None, None