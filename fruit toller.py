from random import randint
import time

playing = True
money = 100

def credit_calc(money):
    return f"£{round(abs(money)/100, 2):.2f}"

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

def double_reward(money):
    money = money + 50
    return money

def triple_reward(money):
    money = money + 100
    return money

def bell_bonus(money):
    money = money + 500
    return money

def bankrupt(money):
    money = 0
    return money

def db_skull(money):
    money = money - 100
    return money

while playing == True:
    player = input("would you like to play: Y/N")
    if player == 'Y' or 'y':
        print ("-20p")
        print(". . . rolling . . .")
        time.sleep(1)
        money = money - 20
        r1 = str(roll(randint(0,5)))
        r2 = str(roll(randint(0,5)))
        r3 = str(roll(randint(0,5)))
        print(r1 + ' : ' + r2 + ' : ' + r3)
        if r1 == "skull" and r2 == "skull" and r3 == "skull":
            bankrupt(money)
            time.sleep(0.4)
            print(credit_calc(money))
        elif r1 == "skull" and r2 == r1 or r2 == "skull" and r3 == r2 or r1 == "skull" and r3 == r1:
            db_skull(money)
            time.sleep(0.4)
            print(credit_calc(money))
        elif r1 == "bell" and r1 == r2 and r1 == r3:
            bell_bonus(money)
            time.sleep(0.4)
            print("whoop, whoop")
            print(credit_calc(money))
        elif r1 == r2 and r1 == r3:
            triple_reward(money)
            time.sleep(0.4)
            print("triple riple")
            print(credit_calc(money))
        elif r1 == r2 or r2 == r3 or r1 == r3:
            double_reward(money)
            time.sleep(0.4)
            print("double trouble")
            print(credit_calc(money))
        else:
            time.sleep(0.4)
            print("unlucky, better luck next time")
            print(credit_calc(money))

