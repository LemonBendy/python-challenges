

# def binary_to_hex(): for later use
#   return hex

# def hex_to_binary(): for later use
#   return binary

# def denary_to_hex(): for later use
#   return hex

# def hex_to_denary(): for later use
#   return denary

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

    
select = input("Would you like to convert (B)inary or (D)enary: ")

if select.lower() == 'd':
    print(denary_to_binary())
elif select.lower() == 'b':
    print(binary_to_denary())
