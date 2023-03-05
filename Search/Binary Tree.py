import sys

my_tree = [["A", 1, 4],
           ["B", 2, -1],
           ["C", 7, -1],
           ["D", -1, -1],
           ["E", 5, 6],
           ["F", -1, -1],
           ["G", 8, -1],
           ["H", -1, -1],
           ["J", -1, -1]]


def get_path(pos):
    global my_tree
    print(pos)



def menu():
    print(f"   Welcome to PATH SEARCH!   \n"
          f"=============================\n"
          f"What would you like to do:   \n"
          f"      1. Print Tree          \n"
          f"      2. Leave Program        ")
    selection = input(f">>>> :")
    match selection:
        case '1':
            a = input(f"Which Location do you want a path to: ")
            get_path(a)
        case '2':
            print("thanks for playing!")
            sys.exit()
