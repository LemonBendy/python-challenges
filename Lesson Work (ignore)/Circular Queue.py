import sys

HP = 0
TP = 0
queue = ['', '', '', '', '', '', '']


def full():
    global HP, TP, queue
    return (TP == (HP - 1)) or ((HP == 0) and (TP == len(queue)))


def isempty():
    global HP, TP
    return HP == TP


def push(item: any) -> None:
    global TP, queue
    if full():
        print("Error")
    else:
        queue[TP] = item
        TP += 1
        if TP > len(queue):
            TP = 0


def pop() -> None:
    global HP, queue
    if isempty():
        print("Error")
    else:
        print(queue[HP])
        HP += 1
        if HP > len(queue):
            HP = 0


def menu():
    print(f"What would you like to do:    \n"
          f"  1. Push Item                \n"
          f"  2. Pop Item              \n"
          f"  3. View Queue               \n"
          f"  4. Exit program             ")
    return input(f">>>>")


def display_queue() -> None:
    """
    Outputs the queue in the terminal
    """
    global HP, TP, queue
    if isempty():
        print("The list is empty")
    else:
        print(f"HP = {HP}")
        for i in queue:
            if i != '':
                print(i)
        print(f"TP = {TP}")


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
