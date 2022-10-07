import random
from random import randint


#name = input("Name:")
def random_int(x):
    n1 = randint(0,x)
    n2 = randint(0,x)
    return n1, n2

def multiple():
    n1, n2 = random_int(12)
    question = int(input("What is " + str(n1) + " x " + str(n2)))
    correct = n1*n2
    if question == correct:
        print("True")
    else:
        print("False")


def addition():
    n1,n2 = random_int(99)
    question = int(input("What is " + str(n1) + " + " + str(n2)))
    correct = n1+n2
    if question == correct:
        print("True")
    else:
        print("False")


def subtraction():
    n1,n2 = random_int(99)
    question = int(input("What is " + str(n1) + " - " + str(n2)))
    correct = n1-n2
    if question == correct:
        print("True")
    else:
        print("False")


def division():
    n1 = randint(0,99)
    n2 = random.sample(1,2,4,5,8,10)
    question = int(input("What is " + str(n1) + " " + str(n2)))
    correct = n1/n2
    if question == correct:
        print("True")
    else:
        print("False")

addition()
subtraction()
division()
