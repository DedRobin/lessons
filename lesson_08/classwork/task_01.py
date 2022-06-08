"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
 Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран
 все его атрибуты.
"""
from task_04 import Animal

class Dog(Animal):

    def talk(self):
        print(self.name, "is barking.")


if __name__ == '__main__':
    dog1 = Dog(height=1, weight=2, name="Rex")

    dog1.show_all_atr()
    dog1.jump()
    dog1.run()
    dog1.talk()

    dog2 = Dog(height=3, weight=5, name="Sharik", age=18)

    dog2.show_all_atr()
    dog2.jump()
    dog2.run()
    dog2.talk()
