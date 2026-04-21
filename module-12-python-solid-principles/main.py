from application.services import OrderService
from infrastructure.factory import get_repository


def main():
    repo = get_repository("memory")  # cambia a "sql" si quieres
    service = OrderService(repo)

    service.create_order(1, 200)
    service.create_order(2, 350)

    orders = service.list_orders()

    for order in orders:
        print(f"Order {order.id}: ${order.total}")


if __name__ == "__main__":
    main()
