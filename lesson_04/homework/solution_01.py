"""
Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], выведите все элементы, которые меньше 5.
"""
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# 1)
# result = [item for item in my_list if item < 5]
# print(result)

# 2)
for item in my_list:
    if item < 5:
        print(item)

