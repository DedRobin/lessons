from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import Product


def update_product() -> None:
    session = create_current_session()

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


if __name__ == '__main__':
    update_product()
