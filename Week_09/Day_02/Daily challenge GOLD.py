input_list = []

for i in range(1, 6):
    user_input = input("Write the name, the age and the score:\n")
    input_list.append(tuple(user_input.split(",")))

input_list.sort(key=lambda x: x[0])

print(input_list)
