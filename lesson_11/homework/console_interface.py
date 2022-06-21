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


def main():
    print(("-" * 25) + "Product database" + ("-" * 25))
    while True:
        print("""Select action:
    1) Create table of products;
    2) Read data of product by it 'id';
    3) Insert data of product;
    4) Update data of product by it 'id';
    5) Remove data of product by it 'id';
    6) Exit.""")
        action = int(input("Selection: "))

        if action == 1:  # CREATE
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

        elif action == 2:  # READ
            try:
                reading_data = read_data()
                show_table(reading_data)
            except sqlite3.OperationalError:
                print("No such table. Create new it.")

        elif action == 3:  # INSERT
            while True:
                field = input("Enter field separated by commas by pattern:\n'product name, price, quantity, comment'\n")
                check = re.match(r"[\d\w ]+, ?\d+(\.\d+)?, ?\d+, ?[\d\w ]+", field)
                if check:
                    field = field.split(",")
                    add_data(*field)
                    break
                else:
                    print("Incorrect data.")

        elif action == 4:  # UPDATE
            show_table(read_data())
            id_number = int(input("Enter id: "))
            edit_field = read_data(id_number)
            edit_field = [list(edit_field[0])]
            while True:
                show_table(edit_field)
                print("""What column do you want to change?
    1) Product name;
    2) Price;
    3) Quantity;
    4) Comment;
    5) Save changes.""")
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
                    break
                else:
                    print("Incorrect choice!")
                update_data(*edit_field[0])
        elif action == 5:  # REMOVE
            id_number = int(input("Enter id: "))
            remove_data(id_number)

        elif action == 6:  # EXIT
            print("Exit from program.")
            break


if __name__ == '__main__':
    main()
