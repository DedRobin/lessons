from sqlalchemy.orm import Session

from shop.create_session_pack import create_current_session
from shop.project.tools.models import *
from shop.project.purchase._print_result_to_console import print_result_to_console
from shop.project.purchase._filter_by_column import _filter_by_column
from shop.project.purchase._create_filter_list import _create_filter_list


def search_by_purchases(session: Session):
    run = True
    while run:
        purchases = test_session.query(Purchase).join(User).join(Product).join(Profile)
        filter_dictionary = _filter_by_column(purchases.first())
        list_of_conditions = _create_filter_list()
        purchases = purchases.filter(*list_of_conditions)
        print_result_to_console(purchases, filter_dictionary)

        go_next = input(" Press something to continue...")


if __name__ == '__main__':
    test_session = create_current_session()
    search_by_purchases(session=test_session)
