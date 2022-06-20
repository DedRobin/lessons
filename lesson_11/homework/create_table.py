import sqlite3


def create_table() -> None:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR,
            price FLOAT,
            quantity INTEGER,
            comment VARCHAR);
            """
        )
