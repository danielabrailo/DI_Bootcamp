# Exercise 1
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Persian("Kitty", 5)
cat2 = Bengal("Lucky", 5)
cat3 = Chartreux("Sunny", 5)

my_cats = [cat1, cat2, cat3]
my_pets = my_cats[0]
for cat in my_cats:
    print(cat.walk())


# Exercise 2
class Dog:
    def __init__(self, dog_name, dog_age, dog_weight):
        self.name = dog_name
        self.age = dog_age
        self.weight = dog_weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} won the fight!")
        else:
            print(f"{other_dog.name} won the fight!")


dog1 = Dog("Charlie", 5, 50)
dog2 = Dog("Bones", 7, 20)
dog3 = Dog("Doggy", 10, 30)

print(dog3.bark())
print(dog1.run_speed())
dog2.fight(dog1)

