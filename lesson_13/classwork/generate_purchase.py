from create_tables import create_current_session
from faker import Faker
from sqlalchemy.orm import Session
from models import User, Profile, Address, Purchase, Product
from random import choice

def generate_purchase(session: Session) -> None:
    fake = Faker()

    users_id = [id_user for id_user in session.query(User).filter_by()]
    products_id = [id_product.id for id_product in session.query(Product).filter_by()]
    purchase = Purchase(user=user,
                        product=product,
                        purchase_quantity=fake.pyint(min_value=1, max_value=product.product_quantity)
                        )

    # session.add_all()
    # session.commit()


if __name__ == '__main__':
    test_session = create_current_session()
    generate_purchase(test_session)
    # search = test_session.query(User).all()
    pass
    # for item in search:
    #     print(item.id)