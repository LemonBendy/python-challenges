total = 0

def add_even(n):
    global total
    if n == 0:
        return total
    if n % 2 == 0:
        total += n
    return add_even(n-1)

print(add_even(int(input("input number: "))))
