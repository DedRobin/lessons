"""
Task_02

Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
"""
result = []
input_number = int(input("Enter a number: "))
for item in range(1, 101):
    if item % input_number == 0:
        result.append(item)
print(result)
