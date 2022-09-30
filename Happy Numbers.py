def happy_number(num):
    num_list = [int(x) for x in str(num)]
    total_list = []
    for x in num_list:
        number = int(num_list[x])
        square = number*number
        if square > 9:
            total_list = total_list + square
    return total_list


numb = input("Input a positive numbernumber:")

print(happy_number(numb))
