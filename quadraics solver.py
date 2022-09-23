def quadsolver():
    a = float(input("Input a:"))
    b = float(input("Input b:"))
    c = float(input("Input c:"))
    d= b*b - 4*a*c
    if d == 0:
        x1 = -b/(2*a)
        x2 = x1
        print(x1,x2)
    elif d>0:
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d ** 0.5) / (2 * a)
        print(x1,x2)
    else:
        print("There is no real solution")


query = input("Would you like to input values: Y/N").lower()
while query == 'y':
    quadsolver()
    query = input("Would you like to input values: Y/N").lower()
else:
    quit()
