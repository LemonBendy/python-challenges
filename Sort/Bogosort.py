# bogosort algorithm

import random

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def isSorted(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def bogosort(list):
    while not isSorted(list):
        random.shuffle(list)
    return list

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = bogosort(randomList(num))
    print(list)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ").lower() != "y":
            break