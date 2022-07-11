from sqlalchemy.orm import Session

from Shop.create_session import create_current_session
from Shop.models import *


def read_all_customers_purchases(session: Session) -> None:
    # name = input("Enter name -> ")
    users = session.query(User).join(Purchase).filter(User.profile[0].name == "Kelly Wallace").all()
    for u in users:
        print(u.profile[0].name, u.purchases[0].purchase_quantity, u.purchases[0].product.product_name)
    print()


if __name__ == '__main__':
    test_session = create_current_session()
    read_all_customers_purchases(test_session)
