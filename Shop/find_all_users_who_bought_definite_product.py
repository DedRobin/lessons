from lesson_13.homework.create_session import create_current_session
from models import User, Purchase, Product, Profile
from sqlalchemy.orm import Session


def find_all_users_who_bought_definite_product(session: Session, product_name: str) -> None:
    profiles = session.query(Profile).join(User).join(Purchase).join(Product).filter(
        Product.product_name == product_name)
    for profile in profiles:
        print(profile.name)


if __name__ == '__main__':
    test_session = create_current_session()
    find_all_users_who_bought_definite_product(test_session, "play")
