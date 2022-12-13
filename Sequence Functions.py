

def f_add(n):
    total = 0
    for i in range(n):
        total = total + int(i+1)
    return total


def f_factorial(n):
    total = 1
    if n == 0:
        total = total
    elif n > 0:
        for i in range(n):
            total = total * int(i+1)
    return total


def fib(n):
    n1 = int(0)
    n2 = int(1)
    n3 = int(0)
    if n == 0:
        return n3
    elif n == 1:
        return n2
    elif n > 0:
        for i in range(n-1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3

#
print(fib(int(input("INPUT NUMBER : "))))


