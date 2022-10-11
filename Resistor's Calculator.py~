#Functions
def band_1_3(band):
    match band.lower():
        case "black":
            return 0
        case "brown":
            return 1
        case "red":
            return 2
        case "orange":
            return 3
        case "yellow":
            return 4
        case "green":
            return 5
        case "blue":
            return 6
        case "violet":
            return 7
        case "grey":
            return 8
        case "white":
            return 9


def band_4(band):
    match band.lower():
        case "black":
            return 1
        case "brown":
            return 10
        case "red":
            return 100
        case "orange":
            return 1,000
        case "yellow":
            return 10,000
        case "green":
            return 100,000
        case "blue":
            return 1,000,000
        case "violet":
            return 10,000,000
        case "grey":
            return 100,000,000
        case "white":
            return 1,000,000,000


def band_5(band):
    match band.lower():
        case "brown":
            return 1
        case "red":
            return 2
        case "orange":
            return 3
        case "yellow":
            return 4
        case "green":
            return 0.5
        case "blue":
            return 0.25
        case "violet":
            return 0.10
        case "grey":
            return 0.05
        case "gold":
            return 5
        case "silver":
            return 10
        case "none":
            return 20
        

#Main Body
modifier = str('')

for i in range(3):
    var = i + 1
    band = str(input("Band " + str(var) + ":"))
    num = str(band_1_3(band))
    modifier = modifier + num
    print(modifier)