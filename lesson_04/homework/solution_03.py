"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""
from math import ceil


def xor_cipher(string: str, cipher_key: str):
    """
    Входящие данные:

        string - фраза, которую нужно зашифровать
        cipher_key - ключ шифрования

    Результат:

        new_cipher_key - зашифрованная фраза
    """

    new_cipher_word = ""  # Здесь будет наш результат

    # Случай, когда длина (string) больше длины (cipher_key):
    # Если len(string) > len(cipher_key), то фраза не зашифруется полностью.
    # В этом случае нужно увеличить длину ключа шифрования путем конкатенации ее самой c собой (с помощью оператора '*')

    if len(string) > len(cipher_key):
        multiplier = ceil((len(string) / len(cipher_key)))  # округление в большую сторону
        cipher_key = cipher_key * multiplier

    # На каждой итерации цикла 'for' мы будем извлекать первый символ ключа, поэтому приведлем ее к списку.
    cipher_key = list(cipher_key)

    # Здесь соотносим символы друг с другом (1-й символ string с 1-м символом key, и т.д.)
    for letter in string:
        new_letter = chr(ord(letter) ^ ord(cipher_key.pop(0)))
        new_cipher_word += new_letter  # каждый символ добавляем в new_cipher_word

    return new_cipher_word


def xor_uncipher(uncipher_word, key):
    return xor_cipher(uncipher_word, key)


if __name__ == "__main__":
    # Test: string < key

    word = "Hello, world!"
    key = "kd 672h"
    cipher_word = xor_cipher(word, key)
    print(cipher_word)
    cipher_word = xor_uncipher(cipher_word, key)
    print(cipher_word)

    # Test  string < key

    word = "point"
    key = "j6!a"
    cipher_word = xor_cipher(word, key)
    print(cipher_word)
    cipher_word = xor_uncipher(cipher_word, key)
    print(cipher_word)
