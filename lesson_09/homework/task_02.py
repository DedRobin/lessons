"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному, при этом диск нельзя класть
на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность
перекладываний, необходимую для решения головоломки.
"""
import random

kernels = {"1": [3, 2, 1],
           "2": [],
           "3": []}

set_of_numbers = [1, 2, 3]

while kernels["3"] != [3, 2, 1]:
    for disk in set_of_numbers:
        if disk in kernels["1"] and disk == kernels["1"][-1]:  # если диск находится в 1-м стержне сверху
            if not kernels["2"]:
                kernels["2"].append(kernels["1"].pop())
            elif not kernels["3"]:
                kernels["3"].append(kernels["1"].pop())
            elif kernels["2"][-1] == disk + 1:
                kernels["2"].append(kernels["1"].pop())
            elif kernels["3"][-1] == disk + 1:
                kernels["3"].append(kernels["1"].pop())
        elif disk in kernels["2"] and disk == kernels["2"][-1]:  # если диск находится в 2-м стержне сверху
            if not kernels["1"]:
                kernels["1"].append(kernels["2"].pop())
            elif not kernels["3"]:
                kernels["3"].append(kernels["2"].pop())
            elif kernels["1"][-1] == disk + 1:
                kernels["1"].append(kernels["2"].pop())
            elif kernels["3"][-1] == disk + 1:
                kernels["3"].append(kernels["2"].pop())
        elif disk in kernels["3"] and disk == kernels["3"][-1]:  # если диск находится в 3-м стержне сверху
            if not kernels["1"]:
                kernels["1"].append(kernels["3"].pop())
            elif not kernels["2"]:
                kernels["2"].append(kernels["3"].pop())
            elif kernels["1"][-1] == disk + 1:
                kernels["1"].append(kernels["3"].pop())
            elif kernels["2"][-1] == disk + 1:
                kernels["2"].append(kernels["3"].pop())
    if max(set_of_numbers) in kernels["3"]:
        set_of_numbers.remove(max(set_of_numbers))
    print(kernels)
