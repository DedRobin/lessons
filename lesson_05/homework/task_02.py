"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы.
"""
import random


def secret_santa(*participants):
    participants = list(participants)
    participants_copy = participants.copy()
    random.shuffle(participants)
    random.shuffle(participants_copy)
    pairs = {}
    while participants_copy and participants_copy:
        first_person = random.choice(participants)
        second_person = random.choice(participants_copy)
        if first_person == second_person:
            continue
        pairs[first_person] = second_person
        participants.remove(first_person)
        participants_copy.remove(second_person)
    return pairs


if __name__ == '__main__':
    my_dict = secret_santa("Oleg", "Piter", "Albert", "Kate", "Alexandr", "Karina", "Sergei", "Ludmila", "Pavel")
    for first, second in my_dict.items():
        print(f"{first} present {second}")
