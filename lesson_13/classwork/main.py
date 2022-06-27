from create_tables import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session

current_session = create_current_session()


def main1(session: Session) -> None:
    users = session.query(User).join(Purchase).join(Product).filter(Product.price >= 995).all()
    for user in users:
        user_id = user.id
        email = user.email
        password = user.password
        print(user_id, email, password)


def main2(session: Session) -> None:
    users = session.query(User).join(Purchase).join(Product).filter(Product.product_name == "product 49").all()
    for user in users:
        print(user.id, user.email)


if __name__ == '__main__':
    # main1(current_session)
    main2(current_session)
