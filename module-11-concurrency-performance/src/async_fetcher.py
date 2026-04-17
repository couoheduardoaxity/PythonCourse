import asyncio
import time

import httpx

from .config import SEM_LIMIT, URLS


async def fetch(client, url, sem):
    async with sem:
        response = await client.get(url)
        return response.status_code


async def run():
    start = time.time()

    sem = asyncio.Semaphore(SEM_LIMIT)

    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url, sem) for url in URLS]
        results = await asyncio.gather(*tasks)

    duration = time.time() - start
    return results, duration


if __name__ == "__main__":
    results, duration = asyncio.run(run())
    print("Async:", duration)
