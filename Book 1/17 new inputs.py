print("1) Square \n2) Triangle \n")
num = int(input("Enter a number: "))

if num == 1:
    w = int(input("Input Width: "))
    h = int(input("Input Height: "))
    a = int(w*h)
    print(f"The area of your quadrilateral is {a}")
elif num == 2:
    w = int(input("Input Width: "))
    h = int(input("Input Height: "))
    a = int((w*h)/2)
    print(f"The area of your triangle is {a}")