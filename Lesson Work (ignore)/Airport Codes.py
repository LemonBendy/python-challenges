aircodes = {
    "LHR": "London Heathrow",
    "MAN": "Manchester",
    "BHX": "Birmingham",
    "EDI": "Edinburgh",
    "LTN": "London Luton"
}
def search():
    key = input("CODE SEARCHING: ")
    if key not in aircodes:
        print("NOT IN DICTIONARY, PLEASE TRY AGAIN")
    else:
        print(f"{aircodes[key]} Airport")
    main()


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
    main()

def export():
    print("not yet") #TO DO

def main():
    print("================\n   1. Search \n   2. Add New \n   3. Export Original Dictionary \n   4. Leave \n================\n")
    select = int(input())
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


main()