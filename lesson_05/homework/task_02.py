"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы.
"""
import random


def secret_santa(*list_of_participants):
    list_of_participants = list(list_of_participants)
    pairs = {}
    while list_of_participants:
        current_participant = random.choice(list_of_participants)
        list_of_participants.remove(current_participant)
        partner = random.choice(list_of_participants)
        list_of_participants.remove(partner)
        pairs[current_participant] = partner
    return pairs


print(secret_santa("Oleg", "Piter", "Albert", "Kate", "Alexandr", "Karina", "Sergei", "Ludmila"))
