"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
"""


def two_most_common_words(text):
    text = text.lower()
    text = text.replace(".", " ")
    my_list = []
    for word in set(text.split()):
        counter = text.count(word)
        my_list.append((counter, word))
    most_common1, most_common2 = sorted(my_list, reverse=True)[0:2]
    return most_common1[1], most_common2[1]


text = "You get money to pay money for you."
print(two_most_common_words(text))
