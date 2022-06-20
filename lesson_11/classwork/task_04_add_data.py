import sqlite3
from datetime import datetime


def add_data(database: str, firstname: str, lastname: str, email: str, password: str, age: int, datetime: str) -> None:
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """INSERT INTO user (firstname, lastname, email, password, age, datetime)
            VALUES (?, ?, ?, ?, ?, ?);            
            """,
            (firstname, lastname, email, password, age, datetime),
        )
        session.commit()


if __name__ == '__main__':
    add_data("users", "Pavel", "Rabekin", "pavelrabekin@gmail.com", "jdfnasdgkfd", 28, str(datetime.now()))
    add_data("users", "Diana", "Sarihova", "dianasarihova@gmail.com", "gfsdg76", 41, str(datetime.now()))
    add_data("users", "Roman", "Gucha", "romangucha@gmail.com", "dfnv56f78dsnb", 18, str(datetime.now()))
    add_data("users", "Pavel", "Korob", "pk-21@gmail.com", "@mpaikf0", 23, str(datetime.now()))
    add_data("users", "Darya", "Kolih", "daryabluray@gmail.com", "123qweasd", 21, str(datetime.now()))
    add_data("users", "Sergei", "Polohov", "ubicanubov227@gmail.com", "19474n78213", 23, str(datetime.now()))
