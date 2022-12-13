def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    while True:
        print(factorial(int(input("Input Number : "))))

main()