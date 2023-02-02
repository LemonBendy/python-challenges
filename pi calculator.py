import random, time

def montecarlo(N: int):
    st = time.time()
    count = int(0)
    for i in range(1, int(N)+1):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1:
            count += 1
    et = time.time()
    timer = et - st
    return f"Pi: {float(4*(count/int(N)))}, Time: {timer}"


def Wallis(N: int):
    st = time.time()
    y = 1
    x = 0
    o = 1
    for i in range(1, int(N) + 1):
        if i % 2==0:
            o += 2
        else:
            x += 2
        y *= x/o
    pi = y * 2
    et = time.time()
    timer = et - st
    return f"Pi: {float(pi)}, Time: {timer}"


def leibniz(N: int):
    st = time.time()
    pi = 0
    n = 4
    d = 1
    for i in range(1, int(N) + 1):
        a = 2 * (i%2) - 1
        pi += a * n/d
        d += 2
    et = time.time()
    timer = et - st
    return f"Pi: {float(pi)}, Time: {timer}"

l = input("INPUT ITERATIONS: ")

print(f" Montecarlo: {montecarlo(l)}")
print(f"     Wallis: {Wallis(l)}")
print(f"    Leibniz: {leibniz(l)}")