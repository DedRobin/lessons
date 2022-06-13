"""
6) Добавить новый класс MyDateTime унаследованный от MyTime.
В конструктор добавить новые атрибуты: day, month, year.
“Исправить” все магические методы для этого класса.

7) Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""
from __future__ import annotations
from task_02 import MyTimeTwo


class MyDateTime(MyTimeTwo):
    MONTHLY_AVERAGE: int = 30

    def __init__(self, year: int = 0, day: int = 0, month: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        super().__init__(hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day
        self.attributes = (year, month, day, hours, month, seconds)

    @staticmethod
    def seconds_to_time(seconds: int) -> MyDateTime:
        years = int(seconds // (60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE * 12))
        seconds = seconds - years * 60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE * 12
        months = seconds // (60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE)
        seconds = seconds - months * 60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE
        days = seconds // (60 * 60 * 24)
        seconds = seconds - (days * 60 * 60 * 24)
        hours = seconds // (60 * 60)
        seconds = seconds - (hours * 3600)
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
        return MyDateTime(year=years, month=months, day=days, hours=hours, minutes=minutes, seconds=seconds)

    def to_seconds(self) -> int:
        from_minutes_to_seconds: int = self.minutes * 60
        from_hours_to_seconds: int = self.hours * 60 * 60
        from_days_to_seconds: int = self.day * 60 * 60 * 24
        from_months_to_seconds: int = self.month * 60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE
        from_years_to_seconds: int = self.year * 60 * 60 * 24 * MyDateTime.MONTHLY_AVERAGE * 12
        output = sum([self.seconds,
                      from_minutes_to_seconds,
                      from_hours_to_seconds,
                      from_days_to_seconds,
                      from_months_to_seconds,
                      from_years_to_seconds])
        return int(output)

    def __eq__(self, other: MyDateTime) -> bool:
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other: MyDateTime) -> bool:
        return self.to_seconds() != other.to_seconds()

    def __gt__(self, other: MyDateTime) -> bool:
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other: MyDateTime) -> bool:
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other: MyDateTime) -> bool:
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other: MyDateTime) -> bool:
        return self.to_seconds() <= other.to_seconds()

    def __add__(self, other: MyDateTime) -> MyDateTime:
        seconds = self.to_seconds() + other.to_seconds()
        return MyDateTime.seconds_to_time(seconds)

    def __sub__(self, other: MyDateTime) -> MyDateTime:
        seconds = self.to_seconds() - other.to_seconds()
        return MyDateTime.seconds_to_time(seconds)

    def __mul__(self, other: int) -> MyDateTime:
        seconds = self.to_seconds() * other
        return MyDateTime.seconds_to_time(seconds)

    def __str__(self) -> str:
        return "{0} years {1} months {2} days {3} hours {4} minutes {5} seconds".format(*self.attributes)


if __name__ == '__main__':
    some_datetime = MyDateTime(year=2, day=11, hours=12, seconds=1)
    some_datetime1 = some_datetime * 3
    some_datetime2 = some_datetime + some_datetime
    print(some_datetime1, some_datetime2, sep="\n")
