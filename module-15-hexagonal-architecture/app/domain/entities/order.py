from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Order:
    id: str
    product: str
    quantity: int

    @staticmethod
    def create(product: str, quantity: int):
        if not product:
            raise ValueError("Product is required")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        return Order(id=str(uuid4()), product=product, quantity=quantity)
