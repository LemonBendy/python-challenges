def quadsolver():
    a = float(input("input a:"))
    b = float(input("input b:"))
    c = float(input("input c:"))
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
        print("there is nor real solution")

quadsolver()