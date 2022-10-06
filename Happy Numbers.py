
## The First 8 numbers are 1, 7, 10, 13, 19, 23, 28, 31
# read around the topic a little, seems to be quite interesting. It seems to be that you could...
# optimise it after the first value if it is equal to certain values <600. Maybe something for a later date


def square_num(n):
  result = 0
  for digit in str(n):
    result += int(digit)**2
  return result

def Happy_Number(number):
  numbers = [number]
  happy = True
  while number != 1:
    number = square_num(number)
    if number in numbers:
      happy = False
      number = 1
    else:
      numbers.append(number)
  return happy

happy_list = []
n = 1
count = 0
while count < 8:
  if Happy_Number(n):
    count +=1
    happy_list.append(n)
  n += 1
print("The first eight happy numbers are:")
print(happy_list)