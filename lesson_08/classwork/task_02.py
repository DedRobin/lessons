"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""
from task_01 import Dog


class NewDog(Dog):
    def change_name(self, new_name):
        self.name = new_name


if __name__ == '__main__':
    dog1 = NewDog(height=1, weight=2, name="Rex")

    print(dog1.name)

    dog1.change_name("Kros")
    print(dog1.name)
