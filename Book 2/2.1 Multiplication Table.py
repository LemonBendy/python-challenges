n = int(input("Input Number: "))
add_or_times = str(input("Would you like to times(x) or add(+): "))
total = 0


if add_or_times.lower() == "x" or add_or_times.lower() == "times":
    total = 1
    for i in range(n):
        x = i+1
        total = total*x
        print(total)
elif add_or_times.lower() == "+" or add_or_times.lower() == "add":
    total = 0
    for i in range(n):
        x = i+1
        total += i
        print(total)

