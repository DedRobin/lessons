"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""
import base64


def xor_cipher(string: str, cipher_key: str, in_out_base64=True) -> str:
    """
    Функция может использоваться как для шифрования, так и для дешифрования.

    Входящие данные:

        string - фраза, которую нужно зашифровать
        cipher_key - ключ шифрования
        in_out_base64 - True, если нужно зашифровать в base64
                        False, если нужно дешифровать из base64
    Результат:

        new_cipher_key - зашифрованная фраза
    """
    # Если in_out_base64 == False
    if not in_out_base64:
        string = string.encode("ascii")
        string = base64.b64decode(string)
        string = string.decode("ascii")

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

    # Если in_out_base64 = True
    if in_out_base64:
        new_cipher_word = new_cipher_word.encode("ascii")
        new_cipher_word = base64.b64encode(new_cipher_word)
        new_cipher_word = new_cipher_word.decode("ascii")
    return new_cipher_word


# def xor_uncipher(uncipher_word: str, uncipher_key: str) -> str:
#     return xor_cipher(uncipher_word, uncipher_key, in_out_base64=False)


if __name__ == "__main__":
    # Test: string < key

    word = "Hello, world!"
    key = "kd 672h"
    cipher_word = xor_cipher(word, key, in_out_base64=True)
    print(cipher_word)
    cipher_word = xor_cipher(cipher_word, key, in_out_base64=False)
    print(cipher_word)

    # Test  string > key

    word = "point"
    key = "j6!amnib"
    cipher_word = xor_cipher(word, key, in_out_base64=True)
    print(cipher_word)
    cipher_word = xor_cipher(cipher_word, key, in_out_base64=False)
    print(cipher_word)

# use library "base64"
# and encode(),decode()
