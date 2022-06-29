from create_tables import create_current_session
from faker import Faker
from sqlalchemy.orm import Session
from models import User, Profile, Address, Product


def generate_user(session: Session) -> None:
    fake = Faker()

    user = User(email=fake.email(), password=fake.password())
    profile = Profile(user=user,
                      name=fake.name(),
                      phone=fake.phone_number(),
                      age=fake.pyint(min_value=18, max_value=80))
    address = Address(user=user, city=fake.city(), address=fake.address())
    product = Product(product_name=fake.word(),
                      price=fake.pyint(min_value=1, max_value=1000),
                      product_quantity=fake.pyint(min_value=1, max_value=100),
                      comment=f"comment {fake.word()}")
    session.add_all((user, profile, address, product))
    session.commit()


if __name__ == '__main__':
    test_session = create_current_session()
    for _ in range(50):
        generate_user(test_session)
