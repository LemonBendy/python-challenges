import random
import time

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list


def bubbleSort(list):
    time1 = time.perf_counter()
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    time2 = time.perf_counter()
    print(f"Time taken: {time2-time1}")
    return list


def main():
    num = int(input("How many numbers do you want to sort: "))
    list = randomList(num)
    bubbleSort(list)


if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ") == "n":
            break


