from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import User, Profile, Address


def update_user() -> None:
    session = create_current_session()
    run = True
    while run:
        print("""Menu -> Users -> Update user:
    What column do you want to change?
        1) Age;
        2) Email;
        3) Name;
        4) Password;
        5) Phone;
        6) <-- Come back.""")

        try:
            selection = int(input("Selection -> "))
        except ValueError:
            print("Incorrect input!")
        else:

            try:
                user_id = int(input("Enter user ID -> "))
            except ValueError:
                print("Incorrect input!")
            else:

                # AGE
                if selection == 1:
                    new_age = int(input("Enter new age -> "))

                # EMAIL
                elif selection == 2:
                    new_email = int(input("Enter new email -> "))

                # NAME
                elif selection == 3:
                    new_name = int(input("Enter new name -> "))

                # PASSWORD
                elif selection == 4:
                    new_password = int(input("Enter new password -> "))

                # PHONE
                elif selection == 5:
                    new_phone = int(input("Enter new phone -> "))

                # EXIT
                elif selection == 6:
                    run = False

                else:
                    print("Incorrect input.")

                current_user = session.query(User).filter_by(id=user_id)
                current_profile = session.query(Profile).filter_by(user_id=user_id)
                current_address = session.query(Address).filter_by(user_id=user_id)
                # result1 = current_user.update({"email": "email"})
                # result1 = current_profile.update({"age": 10})
                # result1 = current_address.update({"city": "Brest"})
                session.commit()
                pass


if __name__ == '__main__':
    update_user()
