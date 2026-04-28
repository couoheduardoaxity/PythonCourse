from datetime import datetime
from uuid import uuid4

from app.domain.entities.order import Order


class CreateOrder:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, customer_id: str, total: float):
        order = Order(
            id=uuid4(),
            customer_id=customer_id,
            total=total,
            created_at=datetime.utcnow(),
        )
        self.repo.save(order)
        return order
