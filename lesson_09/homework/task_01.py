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
    @staticmethod
    def find_edge(point_a: Point, point_b: Point) -> float:
        edge = sqrt(pow((point_a.x - point_b.x), 2) + pow((point_a.y - point_b.y), 2))
        return edge

    def find_area(self) -> float:
        raise NotImplemented

    def find_perimeter(self) -> float:
        raise NotImplemented


class Circle(Figure):
    def __init__(self, center: Point = Point(0, 0), radius: int = 0) -> None:
        self.center = center
        self.radius = radius

    def find_area(self) -> float:
        area = pi * pow(self.radius, 2)
        return area

    def find_perimeter(self) -> float:
        perimeter = 2 * pi * self.radius
        return perimeter


class Triangle(Figure):
    def __init__(self, point_a: Point = Point(0, 0),
                 point_b: Point = Point(0, 0),
                 point_c: Point = Point(0, 0)) -> None:
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.edge_ab = Figure.find_edge(point_a, point_b)
        self.edge_bc = Figure.find_edge(point_b, point_c)
        self.edge_ac = Figure.find_edge(point_a, point_c)

    def find_area(self) -> float:
        half_perimeter = self.find_perimeter() // 2
        area = sqrt(half_perimeter * (half_perimeter - self.edge_ab) *
                    (half_perimeter - self.edge_bc) *
                    (half_perimeter - self.edge_ac))
        return area

    def find_perimeter(self) -> float:
        perimeter = self.edge_ab + self.edge_bc + self.edge_ac
        return perimeter


class Square(Figure):
    def __init__(self, point_a: Point = Point(0, 0),
                 point_b: Point = Point(0, 0)) -> None:
        self.point_a = point_a
        self.point_b = point_b
        self.edge = Figure.find_edge(point_a, point_b)

    def find_area(self) -> float:
        area = pow(self.edge, 2)
        return area

    def find_perimeter(self) -> float:
        perimeter = 4 * self.edge
        return perimeter


if __name__ == '__main__':
    circle_01 = Circle(center=Point(1, 1), radius=10)
    circle_02 = Circle(center=Point(0, 5), radius=3)
    triangle_01 = Triangle(point_a=Point(2, 2), point_b=Point(4, 7), point_c=Point(1, 5))
    triangle_02 = Triangle(point_a=Point(3, 4), point_b=Point(2, 7), point_c=Point(1, 7))
    square_01 = Square(point_a=Point(4, 4), point_b=Point(4, 10))
    square_02 = Square(point_a=Point(3, 10), point_b=Point(0, 12))

    figures = [circle_01, circle_02, triangle_01, triangle_02, square_01, square_02]

    for number, figure in enumerate(figures, 1):
        print(f"{number}. {figure.__class__.__name__}:")
        print(f"\tArea = {figure.find_area():.3f}")
        print(f"\tPerimeter = {figure.find_perimeter():.3f}")
