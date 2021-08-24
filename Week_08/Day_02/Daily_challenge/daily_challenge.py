class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def farm_name(self):
        print(f"{self.name}'s farm")

    def add_animal(self, animal, quantity=1):
        # If the animal already exists just increase, if not create a new one
        if animal in self.animals:
            self.animals[animal] += 1
        else:
            self.animals[animal] = quantity

    def get_info(self):
        for animal, quantity in self.animals.items():
            print(f"{animal}: {quantity}")

    def get_animals_types(self):
        animals_list = [animals for animals in self.animals.keys()]
        sorted_animals = sorted(animals_list)
        return sorted_animals

    def get_short_info(self):
        print(f"{self.name}'s farm has:")
        for animal in self.get_animals_types():
            print(animal)


macdonald = Farm("McDonald")
macdonald.farm_name()
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animals_types())
macdonald.get_short_info()
