from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Order:
    id: UUID
    customer_id: str
    total: float
    created_at: datetime
