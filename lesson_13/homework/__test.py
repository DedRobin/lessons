from create_session import create_current_session
from models import *


def function():
    pass


if __name__ == '__main__':
    test_session = create_current_session()
    table = test_session.query(User, Purchase).join(Purchase).all()
    pass
