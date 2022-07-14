from re import match
from sqlalchemy.orm import Session

from .tools.models import Product


def create_product(session: Session) -> None:
    product_data = input("Enter data separated by commas by pattern:\n'product name, price, quantity, comment'\n")
    check = match(r"[\d\w ]+, ?\d+(\.\d+)?, ?\d+, ?[\d\w ]+", product_data)
    if check:
        product_data = product_data.split(",")
        product_data = [item.strip() for item in product_data]  # product_data = [str, str, str, str]

        # second(product_data[1]) and third(product_data[2]) columns convert to float and integer
        product_data[1:3] = [float(product_data[1]), int(product_data[2])]

        columns = ("product_name", "price", "product_quantity", "comment")

        data = {key: value for key, value in zip(columns, product_data)}
        current_product = Product(**data)

        session.add(current_product)
        session.commit()
    else:
        print("Incorrect data.")


def delete_product(session: Session) -> None:
    while True:
        try:
            id_number = int(input("Enter id for delete product:"))
        except ValueError:
            print(f"Incorrect input.")
        else:
            session.query(Product).filter_by(id=id_number).delete()
            session.commit()
            return


def read_product(session: Session) -> None:
    products = session.query(Product)

    for p in products:
        values = [p.id, p.product_name, p.price, p.product_quantity, p.comment]
        print(values)


def update_product(session: Session) -> None:
    run = True
    key = ""

    while run:

        print("""Menu -> Products -> Update product
What column do you want to change?
    1) Product name;
    2) Price;
    3) Product quantity;
    4) Comment;
    5) <-- Come back.""")

        try:
            selection = int(input("Selection: "))
        except ValueError:
            print("Incorrect input!")

        else:

            # EXIT
            if selection == 5:
                break

            try:
                id_number = int(input("Enter id product: "))
            except ValueError:
                print(f"Incorrect input.")
            else:

                current_product = session.query(Product).get(id_number)
                value = input("Enter new recording:")

                # NAME
                if selection == 1:
                    current_product.product_name = value

                # PRICE
                elif selection == 2:
                    try:
                        value = float(value)
                    except ValueError:
                        print("Incorect unput (enter float)!")
                    else:
                        current_product.price = value

                # QUATITY
                elif selection == 3:

                    try:
                        value = int(value)
                    except ValueError:
                        print("Incorect unput (enter int)!")
                    else:
                        current_product.product_quantity = value

                # COMMENT
                elif selection == 4:
                    current_product.comment = value

                else:
                    print("Incorrect input!")

                session.add(current_product)
                session.commit()
                print("Product is updated.")
