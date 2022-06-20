import sqlite3


def remove_data(id_number: int) -> None:
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """DELETE FROM products
            WHERE id = ?;            
            """,
            (id_number,)
        )
        session.commit()
