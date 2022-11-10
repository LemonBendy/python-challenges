n = int(input("Input Number: "))
total = 0
three_total = 0

for i in range(n):
    total += i + 1
for i in range(n):
    x = i+1
    if x%3 == 0 or x%5 == 0:
        three_total += x
print(f"The sum of all whole numbers preceeding (and including) {n} is {total}")#
print(f"The sum of all whole numbers preceeding (and including) {n} that are divisible by 3 or 5 is {three_total}")
