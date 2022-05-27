"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное
из них.
"""


def summation_and_maximum(*args):
    summation = 0
    for integer in args:
        summation += integer
    maximum = args[0]
    for integer in args[1:]:
        if integer > maximum:
            maximum = integer
    return summation, maximum


print(summation_and_maximum(1, 36, 12, 3, 7, 0, 45, -12, -1, 6, 34, -123, 6, 90))
