import random
import time

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def selectionSort(list):
    time1 = time.perf_counter()
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    time2 = time.perf_counter()
    print(f"Time taken: {time2-time1}")
    return list

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = randomList(num)
    selectionSort(list)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ") == "n":
            break