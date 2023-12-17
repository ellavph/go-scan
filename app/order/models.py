from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.settings.database import Base
from app.models.models import Log
import uuid
from app.user.models import UserModel


class Order(Base, Log):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey(UserModel.id), index=True)
    status = Column(String, nullable=True)
    payment = Column(String, nullable=True)
    initial_value = Column(Float, nullable=True)
    delivery_value = Column(Float, nullable=True)
    amount = Column(Float, nullable=True)
    hash = Column(String, default=lambda: uuid.uuid4().hex, unique=True)
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base, Log):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(String, nullable=True)  # Não é FK por enquanto, pois poderá ser integração
    product_name = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    value = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    order_id = Column(Integer, ForeignKey('order.id'), index=True)

    order = relationship('Order', back_populates='items', cascade='all')

