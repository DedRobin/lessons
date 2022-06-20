import sqlite3


def find_users_by_name(database: str, firstname: str) -> list:
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """SELECT * 
            FROM user
            WHERE firstname = ?;
            """, (firstname,)
        )
    return cursor.fetchall()


if __name__ == '__main__':
    print("Search user 'Pavel'")
    search_result = find_users_by_name(database="users", firstname="Pavel")
    for item in search_result:
        print(item)

    print("\nSearch user 'Roman'")
    search_result = find_users_by_name(database="users", firstname="Roman")
    for item in search_result:
        print(item)

    print("\nSearch user 'Darya'")
    search_result = find_users_by_name(database="users", firstname="Darya")
    for item in search_result:
        print(item)
