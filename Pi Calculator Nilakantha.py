import random


def infinite(h):
    y = 0
    for i in range(1, h+1):
        p = int(i)
        y += p
    return int(y)


def odd(h):
    y = 0
    for i in range(1, h+1):
        p = int(i)
        y = (2*p) - 1
    return int(y)


def polarity_switch(h):
    y = 0
    for i in range(1, h+1):
        p = int(i)
        y += ((-1)**(i+1))*((2*p)-1)
    return int(y)


def infinite_fraction(h):
    y = 0
    for i in range(1, h+1):
        p = int(i)
        y += 1/((2*p) - 1)
    return float(y)


def infinite_fraction_polarity(h):
    y = 1
    for i in range(1, h+1):
        p = int(i)
        y += (-1**(i+1))*1/(2*p)
    return float(y)


def even_fraction_add(h):
    y = 1
    for i in range(1, h+1):
        p = int(i)
        y += 1/(2*p)
    return float(y)


def even_multiply_fraction(h):
    y = 1
    for i in range(1, h+1):
        p = int(i)
        y *= 1/(2*p)
    return float(y)


def leibniz(h):
    y = 0
    for i in range(1, h + 1):
        p = int(i)
        y += 4*(-1)**(i+1)*1/(2*p-1)
    return float(y)


def wallis(h):
    y = 1
    o = 1
    x = 0
    for i in range(1, h + 1):
        if i % 2 == 0:
            o += 2
        else:
            x += 2
        y *= x/o
    return float(2*y)


def montecarlo(h):
    count = 0
    r = 1
    for i in range(1, h):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            count += 1

    return 4.0*count/h


select = int(input("INPUT NUMBER: "))

print(f"         Infinite Series: {infinite(select)}")
print(f"              Odd Number: {odd(select)}")
print(f"      Polarity Switching: {polarity_switch(select)}")
print(f"   Alternating Fractions: {infinite_fraction(select)}")
print(f"  Even Infinite Fraction: {even_fraction_add(select)}")
print(f"      Fraction Switching: {infinite_fraction_polarity(select)}")
print(f" Multiplication fraction: {even_multiply_fraction(select)}")
print(f"              Leibniz pi: {leibniz(select)}")
print(f"                  Wallis: {wallis(select)}")
print(f"              Montecarlo: {montecarlo(select)}")
