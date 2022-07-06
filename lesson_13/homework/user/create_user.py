from re import match

from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import User, Profile, Address


def create_user() -> None:
    session = create_current_session()

    # USER
    email = input("Enter email -> ")
    password = input("Enter password -> ")
    new_user = User(email=email, password=password)

    # PROFILE
    name = input("Enter name -> ")
    phone = input("Enter phone -> ")
    while True:
        try:
            age = int(input("Enter age -> "))
        except ValueError:
            print("Error! Enter integer!")
        else:
            break

    new_profile = Profile(user=new_user, name=name, phone=phone, age=age)

    # ADDRESS
    city = input("Enter city -> ")
    address = input("Enter address -> ")
    new_address = Address(user=new_user, city=city, address=address)

    data = (new_user, new_profile, new_address)

    # COMMIT
    session.add_all(data)
    session.commit()


if __name__ == '__main__':
    create_user()
