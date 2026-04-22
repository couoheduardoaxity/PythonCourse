import pytest
from app.domain.entities.order import Order
from app.infrastructure.repositories.memory_order_repository import (
    MemoryOrderRepository,
)


@pytest.mark.parametrize(
    "repo",
    [
        MemoryOrderRepository(),
    ],
)
def test_repository_contract(repo):
    order = Order.create("phone", 2)

    repo.save(order)

    result = repo.get_by_id(order.id)

    assert result is not None
    assert result.id == order.id
