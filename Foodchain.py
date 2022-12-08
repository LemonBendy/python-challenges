import random
organisms = ['insect', 'rabbit', 'slug', 'thrush', 'vole', 'frog', 'hawk', 'fox']
food_web = {'insect': ['grass'], 'rabbit': ['grass'], 'slug': ['grass'], 'thrush': ['slug', 'insect'],
            'vole': ['insect'], 'frog': ['insect'], 'hawk': ['frog', 'vole', 'thrush'],
            'fox': ['rabbit', 'frog', 'vole']}


def main():
    orglength = len(organisms)
    playerpos, computerpos = random.randint(0, orglength - 1), random.randint(0, orglength - 1)
    playerorg, computerorg = organisms[playerpos], organisms[computerpos]
    print(f"Computer : {computerorg}, Player : {playerorg}")
    if playerorg in food_web[computerorg]:
        print("Player Dies!")
    elif computerorg in food_web[playerorg]:
        print("Computer Dies!")
    else:
        print("Draw!")


main()
