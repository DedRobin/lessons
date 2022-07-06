from ..models import Product
from lesson_13.homework.create_session import create_current_session
from ..show_table import show_table


def read_product() -> None:
    session = create_current_session
    current_products = session.query(Product).filter_by().all()
    show_table(session, current_products)


if __name__ == '__main__':
    read_product()
