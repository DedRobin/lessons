"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
"""

string = input(("Enter string to check if it is palindrome: "))

# if string == string[::-1]:
#     print("Yes")
# else:
#     print("No")

print("yes" if string == string[::-1] else "no")
