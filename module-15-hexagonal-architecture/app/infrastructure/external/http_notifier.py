from app.domain.entities.order import Order


class HttpNotifier:
    def notify(self, order: Order) -> None:
        print(f"[HTTP] Notification sent for order {order.id}")
