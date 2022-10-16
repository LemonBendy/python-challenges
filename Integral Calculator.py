import math

def f(x):
    fun = math.sin(x)
    return fun
def integrate(a, b, n):
    deltax = (b-a)/n
    psi = a + deltax/2
    area = 0
    for i in range(0, n):
        area += f(psi) * deltax
        psi += deltaX

    return area
if'__name__' == '__name__':
    print(integrate(-math.pi, 2**2, 1000))