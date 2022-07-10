from sqlalchemy.orm import Session

from Shop.create_session import create_current_session
from Shop.models import Product


def delete_product(session: Session) -> None:
    while True:
        try:
            id_number = int(input("Enter id for delete product:"))
        except ValueError:
            print(f"Incorrect input.")
        else:
            session.query(Product).filter_by(id=id_number).delete()
            session.commit()
            return


if __name__ == '__main__':
    test_session = create_current_session()
    delete_product(test_session)
