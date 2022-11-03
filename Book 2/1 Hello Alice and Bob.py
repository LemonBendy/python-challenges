name = str(input("Input Name: "))

if name.lower() == "alice" or name.lower() == "bob":
    print(f"Hello {name}")
else:
    print(f"Go away {name}, you are not Alice or Bob")