"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""
import base64


def xor_cipher(string: str, cipher_key: str) -> str:
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
        multiplier = len(string) // len(cipher_key) + len(string) % len(cipher_key)  # округление в большую сторону
        cipher_key = cipher_key * multiplier

    # На каждой итерации цикла 'for' мы будем извлекать первый символ ключа, поэтому приведлем ее к списку.
    cipher_key = list(cipher_key)

    # Здесь соотносим символы друг с другом (1-й символ string с 1-м символом key, и т.д.)
    for letter in string:
        new_letter = chr(ord(letter) ^ ord(cipher_key.pop(0)))
        new_cipher_word += new_letter  # каждый символ добавляем в new_cipher_word

    return new_cipher_word


def xor_uncipher(uncipher_word: str, uncipher_key: str) -> str:
    return xor_cipher(uncipher_word, uncipher_key)


if __name__ == "__main__":
    # Test: string < key

    word = "Hello, world!"
    key = "kd 672h"
    cipher_word = xor_cipher(word, key)
    print(cipher_word)
    cipher_word = cipher_word.encode("ascii")
    print("Encode ascii:", cipher_word)
    for x in cipher_word:
        print(x, end=" ")
    print()
    cipher_word = base64.b64encode(cipher_word)
    print("Encode base64:", cipher_word)
    # cipher_word = xor_uncipher(cipher_word, key)
    # print(cipher_word)

    # Test  string > key

    # word = "point"
    # key = "j6!amnib"
    # cipher_word = xor_cipher(word, key)
    # print(cipher_word)
    # cipher_word = xor_uncipher(cipher_word, key)
    # print(cipher_word)

# use library "base64"
# and encode(),decode()
