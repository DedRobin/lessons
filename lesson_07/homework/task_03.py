"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла
представляет собой запись вида:
Покупатель, Товар, Количество, Стоимость
где:
- Покупатель - имя покупателя (строка без пробелов),
- товар - название товара (строка без пробелов),
- количество - количество приобретенных единиц товара.
    a) Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
       приобретенных им товаров и их стоимость.
    b) Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных
       и их стоимость."""


def show_number_and_cost_for_customer(database):
    list_of_names = []
    names = set([current_list[0] for current_list in database])  # create list with customer names

    # We find number and cost for each customer(list_of_names = [names, numbers, costs])
    for name in names:
        number = [x[2] for x in database if x[0] == name]
        cost = [x[3] for x in database if x[0] == name]
        list_of_names.append([name, sum(number), sum(cost)])

    return list_of_names


def show_number_and_cost_for_things(database):
    list_of_things = []
    things = set([current_list[1] for current_list in database])  # create list with thing names

    # We find number and cost for each thing(list_of_things = [things, numbers, costs])
    for thing in things:
        number = [x[2] for x in database if x[1] == thing]
        cost = [x[3] for x in database if x[1] == thing]
        list_of_things.append([thing, sum(number), sum(cost)])

    return list_of_things


def main():
    database = []
    with open("customers.txt", "r") as file:
        for line in file:
            line = line.strip().split(',')  # remove newline characters and create list splitting line
            line = list(map(lambda x: x.strip(), line))  # remove whitespaces in second column
            line[2:] = [int(x) for x in line[2:]]  # convert number and cost (last 2 elements) in integer
            database.append(line)

    print("List of names:")
    for line in show_number_and_cost_for_customer(database):
        print(line)
    print("\nList of things:")
    for line in show_number_and_cost_for_things(database):
        print(line)


if __name__ == '__main__':
    main()
