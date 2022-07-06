from lesson_13.homework.create_session import create_current_session

from lesson_13.homework.product.create_product import create_product
from lesson_13.homework.product.read_product import read_product
from lesson_13.homework.product.update_product import update_product
from lesson_13.homework.product.delete_product import delete_product
from lesson_13.homework.user.create_user import create_user
from lesson_13.homework.user.delete_user import delete_user
from buy_products import buy_product
from read_all_customers_purchases import read_all_customers_purchases


def main():
    current_session = create_current_session()

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
                            create_product()

                        # READ PRODUCT
                        elif selection_for_1 == 2:
                            read_product()

                        # UPDATE PRODUCT
                        elif selection_for_1 == 3:
                            update_product()

                        # DELETE PRODUCT
                        elif selection_for_1 == 4:
                            delete_product()

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
                            create_user()

                        # READ USERS
                        elif selection_for_2 == 2:
                            pass

                        # UPDATE USER
                        elif selection_for_2 == 3:
                            try:
                                id_number_3 = int(input("Enter id:"))
                            except ValueError:
                                print(f"Incorrect input.")
                            else:
                                pass

                        # DELETE USER
                        elif selection_for_2 == 4:
                            delete_user()

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
    3) Filter purchases(Not work);
    4) <-- Come back.""")
                    try:
                        selection_for_3 = int(input("Selection: "))
                    except ValueError:
                        print("Incorrect input.")
                    else:

                        # BUY PRODUCT
                        if selection_for_3 == 1:
                            buy_product(session=current_session)

                        # SHOW
                        elif selection_for_3 == 2:
                            read_all_customers_purchases(session=current_session)

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
