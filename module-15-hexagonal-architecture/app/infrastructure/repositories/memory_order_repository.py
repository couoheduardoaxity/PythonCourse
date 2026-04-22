from app.domain.entities.order import Order


class MemoryOrderRepository:
    def __init__(self):
        self._orders = {}

    def save(self, order: Order) -> None:
        self._orders[order.id] = order

    def get_by_id(self, order_id: str) -> Order | None:
        return self._orders.get(order_id)
