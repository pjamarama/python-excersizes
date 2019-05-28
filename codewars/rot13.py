import string


def rot13(message):
    new_message = []
    for char in message:
        correction = 0
        if 77 < ord(char) < 90 or 109 < ord(char) < 122:
            correction = 26
        if char.isalpha():
            new_message.append(chr(ord(char) + 13 - correction))
        else:
            new_message.append(char)
    return ''.join(new_message)




print(rot13('Black cat - white cat'))
print(rot13('Test'))
print(rot13('Hence - disregards!'))

