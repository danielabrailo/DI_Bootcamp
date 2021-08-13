# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for item in zip(keys, values):
    print(item)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_sum = 0
for key, value in family.items():
    if value < 3:
        total_sum += 0
        print(f"{key} has a free entrance!")
    elif 3 < value < 12:
        total_sum += 10
        print(f"{key} has to pay $10")
    elif value > 12:
        total_sum += 15
        print(f"{key} has to pay $15")
print(f"The total sum is: {total_sum}")

# Exercise 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home ",
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 2,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    }
}
brand["number_stores"] = 2
print("Zara's clients are for: " + brand["type_of_clothes"])
brand["country_creation"] = "Spain"
if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand["number_stores"])

# Exercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
for i, user in enumerate(users):
    print(user, i)

for i, user in enumerate(users):
    print(i, user)

for i, user in enumerate(sorted(users)):
    print(user, i)

for i, user in enumerate(users):
    if "i" in user:
        print(user, i)

for i, user in enumerate(users):
    if user.startswith("M") or user.startswith("P"):
        print(user, i)
