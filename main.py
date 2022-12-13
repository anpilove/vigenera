import random


# dict = {(i - ord('a')): chr(i) for i in range(ord('a'), ord('z') + 1)}  # создание англиского словаря


def encrypt_vigenera(m: str, keys=[], size=None):
    """ функция для шифрование слова """
    encrypt_str = ''
    if not keys:
        if size is None:
            size = random.randint(5, 10)
        for s in range(size):
            key = chr(random.randint(ord('a'), ord('z')))
            keys.append(key)
    keys_iter = keys * ((len(m) // len(keys)) + 1)
    print(keys)
    for i, char in enumerate(m):

        # encrypt_str += dict[(ord(char) + ord(keys_iter[i]) - ord('a')) % len(dict)]
        encrypt_str += chr((ord(char)+ ord(keys_iter[i])) % 26 + 65 )

    print(encrypt_str)
    print('Keys encrypt', keys)
    return encrypt_str


# def decrypt_vigenera(c: str):
#     decrypt_str = ''
#     for i, char in enumerate(c):
#         decrypt_str += dict[(ord(char) - keys[i] - ord('a')) % len(dict)]
#
#     print(decrypt_str)


encrypt_word = encrypt_vigenera('ATTACKATDAWN', ["L", "E", "M", "O", "N"])

# decrypt_vigenera(encrypt_word)
