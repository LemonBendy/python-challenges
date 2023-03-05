def rec_binary_search(array, result):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2
        if array[midpoint] == result:
            return True
        else:
            if result < array[midpoint]:
                return rec_binary_search(array[:midpoint], result)
            else:
                return rec_binary_search(array[midpoint + 1:], result)


def itr_binary_search(array, result):
    found = False
    while not found and len(array) > 0:
        midpoint = int(len(array)//2)
        if array[int(midpoint)] == result:
            found = True
            return found
        else:
            if result < array[midpoint]:
                array = array[:midpoint]
            else:
                array = array[midpoint + 1:]
    return False


if __name__ == "__main__":
    check= [12,14,23,42,132]
    print(f"Iteration: {itr_binary_search(check, 15)}")
    print(f"Iteration: {itr_binary_search(check, 123)}")
    print(f"Iteration: {itr_binary_search(check, 42)}")
    print(f"Recursion: {rec_binary_search(check, 15)}")
    print(f"Recursion: {rec_binary_search(check, 123)}")
    print(f"Recursion: {rec_binary_search(check, 42)}")