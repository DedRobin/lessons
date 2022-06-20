import sqlite3


def add_data(product_name: str, price: int, quantity: int, comment: str) -> None:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """INSERT INTO products (product_name, price, quantity, comment)
            VALUES (?, ?, ?, ?);            
            """,
            (product_name, price, quantity, comment),
        )
        session.commit()
