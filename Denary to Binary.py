transmission = int((input("How many numbers would you like to convert:")))


def binaryconvert ():
    num = int(input("Input your denary number:"))
    binary = str("")

    while num != 0:
        n1 = num//2
        n2 = num%2
        binary = str(n2) + binary
        num = n1

    return binary

for i in range(transmission):
    bin = binaryconvert()
    print("your binary number is: " + bin)