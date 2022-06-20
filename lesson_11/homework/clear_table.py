import sqlite3


def drop_table() -> None:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DROP TABLE products;
            """
        )
        session.commit()
