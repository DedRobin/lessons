from lesson_13.homework.create_session import create_current_session
from models import User, Purchase, Product, Profile
from sqlalchemy.orm import Session


def find_all_products_which_bought_definite_user(session: Session, name: str) -> None:
    # products = session.query(Product).join(Purchase).join(User).join(Profile).filter(Profile.name == name).all()
    products = session.query(Product.product_name).join(Purchase).join(User).join(Profile).filter(Profile.name == name)
    for product in products:
        print(product.product_name)


if __name__ == '__main__':
    test_session = create_current_session()
    # find_all_products_which_bought_definite_user(test_session)
    find_all_products_which_bought_definite_user(test_session, "Amber Madden")
