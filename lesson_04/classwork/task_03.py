"""
Task_03

Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""
input_number = int(input("Enter a number: "))
result = 0

# counter = 1
# while counter < input_number + 1:
#     result += counter ** 3
#     counter += 1
# print(result)

while input_number > 0:
    result += input_number ** 3
    input_number -= 1
print(result)
