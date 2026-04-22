from app.domain.entities.order import Order


class SQLAlchemyOrderRepository:
    def __init__(self, session):
        self.session = session

    def save(self, order: Order) -> None:
        # Aquí deberías mapear a ORM real
        self.session.add(order)
        self.session.commit()

    def get_by_id(self, order_id: str):
        return self.session.get(Order, order_id)
