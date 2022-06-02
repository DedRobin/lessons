"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""
import random


def get_random_card():
    cards = ("6", "7", "8", "9", "10", "J", "D", "K", "A")
    nominals = ("Hearts", "Diamonds", "Clubs", "Spades")
    random_card = random.choice(cards)
    random_nominal = random.choice(nominals)
    return random_card, random_nominal


if __name__ == "__main__":
    print(get_random_card())
