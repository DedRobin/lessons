from sqlalchemy.orm import Session
from sqlalchemy.orm import Query

from .tools.models import *
from .tools.create_session import create_current_session


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


def _filter_by_column(purchase: Purchase) -> dict:
    all_columns = {"ID": lambda x: x.id,
                   "User name": lambda x: x.user.profile[0].name,
                   "User email": lambda x: x.user.email,
                   "User phone": lambda x: x.user.profile[0].phone,
                   "User age": lambda x: x.user.profile[0].age,
                   "User city": lambda x: x.user.addresses[0].city,
                   "User address": lambda x: x.user.addresses[0].address.replace("\n", " "),
                   "Product name": lambda x: x.product.product_name,
                   "Product price": lambda x: x.product.price,
                   "Product quantity": lambda x: x.product.product_quantity,
                   "Product comment": lambda x: x.product.price,
                   "Purchase quantity": lambda x: x.purchase_quantity}

    current_filter = {"ID": lambda x: x.id}

    while True:
        print("---|  Columns  |---\n")
        print(*current_filter, sep=" | ", end="\n\n")

        try:
            selection = int(input("""Select columns to display:
\t1) User name;
\t2) User email;
\t3) User phone;
\t4) User age;
\t5) User city;
\t6) User address;
\t7) Product name;
\t8) Product price;
\t9) Product quantity;;
\t10) Product comment;
\t11) Purchase quantity;
\t12) Insert all columns;
\t13) Clear filter;
\t14) Apply filter.

\tSelection -> """))
            print()

        except ValueError:
            print("Incorrect input! Enter integer from 1 to 14")
        else:

            # USER NAME
            if selection == 1:
                current_filter["User name"] = lambda x: x.user.profile[0].name

            # USER EMAIL
            elif selection == 2:
                current_filter["User email"] = lambda x: x.user.email

            # USER PHONE
            elif selection == 3:
                current_filter["User phone"] = lambda x: x.user.profile[0].phone

            # USER AGE
            elif selection == 4:
                current_filter["User age"] = lambda x: x.user.profile[0].age

            # USER CITY
            elif selection == 5:
                current_filter["User city"] = lambda x: x.user.addresses[0].city

            # USER ADDRESS
            elif selection == 6:
                current_filter["User address"] = lambda x: x.user.addresses[0].address.replace("\n", " ")

            # PRODUCT NAME
            elif selection == 7:
                current_filter["Product name"] = lambda x: x.product.product_name

            # PRODUCT PRICE
            elif selection == 8:
                current_filter["Product price"] = lambda x: x.product.price

            # PRODUCT COMMENT
            elif selection == 9:
                current_filter["Product comment"] = lambda x: x.product.price

            # PRODUCT QUANTITY
            elif selection == 10:
                current_filter["Product comment"] = lambda x: x.product.product_quantity

            # PURCHASE QUANTITY
            elif selection == 11:
                current_filter["Purchase quantity"] = lambda x: x.purchase_quantity

            # ADD ALL
            elif selection == 12:
                current_filter = all_columns

            # CLEAR FILTER
            elif selection == 13:
                current_filter = {"ID": lambda x: x.id}

            # APPLY FILTER
            elif selection == 14:
                return current_filter

            else:
                print("Incorrect input! Enter integer from 1 to 14.")


def print_result_to_console(purchases: Query, dictionary: dict) -> None:
    column_names = list(dictionary.keys())
    data = []
    for purchase in purchases:
        row = [upload(purchase) for upload in dictionary.values()]
        data.append(row)
    list_of_column = "\n".join("\t" + str(i) + ") " + str(x) for i, x in enumerate(column_names, 1))
    while True:
        try:
            index = int(input(f"Sorted by:\n{list_of_column}\n\n\tSelect -> "))
        except ValueError:
            print(f"Incorrect input! Enter integer 1 or {len(column_names)}.")
        else:
            if index not in range(1, len(column_names) + 1):
                print(f"Incorrect input! Enter integer 1 or {len(column_names)}.")
                continue
            else:
                try:
                    sort_kind = int(input("""Choose kind of sorting:
\t1) Ascending;
\t2) Descending.

\tSelection -> """))
                except ValueError:
                    print("Incorrect input! Enter integer 1 or 2.")
                else:
                    reverse = False
                    if sort_kind == 1:
                        reverse = True
                    elif sort_kind == 2:
                        pass
                    else:
                        print("Incorrect input! Enter integer 1 or 2.")
                        continue

                    data = sorted(data, key=lambda x: x[index - 1], reverse=reverse)
                    print()

                    max_lengths = []
                    for index in range(len(column_names)):
                        column = [str(x[index]) for x in data]

                        max_length_of_data = max(len(x) for x in column)
                        length_of_column_name = len(column_names[index])
                        max_length_of_column = max(max_length_of_data, length_of_column_name) + 2
                        max_lengths.append(max_length_of_column)

                    template_for_data = []  #
                    for length in max_lengths:
                        template_for_data.append("{:^" + f"{length}" + "}")
                    template_for_data = "|" + "|".join(template_for_data) + "|"

                    template_for_line = []
                    for length in max_lengths:
                        template_for_line.append("-" * length)
                    template_for_line = "|" + "|".join(template_for_line) + "|"

                    """RENDERING TABLE"""

                    # SPLITTING LINE
                    print(template_for_line)

                    # HEADER
                    print(template_for_data.format(*column_names))

                    # SPLITTING LINE
                    print(template_for_line)

                    # DATA
                    for row in data:
                        print(template_for_data.format(*row))

                    # SPLITTING LINE
                    print(template_for_line)


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


def read_all_customers_purchases(session: Session) -> None:
    name = input("Enter name -> ")
    users = session.query(User).join(Profile).join(Purchase).filter(Profile.name == name).all()
    if users:
        for u in users:
            print(u.purchases[0].id,
                  u.id,
                  u.profile[0].name,
                  u.purchases[0].product.product_name,
                  u.purchases[0].purchase_quantity, sep=", ")
    else:
        print(f"{name} is not find.")


def search_by_purchases(session: Session):
    purchases = session.query(Purchase).join(User).join(Product).join(Profile)
    filter_dict = _filter_by_column(purchases.first())
    list_of_conditions = _create_filter_list()
    purchases = purchases.filter(*list_of_conditions)
    print_result_to_console(purchases, filter_dict)

