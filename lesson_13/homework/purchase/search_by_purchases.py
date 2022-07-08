from sqlalchemy.orm import Session
from sqlalchemy.sql import and_
from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import *


def search_by_purchases(session: Session):
    list_of_conditions = []
    var = User.id
    a = eval(f"{var} == 4")
    purchases = session.query(Purchase).join(User).join(Product).filter(a)
    purchases1 = session.query(Purchase).join(User).join(Product).filter(User.id == 4)

    # purchases = purchases.
    for x in purchases:
        print(x.user.email)
    to_the_left = None
    to_the_right = None

    condition = int(input("Choice condition operator -> "))

    # EQUEL - "=="
    if condition == 1:
        expression = lambda x, y: x == y
        print(expression(1,1))
        pass

    # MORE THAN - ">"
    elif condition == 2:
        pass
    # LESS THAN - "<"
    elif condition == 3:
        pass

    # MORE THAN OR EQUEL - ">="
    elif condition == 4:
        pass

    # LESS THAB OR EQUEL - "<="
    elif condition == 5:
        pass

    # COME BACK
    elif condition == 6:
        pass


if __name__ == '__main__':
    test_session = create_current_session()
    search_by_purchases(session=test_session)
    # a_str = "1 + 2"
    # a_eval = eval(a_str)
    # print(a_str, a_eval)
