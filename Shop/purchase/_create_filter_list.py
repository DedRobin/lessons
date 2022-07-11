from Shop.models import *


def _operator_choice(selection: int) -> str:
    if selection not in (4, 10, 11):  # (4, 10, 11) == (age, product quantity, purchase quantity)
        condition = int(input("""Operators:
            1) Equal               |   ==
            2) Not equal           |   !=

        Select condition operator -> """))
        # EQUAL - "=="
        if condition == 1:
            return "=="

        # NOT EQUAL
        elif condition == 2:
            return "!="
    else:
        condition = int(input("""Operators:
            1) Equal               |   ==
            2) Not equal           |   !=
            3) More than           |   >
            4) Less than           |   <
            5) More than or equal  |   >=
            6) Less than or equal  |   <=


        Select condition operator -> """))
        # EQUAL - "=="
        if condition == 1:
            return "=="

        # NOT EQUAL
        elif condition == 2:
            return "!="

        # MORE THAN - ">"
        elif condition == 3:
            return ">"

        # LESS THAN - "<"
        elif condition == 4:
            return "<"

        # MORE THAN OR EQUAL - ">="
        elif condition == 5:
            return ">="

        # LESS THAN OR EQUAL - "<="
        elif condition == 6:
            return "<="


def _create_filter_list() -> list:
    expressions = []
    expression = []

    left = True

    while True:
        print("Filters:", *expressions, sep=", ")
        print("Current filter:", expression)

        direction = "left" if left else "right"

        selection = 0
        if len(expression) == 1:
            operator = _operator_choice(selection=selection)
            expression.append(operator)
            continue
        elif len(expression) == 2:
            data = input("Enter data: ")
            data = f"'{data}'"
            expression.append(data)
            expression = " ".join(expression)
            expression = eval(expression)
            expressions.append(expression)
            expression = []
            continue
        try:
            selection = int(input(f"""Select option to the {direction} of operator:
    1) User name;
    2) User email;
    3) User phone;
    4) User age;
    5) User city;
    6) User address;
    7) Product name;
    8) Product price;
    9) Product comment;
    10) Product quantity;
    11) Purchase quantity;
    12) Apply filters.
    """))
        except ValueError:
            print("Incorrect input! Enter integer from 1 to 12.")
        else:

            if selection == 1:
                expression.append("Profile.name")  # USER NAME
            elif selection == 2:
                expression.append("User.email")  # USER EMAIL
            elif selection == 3:
                expression.append("Profile.phone")  # USER PHONE
            elif selection == 4:
                expression.append("Profile.age")  # USER AGE
            elif selection == 5:
                expression.append("Address.city")  # USER CITY
            elif selection == 6:
                expression.append("Address.address")  # USER ADDRESS
            elif selection == 7:
                expression.append("Product.product_name")  # PRODUCT NAME
            elif selection == 8:
                expression.append("Product.price")  # PRODUCT PRICE
            elif selection == 9:
                expression.append("Product.comment")  # PRODUCT COMMENT
            elif selection == 10:
                expression.append("Product.product_quantity")  # PRODUCT QUANTITY
            elif selection == 11:
                expression.append("Purchase.purchase_quantity")  # PURCHASE QUANTITY
            elif selection == 12:
                return expressions  # APPLY FILTERS
            else:
                print("Incorrect input! Enter integer from 1 to 12.")

            left = False
