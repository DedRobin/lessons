"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}". Создать список из 5 имен.
Вызвать функцию для каждого элемента списка в цикле.
"""


def greetings(name):
    print(f"Hello, {name}!")


greetings("Pavel")

names = ["Valera", "Roman", "Kristina", "Albert", "Piter"]

for name in names:
    greetings(name)
