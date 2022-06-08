"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса. Создать объект каждого класса и
вызвать все его методы.
"""


class Animal:
    def __init__(self, *args, **kwargs):
        self.height = kwargs.get("height")
        self.weight = kwargs.get("weight")
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")

    def show_all_atr(self):
        print("Name:", self.name)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Age:", self.age)

    def jump(self):
        print(self.name, "is jumping.")

    def run(self):
        print(self.name, "is running.")

    def talk(self):
        print(self.name, "is something.")


if __name__ == '__main__':
    animal1 = Animal(height=20, weight=40, name="Something", age=50)
    animal1.talk()
