"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
"""


def two_most_common_words(text):
    text = text.lower()

    # Find all alphabet characters and space and apostrophe (')
    text = "".join([character for character in text if character.isalpha() or character == " " or character == "'"])

    # Find 2 most common words
    my_list = [(text.count(" " + word + " "), word) for word in set(text.split())]
    first_most_common, second_most_common = sorted(my_list, reverse=True)[0:2]

    # Find longest word
    longest_word = sorted(my_list, key=lambda x: len(x[1]), reverse=True)[0][1]

    return f"Two most common word: {first_most_common[1]}, {second_most_common[1]}.\nLongest word: {longest_word}."


text = "You get money to pay money for not unnecessary things. So you don't need to spend a lot of money!"
print(two_most_common_words(text))
