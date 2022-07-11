from re import match
from sqlalchemy.orm import Session

from Shop.create_session import create_current_session
from Shop.models import Product, Purchase, User, Profile


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
            pass
        else:
            print(f"Product {product} not find.")

def buy_product(session: Session) -> None:
    # Log into account
    user = _login(session=session)

    product = _choose_product(session=session)

    pass


# current_user = __enter_or_create_user(session)
# current_user_id = current_user.id
#
# current_product_id = __choice_product()
#
# # Find ost quantity of current product
# ost_quantity_current_product = session.query(Product).filter_by(id=current_product_id).first()  # obj Product
# ost_quantity_current_product = ost_quantity_current_product.product_quantity  # pull it quantity
#
# current_purchase_quantity = __choice_purchase_quantity(session, current_product_id, ost_quantity_current_product)
#
# current_purchase = Purchase(purchase_quantity=current_purchase_quantity,
#                             user_id=current_user_id,
#                             product_id=current_product_id)
#
# current_product = session.query(Product).filter_by(id=current_product_id).first()
# current_product.product_quantity -= current_purchase_quantity
#
# session.add(current_purchase)
# session.commit()


if __name__ == '__main__':
    test_session = create_current_session()
    # buy_product(test_session)
    _login(test_session)
