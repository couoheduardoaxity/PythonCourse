from crud.user_crud import create_user, get_users
from db.session import SessionLocal, engine
from models.order import Order
from models.order_item import OrderItem
from sqlalchemy import text
from sqlalchemy.orm import Session


def seed_data(db: Session):
    print("\n--- Seeding users ---")
    user1 = create_user(db, "Juan")
    # user2 = create_user(db, "Ana")

    print("\n--- Creating order with items ---")
    order = Order(user_id=user1.id)
    db.add(order)
    db.commit()
    db.refresh(order)

    items = [
        OrderItem(order_id=order.id, product="Laptop"),
        OrderItem(order_id=order.id, product="Mouse"),
    ]

    db.add_all(items)
    db.commit()

    print(f"Order {order.id} created for user {user1.name}")


def show_data(db: Session):
    print("\n--- Fetching users ---")
    users = get_users(db)
    for user in users:
        print(f"User: {user.id} - {user.name}")

    print("\n--- Query orders with items ---")
    orders = db.query(Order).all()

    for o in orders:
        print(f"\nOrder ID: {o.id} (User {o.user_id})")
        for item in o.items:
            print(f" - Item: {item.product}")


def test_core_sql():
    print("\n--- SQLAlchemy Core (raw SQL) ---")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, name FROM users"))
        for row in result:
            print(row)


def run():
    db = SessionLocal()

    try:
        seed_data(db)
        show_data(db)
        test_core_sql()
    except Exception as e:
        print("❌ Error:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    run()
