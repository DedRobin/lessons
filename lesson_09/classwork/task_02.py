"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""
from __future__ import annotations
from task_01 import MyTimeTwo


class MyTimeTwo(MyTimeTwo):

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @staticmethod
    def seconds_to_time(seconds: int) -> MyTimeTwo:
        hours = seconds // (60 * 60)
        seconds = seconds - hours * 3600
        minutes = seconds // 60
        minutes_to_seconds = seconds - minutes * 60
        seconds = seconds
        return MyTimeTwo(hours=hours, minutes=minutes, seconds=seconds)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __add__(self, other: MyTimeTwo) -> MyTimeTwo:
        seconds = self.to_seconds() + other.to_seconds()
        return MyTimeTwo.seconds_to_time(seconds)

    def __sub__(self, other: MyTimeTwo) -> MyTimeTwo:
        seconds = self.to_seconds() - other.to_seconds()
        return MyTimeTwo.seconds_to_time(seconds)

    def __mul__(self, other: MyTimeTwo) -> MyTimeTwo:
        seconds = self.to_seconds() * other.to_seconds()
        return MyTimeTwo.seconds_to_time(seconds)


if __name__ == '__main__':
    time_1 = MyTimeTwo(hours=1, minutes=2, seconds=3)
    time_2 = MyTimeTwo(hours=1, minutes=2, seconds=3)
    print(time_1 + time_2)
    print(time_1 - time_2)
    print(time_1 * time_2)
