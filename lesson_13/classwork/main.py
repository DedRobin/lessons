from create_tables import create_current_session
from models import User, Purchase, Product
from sqlalchemy.orm import Session

# functions
from find_user_who_has_product_price_more_than import find_user_who_has_product_price_more_than
from find_user_who_has_definite_product import find_user_who_has_definite_product

current_session = create_current_session()


def main():
    find_user_who_has_product_price_more_than(current_session, 995)
    print("-" * 100, "-" * 100, "-" * 100, sep="\n")
    find_user_who_has_definite_product(current_session, "doctor")


if __name__ == '__main__':
    main()
