
from app.settings.database import get_db
from app.user.repositories import UserRepository
from app.user.schemas import UserCreate
from app.utils.utils import hash_password, verify_password


class UserService:
    def __init__(self, db=get_db()):
        self.user_repository = UserRepository(db)

    def authenticate_user(self, username: str, password: str) -> tuple[bool, str]:
        user = self.user_repository.get_user_by_username(username)
        if user and verify_password(password, user.password):
            return True, '1'
        return False, '0'

    def create_user(self, user_data: UserCreate):
        user_data.password = hash_password(password=user_data.password)

        return self.user_repository.create_user(**user_data.dict())

    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)
