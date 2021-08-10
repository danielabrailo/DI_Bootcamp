import random

userString = input("Write a string 10 letters long: ")
string_length = len(userString)
if string_length < 10:
    print("String not long enough")
    exit()
elif string_length > 10:
    print("String too long")
    exit()

print("The first character is: ",
      userString[0], "and the last character is: ", userString[string_length-1])

construction = ""
for x in userString:
    construction += x
    print(construction)

shuffleString = " ".join(random.sample(userString, len(userString)))
print("Shuffled string is: ", shuffleString)
