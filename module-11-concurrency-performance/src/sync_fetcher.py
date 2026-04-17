import time

import httpx

from .config import URLS


def fetch(url):
    response = httpx.get(url)
    return response.status_code


def run():
    start = time.time()

    results = [fetch(url) for url in URLS]

    duration = time.time() - start
    return results, duration


if __name__ == "__main__":
    results, duration = run()
    print("Sync:", duration)
