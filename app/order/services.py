import copy

from app.settings.database import get_db
from app.order.repositories import OrderRepsitory


class OrderService:
    def __init__(self, db=get_db()):
        self.__order_repository = OrderRepsitory(db)

    def create(self, order: dict, user: dict):
        order_created = self.__order_repository.create_order(user_id=user.get('username'), status='pending', payment=order.get('payment'), initial_value=order.get('initial_value'), delivery_value=order.get('delivery_value'), amount=order.get('amount'))
        items = [{'order_id': order_created.id, **item} for item in order.get('items')]
        self.__order_repository.create_order_items(items)
        return order_created.hash

    def detail(self, order_id: str):
        order_detail = self.__order_repository.get_order_by_hash(hash=order_id)
        if not order_detail and order_id.isdigit():
            order_detail = self.__order_repository.get_order_by_id(id=int(order_id))
        return OrderService.detail_template(order_detail)

    @staticmethod
    def detail_template(order):
        r = {
            'id': order.id,
            'payment': order.payment,
            'hash': order.hash,
            'user_id': order.user_id,
            'delivery_value': order.delivery_value,
            'amount': order.amount,
            'items': []
        }
        for i in order.items:
            r['items'].append({
                'id': i.id,
                'amount': i.amount,
                # 'dat_insercao': i.dat_insercao,
                'product_id': i.product_id,
                'product_name': i.product_name,
                'quantity': i.quantity,
                'value': i.value
            })
        return copy.deepcopy(r)

