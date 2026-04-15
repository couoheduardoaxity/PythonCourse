def batch_generator(iterable, batch_size):
    """Divide un iterable en lotes"""
    for i in range(0, len(iterable), batch_size):
        yield iterable[i : i + batch_size]
