from dataclasses import dataclass, field


@dataclass(order=True)
class Order:
    id: int
    product: str
    quantity: int
    price: float
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.quantity * self.price

    def apply_discount(self, percentage: float):
        self.total *= 1 - percentage

    def __str__(self):
        return f"Order(id={self.id}, product={self.product}, total={self.total})"
