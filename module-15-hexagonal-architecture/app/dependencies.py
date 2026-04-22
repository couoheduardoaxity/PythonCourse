from app.infrastructure.external.http_notifier import HttpNotifier
from app.infrastructure.repositories.memory_order_repository import (
    MemoryOrderRepository,
)


def get_repository():
    return MemoryOrderRepository()


def get_notifier():
    return HttpNotifier()
