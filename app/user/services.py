# app/user/services.py
from app.user.models import User
from app.user.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User:
        # Lógica para obter um usuário
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user: User) -> User:
        # Lógica para criar um usuário
        return self.user_repository.save_user(user)
