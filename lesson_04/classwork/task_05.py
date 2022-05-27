"""
Task_05

Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
"""
start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))

result = 0
for item in range(start, end + 1):
    result += item ** 3

print(result)
