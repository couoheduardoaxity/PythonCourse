import hypothesis.strategies as st
from app.orders import apply_discount
from hypothesis import given


@given(st.floats(min_value=0, max_value=1000), st.floats(min_value=0, max_value=100))
def test_discount_never_increases(total, discount):
    result = apply_discount(total, discount)
    assert result <= total
