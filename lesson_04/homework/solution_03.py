"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""
import math


def xor_cipher(string: str, key: str):
    if len(string) < len(key):
        key = key[:len(string)]
    elif len(string) > len(key):
        k = math.ceil((len(string) / len(key)))
        key = key * k
    else:
        pass
    key = list(key)
    return "".join([chr(ord(letter) ^ ord(key.pop())) for letter in string])


def xor_uncipher(string, key):
    return "".join([chr(ord(letter) ^ key) for letter in string])


if __name__ == "__main__":
    cipher_word = xor_cipher("hello", "al")
    print(cipher_word)
    cipher_word = xor_cipher(cipher_word, "key")
    print(cipher_word)
    # uncipher_word = xor_uncipher(cipher_word, 12)
    # print(xor_uncipher(xor_cipher("hello", 12), 12))
