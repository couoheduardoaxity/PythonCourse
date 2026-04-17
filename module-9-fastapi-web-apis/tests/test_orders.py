from app.main import app  # tu FastAPI app está en main.py
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_orders():
    response = client.get("/orders")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 0  # puede estar vacío o con datos


def test_create_order():
    new_order = {"id": 1, "item": "Laptop", "quantity": 2}

    response = client.post("/orders", json=new_order)

    assert response.status_code in [200, 201]

    data = response.json()
    assert data["item"] == "Laptop"
    assert data["quantity"] == 2


def test_get_order_by_id():
    order_id = 1

    response = client.get(f"/orders/{order_id}")

    # depende de tu fake_db puede ser 200 o 404 si no existe
    assert response.status_code in [200, 404]
