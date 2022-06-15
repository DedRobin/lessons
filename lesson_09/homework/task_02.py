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
tower = [4, 3, 2, 1]
kernels = {"1": tower,
           "2": [],
           "3": []}

tower_copy = deepcopy(tower)[::-1]

while kernels["3"] != tower_copy:
    for disk in tower_copy:
        if disk in kernels["1"] and disk == kernels["1"][-1]:  # если диск находится в 1-м стержне сверху
            if not kernels["2"] and len(tower_copy) > 1:
                kernels["2"].append(kernels["1"].pop())
            elif not kernels["3"] and len(tower_copy) > 1:
                kernels["3"].append(kernels["1"].pop())
            elif kernels["2"] and kernels["2"][-1] == disk + 1:
                kernels["2"].append(kernels["1"].pop())
            elif kernels["3"] and kernels["3"][-1] == disk + 1:
                kernels["3"].append(kernels["1"].pop())
        elif disk in kernels["2"] and disk == kernels["2"][-1]:  # если диск находится в 2-м стержне сверху
            if not kernels["1"] and len(tower_copy) > 1:
                kernels["1"].append(kernels["2"].pop())
            elif not kernels["3"] and len(tower_copy) > 1:
                kernels["3"].append(kernels["2"].pop())
            elif kernels["1"] and kernels["1"][-1] == disk + 1:
                kernels["1"].append(kernels["2"].pop())
            elif kernels["3"] and kernels["3"][-1] == disk + 1:
                kernels["3"].append(kernels["2"].pop())
        elif disk in kernels["3"] and disk == kernels["3"][-1]:  # если диск находится в 3-м стержне сверху
            if not kernels["1"] and len(tower_copy) > 1:
                kernels["1"].append(kernels["3"].pop())
            elif not kernels["2"] and len(tower_copy) > 1:
                kernels["2"].append(kernels["3"].pop())
            elif kernels["1"] and kernels["1"][-1] == disk + 1:
                kernels["1"].append(kernels["3"].pop())
            elif kernels["2"] and kernels["2"][-1] == disk + 1:
                kernels["2"].append(kernels["3"].pop())
    if max(tower_copy) in kernels["3"]:
        tower_copy.remove(max(tower_copy))
    print(kernels)
