from sqlalchemy import inspect
from sqlalchemy.orm import Session

from Shop.models import *
from Shop.create_session import create_current_session


def read_product(session: Session) -> None:
    session = create_current_session()
    products = session.query(Product)

    for p in products:
        values = [p.id, p.product_name, p.price, p.product_quantity, p.comment]
        print(values)


if __name__ == '__main__':
    test_session = create_current_session()
    read_product(test_session)
