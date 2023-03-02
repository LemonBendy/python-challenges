def binary_search(array, result):
    found = False
    while not found:
        midpoint = len(array) // 2
        if array[midpoint] == result:
            found = True
            return found
        else:
            if result < array[midpoint]:
                array = array[:midpoint]
            else:
                array = array[midpoint + 1:]
    return found


if __name__ == "__main__":
    hello= [12,14,123,42,32]
    print(binary_search(hello, 123))
    print(binary_search(hello, 42))
    print(binary_search(hello, 15))