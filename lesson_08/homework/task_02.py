"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""
from task_01 import Car


def accelerate_car(car_object: Car, speed: int) -> None:
    for _ in range(speed // 5):
        car_object.increase_speed()


car = Car(brand="Mercedes", model="E500", year=2000)

if __name__ == '__main__':
    car.show_speed()

    accelerate_car(car_object=car, speed=100)  # accelerate our car to 100 km/s

    car.show_speed()
