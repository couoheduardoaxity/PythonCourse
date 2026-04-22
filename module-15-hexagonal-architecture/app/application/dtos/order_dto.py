from pydantic import BaseModel


class CreateOrderDTO(BaseModel):
    product: str
    quantity: int
