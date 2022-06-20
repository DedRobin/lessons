import sqlite3


def create_table(database: str):
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR,
            lastname VARCHAR,
            email VARCHAR,
            password VARCHAR,
            age INTEGER,
            datetime DATETIME);
            """
        )


def main():
    create_table(database="users")


if __name__ == '__main__':
    main()
