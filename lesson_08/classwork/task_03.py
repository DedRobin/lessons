"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""
from task_04 import Animal


class Cat(Animal):
    def talk(self):
        print(self.name, "is meowing.")


if __name__ == '__main__':
    cat = Cat(height=10, weight=20, name="Barsik", age=8)

    cat.talk()
