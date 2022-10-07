

def denary_to_binary():
    num = int(input(("Input your denary number:")))
    binary = str("")

    while num != 0:
        n1 = num//2
        n2 = num%2
        binary = str(n2) + binary
        num = n1
    return binary


def binary_to_denary():
    binary = str(input("Input Binary:"))
    pmax = int(len(binary) - 1)

