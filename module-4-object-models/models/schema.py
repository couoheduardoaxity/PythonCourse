from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    product: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)


class OrderOut(BaseModel):
    id: int
    product: str
    quantity: int
    price: float
    total: float
