import sqlite3
from task_03_create_table import create_table


def drop_table(database: str):
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DROP TABLE user;
            """
        )
        session.commit()


if __name__ == '__main__':
    drop_table("users")
    create_table("users")
