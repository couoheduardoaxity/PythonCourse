from typing import List

from domain.models import Order


class SQLOrderRepository:
    def __init__(self):
        self._db = []  # simulación de base de datos

    def save(self, order: Order) -> None:
        # aquí normalmente harías INSERT
        self._db.append(order)

    def get_all(self) -> List[Order]:
        # aquí normalmente harías SELECT
        return list(self._db)
