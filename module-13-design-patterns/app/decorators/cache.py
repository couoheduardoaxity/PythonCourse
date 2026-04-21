from functools import wraps


def cache(func):
    storage = {}

    @wraps(func)
    def wrapper(*args):
        if args in storage:
            return storage[args]

        result = func(*args)
        storage[args] = result
        return result

    return wrapper
