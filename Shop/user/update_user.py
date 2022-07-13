from getpass import getpass
from sqlalchemy.orm import Session

from Shop.create_session_pack import create_current_session
from Shop.models import User, Profile, Address


def update_user(session: Session) -> None:
    buffer = {}  # buffer for changes in user

    # FILTERS
    filter_for_user = {}
    filter_for_profile = {}
    filter_for_address = {}

    try:
        user_id = int(input("Enter user ID -> "))

    except ValueError:
        print("Incorrect input! Going back.")
    else:
        current_user = session.query(User).filter_by(id=user_id)
        current_profile = session.query(Profile).filter_by(user_id=user_id)
        current_address = session.query(Address).filter_by(user_id=user_id)

        run = True
        while run:
            print(f"""Menu -> Users -> Update user:
            
User - {current_user.first().email}.

What column do you want to change?
    1) Address
    2) Age;
    3) City;
    4) Email;
    5) Name;
    6) Password;
    7) Phone;
    8) Save changes;
    9) <-- Come back.""")
            if buffer:
                print("Your changes:")
                for key, value in buffer.items():
                    print(f"{key}: {value}")
            try:
                selection = int(input("Selection -> "))
            except ValueError:
                print("Incorrect input!")
            else:

                # ADDRESS
                if selection == 1:
                    previous_address = current_address.first().address.replace("\n", " ")
                    new_address = input(f"Enter new address (current age = {previous_address}) -> ")
                    filter_for_address["address"] = new_address
                    buffer["Address"] = f"{previous_address} -> {previous_address}"

                # AGE
                elif selection == 2:
                    previous_age = current_profile.first().age
                    new_age = int(input(f"Enter new age (current age = {previous_age}) -> "))
                    filter_for_profile["age"] = new_age
                    buffer["Age"] = f"{previous_age} -> {new_age}"

                # CITY
                elif selection == 3:
                    previous_city = current_address.first().city
                    new_city = input(f"Enter new city (current city = {previous_city}) -> ")
                    filter_for_address["city"] = new_city
                    buffer["City"] = f"{previous_city} -> {new_city}"

                # EMAIL
                elif selection == 4:
                    previous_email = current_user.first().email
                    new_email = input(f"Enter new email (current email = {previous_email}) -> ")
                    filter_for_user["email"] = new_email
                    buffer["Email"] = f"{previous_email} -> {new_email}"


                # NAME
                elif selection == 5:
                    previous_name = current_profile.first().name
                    new_name = input(f"Enter new name (current age = {previous_name}) -> ")
                    filter_for_profile["name"] = new_name
                    buffer["Name"] = f"{previous_name} -> {new_name}"

                # PASSWORD
                elif selection == 6:
                    while True:
                        previous_password = getpass(prompt="Enter old password (enter 'q' for cancel input) -> ")
                        if previous_password == current_user.first().password:
                            new_password = getpass(prompt="Enter new password -> ")
                            filter_for_user["password"] = new_password
                            buffer["Password"] = f"{len(previous_password) * '*'} -> {len(new_password) * '*'}"
                            break
                        elif previous_password == "q":
                            break
                        else:
                            print("Old and entered password aren't match! ")

                # PHONE
                elif selection == 7:
                    previous_phone = current_profile.first().phone
                    new_phone = input(f"Enter new phone (current phone = {previous_phone}) -> ")
                    filter_for_profile["phone"] = new_phone
                    buffer["Phone"] = f"{previous_phone} -> {new_phone}"

                # SAVE
                elif selection == 8:
                    if buffer:
                        answer = input("Are you sure you want to apply changes?(y/n)")
                        if answer == "y":
                            if filter_for_address:
                                current_address.update(filter_for_address)
                            if filter_for_profile:
                                current_profile.update(filter_for_profile)
                            if filter_for_user:
                                current_user.update(filter_for_user)
                            session.commit()
                            buffer = {}
                            print("Changes applied.")
                    else:
                        print("No changes.")

                # COME BACK
                elif selection == 9:
                    run = False

                else:
                    print("Incorrect input.")


if __name__ == '__main__':
    test_session = create_current_session()
    update_user(test_session)
