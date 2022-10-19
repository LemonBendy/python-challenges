numerator: int = int(input("Input Number To Be Divided: "))
denominator: int = int(input("Input Divider: "))

divided: str = numerator//denominator
remainder: str = numerator%denominator

print(f"{numerator} divided by {denominator} is equal to {divided} remainder {remainder}")
