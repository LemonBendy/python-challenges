a = bool(1)
b = bool(1)
c = bool(0)
x = 0

if (a or b) and (not(c)):
    print("X = 1")
    x = 1
else:
    print("X = 0")
    x = 0

