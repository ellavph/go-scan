from sqlalchemy.orm import Session
from app.order.models import Order, OrderItem
from typing import List


class OrderRepsitory:
    def __init__(self, db: Session):
        self.db = db

    def get_order(self, order_id: int):
        return self.db.query(Order).filter(Order.id == order_id).first()

    def get_order_items(self, order_id: int):
        return list(self.db.query(OrderItem).filter(OrderItem.order_id == order_id))

    def create_order(self, user_id: str, status: str, payment: str, initial_value: float, delivery_value: float, amount: float):
        order = Order(user_id=user_id, status=status, payment=payment, initial_value=initial_value, delivery_value=delivery_value, amount=amount)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def create_order_items(self, items: List[dict]):
        items = [OrderItem(**i) for i in items]
        self.db.add_all(items)
        self.db.commit()
        return items

    def get_order_by_hash(self, hash: str):
        return self.db.query(Order).filter(Order.hash == hash).first()

    def get_order_by_id(self, id: int):
        return self.db.query(Order).filter(Order.id == id).first()
