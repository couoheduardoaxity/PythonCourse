from app.decorators.cache import cache


def test_cache_decorator():
    calls = {"count": 0}

    def slow_function(x):
        calls["count"] += 1
        return x * 2

    cached_function = cache(slow_function)

    assert cached_function(2) == 4
    assert cached_function(2) == 4

    # Solo debe ejecutarse una vez
    assert calls["count"] == 1
