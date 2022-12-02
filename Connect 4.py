import random
import sys

board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]


def show_board():
    global board
    for row in range(0, 6):
        for column in range(0, 5):
            print(board[row][column], "", end=' ')
        print()


def update_board(player):
    global board
    column = input("Which Column: ")
    match column.lower():
        case "a":
            for i in range(0, 5):
                if board[4-i][0] == "0":
                    board[4-i][0] = player
                    positionx = 0
                    positiony = 4-i
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
            print(f"'{column}' is not a column")


def check_winner(x, y, player):
    def horizontal(x):
        if
            return True

            return False
        # checks horizontal and vertical, diagonal at a later date


def main():
    characters = ['x', 'y']
    character = random.choice(characters)
    while True:
        show_board()
        posx, posy = update_board(character)[0], update_board(character)[1]
        if check_winner(posx, posy):
            sys.exit()


main()
