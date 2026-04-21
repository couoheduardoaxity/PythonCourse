from typing import List

from domain.models import Order


class InMemoryOrderRepository:
    def __init__(self):
        self.orders: List[Order] = []

    def save(self, order: Order) -> None:
        self.orders.append(order)

    def get_all(self) -> List[Order]:

        return self.orders
