"""
Используя условие первой задачи из урока, проверить то же самое только для коней.
"""


def find_all_coordinates(x, y):
    for i in range(8):

    return [(x + 2, y + 1),
            (x + 2, y - 1),
            (x - 1, y + 2),
            (x - 1, y - 2)]


def is_figure_beat_each_other(x1, y1, x2, y2):
    for x, y in ((x1, y1), (x2, y2)):
        print(find_all_coordinates(x, y))
    return


def main(x1, y1, x2, y2):
    print(is_figure_beat_each_other(x1, y1, x2, y2))


if __name__ == '__main__':
    main(3, 3, 5, 5)
    # main(1, 2, 3, 2)
    # main(1, 2, 3, 4)
    # main(2, 4, 3, 8)
