from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_order_e2e():
    response = client.post("/orders", json={"product": "tablet", "quantity": 1})

    assert response.status_code == 200

    data = response.json()
    assert data["product"] == "tablet"
