import random

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def display_board():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-+-+-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-+-+-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")


taken_pos = []  # Creating an empty list where all positions taken will be stored


def player_input():
    def correct_input():
        taken_pos.append(player_pos)
        display_board()

    try:
        player_pos = int(input("Enter your position (counting each square from 1 to 9): "))
        if player_pos in taken_pos:
            print("Position taken! Choose another!")
            player_input()
        elif player_pos == 1:
            board[0][0] = "X"
            correct_input()
        elif player_pos == 2:
            board[0][1] = "X"
            correct_input()
        elif player_pos == 3:
            board[0][2] = "X"
            correct_input()
        elif player_pos == 4:
            board[1][0] = "X"
            correct_input()
        elif player_pos == 5:
            board[1][1] = "X"
            correct_input()
        elif player_pos == 6:
            board[1][2] = "X"
            correct_input()
        elif player_pos == 7:
            board[2][0] = "X"
            correct_input()
        elif player_pos == 8:
            board[2][1] = "X"
            correct_input()
        elif player_pos == 9:
            board[2][2] = "X"
            correct_input()
    except:
        print("Wrong input, please enter a number between 1 and 9")
        player_input()


def computer_input():
    def correct_input():
        taken_pos.append(computer_pos)
        print("Computer plays:")
        display_board()

    computer_pos = random.randrange(1, 10)
    if computer_pos in taken_pos:
        computer_input()
    elif computer_pos == 1:
        board[0][0] = "O"
        correct_input()
    elif computer_pos == 2:
        board[0][1] = "O"
        correct_input()
    elif computer_pos == 3:
        board[0][2] = "O"
        correct_input()
    elif computer_pos == 4:
        board[1][0] = "O"
        correct_input()
    elif computer_pos == 5:
        board[1][1] = "O"
        correct_input()
    elif computer_pos == 6:
        board[1][2] = "O"
        correct_input()
    elif computer_pos == 7:
        board[2][0] = "O"
        correct_input()
    elif computer_pos == 8:
        board[2][1] = "O"
        correct_input()
    elif computer_pos == 9:
        board[2][2] = "O"
        correct_input()


def check_win():
    # Checking if the user won
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("You win!")
        return True
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("You win!")
        return True
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("You win!")
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("You win!")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("You win!")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("You win!")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("You win!")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("You win!")
        return True
        # Checking if the computer won
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Computer wins!")
        return True
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Computer wins!")
        return True
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Computer wins!")
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Computer wins!")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Computer wins!")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Computer wins!")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Computer wins!")
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Computer wins!")
        return True


def check_tie():
    if len(taken_pos) == 9:
        print("It's a tie! Game over!")
        return True


def play():
    display_board()
    while True:
        player_input()
        print(taken_pos)
        if check_win():
            break
        if check_tie():
            break
        computer_input()
        print(taken_pos)
        if check_win():
            break
        if check_tie():
            break


play()
