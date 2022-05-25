"""
Task_03

Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""
input_number = int(input("Enter a number: "))
count = 1
result = 0
while count < input_number + 1:
    result += count ** 3
    count += 1
print(result)
