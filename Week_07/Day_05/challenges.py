# Exercise 1
items_list = ["apple", "banana", "cherry"]


def add_item():
    item = input("What item do you want to add?\n")
    index = int(input("At what index would you like to add it?\n"))
    items_list.insert(index, item)
    print(items_list)


add_item()


# Exercise 2
def count_spaces():
    word = input("Write a sentence:\n")
    spaces = word.count(" ")
    print(f"The number of spaces is: {spaces}")


count_spaces()


# Exercise 3
def count_letters():
    sentence = input("Write a sentence:\n")
    count_upper = 0
    count_lower = 0
    for word in sentence:
        if word.isupper():
            count_upper += 1
        elif word.islower():
            count_lower += 1
    print(f"The number of upper case letters is: {count_upper}")
    print(f"The number of lower case letters is: {count_lower}")


count_letters()


# Exercise 4
def my_sum(nums_list):
    nums_sum = 0
    for item in nums_list:
        nums_sum = nums_sum + item
    print(nums_sum)


my_sum([1, 5, 4, 2])


# Exercise 5
def find_max(nums_list):
    max_num = max(nums_list)
    print(max_num)


find_max([0, 1, 3, 50])


# Exercise 6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))


