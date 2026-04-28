from app.application.use_cases.create_order import CreateOrder
from app.application.use_cases.list_orders import ListOrders
from app.infrastructure.api.schemas import OrderCreate
from app.infrastructure.db.repositories import SqlAlchemyOrderRepository
from app.infrastructure.db.session import SessionLocal
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/orders")
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    repo = SqlAlchemyOrderRepository(db)
    use_case = CreateOrder(repo)
    return use_case.execute(data.customer_id, data.total)


@router.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    repo = SqlAlchemyOrderRepository(db)
    use_case = ListOrders(repo)
    return use_case.execute()
