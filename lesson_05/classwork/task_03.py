"""
Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type.
В зависимости от func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""


def f_max(args):
    maximum = args[0]
    for integer in args[1:]:
        if integer > maximum:
            maximum = integer
    return maximum


def f_min(args):
    minimum = args[0]
    for integer in args[1:]:
        if integer < minimum:
            minimum = integer
    return minimum


def min_or_max(func_type, *args):
    if func_type == "max":
        return f_max(args)
    elif func_type == "min":
        return f_min(args)


print(min_or_max("max", 2, 36, 3, 1, -1, 4, 10))
print(min_or_max("min", 2, 36, 3, 1, -1, 4, 10))
