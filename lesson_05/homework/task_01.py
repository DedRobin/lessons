"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.  В результате ее работы на печать
выводятся значения переданных переменных, но только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10.
"""


def three_args(**kwargs):
    result = []
    for variable, argument in kwargs.items():
        if argument != None:
            result.append(f"{variable} = {argument}")
    result = ", ".join(result)
    return f"Переданы аргументы: {result}."


some_dict = {'var1': 10,
             'var2': 43,
             'var3': 'forty six',
             'var4': 12,
             'var5': None,
             'var6': 'twenty'}
print(three_args(**some_dict))
