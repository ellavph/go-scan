# app/user/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.settings.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True) # ID podendo ser CPF, CNPJ ou matricula
    usuario = Column(String, index=True, nullable=True)
    senha = Column(String, nullable=True)
    nome = Column(String, nullable=True)
    sobrenome = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    foto = Column(String, nullable=True)

