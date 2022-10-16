raining = str(input("Is it raining Y/N: "))

if raining.lower == 'y':
    wind = str(input("Is it windy Y/N: "))
    if wind.lower == 'y':
        print("It is too windy for an umbrella")
    elif wind.lower == 'n':
        print("Take an umbrella")
elif raining.lower == 'n':
    print("Enjoy your day")
#else:
    #print("It is either raining, or it is not")