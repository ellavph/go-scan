from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.order.schemas import CreateOrder, CreateOrderResponse, OrderDetail
from app.settings.database import get_db
from app.order.services import OrderService

router = APIRouter()


@router.get('/detail', response_model=OrderDetail)
def get_detail(order_id: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    order_service = OrderService(db)
    detail = order_service.detail(order_id=order_id)
    return detail


@router.post('/create', response_model=CreateOrderResponse)
def create(order: CreateOrder, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    order_service = OrderService(db)
    order_id = order_service.create(order.model_dump(), user=current_user)
    return CreateOrderResponse(order_id=order_id)
