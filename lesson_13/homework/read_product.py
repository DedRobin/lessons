from sqlalchemy.orm import Session
from models import Product
from create_session import create_current_session
from show_table import show_table


def read_product(session: Session) -> None:
    current_products = session.query(Product).filter_by().all()
    show_table(session, current_products)
