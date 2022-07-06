from lesson_13.homework.create_session import create_current_session
from models import *


def function():
    pass


if __name__ == '__main__':
    test_session = create_current_session()
    result = test_session.query(User).first()
    result = result.
    for x in result:
        print(x)
    pass
