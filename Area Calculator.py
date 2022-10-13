#width = float(input("Width: "))
#height = float(input("height: "))
#print("Area: " + str((width * height)) + "cm^2")

def area(width, height):
    a = float(width * height)
    return a

width = float(input("Width: "))
height = float(input("Height: "))
area = area(width, height)
print("Area: " + str(area) + "cm^2")