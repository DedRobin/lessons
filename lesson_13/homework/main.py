from create_session import create_current_session

from add_product import add_product
from read_product import read_product
from remove_product import remove_product
from update_product import update_product
from buy_products import buy_product
from read_all_customers_purchases import read_all_customers_purchases


def main():
    current_session = create_current_session()

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
    5) <-- Come back.""")
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
                            read_product(session=current_session)

                        # UPDATE PRODUCT
                        elif selection_for_1 == 3:
                            try:
                                id_number_3 = int(input("Enter id:"))
                            except ValueError:
                                print(f"Incorrect input.")
                            else:
                                update_product(session=current_session, id_number=id_number_3)

                        # REMOVE PRODUCT
                        elif selection_for_1 == 4:
                            try:
                                id_number_4 = int(input("Enter id:"))
                            except ValueError:
                                print(f"Incorrect input.")
                            else:
                                remove_product(session=current_session, id_number=id_number_4)
                                print(f"Row by id = {id_number_4} is removed.")

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
    3) Filter purchases(Not work);
    4) Come back.""")
                    try:
                        selection_for_2 = int(input("Selection: "))
                    except ValueError:
                        print("Incorrect input.")
                    else:

                        # BUY PRODUCT
                        if selection_for_2 == 1:
                            buy_product(session=current_session)

                        # SHOW
                        elif selection_for_2 == 2:
                            read_all_customers_purchases(session=current_session)

                        # FILTER
                        elif selection_for_2 == 3:
                            pass

                        # COME BACK
                        elif selection_for_2 == 4:
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
