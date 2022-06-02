"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
"""


def two_most_common_words(text):
    text = text.lower()
    text = text.replace(".", " ")
    my_list = [(text.count(word), word) for word in set(text.split())]
    first_most_common, second_most_common2 = sorted(my_list, reverse=True)[0:2]
    return first_most_common[1], second_most_common2[1]

text = "You get money money to pay money for you to."
print(two_most_common_words(text))
