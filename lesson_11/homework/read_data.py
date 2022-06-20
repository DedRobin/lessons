import sqlite3


def read_data() -> list:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """SELECT * 
            FROM products          
            """
        )
    return cursor.fetchall()
