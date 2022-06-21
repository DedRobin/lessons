"""
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию
и вводить необходимые данные.
"""
import sqlite3
import re
from create_table import create_table
from add_data import add_data
from read_data import read_data
from update_data import update_data
from remove_data import remove_data
from drop_table import drop_table


def show_table(data: list) -> None:
    columns = ["ID", "Product name", "Price", "Quantity", "Comment"]
    print(("|" + "-" * 20) * 5 + "|")
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(*columns))
    print(("|" + "-" * 20) * 5 + "|")
    for item in data:
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(*item))
    print(("|" + "-" * 20) * 5 + "|")


def menu_create_table():
    try:
        create_table()
    except sqlite3.OperationalError:
        while True:
            print("Are you sure? Creating new table will delete old table.")
            action = input("Selection(y/n): ")
            if action.lower() == "y":
                drop_table()
                create_table()
                print("Table is created.")
                break
            elif action.lower() == "n":
                break
            else:
                print("incorrect choice!")


def menu_read_data():
    try:
        reading_data = read_data()
        show_table(reading_data)
    except sqlite3.OperationalError:
        print("No such table. Create new it.")


def menu_insert_data():
    while True:
        field = input("Enter field separated by commas by pattern:\n'product name, price, quantity, comment'\n")
        check = re.match(r"[\d\w ]+, ?\d+(\.\d+)?, ?\d+, ?[\d\w ]+", field)
        if check:
            field = field.split(",")
            add_data(*field)
            break
        else:
            print("Incorrect data.")


def menu_update_data():
    show_table(read_data())
    id_number = int(input("Enter id: "))
    edit_field = read_data(id_number)
    edit_field = [list(edit_field[0])]  # [()] --> [[]] for editing
    run = True
    while run:
        show_table(edit_field)
        print("""What column do you want to change?
        1) Product name;
        2) Price;
        3) Quantity;
        4) Comment;
        5) Save changes;
        6) Cancel changes""")
        action = int(input("Selection: "))
        if action == 1:
            edit_field[0][1] = input("Enter product name: ")
        elif action == 2:
            edit_field[0][2] = input("Enter price: ")
        elif action == 3:
            edit_field[0][3] = input("Enter quantity: ")
        elif action == 4:
            edit_field[0][4] = input("Enter comment: ")
        elif action == 5:
            run = False
        elif action == 6:
            print("Cancel changes.")
            break
        else:
            print("Incorrect choice!")
    else:
        print("Changes applied.")
        update_data(*edit_field[0])


def menu_remove_data():
    id_number = int(input("Enter id: "))
    remove_data(id_number)


def main():
    print(("-" * 45) + "Product database" + ("-" * 45))
    while True:
        print("""Select action:
    1) Create table of products;
    2) Read data of products;
    3) Insert data of products;
    4) Update data of products;
    5) Remove data of products;
    6) Exit.""")
        action = int(input("Selection: "))

        # CREATE
        if action == 1:
            menu_create_table()

        # READ
        elif action == 2:
            menu_read_data()

        # INSERT
        elif action == 3:
            menu_insert_data()

        # UPDATE
        elif action == 4:
            menu_update_data()

        # REMOVE
        elif action == 5:
            menu_remove_data()

        # EXIT
        elif action == 6:
            print("Exit from program.")
            break


if __name__ == '__main__':
    main()
