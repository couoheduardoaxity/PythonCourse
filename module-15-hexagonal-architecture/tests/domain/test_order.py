import pytest
from app.domain.entities.order import Order


def test_create_order_success():
    order = Order.create("laptop", 1)

    assert order.product == "laptop"
    assert order.quantity == 1


def test_create_order_invalid_quantity():
    with pytest.raises(ValueError):
        Order.create("laptop", 0)
