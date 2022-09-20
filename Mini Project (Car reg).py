name = input("Name:")
print("::::::::::::::") #sytactic glitter
tel = input("Mobile Number:")
print("::::::::::::::")
reg = input("Car Registration:")
print("::::::::::::::")
year = (input("Year Registered:"))
numbers = [str(num) for num in range(10)]


def reg_check(name, tel, reg, year, numbers):
    if int(year) <= 2001:
        print("No rules apply")
    else:
        year = year[2::]
        year2 = int(year) + 50

    for i in list(reg[2:4]):
        if i not in numbers:
            check = False
        else:
            check = True

    if (reg[0:2].isupper() == True) and (reg[4::].isupper() == True) and (check == True):
        return True
    else:
        return False

if reg_check(name, tel, reg, year, numbers) == True:
    print("Registration Complete")
elif reg_check(name, tel, reg, year, numbers) == False:
    print("Incorrect")


#print(name, tel, reg, year, year2, reg[5:8])

