from stack import *


size = 10
teststack = Stack(size)
for i in range(size):
    teststack.push(i+1)
print(teststack.alist)
print(teststack.pop())
print(teststack.alist)
