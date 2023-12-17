from typing import Optional

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from uuid import uuid4


class Item(BaseModel):
    product_id: str = Field(None, example='5550')
    product_name: str = Field(None, example='Coca cola 2L')
    amount: float = Field(None, example=31.50)
    value: float = Field(None, example=10.50)
    quantity: int = Field(None, example=3)

    class Config:
        extra = "ignore"


class CreateOrder(BaseModel):
    # user_id: str = Field(None, example='exemplo@exemplo.com.br')
    payment: str = Field(None, example='credit')
    initial_value: float = Field(None, example=31.50)
    delivery_value: float = Field(None, example=5.00)
    amount: float = Field(None, example=36.50)
    items: List[Item]

    class Config:
        extra = "ignore"


class CreateOrderResponse(BaseModel):
    order_id: str = Field(None, example=str(uuid4()))


class ItemDetail(Item):
    product_id: int = Field(None)


class OrderDetail(CreateOrder):
    user_id: str
    items: List[ItemDetail]
