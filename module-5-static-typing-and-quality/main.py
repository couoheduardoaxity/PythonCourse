from models.order import create_order, update_status


def main() -> None:
    order = create_order(1, 100.0)
    order = update_status(order, "paid")

    print(order)


if __name__ == "__main__":
    main()
