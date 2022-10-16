over = int(input(("Input a number over 100: ")))

if over >= 100:
    under = int(input("Input a number under 100: "))
    div = round(over/under)
    print(str(under) + " goes into " + str(over) + ", " + str(div) + " times")
elif over < 100:
    print("Over 100 please")
    quit()
