from domain.models import Order
from domain.ports import OrderRepository


class OrderService:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def create_order(self, order_id: int, total: float):
        if total <= 0:
            raise ValueError("Total must be positive")

        order = Order(order_id, total)
        self.repo.save(order)

    def list_orders(self):
        return self.repo.get_all()
