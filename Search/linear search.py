def search(arr, target):
    found = False
    n = 0
    while not found or (n < len(arr)):
        if arr[n] == target:
            found = True
            return n
        n += 1
    return -1


def main():
    myList = ["Abd", "Ed", "Zack", "Jill", "Sara", "Tom", "Sam"]
    name = input("Enter a name: ")
    result = search(myList, name)
    if result != -1:
        print(name + " has been found in position " + str(result))
    else:
        print("Sorry .... " + name + " is not in my list")


if __name__ == "__main__":
    main()
