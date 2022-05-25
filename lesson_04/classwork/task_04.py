"""
Task_04

Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""
import random

random_number = 0
while random_number != 7:

    print(random_number)
    random_number = random.randint(1, 10)
