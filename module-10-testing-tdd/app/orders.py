class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)


def apply_discount(total, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Invalid discount")
    return total * (1 - percentage / 100)


def fetch_order_from_api(api_client, order_id):
    return api_client.get_order(order_id)
