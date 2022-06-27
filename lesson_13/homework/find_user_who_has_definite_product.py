from create_tables import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session


def find_user_who_has_definite_product(session: Session, product_name: str) -> None:
    users = session.query(User).join(Purchase).join(Product).filter(Product.product_name == product_name).all()
    for user in users:
        print(user.id, user.email)


if __name__ == '__main__':
    test_session = create_current_session()
    find_user_who_has_definite_product(test_session, "doctor")
