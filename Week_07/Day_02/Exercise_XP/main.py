import random


# Exercise XP
# Exercise 1
def display_message():
    print("We are learning Python!")


display_message()


# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("1984")


# Exercise 3
def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")


describe_city("Tel Aviv")


# Exercise 4
def random_numbers(num):
    num2 = random.randrange(1, 101)
    if num == num2:
        print("Success! It's the same number!")
    print(f"Numbers are different! You chose: {num} and the machine chose: {num2}")


random_numbers(26)


# Exercise 5
def make_shirt(size="L", message="I love Python"):
    print(f"The size is {size} and the message is {message}")


make_shirt("S", "Hello world")
make_shirt("L")
make_shirt("M")

# Exrecise 6
magicians = ["David Blaine", "Jerry Sadowitz", "Dynamo", "Apollo Robbins"]

def show_magicians(names):
    for name in names:
        print(name)


def make_great(modify_list):
    copy_list = modify_list.copy()
    modify_list.clear()
    while len(copy_list) != 0:
        changed_name = copy_list.pop() + " the Great"
        modify_list.append(changed_name)


show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
