"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""


class MyTimeTwo:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __eq__(self, other) -> bool:
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __repr__(self):
        return f"{self.hours, self.minutes, self.seconds}"


if __name__ == '__main__':
    time_1 = MyTimeTwo(hours=10, minutes=20, seconds=30)
    time_2 = MyTimeTwo(hours=10, minutes=20, seconds=30)
    time_3 = MyTimeTwo(hours=9, minutes=20, seconds=30)
    time_4 = MyTimeTwo(hours=11, minutes=20, seconds=30)

    print(time_1.to_seconds())
    print("eq", time_1 == time_2)  # __eq__
    print("ne", time_1 != time_3)  # __ne__
    print("gt", time_4 > time_1)  # __gt__
    print("lt", time_3 < time_1)  # __lt__
    print("ge", time_2 >= time_1)  # __ge__
    print("ge", time_4 >= time_1)  # __ge__
    print("le", time_2 >= time_1)  # __le__
    print("le", time_1 >= time_3)  # __le__
