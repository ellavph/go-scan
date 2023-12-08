# app/user/repositories.py
from typing import Optional
from app.user.models import User

class UserRepository:
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        # Lógica para recuperar um usuário por ID (simulação)
        return User(id=user_id, username=f"user{user_id}", email=f"user{user_id}@example.com")

    def save_user(self, user: User) -> User:
        # Lógica para salvar um usuário (simulação)
        return user