import sys
count = 0


def get_total(card, n):
    total = 0
    number = str(card)
    for i in range(n):
        if (i+1) % 2 == 0:
            new_no = int(number[i])*2
            if new_no > 9:
                new_no = str(new_no)
                add = int(new_no[0]) + int(new_no[1])
            else:
                add = new_no
        else:
            add = int(number[i])
        total = int(total) + int(add)
    return total


def is_valid(sums, n):
    r = sums % 10
    return r == 0


while count < 4:
    card_number = input("Input Card No: ")
    length = len(card_number)
    totals = get_total(card_number, length)
    if is_valid(totals, length):
        print("Correct Number")
        sys.exit()
    else:
        print("Incorrect Number, Please try again")
        count += 1
        print(f"you have {4 - count} attempt(s) left")

print("You have run out of attempts")
sys.exit()
