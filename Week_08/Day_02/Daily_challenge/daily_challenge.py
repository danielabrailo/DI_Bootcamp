from typing import List


class Farm:
    def __init__(self, farm_name: str):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal: str, quantity=1) -> None:
        self.animals[animal] = self.animals.get(animal, 0) + quantity

    def get_info(self) -> None:
        print(f"{self.name}'s farm")
        for animal, quantity in self.animals.items():
            print(f"{animal}: {quantity}")

    def get_animals_types(self) -> List:
        return sorted(self.animals.keys())

    def get_short_info(self):
        print(f"{self.name}'s farm has:")
        for animal in self.get_animals_types():
            print(animal)


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animals_types())
macdonald.get_short_info()
