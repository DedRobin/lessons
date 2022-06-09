"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""
from task_01 import Car

car = Car(brand="Mercedes", model="E500", year=2000)
car.show_speed()

# accelerate our car to 100 km/s

end_speed: int = 100
for _ in range(end_speed // 5):
    car.increase_speed()

car.show_speed()
