# Exercise 1
my_fav_numbers = {11, 8, 15}
my_fav_numbers.add(5)
my_fav_numbers.add(23)
my_fav_numbers.pop()

friend_fav_numbers = {7, 32, 45}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Exercise 2 - You cannot add items to a tuple

# Exercise 3
for numbers in range(1, 21):
    print(numbers)

# Exercise 4
floats_list = []
counter = 1
while counter < 5:
    counter += 0.5
    floats_list.append(counter)

print(floats_list)

# Exercise 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
 # *********  Counting Apples *******
counter = 0
for items in basket:
    if items == "Apples":
        counter += 1
print(counter)

# Exercise 6
my_name = "Daniela"
user_name = " "
while user_name != my_name:
    user_name = input("What is your name? ")

# Exercise 7
verbs = ["sing", "dance", "speak", "talk", "walk", "write", "look"]
for item in verbs:
    if int(verbs.index(item)) % 2 == 0:
        print(item)

# Exercise 8
for nums in range(1500, 2501):
    if (nums % 5) == 0:
        print(nums)
    elif (nums % 7) == 0:
        print(nums)

# Exercise 9
user_fruits = input("What are your favorite fruits? Write them separated with a single space: ")
list(user_fruits)
any_fruit = input("Write any fruit: ")
if any_fruit in user_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 10
toppings = []
new_topping = " "
total_sum = 10

while new_topping != "quit":
    new_topping = input("Write a pizza topping, write 'quit' to finish: ")
    toppings.append(new_topping)
    total_sum += 2.5
    print("We'll add the topping to the pizza")

toppings.pop() #Removing the 'quit' from the list
print("The toppings are: ")
for item in toppings:
    print(item)
print(f"And the final price is: {total_sum - 2.5 }") #Taking the 2.5 from the quit

# Exercise 11
total_sum = 0
active = True
while active:
    age = input("Write the age of the person who wants the ticket, write 'quit' when you are finished: ")
    if age == "quit":
        active = False
    elif int(age) < 3:
        total_sum += 0
    elif 3 <= int(age) <= 12:
        total_sum += 10
    elif int(age) > 12:
        total_sum += 15

print(f"The total price is: {total_sum}")

teens_allowed = []
active = True
while active:
    name = input("Write your name, write 'quit' when you are finished: ")
    if name == "quit":
        active = False
        break
    age = input("Write your age: ")
    if int(age) > 21:
        teens_allowed.append(name)
print(f"The people allowed to see the movie are: {teens_allowed}")

# Exercise 12
names = ["Ana", "Jose", "David", "Juliette", "Oscar", "Mary"]
for name in names:
    age = input(f"How old is {name}? ")
    if int(age) < 16:
        names.remove(name)

print(names)
