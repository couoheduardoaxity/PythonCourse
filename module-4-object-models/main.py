from models.order import Order
from models.schema import OrderIn, OrderOut


def run():
    data = {"product": "Laptop", "quantity": 2, "price": 15000}

    # Validación
    order_in = OrderIn(**data)

    # Crear entidad
    order = Order(
        id=1, product=order_in.product, quantity=order_in.quantity, price=order_in.price
    )

    # Lógica
    order.apply_discount(0.1)

    # Salida
    order_out = OrderOut(**order.__dict__)

    print(order_out.model_dump())


if __name__ == "__main__":
    run()
