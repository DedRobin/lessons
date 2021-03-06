"""
2) Переопределить магические методы сложения, вычитания, умножения на число.
"""
from __future__ import annotations
from task_01 import MyTime


class MyTimeTwo(MyTime):

    @staticmethod
    def seconds_to_time(seconds: int) -> MyTimeTwo:
        hours = seconds // 60 * 60
        seconds = seconds - hours * 3600
        minutes = seconds // 60
        seconds = seconds - minutes * 60
        return MyTimeTwo(hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other: MyTimeTwo) -> MyTimeTwo:
        seconds = self.to_seconds() + other.to_seconds()
        return MyTimeTwo.seconds_to_time(seconds)

    def __sub__(self, other: MyTimeTwo) -> MyTimeTwo:
        seconds = self.to_seconds() - other.to_seconds()
        return MyTimeTwo.seconds_to_time(seconds)

    def __mul__(self, other: int) -> MyTimeTwo:
        seconds = self.to_seconds() * other
        return MyTimeTwo.seconds_to_time(seconds)


if __name__ == '__main__':
    time_1 = MyTimeTwo(hours=1, minutes=2, seconds=3)
    time_2 = MyTimeTwo(hours=1, minutes=2, seconds=3)
    test_add = time_1 + time_2
    test_sub = time_1 - time_2
    test_mul = time_1 * 3
    print(test_add.hours, test_add.minutes, test_add.seconds)
    print(test_sub.hours, test_sub.minutes, test_sub.seconds)
    print(test_mul.hours, test_mul.minutes, test_mul.seconds)
