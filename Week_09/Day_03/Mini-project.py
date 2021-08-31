""" Characters Game"""


class Character:

    def __init__(self, name, life: int = 20, attack: int = 10):
        self.name = name
        self.life = life
        self.attack = attack
        print(f"Creating the Character {name} with life {life} and attack {attack}")

    def basic_attack(self, other_character):
        other_character.life -= self.attack


class Druid(Character):
    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other_char):
        other_char.life -= (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):

    def brawl(self, other_char):
        other_char.life -= (2 * self.attack)
        self.life += (0.5 * self.attack)

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, other_char):
        other_char.attack -= 3


class Mage(Character):

    def curse(self, other_char):
        other_char.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other_char):
        other_char.life -= self.attack / self.life



