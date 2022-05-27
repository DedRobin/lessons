"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".
"""


def month_to_season(number_of_month):
    # if number_of_month in (1, 2, 12):
    #     return "Winter"
    # elif number_of_month in (3, 4, 5):
    #     return "Spring"
    # elif number_of_month in (6, 7, 8):
    #     return "Summer"
    # else:
    #     return "Autumn"

    dict_of_seasons = {
        "Winter": [1, 2, 12],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11]
    }
    for season, month_list in dict_of_seasons.items():
        if number_of_month in month_list:
            return season


print(month_to_season(6))
