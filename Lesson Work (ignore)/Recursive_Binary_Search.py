def binary_search(array, result):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2
        if array[midpoint] == result:
            return True
        else:
            if result < array[midpoint]:
                return binary_search(array[:midpoint], result)
            else:
                return binary_search(array[midpoint + 1:], result)


if __name__ == "__main__":
    hello= [12,14,123,42,32]
    print(binary_search(hello, 15))
    print(binary_search(hello, 123))
    print(binary_search(hello, 42))