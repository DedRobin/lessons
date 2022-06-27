from create_tables import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session

# functions
from find_user_who_has_product_price_more_than import find_user_who_has_product_price_more_than
from find_user_who_has_definite_product import find_user_who_has_definite_product

current_session = create_current_session()


def main():
    print("\nResult №1")
    find_user_who_has_product_price_more_than(current_session, 900)
    print("\nResult №2")
    find_user_who_has_definite_product(current_session, "beyond")


if __name__ == '__main__':
    main()
