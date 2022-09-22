import random

def roller():
    roll = random.randint(0,5)
    if roll == 1:
        icon = 'Cherry'
    elif roll == 2:
        icon = 'Bell'
    elif roll == 3:
        icon = 'Lemon'
    elif roll == 4:
        icon = 'Orange'
    elif roll == 5:
        icon = 'Star'
    elif roll == 6:
        icon == 'Skull'
    return icon

go = input("Would you like to roll? Y/N")

if go == 'Y':
    for i in range(0,3):
        print(roller())
