from time import sleep
import sys

stack = ['', '', '', '', '', '', '', '', '']
sp = 0


def add_item():
    global stack, sp
    stack[sp] = input("Add item: ")
    sp += 1


def del_item():
    global stack, sp
    sp -= 1
    stack[sp] = ''


def isempty():
    global sp
    return sp == 0


def full():
    global stack, sp
    if sp == (len(stack) - 1):
        print("The name list is full, no values can be added sorry ")
        return True
    else:
        return False


def display_stack():
    global stack
    if isempty():
        print("The list is empty")
    else:
        for i in stack:
            print(i)


def menu():
    print(f"What would you like to do:    \n"
          f"  1. Push Item                \n"
          f"  2. Delete Item              \n"
          f"  3. View Stack               \n"
          f"  4. Exit program             ")
    return input(f">>>>")


def main():
    global stack, sp
    display_stack()
    while True:
        if full():
            print("The stack is full, no values can be added sorry ")
            sys.exit()
        else:
            match menu():
                case "1":
                    add_item()
                case "2":
                    del_item()
                    display_stack()
                case "3":
                    display_stack()
                    sleep(1)  # stops the user from having too much data at once
                case "4":
                    sys.exit()
                case _:
                    print("invalid input")


main()
