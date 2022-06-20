import sqlite3


def find_users_by_age_range(database: str, start_age: int, end_age: int) -> list:
    with sqlite3.connect(f"{database}.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """SELECT * 
            FROM user
            WHERE (? <= age) AND (age <= ?);
            """, (start_age, end_age)
        )
    return cursor.fetchall()


if __name__ == '__main__':
    print("Age from 18 to 23:")
    search_result = find_users_by_age_range(database="users", start_age=18, end_age=23)
    for item in search_result:
        print(item)

    print("\nAge from 28 to 45:")
    search_result = find_users_by_age_range(database="users", start_age=28, end_age=45)
    for item in search_result:
        print(item)

    print("\nAge from 23 to 41:")
    search_result = find_users_by_age_range(database="users", start_age=23, end_age=41)
    for item in search_result:
        print(item)
