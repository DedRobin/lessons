from __create_tables import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session

# functions
from find_user_who_has_product_price_more_than import find_user_who_has_product_price_more_than
from find_user_who_has_definite_product import find_user_who_has_definite_product
from find_all_products_which_bought_definite_user import find_all_products_which_bought_definite_user
from find_all_users_who_bought_definite_product import find_all_users_who_bought_definite_product

current_session = create_current_session()


def main():
    print("\nResult №1")
    find_user_who_has_product_price_more_than(current_session, 900)
    print("\nResult №2")
    find_user_who_has_definite_product(current_session, "place")
    print("\nResult №3")
    find_all_users_who_bought_definite_product(current_session, "place")
    print("\nResult №4")
    find_all_products_which_bought_definite_user(current_session, "Luis Howell")


if __name__ == '__main__':
    main()
