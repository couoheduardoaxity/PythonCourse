from unittest.mock import MagicMock

from app.orders import fetch_order_from_api


def test_fetch_order():
    mock_api = MagicMock()
    mock_api.get_order.return_value = {"id": 1, "total": 100}

    result = fetch_order_from_api(mock_api, 1)

    assert result["id"] == 1
    mock_api.get_order.assert_called_once_with(1)
