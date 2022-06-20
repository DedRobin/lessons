"""
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию
и вводить необходимые данные.
"""
import sqlite3
from create_table import create_table
from add_data import add_data
from read_data import read_data
from read_data_by_id import read_data_by_id
from update_data_by_id import update_data_by_id
from remove_data import remove_data
from clear_table import drop_table


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
                print("Are you sure? Creating new table will delete old table.")
                action = input("Selection(y/n): ")
                if action.lower() == "y":
                    drop_table()
                    create_table()

        elif action == 2:  # READ
            try:
                result = read_data()
                if not result:
                    print("Table is empty.")
                for item in result:
                    print(item)
            except sqlite3.OperationalError:
                print("No such table. Create new it.")

        elif action == 3:  # INSERT
            pass

        elif action == 5:  # REMOVE
            id_number = int(input("Ented id: "))
            remove_data(id_number)
        elif action == 6:  # EXIT
            print("Exit from program.")
            break


if __name__ == '__main__':
    main()
