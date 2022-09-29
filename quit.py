
num = int(input("What number would you like to convert?"))
binary = ""

print(num % 2)

while num != 0:
    if num%2 == 0:
        num = num%2
        binary = (binary + '0')
    elif num%2 == 1:
        num = num%2
        binary = (binary + '1')


print(binary)