from infrastructure.memory_repo import InMemoryOrderRepository
from infrastructure.sql_repo import SQLOrderRepository


def get_repository(repo_type: str):
    if repo_type == "memory":
        return InMemoryOrderRepository()
    elif repo_type == "sql":
        return SQLOrderRepository()
    else:
        raise ValueError("Unknown repository type")
