"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному, при этом диск нельзя класть
на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность
перекладываний, необходимую для решения головоломки.
"""
from copy import deepcopy

number_of_disks = 3

tower = list(range(number_of_disks, 0, -1))
# kernels = {"1": tower, "2": [], "3": []}
kernels = [tower, [], []]

all_disks = deepcopy(tower)[::-1]

while kernels[2] != tower:

    top_layer = [kernel[-1] if kernel else None for kernel in kernels]  # верхний слой стержней
      # тек. стерень и диск
    for kernel, disk in enumerate(all_disks):  # ищем в каком из стержней есть текущий диск

        if disk == top_layer[kernel]:  # диск есть в стержне

            remove_disk = kernels[kernel].pop() # извлечение диска из текущего стержня kernel

            # оставшиеся стержни (если kernel=0, то ost_kernels = (1,2))
            another_kernels = (((kernel + 1) % 3), ((kernel + 2) % 3))

            for kernel_from_another in another_kernels:
                if kernels[kernel_from_another] and top_layer[kernel_from_another] == disk + 1:# если стержень не пуст и величина ДИСКА меньше величины верхнего диска на 1

                    kernels[kernel_from_another].append(remove_disk)

                # elif

                elif not kernels[kernel_from_another]:  # пустой стержень

                    kernels[kernel_from_another].append(remove_disk)  # вставка в другой стержень

        pass
    if max(all_disks) in kernels[2]:
        all_disks.remove(max(all_disks))

    print(kernels)
