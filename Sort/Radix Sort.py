# radix sort

import random

def randomList(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 100))
    return list

def radixSort(list):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range( RADIX )]
        # split list between lists
        for  i in list:
            tmp = i // placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False
        # empty lists into list array
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                list[a] = i
                a += 1
        # move to next digit
        placement *= RADIX
    return list

def main():
    num = int(input("How many numbers do you want to sort: "))
    list = radixSort(randomList(num))
    print(list)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to sort another list? (y/n): ").lower() != "y":
            break