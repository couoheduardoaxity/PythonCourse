import pytest
from src.async_fetcher import run as async_run
from src.sync_fetcher import run as sync_run


def test_sync_fetcher():
    results, _ = sync_run()
    assert all(r == 200 for r in results)


@pytest.mark.asyncio
async def test_async_fetcher():
    results, _ = await async_run()
    assert all(r == 200 for r in results)
