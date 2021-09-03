from game import Game


def get_user_menu_choice():
    choice = input("What would you like to do next? Play a new (G)ame, (S)how scores or (Q)uit? \n")
    if choice not in ["G", "S", "Q"]:
        print("Invalid answer")
    return choice


def print_results(results):
    print("The results are:")
    for key, value in Game.results.items():
        print(f"{key}: {value}")


def main():
    flag = True
    while flag:
        choice = get_user_menu_choice()
        if choice == "Q":
            flag = False
        elif choice == "G":
            new_game = Game()
            new_game.play()
        elif choice == "S":
            print_results(Game.results)


main()
