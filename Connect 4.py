from random import choice

board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]


def show_board():
    global board
    for row in range(0, 6):
        for column in range (0,5):
            print(board[row][column],"   ", end=' ')
        print()


def update_board(player):
    column = input("Which Column: ")
    match column.lower():
        case "a":
            print("A")
        case "b":
            print("B")
        case "c":
            print("C")
        case "d":
            print("D")
        case "e":
            print("E")


def check_winner():
    print()
    #checks horizontal and vertical, diagonal at a later date


def main():
    show_board()
    update_board()
    #main game 


show_board()