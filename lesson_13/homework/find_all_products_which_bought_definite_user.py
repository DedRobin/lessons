from create_tables import create_current_session
from models import User, Purchase, Product, Profile
from sqlalchemy.orm import Session
from sqlalchemy.sql import or_, and_


def find_all_products_which_bought_definite_user(session: Session, name: str) -> None:
    products = session.query(Product).join(Purchase).join(User).join(Profile).filter(Profile.name == name).all()
    for product in products:
        print(product.product_name)


if __name__ == '__main__':
    test_session = create_current_session()
    # find_all_products_which_bought_definite_user(test_session)
    find_all_products_which_bought_definite_user(test_session, "Lori Harris")
