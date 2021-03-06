from sqlalchemy.orm import Session

from lesson_13.homework.models import *
from lesson_13.homework.create_session import create_current_session


def read_users(session: Session) -> None:
    tables = session.query(User, Profile, Address).join(Profile, Address)
    for user, profile, address in tables:
        values = [user.email, profile.name, profile.phone, profile.age, address.city, address.address]
        print(values)


if __name__ == '__main__':
    test_session = create_current_session()
    read_users(test_session)
