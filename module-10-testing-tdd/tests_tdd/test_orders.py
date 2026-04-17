import pytest
from app.orders import Order, apply_discount


@pytest.fixture
def sample_items():
    return [
        {"price": 10, "quantity": 2},
        {"price": 5, "quantity": 1},
    ]


def test_order_total(sample_items):
    order = Order(sample_items)
    assert order.total() == 25


@pytest.mark.parametrize(
    "total,discount,expected",
    [
        (100, 10, 90),
        (200, 50, 100),
        (50, 0, 50),
    ],
)
def test_apply_discount(total, discount, expected):
    assert apply_discount(total, discount) == expected


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
