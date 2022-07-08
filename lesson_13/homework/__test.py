from sqlalchemy.sql import and_, or_

from create_session import create_current_session
from models import *

session = create_current_session()


def main1(session):
    # sql_query_user = session.query(User)
    sql_query_profile = session.query(Profile).join(User).join(Purchase).join(Product).filter(
        Product.product_name == "seem")
    # sql_query_address = session.query(Address)
    # sql_query_product = session.query(Product).join(Purchase).join(User).join(Profile).filter(Product.product_name == "seem")
    # sql_query_purchase = session.query(Purchase)

    for row in sql_query_profile:
        print(row.name, row.user.email)


def main2(session):
    user = session.query(User).first()
    profile_1 = session.query(Profile).first()

    profile_from_user = user.addresses
    print(user.profile.age)


def main3(session):
    purchases = session.query(Purchase).join(User).join(Product).filter(or_(
        Product.product_name == 'seem', Product.product_name == 'reduce', Product.product_name == 'especially'))
    for p in purchases:
        print(p.user.profile[0].name)


if __name__ == '__main__':
    # main1(session)
    # main2(session)
    # main3(session)
