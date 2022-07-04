from sqlalchemy.orm import Session
from create_session import create_current_session
from models import Purchase
from show_table import show_table


def read_all_customers_purchases(session: Session) -> None:
    current_purchases = session.query(Purchase).filter_by()
    a = current_purchases[0].__tablename__
    show_table(session, current_purchases)


if __name__ == '__main__':
    test_session = create_current_session()
    read_all_customers_purchases(test_session)
