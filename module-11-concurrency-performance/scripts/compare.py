import asyncio

from src.async_fetcher import run as async_run
from src.cpu_bound import run as cpu_run
from src.sync_fetcher import run as sync_run


def main():
    _, sync_time = sync_run()
    print(f"Sync: {sync_time:.2f}s")

    _, async_time = asyncio.run(async_run())
    print(f"Async: {async_time:.2f}s")

    _, cpu_time = cpu_run()
    print(f"CPU (multiprocessing): {cpu_time:.2f}s")


if __name__ == "__main__":
    main()
