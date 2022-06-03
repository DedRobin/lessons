"""
Написать функцию, которая будет вызывать задержку выполнения программы случайным образом от 1-й до 5-ти секунд.
Написать декоратор, который будет выводить на печать время выполнения этой функции (end_time - start_time).
"""
import time
import random
from datetime import datetime


def decorator(function):
    def display_time():
        start_time = datetime.now()
        function()
        end_time = datetime.now()
        common_time = end_time - start_time
        print(f"Execution time of function '{display_time.__name__}()' = {common_time}.")

    return display_time


@decorator
def sleep_time():
    random_time = random.randint(1, 5)
    time.sleep(random_time)


def main():
    sleep_time()


if __name__ == '__main__':
    main()
