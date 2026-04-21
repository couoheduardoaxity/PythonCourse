class PriceProvider:
    def get_price(self, product_id: str) -> float:
        raise NotImplementedError


class ExternalAPIAdapter(PriceProvider):
    def __init__(self, api):
        self.api = api

    def get_price(self, product_id: str) -> float:
        return self.api.get_price(product_id)
