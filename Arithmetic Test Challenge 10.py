from re import sub
import secrets
from random import randint


i = 0
y = 1
#name = input("Name:")


def random_int(x):
    n1 = randint(0, x)
    n2 = randint(0, x)
    return n1, n2


def multiple():
    global i, y
    n1, n2 = random_int(12)
    question = int(input(str(y) + ". What is " + str(n1) + " x " + str(n2) + ": "))
    correct = n1*n2
    if question == correct:
        i += 1
        y += 1
    else:
        y += 1


def addition():
    global i, y
    n1, n2 = random_int(99)
    question = int(input(str(y) + ". What is " + str(n1) + " + " + str(n2) + ": "))
    correct = n1+n2
    if question == correct:
        i += 1
        y += 1
    else:
        y += 1


def subtraction():
    global i, y
    n1, n2 = random_int(99)
    question = int(input(str(y) + ". What is " + str(n1) + " - " + str(n2) + ": "))
    correct = n1-n2
    if question == correct:
        i += 1
        y += 1
    else:
        y += 1


def division():
    global i, y 
    n1 = randint(0, 99)
    nums = (1, 2, 4, 5, 8, 10)
    n2: int = secrets.choice(nums)
    question = float(input(str(y) + ". What is " + str(n1) + " ÷ " + str(n2) + ": "))
    correct = n1/n2
    if question == correct:
        i += 1
        y += 1
    else:
        y += 1

def select(num):
    match num:
        case 0:
            return addition()
        case 1:
            return multiple()
        case 2:
            return division()
        case 3:
            return subtraction()

for x in range(10):
    
    rand = randint(0,3)
    select(rand)
print(i)