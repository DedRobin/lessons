import sqlite3


def update_data(id_number: int,
                product_name: str,
                price: float,
                quantity: int,
                comment: str) -> None:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """UPDATE products
                SET product_name=?, price=?, quantity=?, comment=?
                WHERE id = ?;            
            """,
            (product_name, price, quantity, comment, id_number)
        )
        session.commit()
