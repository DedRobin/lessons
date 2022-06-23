from sqlalchemy.orm import Session
from models import Product


def read_product(session: Session) -> None:
    current_products = session.query(Product).filter(Product.id > 0).all()
    for current_product in current_products:
        print(current_product.product_name,
              current_product.price,
              current_product.product_quantity,
              current_product.comment)
