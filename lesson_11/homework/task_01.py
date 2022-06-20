"""
1) Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3


def create_table(database: str):
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR,
            price INTEGER,
            quantity INTEGER,
            comment VARCHAR);
            """
        )


if __name__ == '__main__':
    create_table("products")
