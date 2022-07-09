from sqlalchemy.orm import Session

from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import *
from lesson_13.homework.rendering import rendering

def _choice_condition() -> str:
    condition = int(input("""Operators:
    1) Equel               |   ==
    2) More than           |   >
    3) Less than           |   <
    4) More than or equel  |   >=
    5) Less than or eqel   |   <=
    6) Not equel           |   !=

Choice condition operator -> """))

    # EQUAL - "=="
    if condition == 1:
        return "=="

    # MORE THAN - ">"
    elif condition == 2:
        return ">"
    # LESS THAN - "<"
    elif condition == 3:
        return "<"

    # MORE THAN OR EQUAL - ">="
    elif condition == 4:
        return ">="

    # LESS THAN OR EQUAL - "<="
    elif condition == 5:
        return "<="


def _filter_by_column(purchase: Purchase) -> dict:
    all_columns = {"User name": lambda x: x.user.profile[0].name,
                   "User email": lambda x: x.email,
                   "User phone": lambda x: x.profile[0].phone,
                   "User age": lambda x: x.profile[0].age,
                   "User city": lambda x: x.addresses[0].city,
                   "User address": lambda x: x.addresses[0].address.replace("\n", " "),
                   "Product name": lambda x: x.product_name,
                   "Product price": lambda x: x.price,
                   "Product comment": lambda x: x.price,
                   "Purchase quantity": lambda x: x.purchase_quantity}

    filter_columns = {}
    current_filter = filter_columns

    while True:
        print("Current filter:")
        print(*current_filter, sep=" | ", end="\n\n")

        try:
            selection = int(input("""What column do you watch?
    1) User name;
    2) User email;
    3) User phone;
    4) User age;
    5) User city;
    6) User address;
    7) Product name;
    8) Product price;
    9) Product comment;
    10) Purchase quantity;
    11) All;
    12) Clear filter;
    13) Apply filter.
    
    Selection -> """))

        except ValueError:
            print("Incorrect input! Enter integer from 1 to 12")
        else:

            # USER NAME
            if selection == 1:
                filter_columns["User name"] = lambda x: x.profile[0].name

            # USER EMAIL
            elif selection == 2:
                filter_columns["User email"] = lambda x: x.user.email

            # USER PHONE
            elif selection == 3:
                filter_columns["User phone"] = lambda x: x.user.profile[0].phone

            # USER AGE
            elif selection == 4:
                filter_columns["User age"] = lambda x: x.user.profile[0].age

            # USER CITY
            elif selection == 5:
                filter_columns["User city"] = lambda x: x.user.addresses[0].city

            # USER ADDRESS
            elif selection == 6:
                filter_columns["User address"] = lambda x: x.user.addresses[0].address.replace("\n", " ")

            # PRODUCT NAME
            elif selection == 7:
                filter_columns["Product name"] = lambda x: x.product.product_name

            # PRODUCT PRICE
            elif selection == 8:
                filter_columns["Product price"] = lambda x: x.product.price

            # PRODUCT COMMENT
            elif selection == 9:
                filter_columns["Product comment"] = lambda x: x.product.price

            # PURCHASE QUANTITY
            elif selection == 10:
                filter_columns["Purchase quantity"] = lambda x: x.purchase_quantity

            # ADD ALL
            elif selection == 11:
                return all_columns

            # CLEAR FILTER
            elif selection == 12:
                filter_columns = {}

            # APPLY FILTER
            elif selection == 13:
                return filter_columns

            else:
                print("Incorrect input! Enter integer from 1 to 12.")


def search_by_purchases(session: Session):
    list_of_conditions = []
    purchases = test_session.query(Purchase).join(User).join(Product)
    filter_dict = _filter_by_column(purchases.first())
    rendering(purchases, filter_dict)



if __name__ == '__main__':
    test_session = create_current_session()
    search_by_purchases(session=test_session)
    # purchase = test_session.query(Purchase).join(User).join(Product).first()
    # print(purchase.user.profile[0].name)
