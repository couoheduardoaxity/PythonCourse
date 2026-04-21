import pytest
from application.services import OrderService
from infrastructure.memory_repo import InMemoryOrderRepository
from infrastructure.sql_repo import SQLOrderRepository


def test_create_order():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)

    service.create_order(1, 100)

    orders = service.list_orders()
    assert len(orders) == 1
    assert orders[0].total == 100


@pytest.mark.parametrize("repo", [InMemoryOrderRepository(), SQLOrderRepository()])
def test_lsp(repo):
    service = OrderService(repo)

    service.create_order(1, 50)
    orders = service.list_orders()

    assert len(orders) == 1
