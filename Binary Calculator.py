from random import randint, random
from time import sleep

# def binary_to_hex(): for later use
#   return hex

# def hex_to_binary(): for later use
#   return binary

# def denary_to_hex(): for later use
#   return hex

# def hex_to_denary(): for later use
#   return denary


##FUNCTIONS
def denary_to_binary():
    num = int(input("Input your denary number:"))
    binary = str("")

    while num != 0:
        n1 = num//2
        n2 = num % 2
        binary = str(n2) + binary
        num = n1
    return binary


def binary_to_denary():
    num = int(input("Input Binary:"))
    denary = 0
    power = 1
    while num > 0:
        rem = num % 10
        num = num//10
        denary += rem*power
        power = power*2
    return denary

#MAIN BODY

select = (input("What would you like to translate: \n"
               "1: Denary to Binary:1: \n"
               "2: Binary to Denary:2: \n"
               "3:       Quit      :3: \n"
               "====================== \n"
               ": "))

if select == 1:
     num = str(denary_to_binary())
     print("Binary Value : " + num)
elif select == 2:
    num = str(binary_to_denary())
    print("Denary Value : " + num)
elif select == 3 or select == "":
    print("Quitting...")
    sleep(1)
    print("Done")
    quit()
