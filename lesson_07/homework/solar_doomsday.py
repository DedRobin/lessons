"""
Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum
antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have
one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar
Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12
square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would
leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar
panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make
out of those panels, starting with the largest squares first. So, following the example above, solution(12)
would return [9, 1, 1, 1].
"""
from math import sqrt, floor


def solution_1(area: int) -> list:
    squares = []
    while area > 0:
        max_square = int(area ** 0.5) ** 2
        squares.append(max_square)
        area = area - max_square
    return squares


def solution_2(area: int) -> list:
    # basic case for exit from recursion
    if area <= 0:
        return []
    else:
        max_square = sqrt(area)
        max_square = floor(max_square)
        max_square = pow(max_square, 2)
        return [max_square] + solution_2(area - max_square)


if __name__ == '__main__':
    numbers = [12, 542, 99482, 126, 14234, 1283, 0, 19214, 47, 28, 18, 265, 3, 6, 197, -193]
    for number in numbers:
        print(solution_1(number))
        print(solution_2(number))
