# Rock-paper-scissors game
import random


class Game:
    results = {"win": 0, "loss": 0, "draw": 0}

    def get_user_item(self):
        flag = True
        while flag:
            user_choice = input("Choose your move: (R)ock, (P)aper or (S)cissors:\n")
            if user_choice in ["R", "P", "S"]:
                flag = False
                return user_choice

    def get_computer_item(self):
        choices = ["R", "S", "P"]
        computer_choice = random.choice(choices)
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        if user_item == "R" and computer_item == "R":
            # self.results["draw"] += 1
            return "draw"
        elif user_item == "P" and computer_item == "P":
            # self.results["draw"] += 1
            return "draw"
        elif user_item == "S" and computer_item == "S":
            # self.results["draw"] += 1
            return "draw"
        elif computer_item == "R" and user_item == "P":
            # self.results["win"] += 1
            return "win"
        elif computer_item == "P" and user_item == "S":
            # self.results["win"] += 1
            return "win"
        elif computer_item == "S" and user_item == "R":
            # self.results["win"] += 1
            return "win"
        elif computer_item == "R" and user_item == "S":
            # self.results["loss"] += 1
            return "loss"
        elif computer_item == "P" and user_item == "R":
            # self.results["loss"] += 1
            return "loss"
        elif computer_item == "S" and user_item == "P":
            # self.results["loss"] += 1
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if self.get_game_result(user_item, computer_item) == "draw":
            self.results["draw"] += 1
            print("It's a draw!")
        elif self.get_game_result(user_item, computer_item) == "win":
            self.results["win"] += 1
            print("You win!")
        elif self.get_game_result(user_item, computer_item) == "loss":
            self.results["loss"] += 1
            print("You lose!")

