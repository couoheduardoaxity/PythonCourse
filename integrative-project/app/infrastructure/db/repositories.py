from app.domain.entities.order import Order
from app.domain.repositories import OrderRepository
from app.infrastructure.db.models import OrderModel


class SqlAlchemyOrderRepository(OrderRepository):

    def __init__(self, session):
        self.session = session

    def save(self, order: Order):
        db_order = OrderModel(
            id=str(order.id),
            customer_id=order.customer_id,
            total=order.total,
            created_at=order.created_at,
        )
        self.session.add(db_order)
        self.session.commit()

    def get(self, order_id: str):
        db_order = self.session.query(OrderModel).get(order_id)
        return db_order

    def list(self):
        return self.session.query(OrderModel).all()
