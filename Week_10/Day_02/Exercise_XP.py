# Exercise 1
import functions
from functions import sum_nums
from functions import sum_nums as sn

print(functions.sum_nums(1, 2))

# Exercise 2
import random

random_num = random.randrange(1, 101)
user_num = input('Choose a number between 1 and 100:\n')
if random_num == user_num:
    print("It's the same number!")
else:
    print("It's not the same number")

# Exercise 3
import string

result = ''.join((random.choice(string.ascii_letters) for x in range(5)))
print(f"Random generated string is: {result}")