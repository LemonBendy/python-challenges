def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for char in input_string:
        if char != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = char
        else:
            count += 1
    else:
        try:
            entry = (char, count)
            lst.append(entry)
            return (str(lst), 0)
        except Exception as e:
            print("Error: ", e)
            return (str(e), 1)

def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return str(q)

def main():
    input_string = input("Enter a string to encode: ")
    value = encode(input_string)
    if value[1] == 0:
        print(f"Encoded value is: {value[0]}")
        print(f"Decoded value is: {decode(value[0][1:-1].split(', '))}")
    else:
        print("Error: ", value[0])

if __name__ == "__main__":
    main()