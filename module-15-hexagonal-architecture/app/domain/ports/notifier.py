from typing import Protocol

from app.domain.entities.order import Order


class Notifier(Protocol):
    def notify(self, order: Order) -> None: ...
