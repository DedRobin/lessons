from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.product.create_product import create_product
from lesson_13.homework.product.read_product import read_product
from lesson_13.homework.product.update_product import update_product
from lesson_13.homework.product.delete_product import delete_product
from lesson_13.homework.user.create_user import create_user
from lesson_13.homework.user.read_users import read_users
from lesson_13.homework.user.update_user import update_user
from lesson_13.homework.user.delete_user import delete_user


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
    2) Show all customer's purchases;
    3) Filter purchases;
    4) <-- Come back.""")
                    try:
                        selection_for_3 = int(input("Selection: "))
                    except ValueError:
                        print("Incorrect input.")
                    else:

                        # BUY PRODUCT
                        if selection_for_3 == 1:
                            pass

                        # SHOW
                        elif selection_for_3 == 2:
                            pass

                        # FILTER
                        elif selection_for_3 == 3:
                            pass

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
