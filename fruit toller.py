from random import randint
import time
import sys

playing = True
money = 100


def credit_calc(amount):
	return f"£{round(abs(amount)/100, 2):.2f}"


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


def double_reward(amount):
	moneys = amount + 70
	return moneys


def triple_reward(amount):
	moneys = amount + 120
	return moneys


def bell_bonus(amount):
	moneys = amount + 520
	return moneys


def bankrupt():
	moneys = 0
	return moneys


def db_skull(amount):
	moneys = amount - 80
	return moneys


while playing:
	print("You have " + credit_calc(money))
	if money > 0:
		player = str(input("Would you like to play: Y/N"))
		if player == 'y' or player == 'Y':
			print("-20p")
			print(". . . rolling . . .")
			time.sleep(1)
			money = money - 20
			r1 = str(roll(randint(0, 5)))
			r2 = str(roll(randint(0, 5)))
			r3 = str(roll(randint(0, 5)))
			print(r1 + ' : ' + r2 + ' : ' + r3)
			if r1 == "skull" and r2 == "skull" and r3 == "skull":
				money = bankrupt()
				time.sleep(0.4)
			elif r1 == "skull" and r2 == r1 or r2 == "skull" and r3 == r2 or r1 == "skull" and r3 == r1:
				money = db_skull(money)
				time.sleep(0.4)
				print("Two skulls! Unlucky")
			elif r1 == "bell" and r1 == r2 and r1 == r3:
				money = bell_bonus(money)
				time.sleep(0.4)
				print("whoop, whoop")
			elif r1 == r2 and r1 == r3:
				money = triple_reward(money)
				time.sleep(0.4)
				print("triple ripple")
				print(". . . +£1 . . .")
			elif r1 == r2 or r2 == r3 or r1 == r3:
				money = double_reward(money)
				time.sleep(0.4)
				print("double trouble")
				print(". . . +50p . . .")
			else:
				time.sleep(0.4)
				print("unlucky, better luck next time")
		elif player == 'n' or player == 'N':
			print("thanks for playing")
			sys.exit()
	else:
		print("You have can't afford to go again")
		sys.exit()
