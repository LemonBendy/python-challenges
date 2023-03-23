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
    print("   4. Print Dictionary             ")
    print("   5. Leave                        ")
    print("===================================")
    select = input(">>>> ")
    match select:
        case "1":
            search()
            menu()
        case "2":
            add_new()
            menu()
        case "3":
            export()
            menu()
        case "4":
            with open("codes.json", "r") as file:
                aircodes = json.load(file)
                print(aircodes)
                file.close()
            menu()
        case "5":
            quit()
        case other:
            menu()

def search():
    with open('codes.json', "r") as file:
        aircodes = json.load(file)
        file.close()
    key = str(input("Code: ").upper())
    if key in aircodes:
        print(f"{aircodes[key]} Airport")
    else:
        print("Code not found")

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


def export():
    with open('codes.json', "w") as file:
        json.dump(aircodes, file)
        file.close()
    print("Exported to codes.json")


menu()