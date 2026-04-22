from app.application.dtos.order_dto import CreateOrderDTO
from app.domain.entities.order import Order
from app.domain.ports.notifier import Notifier
from app.domain.ports.order_repository import OrderRepository


class CreateOrder:
    def __init__(self, repository: OrderRepository, notifier: Notifier):
        self.repository = repository
        self.notifier = notifier

    def execute(self, dto: CreateOrderDTO) -> Order:
        order = Order.create(dto.product, dto.quantity)

        self.repository.save(order)
        self.notifier.notify(order)

        return order
