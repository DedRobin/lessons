"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
название города и выводит на печать страну.
"""


def find_country(city, countries):
    for country, cities in countries.items():
        if city in cities:
            print(country)
            break
    else:
        print("No matches!")


def main():
    countries = {"Belarus": ["Minsk", "Mogilev", "Vitebsk", "Grodno", "Gomel", "Brest"],
                 "Russia": ["Moscow", "St. Petersburg", "Yekaterinburg", "Nizhny Novgorod", "Sochi"],
                 "Poland": ["Warsaw", "Krakow", "Gdansk", "Wroclaw", "Vlyublin"],
                 "USA": ["New York", "Washington", "Chicago", "Boston", "Detroit"]}
    city = "Krakow"
    find_country(city, countries)
    city = "Minsk"
    find_country(city, countries)
    city = "St. Petersburg"
    find_country(city, countries)
    city = "Boston"
    find_country(city, countries)
    city = "Paris"
    find_country(city, countries)


if __name__ == '__main__':
    main()
