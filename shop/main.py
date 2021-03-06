from project.purchase_methods import *
from project.product_methods import *
from project.tools.create_session import create_current_session
from project.user_methods import *


def main():
    session = create_current_session()

    run = True

    while run:
        print("""Menu:
    1) Products;
    2) Users;
    3) Purchases;
    4) Exit.""")

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
    4) Delete product;
    5) <-- Come back.""")
                    try:
                        selection_for_1 = int(input("Selection: "))
                    except ValueError:
                        print(f"Incorrect input.")
                    else:

                        # CREATE PRODUCT
                        if selection_for_1 == 1:
                            create_product(session)

                        # READ PRODUCT
                        elif selection_for_1 == 2:
                            read_product(session)

                        # UPDATE PRODUCT
                        elif selection_for_1 == 3:
                            update_product(session)

                        # DELETE PRODUCT
                        elif selection_for_1 == 4:
                            delete_product(session)

                        # COME BACK
                        elif selection_for_1 == 5:
                            run_for_1 = False

                        # INCORRECT INPUT
                        else:
                            print(f"Incorrect selection -> '{selection_for_1}'.")


            # ------------------------------
            # USER
            elif selection == 2:

                run_for_2 = True

                while run_for_2:
                    print("""Menu -> Users:
    1) Create user;
    2) Read users;
    3) Update user;
    4) Delete user;
    5) <-- Come back.""")
                    try:
                        selection_for_2 = int(input("Selection: "))
                    except ValueError:
                        print(f"Incorrect input.")
                    else:

                        # CREATE USER
                        if selection_for_2 == 1:
                            create_user(session)

                        # READ USERS
                        elif selection_for_2 == 2:
                            read_users(session)

                        # UPDATE USER
                        elif selection_for_2 == 3:
                            update_user(session)

                        # DELETE USER
                        elif selection_for_2 == 4:
                            delete_user(session)

                        # COME BACK
                        elif selection_for_2 == 5:
                            run_for_2 = False

                        # INCORRECT INPUT
                        else:
                            print(f"Incorrect selection -> '{selection_for_2}'.")



            # PURCHASES
            elif selection == 3:

                run_for_3 = True

                while run_for_3:
                    print("""Menu -> Purchases:
    1) Buy product;
    2) Read all customer's purchases;
    3) Filter purchases;
    4) <-- Come back.""")
                    try:
                        selection_for_3 = int(input("Selection: "))
                    except ValueError:
                        print("Incorrect input.")
                    else:

                        # BUY PRODUCT
                        if selection_for_3 == 1:
                            buy_product(session=session)

                        # SHOW
                        elif selection_for_3 == 2:
                            read_all_customers_purchases(session=session)

                        # FILTER
                        elif selection_for_3 == 3:
                            search_by_purchases(session)

                        # COME BACK
                        elif selection_for_3 == 4:
                            run_for_3 = False

                        else:
                            print(f"Incorrect selection -> '{selection_for_3}'.")

            # EXIT
            elif selection == 4:
                run = False

            else:
                print(f"Incorrect selection -> '{selection}'.")

    else:
        print("Exit from program.")


if __name__ == "__main__":
    main()
