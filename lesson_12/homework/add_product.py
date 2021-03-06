from re import match
from create_current_session import create_current_session
from sqlalchemy.orm import Session
from models import Product


def add_product(session: Session) -> None:
    row = input("Enter data separated by commas by pattern:\n'product name, price, quantity, comment'\n")
    check = match(r"[\d\w ]+, ?\d+(\.\d+)?, ?\d+, ?[\d\w ]+", row)
    if check:
        row = row.split(",")
        row = [item.strip() for item in row]  # row = [str, str, str, str]

        # second(row[1]) and third(row[2]) columns convert to float and integer
        row[1:3] = [float(row[1]), int(row[2])]

        columns = ("product_name", "price", "product_quantity", "comment")

        data = {key: value for key, value in zip(columns, row)}
        current_product = Product(**data)

        session.add(current_product)
        session.commit()
    else:
        print("Incorrect data.")


if __name__ == '__main__':
    test_session = create_current_session()
    add_product(test_session)
