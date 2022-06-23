from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Purchase
from utils import create_db_engine, create_db_engine_if_not_exists

from add_product import add_product
from remove_product import remove_product


def main():
    engine = create_db_engine()
    create_db_engine_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    run = True

    while run:
        print("""Menu:
    1) Products;
    2) Purchases;
    3) Exit.""")

        try:
            selection = int(input("Selection: "))
        except ValueError:
            print("Incorrect input.")
        else:
            # PRODUCTS
            if selection == 1:

                run_for_1 = True

                while run_for_1:
                    print("""Menu -> Products:
    1) Create product;
    2) Read product data;
    3) Update product;
    4) Remove product;
    5) Come back.""")
                    try:
                        selection_for_1 = int(input("Selection: "))
                    except ValueError:
                        print(f"Incorrect input.")
                    else:
                        # CREATE PRODUCT
                        if selection_for_1 == 1:
                            add_product(session=current_session)

                        # READ PRODUCT
                        elif selection_for_1 == 2:
                            pass

                        elif selection_for_1 == 3:
                            pass

                        # UPDATE PRODUCT
                        elif selection_for_1 == 4:
                            id_number = int(input("Enter id:"))
                            remove_product(session=current_session, id_number=id_number)
                            print(f"Row by id = {id_number} is removed.")

                        # COME BACK
                        elif selection_for_1 == 5:
                            run_for_1 = False

                        # INCORRECT INPUT
                        else:
                            print(f"Incorrect selection -> '{selection_for_1}'.")

            # PURCHASES
            elif selection == 2:

                run_for_2 = True

                while run_for_2:
                    print("""Menu -> Purchases:
    1) Buy product;
    2) Show all customer's purchases;
    3) Update product;
    4) Remove product;
    5) Come back.""")
                    try:
                        selection_for_2 = int(input("Selection: "))
                    except ValueError:
                        print("Incorrect input.")
                    else:
                        if selection_for_2 == 1:
                            pass

                        elif selection_for_2 == 2:
                            pass

                        elif selection_for_2 == 3:
                            pass

                        elif selection_for_2 == 4:
                            pass

                        elif selection_for_2 == 5:
                            run_for_2 = False

                        else:
                            print(f"Incorrect selection -> '{selection_for_2}'.")

            # EXIT
            elif selection == 3:
                run = False

            else:
                print(f"Incorrect selection -> '{selection}'.")

    else:
        print("Exit from program.")


if __name__ == "__main__":
    main()
