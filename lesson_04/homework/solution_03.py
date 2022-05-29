"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""
import math


def xor_cipher(string: str, key: str):
    string = list(string)
    if len(string) < len(key):
        key = key[:len(string)]
    elif len(string) > len(key):
        k = math.ceil((len(string) / len(key)))  # округление в большую сторону
        key = key * k
    key = list(key)
    cipher_word = ""
    for letter in string:
        print(letter, end=" ")
        new_letter = chr(ord(letter) ^ ord(key.pop(0)))
        print(new_letter)
        cipher_word += new_letter
    return cipher_word

    # return "".join([chr(ord(letter) ^ ord(key.pop())) for letter in repr(string)])


def xor_uncipher(string, key):
    return "".join([chr(ord(letter) ^ key) for letter in string])


if __name__ == "__main__":
    cipher_word = xor_cipher("hello", "kgghjk")
    print(repr(cipher_word))
    cipher_word = xor_cipher(cipher_word, "kgghjk")
    print(cipher_word)
    # uncipher_word = xor_uncipher(cipher_word, 12)
    # print(xor_uncipher(xor_cipher("hello", 12), 12))
