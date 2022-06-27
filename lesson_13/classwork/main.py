from create_tables import create_current_session
from models import User, Purchase, Product

def main():
    current_session = create_current_session()

    users = current_session.query(User).join(Purchase).join(Product).filter(
        Product.price >= 100)
    ).all()