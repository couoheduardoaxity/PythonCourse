from app.application.use_cases.create_order import CreateOrder


class FakeRepo:
    def __init__(self):
        self.saved = []

    def save(self, order):
        self.saved.append(order)


def test_create_order():
    repo = FakeRepo()
    use_case = CreateOrder(repo)

    order = use_case.execute("123", 100)

    assert order.customer_id == "123"
    assert len(repo.saved) == 1
