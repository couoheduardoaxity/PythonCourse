from pydantic import BaseModel


class OrderCreate(BaseModel):
    product: str
    quantity: int
