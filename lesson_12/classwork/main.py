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


def update_or_create(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        address = user.addresses[0]
        address.city = city
        address.address = address
    else:
        address = Address(user=user, city=city, address=address)

    session.add(address)
    session.commit()

    return address


if __name__ == "__main__":
    engine = create_db_engine()
    create_db_engine_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

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
