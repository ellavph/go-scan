# app/user/security.py
from typing import Optional
from app.user.schemas import UserSchema


class UserRepository:
    def get_user_by_id(self, user_id: int):
        # Lógica para recuperar um usuário por ID (simulação)
        return {}

        #return User(id=user_id, username=f"user{user_id}", email=f"user{user_id}@example.com")

    def save_user(self, user: UserSchema) -> UserSchema:
        # Lógica para salvar um usuário (simulação)
        return {}
