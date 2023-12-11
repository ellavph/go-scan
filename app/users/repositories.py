from app.settings.database import get_db
from app.users.models import UserModel
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session = get_db()):
        self.db = db

    def create_user(self, document: str, username: str, password: str, email: str):
        user = UserModel(id=document, username=username, password=password, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str):
        return self.db.query(UserModel).filter(UserModel.username == username).first()
