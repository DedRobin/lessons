"""
Используя условие первой задачи из урока, проверить то же самое только для коней.
"""


def find_all_coordinates_for_horse(x, y):
    """
    This function finds all coordinates that horse moves to it.
    """
    if 1 <= x <= 8 and 1 <= y <= 8:
        all_coordinates = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
                           (x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2),
                           (x, y)]

        all_coordinates = list(
            filter(lambda current_tuple: 1 <= current_tuple[0] <= 8 and 1 <= current_tuple[1] <= 8, all_coordinates))
        return all_coordinates
    else:
        raise Exception("You must enter a number from 1 to 8.")


def is_figure_beat_each_other(x1, y1, x2, y2):
    # We find all coordinates for first and second horse figure
    # using the function 'find_all_coordinates_for_horse()'
    first_horse = find_all_coordinates_for_horse(x1, y1)
    second_horse = find_all_coordinates_for_horse(x2, y2)
    for coordinates in first_horse:
        if coordinates in second_horse:
            return True
    return False


def main():
    x1, y1, x2, y2 = 1, 1, 3, 1
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 1, 3, 5, 8
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 1, 1, 8, 0
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 6, 7, 7, 7
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 3, 1, 1, 1
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 3, 5, 3, 1
    print(is_figure_beat_each_other(x1, y1, x2, y2))
    x1, y1, x2, y2 = 1, 1, 2, 3
    print(is_figure_beat_each_other(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
