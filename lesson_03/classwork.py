# Task_01

In [1]: x = 17 / 2 * 3 + 2

In [2]: x
Out[2]: 27.5

# Task_02

In [3]: x = 17 /( 2 * 3) + 2

In [4]: x
Out[4]: 4.833333333333334

In [5]: x = 17 / (2 * 3 + 2)

In [6]: x
Out[6]: 2.125

# Task_03

In [7]: roman = 26

In [8]: oleg = 28

In [9]: piter = 31

In [10]: summation = roman + oleg + piter

In [11]: summation
Out[11]: 85

# Task_04

In [12]: avarage = summation // 3

In [13]: avarage
Out[13]: 28

# Task_05

In [14]: my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]

In [15]: my_list
Out[15]: [1, 1.0, 2, 2, 5.0, 'python', 'python3', 'python3']

In [16]: my_set = set(my_list)

In [17]: my_set
Out[17]: {1, 2, 5.0, 'python', 'python3'}

In [18]: number_of_uni_el = len(my_list) - len(my_set)

In [19]: number_of_uni_el
Out[19]: 3

# Task_06

In [23]: my_list[4:1:-1]
Out[23]: [5.0, 2, 2]

In [24]: my_list[2:5][::-1]
Out[24]: [5.0, 2, 2]

# Task_07

In [28]: side_of_square = 13

In [29]: perimeter_square_diagonale
Out[29]: [40, 20, 14.142135623730951]

In [30]: perimeter_square_diagonale = [side_of_square * 4, side_of_square ** 2, (2 * side_of_square**2)**0.5]

In [31]: perimeter_square_diagonale
Out[31]: [52, 169, 18.384776310850235]

In [32]: from math import sqrt

In [33]: perimeter_square_diagonale = [side_of_square * 4, side_of_square
    ...: ** 2, sqrt(2 * side_of_square**2)]

In [34]: perimeter_square_diagonale
Out[34]: [52, 169, 18.384776310850235] 

