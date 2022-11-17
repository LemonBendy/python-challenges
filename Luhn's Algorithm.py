#   from time import sleep
card_number = 79927398713
count = 0


def get_total(card, n):
    total = 0
    number = str(card)
    for i in range(n):
        if (i+1) % 2 == 0:
            new_no = int(number[i])*2
            temp1 = int(str(new_no[0]))
            temp2 = int(str(new_no[1]))
            add = int(temp1) + int(temp2)
        else:
            add = int(number[i])
        total = int(total) + int(add)
    print(total)
    return total


def is_valid(sums, n):
    r = sums % (n-1)
    return r == 0


while count < 4:
    card_number = input("Input Card No: ")
    length = len(str(card_number))
    totals = get_total(card_number, length)
    if is_valid(totals, length):
        print("Correct Number")
        # sleep(0.5)
        quit()
    else:
        print("Incorrect Number, Please try again")
        count += 1
        print(f"you have {4 - count} attempt(s) left")
        # sleep(0.5)

print("You have run out of attempts")
