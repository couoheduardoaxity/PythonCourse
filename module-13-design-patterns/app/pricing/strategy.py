from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class RegularPricing(PricingStrategy):
    def calculate(self, price: float) -> float:
        return price


class DiscountPricing(PricingStrategy):
    def calculate(self, price: float) -> float:
        return price * 0.9


class PremiumPricing(PricingStrategy):
    def calculate(self, price: float) -> float:
        return price * 1.2
