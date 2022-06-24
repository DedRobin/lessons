from create_current_session import create_current_session
from sqlalchemy.orm import Session
from models import Product, Purchase


def show_table(session: Session, model_object: list) -> None:
    if isinstance(model_object[0], Product):
        columns = ["ID", "Product name", "Price", "Product Quantity", "Comment"]
        print(("|" + "-" * 30) * 5 + "|")
        print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format(*columns))
        print(("|" + "-" * 30) * 5 + "|")
        for current_product in model_object:
            values = [current_product.id,
                      current_product.product_name,
                      current_product.price,
                      current_product.product_quantity,
                      current_product.comment]
            print("|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|".format(*values))
        print(("|" + "-" * 30) * 5 + "|")

    elif isinstance(model_object[0], Purchase):
        columns = ["ID", "Purchase Quantity", "User name", "Product"]
        print(("|" + "-" * 30) * 4 + "|")
        print("|{:^30}|{:^30}|{:^30}|{:^30}|".format(*columns))
        print(("|" + "-" * 30) * 4 + "|")
        for current_purchase in model_object:
            values = [current_purchase.id,
                      current_purchase.purchase_quantity,
                      current_purchase.user.user_name,
                      current_purchase.product.product_name]
            print("|{:^30}|{:^30}|{:^30}|{:^30}|".format(*values))
        print(("|" + "-" * 30) * 4 + "|")


if __name__ == '__main__':
    test_session = create_current_session()
    test_product = test_session.query(Product).filter_by().all()
    show_table(test_session, test_product)
    test_purchase = test_session.query(Purchase).filter_by().all()
    show_table(test_session, test_purchase)
