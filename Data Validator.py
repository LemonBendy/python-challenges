# format dd/mm/yyyy
# check format


# 30 days, April [04], June [06], September [09], November [11]
# 31 days, January [01], March [03], May [05], July [07], August [08], October [10], December [12]
# 28 days, February [02]
# 29 days, February Leap Year [02]

def isleap(year: int):
    leap_result: int = int(year) % 4
    if int(leap_result) == 0:
        return True
    else:
        return False


def isvalid(date):
    if len(date) > 6:
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:])
        if 12 >= int(month) > 0:
            print("correct month")  # remove once done
            month_new = str(date[3:5])
            match str(month_new):
                case "01", "03", "05", "07", "08", "10", "12":
                    if 31 >= day > 0:
                        print("31 true")
                        return True
                    else:
                        print("31 false")
                        return False
                case "04", "06", "09", "11":
                    if 30 >= day > 0:
                        print("30 true")
                        return True
                    else:
                        print("30 false")
                        return False
                case "02":
                    if isleap(year):
                        if 29 >= day > 0:
                            print("leaped")
                            return True
                        else:
                            print("leaped false")
                            return False
                    else:
                        if 28 >= day > 0:
                            print("not leaped")
                            return True
                        else:
                            print("not leaped false")
                            return False
        else:
            print("Incorrect Date, format")
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


isvalid(userinput)
