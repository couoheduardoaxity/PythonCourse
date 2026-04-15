from typing import Literal, Protocol, TypedDict


# TypedDict → estructura tipo JSON
class Order(TypedDict):
    id: int
    total: float
    status: str


# Literal → valores restringidos
OrderStatus = Literal["pending", "paid", "shipped"]


# Protocol → contratos (como interfaces)
class DiscountStrategy(Protocol):
    def apply(self, total: float) -> float: ...


def create_order(order_id: int, total: float) -> Order:
    return {
        "id": order_id,
        "total": total,
        "status": "pending",
    }


def update_status(order: Order, status: OrderStatus) -> Order:
    order["status"] = status
    return order


def apply_discount(order: Order, strategy: DiscountStrategy) -> Order:
    order["total"] = strategy.apply(order["total"])
    return order
