# app/user/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.settings.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True) # ID podendo ser CPF, CNPJ ou matricula
    username = Column(String, index=True, nullable=True)
    password = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    picture = Column(String, nullable=True)
