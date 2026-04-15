import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"Tiempo: {end - self.start:.4f} segundos")
