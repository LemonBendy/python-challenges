import random
import sys

board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]


def show_board():  # prints the board
    global board  # hello there
    for row in range(0, 6):  # general kenobi
        for column in range(0, 5):
            print(board[row][column], "", end=' ')
        print()


def update_board(player):  # handles board updates and will return x and y pos for check_winner()
    global board
    print(f"Current Player is '{player}'")
    column = input("Which Column: ")
    match column.lower():
        case "a":
            for i in range(0, 5):
                if board[4 - i][0] == "0":
                    board[4 - i][0] = player
                    return
        case "b":
            for i in range(0, 5):
                if board[4 - i][1] == "0":
                    board[4 - i][1] = player
                    return
        case "c":
            for i in range(0, 5):
                if board[4 - i][2] == "0":
                    board[4 - i][2] = player
                    return
        case "d":
            for i in range(0, 5):
                if board[4 - i][3] == "0":
                    board[4 - i][3] = player
                    return
        case "e":
            for i in range(0, 5):
                if board[4 - i][4] == "0":
                    board[4 - i][4] = player
                    return
        case _:
            print(f"'{column}' is not a column, you have missed your go")
            quit_condition = input("Would you like to quit Y/N: ")
            if quit_condition.lower() == 'y':
                sys.exit()
            main()


def check_winner(player):  # going to be complicated, because 2D lists
    global board

    def horizontal(char):
        # Horizontal checker
        for j in range(0, 5):
            for i in range(3, 5):
                if (board[j][i] == board[j][i - 1] ==
                        board[j][i - 2] == board[j][i - 3] == char):
                    return True

    def vertical(char):
        for i in range(0, 5):
            for j in range(3, 5):
                if (board[j][i] == board[j - 1][i] ==
                        board[j - 2][i] == board[j - 3][i] == char):
                    return True

    def diagonal(char):
        for i in range(0, 4):
            for j in range(0, 3):
                if (board[j][i] == board[j - 1][i - 1] ==
                        board[j - 2][i - 2] == board[j - 3][i - 3] == char or
                        board[j - 3][i] == board[j - 2][i - 1] ==
                        board[j - 1][i - 2] == board[j][i - 3] == char):
                    return True

    if not horizontal(player) and not vertical(player) and not diagonal(player):
        return
    return True


def menu():
    print(f"Welcome to Connect 4!       \n"
          f"============================\n"
          f"What would you like to do:  \n"
          f"      1. Start Game         \n"
          f"      2. Leave Game         ")
    selection = input(f">>>> :")
    match selection:
        case '1':
            main()
        case '2':
            print("thanks for playing!")
            sys.exit()


def main():  # main function to run the game
    characters = ['X', 'Y']
    character = random.choice(characters)
    while True:
        if character == 'X':
            character = 'Y'
        else:
            character = 'X'
        show_board()
        update_board(character)
        if check_winner(character):
            break
    print("\n" * 20)
    print("The winning board is : ")
    show_board()
    print("Thanks for Playing!")


menu()
