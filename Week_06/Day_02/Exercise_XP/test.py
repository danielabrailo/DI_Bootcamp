# Exercise 1
print("Hello World " * 4)

# Exercise 2
calculation = (99**3) * 8
print(calculation)

# Exercise 3
# >>> 5 < 3 --> False
# >>> 3 == 3 --> True
# >>> 3 == "3" --> False
# >>> "3" > 3 --> Error
# >>> "Hello" == "hello" --> False

# Exercise 4
computer_brand = "Samsung"
print(f"I have a {computer_brand} computer")

# Exercise 5
name = "Daniela"
age = 29
shoe_size = 35
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}"
print(info)

# Exercise 6
a = 20
b = 15

if a > b:
    print("Hello world")

# Exercise 7
number = input("Write any number: ")
if int(number) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Exercise 8
my_name = "Daniela"
user_name = input("What is your name? ")

if my_name == user_name:
    print("How funny! We have the same name!")

# Exercise 9
user_heigth = input("Write your height in inches: ")
if int(user_heigth) > 57:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride!")
