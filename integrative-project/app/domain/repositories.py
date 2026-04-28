from abc import ABC, abstractmethod
from typing import List

from .entities.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass
