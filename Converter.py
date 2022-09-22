type = input("Would you like to convert: length, area, weight, time?")

def length_to_m(unit, amount):
    m = "metres"
    amount = int(amount)
    match unit:
        case 'mm':
            print(amount/10000 + " " + m)
        case 'cm':
            print(amount/100 + " " + m)
        case ' m':
            print("Already in " + m)
        case 'km':
            print(amount*1000 + " " + m)

if type == 'length':
    query = input("how much would you like to convert:")
    units = query[-2:]
    amount = int(query[:-2])
    length_to_m(units, amount)


