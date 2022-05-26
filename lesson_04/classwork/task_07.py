"""
Task_07

Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется
первый список. Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого есть
в первых двух списках, но отсутствуют в третьем.
"""
# Variables
first_list, second_list, third_list = [], [], []
all_lists = [first_list, second_list, third_list]

"""
We need to create 3 lists with numbers. First let's iterate all lists (all_lists). 
Add numbers to each of the lists (current_list).
If enter integer - add int in list (current_list.
Id enter string - break loop "while" and go to next list (current_list).
"""

for current_list in all_lists:
    while True:
        try:
            print(f"The first list = {first_list}",
                  f"The second list = {second_list}",
                  f"The third list = {third_list}", sep="\n")
            add_number = int(input("""Enter a integer to add in list.
Enter a string to create current list.
Our choice: """))
            print("-" * 50)
            current_list.append(add_number)
        except ValueError:
            print("You enter a string character. Finish adding numbers to current list.")
            print("-" * 50)
            break

# Create common set of numbers with all lists.
common = {item for current_list in all_lists for item in current_list}

"""
Iterate common set of numbers to create list of numbers 
which include in first and second lists but don't include in third list
"""
result = [item for item in common
          if item in first_list
          and item in second_list
          and item not in third_list]

print(result)
