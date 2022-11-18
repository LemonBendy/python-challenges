square = [[0, 1, 2, 3, 4, 5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]


def display(grid):
    for v in range(0, 5):
        for c in range(0, 6):
            print(f"  {grid[c][v]}  ", end="|")
        print()
        print("------------------------------------")


def decipher(cryptogram, grid):
    square = grid
    cryptogram = cryptogram.replace(" ", "")  # remove spaces
    crypto = cryptogram.split(",")  # split by comma and change converts to a list
    word = ""  # initialise the value of word to empty string
    for i in crypto:
        letter = square[int(i[0])][int(i[1])]
        word = word + letter
    return word


def main():
    display(square)
    code = input(" Enter Cryptogram (the ciphered message) ...  ")

    print("The Secret word is ... " + decipher(code, square))


main()
