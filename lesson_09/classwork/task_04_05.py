"""
4) Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.

5) Создать второй объект класса MyTime,
найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать результат.
"""
from task_02 import MyTimeTwo

# for task_04
my_time_01 = MyTimeTwo(hours=2, minutes=30, seconds=30)
my_time_mul = my_time_01 * 2
print(my_time_mul)

# for task_05
my_time_02 = MyTimeTwo(hours=7, minutes=45)
my_time_add = my_time_01 + my_time_02
print(my_time_add)
