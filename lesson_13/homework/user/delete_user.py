from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import User, Address, Profile


def delete_user() -> None:
    session = create_current_session()
    while True:
        try:
            id_number = int(input("Enter user ID which you want to remove it -> "))
        except ValueError:
            print(f"Incorrect input.")
        else:
            check_id = session.query(User).filter_by(id=id_number).all()
            if check_id:
                session.query(Address).filter_by(user_id=id_number).delete()
                session.query(Profile).filter_by(user_id=id_number).delete()
                session.query(User).filter_by(id=id_number).delete()
                session.commit()
                return
            else:
                print("ID is not find.")
                continue


if __name__ == '__main__':
    delete_user()
