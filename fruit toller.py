from random import randint

playing = True
money = 100

def roll(roll_number):
  match roll_number:
    case 0:
      return "cherry"
    case 1:
      return "bell"
    case 2:
      return "lemon"
    case 3:
      return "orange"
    case 4:
      return "star"
    case 5:
      return "skull"


while playing == True:
    player = input("would you like to play: Y/N")
    if player == 'Y' or 'y':
        print(money + " -20")
        money = money - 20
        roll1 = str(roll(randint(0,5)))
        roll2 = str(roll(randint(0,5)))
        roll3 = str(roll(randint(0,5)))
        print(roll1 + ' : ' + roll2 + ' : ' + roll3)
        if roll1 and roll2 == "star" or roll2 and roll3 == "star" or roll1 and roll3 == "star":
            print("whoop")

