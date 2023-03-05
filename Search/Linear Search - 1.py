def linear_search(array, result):
    found = False
    index = 0
    while index < len(array):
        if array[index] == result:
                found = True
                return found
        else:
            index += 1
    return found


hello= [12,14,123,42,32]

linear_search(hello, 15)


