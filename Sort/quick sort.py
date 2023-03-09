import random
import time

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def quickSort(list):
    time1 = time.perf_counter()
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
    items_greater = []
    items_lower = []
    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = randomList(num)
    print(quickSort(list))

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ") == "n":
            break