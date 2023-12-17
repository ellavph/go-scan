from app.user.models import UserModel, UserBalance, LogUserBalance
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, password: str, email: str, first_name: str = None, last_name: str = None, document: str = None, username: str = None):
        user = UserModel(id=email, username=email, password=password, email=email, first_name=None, last_name=None, profile='user')
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_balance(self, user_id: str):
        balance = UserBalance(user_id=user_id, balance=0)
        self.db.add(balance)
        self.db.commit()
        self.db.refresh(balance)
        return balance

    def get_user_by_username(self, username: str):
        return self.db.query(UserModel).filter(UserModel.username == username, UserModel.status).first()

    def get_user_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def get_user_by_id(self, document: str):
        return self.db.query(UserModel).filter(UserModel.id == document).first()

    def get_user_by_field(self, field_name: str, field_value: str):
        return self.db.query(UserModel).filter_by(**{field_name: field_value}).first()

    def get_user_balance(self, user_id: str):
        return self.db.query(UserBalance).filter(UserBalance.user_id == user_id).first()

    def get_user_transaction_history(self, balance_id: str, month_and_year: str):
        return list(self.db.query(LogUserBalance).filter(LogUserBalance.balance_id == balance_id, LogUserBalance.month_and_year == month_and_year))

    def get_all_users(self):
        return list(self.db.query(UserModel).filter(UserModel.status))
