from re import match
from sqlalchemy.orm import Session

from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import Product


def create_product(session: Session) -> None:
    product_data = input("Enter data separated by commas by pattern:\n'product name, price, quantity, comment'\n")
    check = match(r"[\d\w ]+, ?\d+(\.\d+)?, ?\d+, ?[\d\w ]+", product_data)
    if check:
        product_data = product_data.split(",")
        product_data = [item.strip() for item in product_data]  # product_data = [str, str, str, str]

        # second(product_data[1]) and third(product_data[2]) columns convert to float and integer
        product_data[1:3] = [float(product_data[1]), int(product_data[2])]

        columns = ("product_name", "price", "product_quantity", "comment")

        data = {key: value for key, value in zip(columns, product_data)}
        current_product = Product(**data)

        session.add(current_product)
        session.commit()
    else:
        print("Incorrect data.")


if __name__ == '__main__':
    test_session = create_current_session()
    create_product(test_session)
