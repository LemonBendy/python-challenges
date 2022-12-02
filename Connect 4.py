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
    column = input("Which Column: ")
    match column.lower():
        case "a":
            for i in range(0, 5):
                if board[4 - i][0] == "0":
                    board[4 - i][0] = player
                    positionx = 0
                    positiony = 4 - i
                    return positionx, positiony
        case "b":
            for i in range(0, 5):
                if board[4 - i][1] == "0":
                    board[4 - i][1] = player
                    positionx = 1
                    positiony = 4 - i
                    return positionx, positiony
        case "c":
            for i in range(0, 5):
                if board[4 - i][2] == "0":
                    board[4 - i][2] = player
                    positionx = 2
                    positiony = 4 - i
                    return positionx, positiony
        case "d":
            for i in range(0, 5):
                if board[4 - i][3] == "0":
                    board[4 - i][3] = player
                    positionx = 3
                    positiony = 4 - i
                    return positionx, positiony
        case "e":
            for i in range(0, 5):
                if board[4 - i][4] == "0":
                    board[4 - i][4] = player
                    positionx = 4
                    positiony = 4 - i
                    return positionx, positiony
        case _:
            print(f"'{column}' is not a column, you have missed your go")
            quit_condition = input("Would you like to quit Y/N: ")
            if quit_condition.lower() == 'y':
                sys.exit()
            main()


def check_winner(xvalue, yvalue, player):  # going to be complicated, because 2D lists
    def horizontal(x, char):
        print(x + char)
        # checks horizontal

    def vertical(y, char):
        print(y + char)
        # checks vertical

    horizontal(xvalue, player)
    vertical(yvalue, player)


def menu():
    print(f"Welcome to Connect 4!       \n"
          f"============================\n"
          f"What would you like to do:  \n"
          f"      1. Start Game         \n"
          f"      2. Leave Game         ")
    selection = input(f">>>>")
    match selection:
        case '1':
            main()
        case '2':
            print("thanks for playing!")
            sys.exit()


def main():  # main function to run the game
    characters = ['x', 'y']
    character = random.choice(characters)
    while True:
        if character == 'x':
            character = 'y'
        else:
            character = 'x'
        show_board()
        update_board(character)
    menu()

menu()
