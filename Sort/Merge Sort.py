# merge sort

import random

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = randomList(num)
    print(mergeSort(list))

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ").lower() != "y":
            break
