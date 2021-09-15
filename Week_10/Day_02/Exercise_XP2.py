# Exercise 1
import datetime


def show_date():
    print(datetime.datetime.now())


# Exercise 2
from datetime import date

date_today = datetime.date.today()
date_target = date(date_today.year + 1, 1, 1)
print(f"The 1st of January is in {date_target - date_today}")

# Exercise 3
from datetime import datetime
user_input = input("Write your birthdate in the following format: YYYY/MM/DD HH:MM:SS\n")
user_birthday = datetime.strptime(user_input, "%Y/%m/%d %H:%M:%S")
date_now = datetime.now()
time_delta = date_now - user_birthday
total_seconds = time_delta.total_seconds()
minutes = total_seconds/60
print(f"You have been alive for {minutes} minutes")


# Exercise 4
from datetime import date
holiday_date = date(2021, 9, 20)
holiday_name = "Succot"
delta = holiday_date - date_today
print(f"The next holiday is {holiday_name} and it is in {delta.days} days")


# Exercise 5
age = int(input("What is your age in seconds?\n"))
earth = age / 31557600
mercury = earth * 0.2408467
venus = earth * 0.61519726
mars = earth * 1.8808158
jupiter = earth * 11.862615
saturn = earth * 29.447498
uranus = earth * 84.016846
neptune = earth * 164.79132

print(f"You are {round(earth, 2)} Earth-years old")
print(f"You are {round(mercury, 2)} Mercury-years old")
print(f"You are {round(venus, 2)} Venus-years old")
print(f"You are {round(mars, 2)} Mars-years old")
print(f"You are {round(jupiter, 2)} Jupiter-years old")
print(f"You are {round(saturn, 2)} Saturn-years old")
print(f"You are {round(uranus, 2)} Uranus-years old")
print(f"You are {round(neptune, 2)} Neptune-years old")


# Exercise 6
from faker import Faker

fake = Faker()
user = [{}] * 5


def add_data():
    for i in user:
        i['name'] = fake.name()
        i['address'] = fake.address()
        i['language'] = fake.language_code()


add_data()
print(user)
