"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5),
уменьшение скорости (скорость -5),
стоп (сброс скорости на 0),
отображение скорости,
задний ход (изменение знака скорости).
"""


class Car:
    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.speed = kwargs.get("speed", 0)

    def increase_speed(self) -> None:
        self.speed += 5

    def decrease_speed(self) -> None:
        self.speed -= 5

    def stop(self) -> None:
        self.speed = 0

    def show_speed(self) -> None:
        print(self.speed, "km/s")

    def reverse(self) -> None:
        self.speed *= -1

    def show_all(self):
        print(self.brand, self.model, self.year, self.speed, sep="\n")


if __name__ == '__main__':
    car_1 = Car(brand="VW", model="Passat B3", year="fdsf")
    car_1.show_all()
