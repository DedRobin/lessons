from sqlalchemy.orm import Session
from models import Product


def update_product(session: Session, id_number: int) -> None:
    run = True
    key = ""
    while run:

        print("""What column do you want to change?
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
            current_product = session.query(Product).get(id_number)
            value = input("Enter new recording:")

            if selection == 1:
                current_product.product_name = value

            elif selection == 2:
                value = float(value)
                current_product.price = value

            elif selection == 3:
                value = int(value)
                current_product.product_quantity = value

            elif selection == 4:
                current_product.comment = value

            elif selection == 5:
                break

            else:
                print("Incorrect input!")

            session.add(current_product)
            session.commit()
            print("Product is updated.")
