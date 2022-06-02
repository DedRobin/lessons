"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык. Написать две функции,
одна переводит слово с английского на русский, где слово - это входной параметр, вторая функция - с русского на
английский.
"""


def eng_into_rus(word):
    return dictionary[word]


def rus_into_eng(word):
    my_dict = {rus: eng for eng, rus in dictionary.items()}
    return my_dict[word]
    # for eng, rus in dictionary.items():
    #     if rus == word:
    #         return eng


dictionary = {
    "cat": "кот",
    "apple": "яблоко",
    "mouse": "мышь",
    "hat": "шляпа",
    "green": "зеленый"
}

with open("dictionary.csv", "w") as file:
    for key, value in dictionary.items():
        file.write(f"{key}, {value}\n")

if __name__ == "__main__":
    print(eng_into_rus("mouse"))
    print(rus_into_eng("яблоко"))
