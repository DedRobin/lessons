import sqlite3


def remove_all_data(database_name: str):
    with sqlite3.connect(f"{database_name}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """DELETE FROM user;
            """)

if __name__ == '__main__':
    remove_all_data("users")
