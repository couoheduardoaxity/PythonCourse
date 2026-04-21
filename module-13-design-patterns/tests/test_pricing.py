from app.pricing.context import PriceCalculator
from app.pricing.strategy import DiscountPricing, PremiumPricing


def test_discount_pricing():
    calculator = PriceCalculator(DiscountPricing())
    assert calculator.calculate(100) == 90


def test_premium_pricing():
    calculator = PriceCalculator(PremiumPricing())
    assert calculator.calculate(100) == 120
