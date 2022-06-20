from task_05_find_users_by_name import find_users_by_name
from task_06_find_users_by_age_range import find_users_by_age_range


def print_result(result: list) -> None:
    if not result:
        print("Not matches")
    else:
        print("Result of searching:")
        for item in result:
            print(item)


def find_users_by_name_or_age_range(database: str) -> None:
    flag_for_exit = False
    while not flag_for_exit:
        print("-" * 100)
        print("How do you want searching users?\nSelections:\n1) by name\n2) by age range\n3) exit")
        selection = int(input())
        if selection == 1:
            name = input("Enter a name: ")
            name = name.capitalize()
            result = find_users_by_name(database=database, firstname=name)
            print_result(result)
        elif selection == 2:
            age_from = int(input("Enter age from: "))
            age_to = int(input("Enter age to: "))
            result = find_users_by_age_range(database=database, start_age=age_from, end_age=age_to)
            print_result(result)
        elif selection == 3:
            print("Exit from program.")
            flag_for_exit = True
        else:
            print("Incorrect selection!\n")


if __name__ == '__main__':
    find_users_by_name_or_age_range("users")
