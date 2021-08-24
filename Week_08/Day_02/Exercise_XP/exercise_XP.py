import string
# Exercise 1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def oldest(*args):
#     cat_name = ""
#     cat_age = 0
#     for x in args:
#         if x.age > cat_age:
#             cat_age = x.age
#             cat_name = x.name
#     print(f"The oldest cat is {cat_name} and is {cat_age} years old")
#
#
# cat1 = Cat("Kitty", 3)
# cat2 = Cat("Lucky", 5)
# cat3 = Cat("Sunny", 7)
# oldest(cat1, cat2, cat3)

# Exercise 2
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
#
#     def bark(self):
#         print(f"{self.name} goes wolf!")
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")
#
#
# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
#
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is bigger")
# else:
#     print(f"{sarahs_dog.name} is bigger")


# Exercise 3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for item in self.lyrics:
#             print(item)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()


# Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for item in self.animals:
            print(item)

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("The animal does not exist in the zoo")

    def sort_animals(self):
        for letter in list(string.ascii_lowercase):
            animals_list = [animal for animal in self.animals if animal.startswith(letter)]
            sorted_list = sorted(animals_list)
            if sorted_list:
                print(sorted_list)


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Dog")
ramat_gan_safari.add_animal("Monkey")
ramat_gan_safari.add_animal("Mice")
ramat_gan_safari.add_animal("Dolphin")
ramat_gan_safari.add_animal("Elephant")


ramat_gan_safari.sell_animals("Elephant")

ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()

