from app.application.dtos.order_dto import CreateOrderDTO
from app.application.use_cases.create_order import CreateOrder
from app.dependencies import get_notifier, get_repository
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


@app.post("/orders")
def create_order(
    dto: CreateOrderDTO, repo=Depends(get_repository), notifier=Depends(get_notifier)
):
    use_case = CreateOrder(repo, notifier)

    try:
        order = use_case.execute(dto)
        return {"id": order.id, "product": order.product, "quantity": order.quantity}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
