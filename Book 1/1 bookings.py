price = float(input("Input price: "))
pop = int(input("How many people: "))

ppp = price/pop

print("The price per person is :" + f" £{round(abs(ppp),2):.2f}")