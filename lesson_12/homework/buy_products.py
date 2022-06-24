from re import match
from models import Product, Purchase, User
from sqlalchemy.orm import Session
from create_current_session import create_current_session


def __enter_or_create_user(session: Session) -> User:
    run_1 = True
    while run_1:
        input_user = input("Enter first and last names by pattern 'first_name last_name':").lower()
        check = match(r"\w+ \w+", input_user)
        if not check:
            print("Incorrect name!")
            continue
        else:
            run_2 = True
            while run_2:
                current_user = session.query(User).filter_by(user_name=input_user).first()
                if not current_user:
                    add_user = User(user_name=input_user)
                    session.add(add_user)
                    session.commit()
                    continue
                else:
                    return current_user


def __choice_product() -> int:
    run = True
    while run:
        try:
            input_product_id = int(input("Enter product id: "))
        except ValueError:
            print("Incorrect input!")
        else:
            return input_product_id


def __choice_purchase_quantity(session: Session, product_id: int, ost_quantity: int) -> int:
    run = True
    while run:
        try:
            input_purchase_quantity = int(input(f"Enter purchase quantity(ost {ost_quantity}): "))
        except ValueError:
            print("Incorrect input!")
        else:
            if ost_quantity < input_purchase_quantity:
                print(f"Incorrent input! Enter less than or equel {ost_quantity}.")
                continue
            return input_purchase_quantity


def buy_product(session: Session) -> None:
    current_user = __enter_or_create_user(session)
    current_user_id = current_user.id

    current_product_id = __choice_product()

    # Find ost quantity of current product
    ost_quantity_current_product = session.query(Product).filter_by(id=current_product_id).first()  # obj Product
    ost_quantity_current_product = ost_quantity_current_product.product_quantity  # pull it quantity

    current_purchase_quantity = __choice_purchase_quantity(session, current_product_id, ost_quantity_current_product)

    current_purchase = Purchase(purchase_quantity=current_purchase_quantity,
                                user_id=current_user_id,
                                product_id=current_product_id)

    current_product = session.query(Product).filter_by(id=current_product_id).first()
    current_product.product_quantity -= current_purchase_quantity

    session.add(current_purchase)
    session.commit()


if __name__ == '__main__':
    current_session = create_current_session()
    buy_product(current_session)
    # purchase = current_session.query(Purchase).filter_by(id=1).first()
    # print(purchase.user.user_name)
