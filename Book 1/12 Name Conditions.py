name: str = input("Input First Name: ")

if len(name) < 5:
    s_name = input("Input Last Name: ")
    full_name = name+s_name
    print(full_name.upper())
else:
    print(name.lower())
