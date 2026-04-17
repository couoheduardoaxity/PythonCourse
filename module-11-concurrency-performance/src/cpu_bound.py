import time
from concurrent.futures import ProcessPoolExecutor


def heavy_task(n):
    total = 0
    for i in range(10_000_000):
        total += i % n
    return total


def run():
    start = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_task, [1, 2, 3, 4]))

    duration = time.time() - start
    return results, duration


if __name__ == "__main__":
    results, duration = run()
    print("CPU:", duration)
