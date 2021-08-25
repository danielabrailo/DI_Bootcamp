from Exercise_XP import Dog
import random


class PetDog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight, trained=False):
        super().__init__(dog_name, dog_age, dog_weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{self.name},{args} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks_list = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs",
                           f"{self.name} shakes your hand", f"{self.name} plays dead"]
            print(random.choice(tricks_list))


dog1 = PetDog("Charlie", 5, 50)
dog2 = PetDog("Bones", 7, 20)
dog3 = PetDog("Doggy", 10, 30)

dog1.train()
dog1.play("Bones", "Doggy")
dog1.do_a_trick()
