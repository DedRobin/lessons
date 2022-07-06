from lesson_13.homework.create_session import create_current_session
from lesson_13.homework.models import Product


def delete_product() -> None:
    try:
        id_number = int(input("Enter id for delete product:"))
    except ValueError:
        print(f"Incorrect input.")
    else:
        pass
    session = create_current_session()
    session.query(Product).filter_by(id=id_number).delete()
    session.commit()


if __name__ == '__main__':
    delete_product()
