def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            print(1)
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                print(list)
    return list

abd = [23,47,15,44,95,11,30]
list = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(abd))


