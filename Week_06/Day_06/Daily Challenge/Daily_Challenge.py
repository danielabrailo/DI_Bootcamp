# Caesar cypher with small letters
def caesar_encrypt(c_text):
    c = ''
    for i in c_text:
        if (i == ' '):
            c += ' '
        else:
            c += (chr((ord(i) + 4 - 96) % 26 + 97))
    return c


def caesar_decrypt(c_text):
    c = ''
    for i in c_text:
        if (i == ' '):
            c += ' '
        else:
            c += (chr((ord(i) - 4 - 97) % 26 + 96))
    return c


plain = 'itnsl ymj ifnqd hmfqqjslj'
cipher = caesar_encrypt(plain)
decipher = caesar_decrypt(plain)

answer = input("If you want to cipher type 'C', if you want to decipher type 'D': ")
if answer == "C":
    print(f"The text is: {plain}")
    print(f"The crypted text is: {cipher}")
elif answer == "D":
    print(f"The text is: {plain}")
    print(f"The decrypted text is: {decipher}")


