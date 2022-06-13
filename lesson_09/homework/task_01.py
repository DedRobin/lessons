"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса
Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""
from __future__ import annotations

from math import pi, pow, sqrt


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, center: Point = Point(0, 0), radius: int = 0) -> None:
        self.center = center
        self.radius = radius

    def find_area(self) -> float:
        area = pow(pi * self.radius, 2)
        return area

    def find_perimeter(self) -> float:
        perimeter = 2 * pi * self.radius
        return perimeter

    def print_points(self) -> tuple[tuple[int, int], int]:
        return (self.center.x, self.center.x), self.radius


class Triangle(Figure):
    def __init__(self, point_a: Point = Point(0, 0),
                 point_b: Point = Point(0, 0),
                 point_c: Point = Point(0, 0)) -> None:
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.edge_ab = sqrt(pow((point_a.x - point_b.x), 2) + pow((point_a.y - point_b.y), 2))
        self.edge_bc = sqrt(pow((point_b.x - point_c.x), 2) + pow((point_b.y - point_c.y), 2))
        self.edge_ac = sqrt(pow((point_a.x - point_c.x), 2) + pow((point_a.y - point_c.y), 2))

    def find_area(self) -> float:
        half_perimeter = self.find_perimeter() // 2
        area = sqrt(half_perimeter * (half_perimeter - self.edge_ab) *
                    (half_perimeter - self.edge_bc) *
                    (half_perimeter - self.edge_ac))
        return area

    def find_perimeter(self) -> float:
        perimeter = self.edge_ab + self.edge_bc + self.edge_ac
        return perimeter

    def print_points(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        return ((self.point_a.x, self.point_a.y),
                (self.point_b.x, self.point_b.y),
                (self.point_c.x, self.point_c.y))


class Square(Figure):
    def __init__(self, point_a: Point = Point(0, 0),
                 point_b: Point = Point(0, 0)) -> None:
        self.point_a = point_a
        self.point_b = point_b
        self.edge = sqrt(pow((point_a.x - point_b.x), 2) + pow((point_a.y - point_b.y), 2))

    def find_area(self) -> float:
        area = pow(self.edge, 2)
        return area

    def find_perimeter(self) -> float:
        perimeter = 4 * self.edge
        return perimeter

    def print_points(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return ((self.point_a.x, self.point_a.y),
                (self.point_b.x, self.point_b.y))


if __name__ == '__main__':
    figures = [Circle(center=Point(1, 1), radius=10),
               Triangle(point_a=Point(2, 2), point_b=Point(4, 7), point_c=Point(1, 5)),
               Square(point_a=Point(4, 4), point_b=Point(4, 10)),
               Circle(center=Point(4, 2), radius=8)]
    perimeters_and_areas = {}
    for number, figure in enumerate(figures, 1):
        key = f"{figure}"
        perimeters_and_areas[key] = {"perimeter": figure.find_perimeter(),
                                     "area": figure.find_area()}
    for current_figure, perimeter_and_area in perimeters_and_areas.items():
        print(current_figure, perimeter_and_area)
