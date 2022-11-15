def isleap(year: int):
    leap_result: int = int(year) % 4
    return int(leap_result) == 0


def isvalid(date):
    if len(date) > 6:
        day = int(date[0:2])
        month = date[3:5]
        year = date[6:]
        if 12 >= int(month) > 0:
            month_new = str(date[3:5])
            match str(month_new):
                case "01" | "03" | "05" | "07" | "08" | "10" | "12":
                    return 31 >= day > 0
                case "04" | "06" | "09" | "11":
                    return 30 >= day > 0
                case "02":
                    if isleap(year):
                        return 29 >= day > 0
                    else:
                        return 28 >= day > 0
        else:
            return False
    else:
        return False

userinput = str(input("Input Date 'dd/mm/yyyy': "))
while True:
    if isvalid(userinput):
        print("Correct Format")
        quit()
    else:
        print("Incorrect Format")
        userinput = input("Input Date 'dd/mm/yyyy': ")
