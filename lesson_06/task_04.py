"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае
положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту,
либо сумма его карт больше 21-го.
"""
from task_03 import get_random_card

nominal_to_number = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 1}
deck_of_cards = [('6', 'Hearts'), ('6', 'Diamonds'), ('6', 'Clubs'), ('6', 'Spades'),
                 ('7', 'Hearts'), ('7', 'Diamonds'), ('7', 'Clubs'), ('7', 'Spades'),
                 ('8', 'Hearts'), ('8', 'Diamonds'), ('8', 'Clubs'), ('8', 'Spades'),
                 ('9', 'Hearts'), ('9', 'Diamonds'), ('9', 'Clubs'), ('9', 'Spades'),
                 ('10', 'Hearts'), ('10', 'Diamonds'), ('10', 'Clubs'), ('10', 'Spades'),
                 ('J', 'Hearts'), ('J', 'Diamonds'), ('J', 'Clubs'), ('J', 'Spades'),
                 ('D', 'Hearts'), ('D', 'Diamonds'), ('D', 'Clubs'), ('D', 'Spades'),
                 ('K', 'Hearts'), ('K', 'Diamonds'), ('K', 'Clubs'), ('K', 'Spades'),
                 ('A', 'Hearts'), ('A', 'Diamonds'), ('A', 'Clubs'), ('A', 'Spades')]

card, _ = get_random_card()
deck_of_cards.remove((card, _))
current_number = nominal_to_number[card]
print(f"You get card - {card}({_}).\nCurrent number = {current_number}.")

while True:
    # Exit if more then 21
    if current_number > 21:
        print(f"You get more then 21.\nOur number {current_number}.")
        break

    choice = input("Do you want to get next card?(y/n)\n")

    # Exit if use enter "n"
    if choice == "n":
        print(f"You answer 'No'.\nOur number {current_number}.")
        break

    # Get new card and remove it from deck of cards
    while True:
        card, _ = get_random_card()
        if (card, _) in deck_of_cards:
            deck_of_cards.remove((card, _))
        else:
            continue  # get card again

        # If get "A" we do choice between "1" and "11"
        if card == "A":
            choice_number_for_ace_card = 0
            while choice_number_for_ace_card != 1 and choice_number_for_ace_card != 2:
                choice_number_for_ace_card = int(input("You get 'A'. What do you want to add?\n1) 1\n2) 11\n"))
                if choice_number_for_ace_card == 1:
                    current_number += 1
                elif choice_number_for_ace_card == 2:
                    current_number += 11
                else:
                    print("Incorrect choice!")
            else:
                break
        else:
            current_number += nominal_to_number[card]
            break
    print(f"You get card - {card}({_}).\nCurrent cum = {current_number}.")
