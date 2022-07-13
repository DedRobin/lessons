from shop.models import *


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
