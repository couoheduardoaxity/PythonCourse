from typing import Protocol

from app.domain.entities.order import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...

    def get_by_id(self, order_id: str) -> Order | None: ...
