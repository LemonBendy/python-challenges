import random

def randomList(a):
    list = []
    for i in range(0, int(a)):
        list.append(random.randint(1, 100))
    return list

def selectionsort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

def quickSort(list):
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

def insertionSort(list):
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index
        while position>0 and list[position-1]>currentvalue:
            list[position]=list[position-1]
            position = position-1
        list[position]=currentvalue
    return list

def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
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

def menu():
    print(f"===== Pick a Sorting Algorithm =====\n"
          "1. Selection Sort\n"
          "2. Quick Sort\n"
          "3. Insertion Sort\n"
          "4. Bubble Sort\n"
          "5. Bogosort\n"
          "6. Merge Sort\n"
          "7. Quit")
    choice = int(input(">>> "))
    num = input(f"\rHow many numbers would you like to sort: ")
    match choice:
        case 1:
            print(selectionsort(randomList(num)))
            menu()
        case 2:
            print(quickSort(randomList(num)))
            menu()
        case 3:
            print(insertionSort(randomList(num)))
            menu()
        case 4:
            print(bubbleSort(randomList(num)))
            menu()
        case 5:
            print(bogosort(randomList(num)))
            menu()
        case 6:
            print(mergeSort(randomList(num)))
            menu()
        case _:
            quit()

menu()