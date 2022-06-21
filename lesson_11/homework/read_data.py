import sqlite3


def read_data(id_name: int = None) -> list:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        if not id_name:
            cursor.execute(
                """SELECT * 
                FROM products;        
                """
            )
        else:
            cursor.execute(
                """SELECT * 
                FROM products
                WHERE id = ?;        
                """, (id_name,)
            )
    return cursor.fetchall()
