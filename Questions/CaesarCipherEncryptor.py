def caesarCipherEncryptor(string, key):
    encrypted = ""
    for letter in string:
        letterUnicode = ord(letter)
        if key/26 > 1:
            key = key%26
        if letterUnicode + key > 122:
            encrypted += chr((letterUnicode + key)%122 + 96)
        else:
            encrypted += chr(letterUnicode + key)

    return encrypted


print(caesarCipherEncryptor("abc", 2))


# Other Solution

# def caesarCipherEncryptor(string, key):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encoded = ""
#     for letter in string:
#         letterIndex = alphabet.index(letter)
#         if letterIndex + key > 25:
#             encoded += alphabet[((letterIndex + key)%26)]
#         else:
#             encoded += alphabet[letterIndex + key]

#     return encoded