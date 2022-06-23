from sqlalchemy.orm import Session
from models import Product


def remove_product(session: Session, id_number: int) -> None:
    session.query(Product).filter_by(id=id_number).delete()
    session.commit()
