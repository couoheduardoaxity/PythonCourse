from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_order():
    response = client.post("/orders", json={"customer_id": "123", "total": 200})

    assert response.status_code == 200
