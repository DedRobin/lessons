"""
Task_06

Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m),
а также количество x этих чисел.
"""
# Variables
start = int(input(("Enter a start number: ")))
end = int(input(("Enter a end number: ")))
prime_numbers = []

for current_number in range(start, end + 1):
    # Number less then or equal to zero isn't prime number.
    if current_number <= 0 or current_number == 1:
        continue

    # Number 2 is prime number so we display it.
    elif current_number == 2:
        prime_numbers.append(current_number)
        continue

    # Run loop which break it if number is divisible.
    for x in range(2, current_number // 2):
        if current_number % x == 0:
            break
    # If loop din't find it then display "current_number".
    else:
        prime_numbers.append(current_number)

print("Prime numbers:", *prime_numbers, "\nCounter of prime numbers: ", len(prime_numbers))
