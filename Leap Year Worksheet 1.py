def isleap(year):
    # Year is an integer
    year = int(year)
    if year <= 0:
        print("Years cannot have zero or negative values")
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("this is a leap year")
    else:
        print("this is not a Leap Year")


TestYear = input("Enter Year and I will check it if it is leap or not... ")

isleap(TestYear)
