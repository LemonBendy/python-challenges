import random

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def insertionSort(list):
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index
        while position>0 and list[position-1]>currentvalue:
            list[position]=list[position-1]
            position = position-1
        list[position]=currentvalue
    return list

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = insertionSort(randomList(num))
    print(list)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ") == "n":
            break
