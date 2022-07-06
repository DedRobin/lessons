from re import match

from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import Product


def create_user() -> None:
    session = create_current_session()
    row = input("Enter data separated by commas by pattern:\n', price, quantity, comment'\n")
    check = match(r"\w+ \w+", row)
    if check:
        columns = ("product_name", "price", "product_quantity", "comment")

        data = {key: value for key, value in zip(columns, row)}
        current_product = Product(**data)

        session.add(current_product)
        session.commit()
    else:
        print("Incorrect data.")


if __name__ == '__main__':
    create_product()
