import copy
from typing import Tuple, Dict

from app.settings.database import get_db
from app.user.repositories import UserRepository
from app.user.schemas import UserCreate, UserDetailsResponse, UserLogin
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
            access_token = AuthService.create_access_token(data={"username": user.username, "document": user.id, 'profile': user.profile}, expires_delta=access_token_expires)

            # Gera o token JWT de atualização
            refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRES)  # Expira em 2 minutos, ajuste conforme necessário
            refresh_token = AuthService.create_access_token(data={"username": user.username, "document": user.id, 'profile': user.profile}, expires_delta=refresh_token_expires)

            # Retorna ambos os tokens
            return True, {"access_token": access_token, "refresh_token": refresh_token}
        return False, {}

    def create_user(self, user_data: UserCreate):
        user_data.password = hash_password(password=user_data.password)

        user = self.user_repository.create_user(**user_data.model_dump())
        if user:
            self.user_repository.create_balance(user_id=user.id)

        return user

    def get_user(self, user_data: UserCreate):
        fields_to_check = ["username", "email", "document"]

        for field in fields_to_check:
            user = None
            if hasattr(user_data, field):
                user = self.user_repository.get_user_by_field('id' if field == 'document' else field, getattr(user_data, field))

            if user:
                return user, field  # Retorna o usuário e o campo correspondente

        return None, None

    def get_details(self, current_user: dict):
        user = self.user_repository.get_user_by_id(document=current_user.get('document'))
        if user is None:
            return None
        balance = self.user_repository.get_user_balance(user.id)
        if not balance:
            return None

        return {
            'username': user.username,
            'name': user.first_name if user.first_name else '',
            'id': user.id,
            'balance': balance.balance if balance.balance >= 0 else balance.balance * -1,
            'picture': user.picture if user.picture else 'default.svg'
        }

    def transaction_history(self, user_id: str, month_and_year: str, current_user: dict):
        historic = []
        if current_user.get('profile') not in ['admin']:
            return historic, 'Not authorized', 403

        user = self.user_repository.get_user_by_id(document=user_id)
        if user is None:
            return historic, 'User not found', 404

        balance = self.user_repository.get_user_balance(user.id)

        if not balance and not month_and_year:
            return historic, 'Bad request: No balance and no specified month/year', 400

        historic = self.user_repository.get_user_transaction_history(balance_id=balance.id, month_and_year=month_and_year)

        if not historic:
            return [], 'No transaction history available for the specified date', 200

        return historic, 'Transaction history retrieved successfully', 200

    def get_all_users(self, current_user: dict):
        if current_user.get('profile') not in ['admin']:
            return []
        all_users_database = self.user_repository.get_all_users()
        return [{k: v for k, v in u.__dict__.items() if k not in ['password']} for u in all_users_database]
