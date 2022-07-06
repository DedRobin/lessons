from lesson_13.homework.create_session import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session


def find_user_who_has_product_price_more_than(session: Session, price: int) -> None:
    users = session.query(User, Purchase.purchase_quantity).join(Purchase).join(Product).filter(Product.price > price)
    for user in users:
        user_id = user.id
        email = user.email
        print(user_id, email)


if __name__ == '__main__':
    test_session = create_current_session()
    find_user_who_has_product_price_more_than(test_session, 900)
