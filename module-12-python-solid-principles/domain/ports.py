from typing import List, Protocol

from .models import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...

    def get_all(self) -> List[Order]: ...
