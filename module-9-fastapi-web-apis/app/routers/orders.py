from app.core.deps import get_current_user
from app.schemas.order import OrderCreate
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/orders")

fake_db = []


@router.post("/")
def create_order(order: OrderCreate, user: str = Depends(get_current_user)):
    new_order = {
        "id": len(fake_db) + 1,
        "product": order.product,
        "quantity": order.quantity,
        "user": user,
    }
    fake_db.append(new_order)
    return new_order


@router.get("/")
def get_orders(user: str = Depends(get_current_user)):
    return fake_db
