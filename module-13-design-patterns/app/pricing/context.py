from app.pricing.strategy import PricingStrategy


class PriceCalculator:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate(self, price: float) -> float:
        return self.strategy.calculate(price)
