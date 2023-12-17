
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.settings.database import Base
from app.models.models import Log


class UserModel(Base, Log):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)  # ID podendo ser CPF, CNPJ ou matricula
    username = Column(String, index=True, nullable=True)
    password = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    picture = Column(String, nullable=True)
    profile = Column(String, nullable=True)
    # Relacionamento bidirecional com UserBalance
    user_balance = relationship("UserBalance", back_populates="user_model")


class UserBalance(Base, Log):
    __tablename__ = "user_balance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("user.id"), index=True)  # Chave estrangeira referenciando user_model.id
    balance = Column(Float, nullable=True)

    # Relacionamento bidirecional com UserModel
    user_model = relationship("UserModel", back_populates="user_balance")


class LogUserBalance(Base, Log):
    __tablename__ = "log_user_balance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    balance_id = Column(Integer, ForeignKey("user_balance.id"), index=True)
    previous_value = Column(Float, nullable=True)
    current_value = Column(Float, nullable=True)
    transaction_value = Column(Float, nullable=True)
    month_and_year = Column(String, nullable=True)
    type = Column(String, nullable=True)
