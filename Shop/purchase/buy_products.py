from sqlalchemy.orm import Session

from Shop.create_session_pack import create_current_session
from Shop.models import Product, Purchase, User


def _login(session: Session) -> User:
    while True:
        email = input("Enter email -> ")
        password = input("Enter password -> ")
        query = session.query(User).filter_by(email=email, password=password).first()
        if query:
            name = query.profile[0].name
            print(f"Welcome, {name}.")
            return query
        else:
            print(f"User {email} not find.")


def _choose_product(session: Session) -> Product:
    while True:
        product = input("Enter product name -> ")
        query = session.query(Product).filter_by(product_name=product).first()
        if query:
            product = query.product_name
            print(f"Your selection -> {product}")
            return query
        else:
            print(f"Product {product} not find.")


def buy_product(session: Session) -> None:
    # Log into account
    user = _login(session=session)

    # Product selection
    product = _choose_product(session=session)

    while True:
        try:
            purchase_quantity = int(input("How much do you want to buy?\nAnswer-> "))
        except ValueError:
            print("Incorrect input! Enter integer.")
        else:
            # Calculate difference
            current_quantity = product.product_quantity
            ost = current_quantity - purchase_quantity
            product.product_quantity = ost

            # Create purchase
            purchase = Purchase(user=user, product=product, purchase_quantity=purchase_quantity)

            # COMMIT
            session.add(purchase)
            session.commit()

            print(f"{user.profile[0].name} bought {purchase.purchase_quantity} {product.product_name}.")
            return None


if __name__ == '__main__':
    test_session = create_current_session()
    buy_product(test_session)
