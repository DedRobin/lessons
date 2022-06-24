from sqlalchemy.orm import Session
from models import Purchase
from show_table import show_table


def read_all_customers_purchases(session: Session) -> None:
    current_purchases = session.query(Purchase).filter_by().all()
    show_table(session, current_purchases)
