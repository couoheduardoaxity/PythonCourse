from app.adapters.external_api import ExternalPriceAPI
from app.adapters.price_adapter import ExternalAPIAdapter


def test_external_api_adapter():
    api = ExternalPriceAPI()
    adapter = ExternalAPIAdapter(api)

    price = adapter.get_price("product-1")

    assert price == 100.0
