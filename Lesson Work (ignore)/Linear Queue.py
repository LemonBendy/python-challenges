import sys

HP = 0
TP = 0
queue = ['', '', '', '', '', '', '']


def isempty():
    global HP, TP
    return HP == TP


def full():
    return TP == len(queue)


def push(item):
    global TP, queue
    if full():
        print("Error Queue is Full")
    else:
        queue[TP] = item
        TP += 1


def pop():
    global HP, queue
    if isempty():
        print("Error Queue is Empty")
    else:
        print(queue[HP])
        queue[HP] = ''
        HP += 1


def display_queue():
    global HP, Tp, queue
    if isempty():
        print("The list is empty")
    else:
        print(f"HP = {HP}")
        for i in queue:
            if i != '':
                print(i)
        print(f"TP = {TP}")


def menu():
    print(f"What would you like to do:    \n"
          f"  1. Push Item                \n"
          f"  2. Pop Item              \n"
          f"  3. View Queue               \n"
          f"  4. Exit program             ")
    return input(f">>>>")


def main():
    while True:
        selection = menu()
        match selection:
            case "1":
                value = input("What would you like to push: ")
                push(value)
                display_queue()
            case "2":
                pop()
                display_queue()
            case "3":
                display_queue()
            case "4":
                print("Thanks for using the program!")
                sys.exit()
            case _:
                main()


main()
