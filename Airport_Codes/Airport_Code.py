import json

aircodes = {
    "LHR": "London Heathrow",
    "MAN": "Manchester",
    "BHX": "Birmingham",
    "EDI": "Edinburgh",
    "LTN": "London Luton"
}

def menu():
    print("===================================")
    print("   1. Search                       ")
    print("   2. Add New                      ")
    print("   3. Export Original Dictionary   ")
    print("   4. Leave                        ")
    print("===================================")
    select = int(input(">>>> "))
    match select:
        case 1:
            search()
        case 2:
            add_new()
        case 3:
            export()
        case 4:
            quit()
        case other:
            quit()

def search():
    key = input("CODE SEARCHING: ")
    if key not in aircodes:
        print("NOT IN DICTIONARY, PLEASE TRY AGAIN")
    else:
        print(f"{aircodes[key]} Airport")
    menu()

def add_new():
    key = str(input("Code: ").upper())
    if len(key) == 3 and key.isalpha():
        value = input("Name: ")
        if len(value) != 0:
            aircodes[key] = value
            print(aircodes)
        else:
            print("no null data values allowed")
    else:
        print("Invalid Data Input, TRY AGAIN")
    menu()

def export():
    with open("Airport_Codes\codes.json", "w") as file:
        json.dump(aircodes, file)
    print("Exported to codes.json")
    menu()

menu()