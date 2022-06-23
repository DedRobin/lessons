from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address
from utils import create_db_engine, create_db_engine_if_not_exists


def create_user(session: Session, email: str, password: str, phone: str, age: int, city: str, address: str) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all((user, profile, address))
    session.commit()

    return user


def update_or_create(session: Session, user: Profile, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        current_address = Address(user=user, city=city, address=address)

    session.add(current_address)
    session.commit()

    return current_address


def search_by_age(session: Session, input_profiles: list):
    for profile in input_profiles:
        print(profile.user.email)


if __name__ == "__main__":
    engine = create_db_engine()
    create_db_engine_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    # data = [[current_session, "pavelrabekin@gmail.com", "123qweasd", "+375259825663", 28, "Minsk", "Bachilo 4-134"],
    #         [current_session, "romanustomenko@gmail.com", "asdxcz", "+375334328676", 18, "Grodno", "Kabushkino 123-14"],
    #         [current_session, "karinadoroh@gmail.com", "145afsd", "+375299815348", 24, "Brest", "Lisua 1-73"]]
    # for field in data:
    #     user = create_user(*field)

    # user = create_user(session=current_session,
    #                    email="pavelrabekin@gmail.com",
    #                    password="123qweasd",
    #                    phone="+375258375298",
    #                    age=28,
    #                    city="Minsk",
    #                    address="Bachilo 4-134")

    # user = current_session.query(User).filter_by(email="pavelrabekin@gmail.com").first()
    # update_or_create(session=current_session,
    #                  user=user,
    #                  city="new city",
    #                  address="new address")

    users_by_age = current_session.query(Profile).filter(Profile.age == 18).all()
    search_by_age(current_session, users_by_age)
