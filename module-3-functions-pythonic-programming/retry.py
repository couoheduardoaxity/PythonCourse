import time


def retry(max_retries=3, delay=1, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):  # 👈 AQUÍ
            retries = 0
            current_delay = delay

            while retries < max_retries:
                try:
                    return func(*args, **kwargs)  # 👈 Y AQUÍ
                except Exception as e:
                    print(f"Error: {e}, reintentando...")
                    time.sleep(current_delay)
                    retries += 1
                    current_delay *= backoff

            raise Exception("Máximo de reintentos alcanzado")

        return wrapper

    return decorator
