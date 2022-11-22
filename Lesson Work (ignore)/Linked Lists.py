import keyboard

names = [["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10],
         ["", -10]]
head = 0


def add_driver(names_list):
    x = 9
    y = x
    while x >= 0:
        driver = input("Input REG to join: ")
        if names_list[x][1] == "":
            x = x-1
        else:
            names_list[x][0] = str(driver)
            names_list[x][1] = x+1
            x = x-1
    for i in range(y+1):
        i = i
        print(names_list[i][0])


add_driver(names)
