from create_tables import create_current_session
from faker import Faker
from sqlalchemy.orm import Session
from models import User, Purchase, Product
from random import choice


def generate_purchase(session: Session) -> None:
    fake = Faker()

    user = choice(session.query(User).filter_by().all())  # random user
    product = choice(session.query(Product).filter_by().all())  # random product
    purchase = Purchase(user=user,
                        product=product,
                        purchase_quantity=fake.pyint(min_value=1, max_value=product.product_quantity)
                        )

    session.add(purchase)
    session.commit()


if __name__ == '__main__':
    test_session = create_current_session()
    for _ in range(50):
        generate_purchase(test_session)
