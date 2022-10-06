


def binary_to_denary():
    binary = input("Input your binary number:")
    denary = 0
    for i in binary:
        denary = denary**2 + int(i)
    return denary



print(binary_to_denary())