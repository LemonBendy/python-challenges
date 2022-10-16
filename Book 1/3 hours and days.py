days = int(input("How many days: "))

hours = int(days*24)
minutes = int(hours*60)
seconds = int(minutes*60)

print("In " + str(days) + " days, there are:\n" + str(hours) + " hours\n" + str(minutes) + " minutes\n" + str(seconds) + " seconds")